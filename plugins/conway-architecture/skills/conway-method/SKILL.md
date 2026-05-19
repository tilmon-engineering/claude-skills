---
name: conway-method
description: Use when working in a project that has a `.agents/` directory or when the user asks about Conway Architecture, the conway-architecture plugin, domain agents, owned_paths enforcement, or how to coordinate a persistent subagent team that shadows the application's architecture
---

# Conway Architecture: the method

## Core idea

Conway's Law observes that **a system's architecture tends to resemble the communication structure of the team that built it**. Usually treated as a warning. Here, it's used as a tool: design the team you want, and let the architecture follow.

The team is a **persistent, domain-scoped subagent team**. Each domain owns a disjoint slice of the codebase, declared as path globs. The coordinator (the main session agent) routes work; the domain agents do the work. The boundaries are enforced by a `PreToolUse` hook, not just by convention.

## When to use

- The project has (or should have) a `.agents/` directory with per-domain `AGENTS.md` files.
- You are about to delegate work across domains and need to know who owns what.
- The user mentions "Conway", "the team", "domain agents", or asks why a write was blocked.
- You see hook denials mentioning "Conway:" — that's this method enforcing itself.

Skip when: the project has no `.agents/` directory. The plugin is a no-op there.

## Vocabulary

| Term | Meaning |
|---|---|
| **Coordinator** | The main session agent. Owns the roadmap, never edits domain-owned files. Identifiable in hook input by the *absence* of `agent_type`. |
| **Domain agent** | A teammate spawned via `Agent(team_name=…, name=<domain>, …)`. The `name` matches a directory under `.agents/`. Identifiable in hook input by `agent_type == <domain>`. |
| **`owned_paths`** | YAML frontmatter list of fnmatch globs in each `.agents/<domain>/AGENTS.md`. The teeth of the method. |
| **`.agents/_shared/`** | Cross-cutting territory the coordinator owns: roster (`AGENTS.md`), `ROADMAP.md`, `contracts/`. |
| **Non-overlap invariant** | No two domains may claim the same path. The system's discipline depends on this; `/conway-init` and `/conway-validate` enforce it. |

## Files this method maintains

```
.agents/
├── _shared/
│   ├── AGENTS.md         # roster + routing rules (coordinator-writable)
│   ├── ROADMAP.md        # what's in flight (coordinator-writable)
│   └── contracts/        # inter-domain interfaces (coordinator + acks)
└── <domain>/
    ├── AGENTS.md         # charter with owned_paths frontmatter
    ├── notes/            # private working memory (owner-writable)
    └── decisions/        # durable record of choices (owner-writable)
```

## Enforcement

A `PreToolUse` hook on `Write|Edit` runs `enforce-ownership.py`. The decision table:

| Caller | Path | Decision |
|---|---|---|
| Coordinator (no `agent_type`) | `.agents/_shared/**` | allow |
| Coordinator | `.agents/<domain>/**` | **deny** — delegate to `<domain>` |
| Coordinator | matches a domain's `owned_paths` | **deny** — delegate to that domain |
| Coordinator | uncovered path | allow |
| Domain agent `D` | `.agents/D/**` | allow (their own notes) |
| Domain agent `D` | matches `D`'s `owned_paths` | allow |
| Domain agent `D` | matches another domain's `owned_paths` | **deny** — wrong owner |
| Domain agent `D` | uncovered path | **deny** — claim it or route via coordinator |

If `.agents/` does not exist in the project, the hook is a no-op.

## Coordinator discipline

When you are the main session agent in a Conway project, your operating posture changes:

1. **Read `.agents/_shared/AGENTS.md` first.** It is your charter.
2. **Delegate, don't do.** If a task touches a domain's owned paths, you send the teammate a message. You do not pick up the file yourself, even if "it would be faster."
3. **Update the roadmap, not the code.** Your editable surface is `_shared/` and uncovered files.
4. **Boundary smells.** If a task keeps bouncing between two domains, the boundary is probably wrong. Surface it; consider `/conway-propose-agent` or moving the boundary. Do not paper over it by doing the work yourself — that is the failure mode this method exists to prevent.
5. **End-of-session hygiene.** Ask each active teammate to drop a note in `.agents/<name>/notes/<date>.md`. That note *is* the next session's memory of them.

## Domain agent discipline

When you are spawned as a named teammate in a Conway team, the first action of your first turn is always the same rehydration ritual:

1. Read `.agents/<your-name>/AGENTS.md` — that is your charter, including `owned_paths`.
2. Skim `.agents/<your-name>/notes/` newest first — that is your working memory from past sessions.
3. Skim `.agents/<your-name>/decisions/` — durable choices you've made.
4. Read any `.agents/_shared/contracts/` that touch your declared interfaces.
5. Read `.agents/_shared/AGENTS.md` to know who your peers are and what they own.
6. Report ready.

Then, while working:

