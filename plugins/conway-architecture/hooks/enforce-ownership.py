#!/usr/bin/env python3
"""
Conway Architecture ownership enforcement.

Runs as a PreToolUse hook on Write|Edit. Reads JSON from stdin describing the
tool call. Decides allow/deny based on:

  1. Whether the caller is the coordinator (no agent_type field) or a named
     teammate (agent_type == teammate name, per the empirical probe in v0.0.1).
  2. Whether the requested file_path falls under a domain's owned_paths
     (declared as fnmatch globs in the `owned_paths` frontmatter list of
     each `.agents/<domain>/AGENTS.md`).

Rules:
  - If `.agents/` does not exist in the project, the plugin is not initialized
    here -> allow everything (no-op).
  - Coordinator may write under `.agents/_shared/` and any path NOT claimed by
    a domain. Writing into a domain's owned_paths is denied with a message
    naming the owner.
  - Teammate may write under `.agents/<their-name>/` (their private notebook)
    and any path matching their own owned_paths. Writing anywhere else is
    denied with a message naming the actual owner (or "no owner").

Output: a JSON object on stdout per the Claude Code hook spec.
"""

from __future__ import annotations

import fnmatch
import json
import os
import re
import sys
from pathlib import Path


def find_project_root(cwd: str) -> Path:
    """Walk up from cwd looking for a `.agents/` directory. Returns None-ish
    (the cwd itself) if not found; caller treats no-`.agents/` as a no-op."""
    p = Path(cwd).resolve()
    for candidate in [p, *p.parents]:
        if (candidate / ".agents").is_dir():
            return candidate
    return p


def parse_frontmatter(text: str) -> dict:
    """Tiny YAML-ish frontmatter parser. We only care about `owned_paths`,
    which we accept as a YAML flow list (`[a, b]`) or a block list (lines
    starting with `- `). Anything we can't parse cleanly returns {}."""
    m = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    body = m.group(1)
    out: dict = {}
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        flow = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*\[(.*)\]\s*$", line)
        block_header = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*$", line)
        scalar = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.+)\s*$", line)
        if flow:
            key = flow.group(1)
            items = [s.strip().strip('"').strip("'") for s in flow.group(2).split(",") if s.strip()]
            out[key] = items
            i += 1
        elif block_header:
            key = block_header.group(1)
            i += 1
            items = []
            while i < len(lines) and re.match(r"^\s*-\s+", lines[i]):
                items.append(re.sub(r"^\s*-\s+", "", lines[i]).strip().strip('"').strip("'"))
                i += 1
            if items:
                out[key] = items
            else:
                # not a list, skip
                pass
        elif scalar:
            out[scalar.group(1)] = scalar.group(2).strip().strip('"').strip("'")
            i += 1
        else:
            i += 1
    return out


def load_domains(project_root: Path) -> dict[str, list[str]]:
    """Returns {domain_name: [owned_path_glob, ...]} for every
    `.agents/<name>/AGENTS.md` with parseable frontmatter."""
    domains: dict[str, list[str]] = {}
    agents_dir = project_root / ".agents"
    if not agents_dir.is_dir():
        return domains
    for child in sorted(agents_dir.iterdir()):
        if not child.is_dir() or child.name.startswith("_"):
            continue
        manifest = child / "AGENTS.md"
        if not manifest.is_file():
            continue
        try:
            fm = parse_frontmatter(manifest.read_text())
        except OSError:
            continue
        paths = fm.get("owned_paths") or []
        if isinstance(paths, list):
            domains[child.name] = paths
    return domains


def matches_any(rel_path: str, globs: list[str]) -> bool:
    return any(fnmatch.fnmatch(rel_path, g) or fnmatch.fnmatch(rel_path, g.rstrip("/") + "/**") for g in globs)


def find_owners(rel_path: str, domains: dict[str, list[str]]) -> list[str]:
    return [name for name, globs in domains.items() if matches_any(rel_path, globs)]


def decide(payload: dict) -> dict:
    cwd = payload.get("cwd") or os.getcwd()
    project_root = find_project_root(cwd)
    domains = load_domains(project_root)

    if not domains:
        return {"hookSpecificOutput": {"permissionDecision": "allow"}}

    tool_input = payload.get("tool_input") or {}
    file_path = tool_input.get("file_path")
    if not file_path:
        return {"hookSpecificOutput": {"permissionDecision": "allow"}}

    try:
        rel = str(Path(file_path).resolve().relative_to(project_root))
    except ValueError:
        # outside project root entirely -> not our business
        return {"hookSpecificOutput": {"permissionDecision": "allow"}}

    caller = payload.get("agent_type")  # absent for coordinator/main agent
    owners = find_owners(rel, domains)

    # Always allow writes under a domain's own private directory by that domain
    if caller and rel.startswith(f".agents/{caller}/"):
        return {"hookSpecificOutput": {"permissionDecision": "allow"}}

    # Coordinator (no agent_type) writing _shared is always fine
    if caller is None and rel.startswith(".agents/_shared/"):
        return {"hookSpecificOutput": {"permissionDecision": "allow"}}

    # Coordinator writing into any domain's private dir is a delegation violation
    if caller is None and rel.startswith(".agents/") and not rel.startswith(".agents/_shared/"):
        parts = rel.split("/", 2)
        domain_dir = parts[1] if len(parts) >= 2 else "?"
        return {
            "hookSpecificOutput": {
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"Conway: coordinator cannot edit .agents/{domain_dir}/ directly. "
                    f"Delegate to the '{domain_dir}' teammate via SendMessage."
                ),
            }
        }

    if caller is None:
        # coordinator writing outside .agents/
        if owners:
            return {
                "hookSpecificOutput": {
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        f"Conway: '{rel}' is owned by {sorted(owners)}. "
                        f"Coordinator must delegate; do not edit domain-owned files directly."
                    ),
                }
            }
        return {"hookSpecificOutput": {"permissionDecision": "allow"}}

    # caller is a named teammate
    if caller in owners:
        return {"hookSpecificOutput": {"permissionDecision": "allow"}}

    if owners:
        return {
            "hookSpecificOutput": {
                "permissionDecision": "deny",
                "permissionDecisionReason": (
                    f"Conway: '{caller}' may not edit '{rel}' (owned by {sorted(owners)}). "
                    f"Your owned_paths are {domains.get(caller, [])}."
                ),
            }
        }

    return {
        "hookSpecificOutput": {
            "permissionDecision": "deny",
            "permissionDecisionReason": (
                f"Conway: '{rel}' is not in any domain's owned_paths. "
                f"'{caller}' owns {domains.get(caller, [])}; "
                f"have the coordinator route this to the right teammate or claim the path."
            ),
        }
    }


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        # Don't block on malformed input; let Claude proceed.
        print(json.dumps({"hookSpecificOutput": {"permissionDecision": "allow"}}))
        return 0

    result = decide(payload)
    print(json.dumps(result))
    return 0


if __name__ == "__main__":
    sys.exit(main())