- You may edit your own files freely. The hook will block you from anything outside your `owned_paths`.
- If the coordinator routes you a task that crosses into another domain, push back. The right move is for the coordinator to break the task up or update a shared contract.
- Write notes as you go. You will not exist next session; future-you depends on what you leave behind in `notes/` and `decisions/`.

## Reentrant vs workspace-mutating actions

Conway's boundary applies to **runtime side effects**, not just file writes. The same logic that keeps two agents from editing the same file keeps them from stepping on each other's build artifacts, server ports, browser instances, or mutation-test scratch checkouts. The contract:

**Teammates may run reentrant, scope-local actions freely.** These are safe because two domains doing them in parallel cannot collide:

- Unit tests scoped to the teammate's owned files / crate (e.g., `cargo test -p <crate>`, `pytest path/to/file`).
- Formatters and linters scoped to owned files (`rustfmt`, `prettier`, `eslint --fix` on owned paths).
- `cargo check` / type-checks limited to the teammate's crate.
- Reading anything: `cat`, `grep`, `git log`, `git diff`, `git status`.

**Teammates do not run workspace-mutating or exclusive-resource actions.** These either touch shared global state (the whole target dir, a port, a database, a browser) or take long enough that two parallel runs would interfere. Examples:

- Full workspace builds (`just build`, `cargo build --workspace`, `bazel build //...`).
- Integration / end-to-end test suites (`just test`, `just test-integration`, Playwright/Cypress, anything that boots a server or fixture DB).
- Mutation testing (`cargo-mutants`, `just mutants`) — operates on the whole tree and is long-running.
- Live debug environments / dev servers (`dx serve`, `npm run dev`, hot-reload watchers).
- Workspace-wide format/lint sweeps (`just fix`, `just format`, `just machete`).
- Anything that writes to remote services, mutates shared infra, or requires exclusive ports.
- Commits, pushes, branch operations — coordinator-only.

**The completion contract.** A teammate completes its task to the best of its ability using scope-local checks, then **signals status back to the coordinator** rather than verifying against workspace-mutating tooling. A typical handoff looks like:

> "Changes made: <files>. Verified locally: `cargo test -p polytoken-web` passes, `rustfmt` clean. Not run (coordinator territory): full build, integration tests, dev-server smoke. Ready for orchestration."

The coordinator then runs (or chooses not to run) the workspace-mutating checks — serializing them across teammates so two domains' edits get tested together, not in isolation. If a workspace-mutating check fails, the coordinator routes the failure back to the implicated domain(s) with a precise reproducer.

**Why this matters.** Without this rule, two teammates running `just build` in parallel will fight over `target/`, two `dx serve` invocations will fight over the same port, and `cargo-mutants` runs will silently corrupt each other's scratch directories. The hook does not enforce this — it is a discipline that lives in each domain's charter. State it explicitly in the "Conventions" section of `AGENTS.md` for any domain whose work could plausibly tempt it across the line.

## Failure modes (and how to spot them)

| Symptom | Likely cause | Fix |
|---|---|---|
| Coordinator hits a hook denial citing a domain | Coordinator is doing work it should delegate | Send a message to the named owner instead |
| Teammate hits a hook denial naming another domain | Boundary is wrong, or task was mis-routed | Coordinator re-routes, or `.agents/_shared/AGENTS.md` gets revised |
| Teammate hits a denial citing "no owner" | New territory has no domain | Coordinator either claims it under an existing domain or proposes a new one |
| Two domains constantly need to update each other's contracts | The interface lives in the wrong place | Promote the contract to `_shared/contracts/`, gate changes on multi-domain ack |
| Notes never get written | End-of-session hygiene skipped | Add to coordinator's end-of-turn checklist; without notes, every session starts blind |
| Two teammates' builds / dev servers / mutation runs collide | Workspace-mutating action was run by a teammate instead of the coordinator | Reaffirm the reentrant-vs-mutating contract; teammate runs only scope-local checks and signals status back |

## Hook input shape (for reference)

Empirically verified in v0.0.1. PreToolUse stdin includes:

```json
{
  "session_id": "...",
  "cwd": "/abs/path/to/project",
  "tool_name": "Write",
  "tool_input": { "file_path": "...", "content": "..." },
  "agent_type": "<teammate-name>",   // absent when coordinator is calling
  "agent_id": "<stable-uuid>"         // absent when coordinator is calling
}
```

The enforcement hook keys on `agent_type` (the teammate's `name`) and `tool_input.file_path`.

## Commands

| Command | Purpose |
|---|---|
| `/conway-init` | Bootstrap a team in a new project (interview-driven). |
| `/conway-session` | Materialize the team for a session (TeamCreate + spawn members). |

## Status of this skill

v0.1. The enforcement hook is smoke-tested; the method itself has not been pressure-tested with subagents per `writing-skills` RED-GREEN-REFACTOR. Treat the discipline guidance above as a starting point that may need to tighten under real use. Bug reports welcome — the most valuable signal is "the coordinator absorbed work that should have been delegated and the hook didn't stop it."
