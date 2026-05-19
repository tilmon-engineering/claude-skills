# conway-architecture

**Conway's Law, inverted.** The observation that "a system tends to resemble the communication structure of the team that built it" is usually treated as a warning. This plugin treats it as a tool: define the team you want the architecture to look like, and let the architecture follow.

The team is a **persistent, domain-scoped subagent team**. Each domain owns a disjoint slice of the codebase. The coordinator (the main session agent) routes work; domain agents do the work. The boundaries are enforced by a `PreToolUse` hook, not just by convention.

## Quick start

In a project you want to organize this way:

```
/conway-init      # interview-driven team setup, writes .agents/
```

Then, in each subsequent session:

```
/conway-session   # materializes the team via TeamCreate and spawns domain agents
```

The plugin is a no-op in projects without a `.agents/` directory, so you can have it installed everywhere and it only activates where you've initialized it.

## What you get

- **`.agents/<domain>/AGENTS.md`** — each domain agent's charter. YAML frontmatter declares `owned_paths` (fnmatch globs). The agent rehydrates from this file every session.
- **`.agents/<domain>/notes/`, `decisions/`** — per-domain working memory and durable decisions. Owner-writable; peer-readable.
- **`.agents/_shared/AGENTS.md`** — the roster and routing rules. Coordinator-owned.
- **`.agents/_shared/ROADMAP.md`** — what's in flight. Coordinator-owned.
- **`.agents/_shared/contracts/`** — text specs of inter-domain interfaces (producer + consumers + shape + change protocol). The dependency graph in prose, not a shared code area; implementations live in each domain's own `owned_paths`.

## How enforcement works

A `PreToolUse` hook on `Write|Edit` reads stdin, identifies the caller (coordinator vs. teammate by the presence of the `agent_type` field), and matches the requested `file_path` against every domain's `owned_paths`. Decisions:

| Caller | Path | Decision |
|---|---|---|
| Coordinator | `.agents/_shared/**` | allow |
| Coordinator | a domain's owned path or `.agents/<domain>/**` | **deny — delegate** |
| Coordinator | uncovered | allow |
| Domain agent `D` | `D`'s owned paths or `.agents/D/**` | allow |
| Domain agent `D` | another domain's path | **deny — wrong owner** |
| Domain agent `D` | uncovered | **deny — claim it or route via coordinator** |

The hook keys on `agent_type` carrying the teammate's `name`, verified empirically in v0.0.1.

## Status

v0.1 — first working release. The enforcement hook is smoke-tested across the eight relevant cases. The `conway-method` skill that codifies coordinator/teammate discipline has not yet been pressure-tested per the `writing-skills` RED-GREEN-REFACTOR cycle; that's planned for v0.2 alongside the `/conway-propose-agent` and `/conway-validate` commands.

## Components

- **Skill** `conway-method` — the method itself: vocabulary, decision table, coordinator discipline, domain agent discipline, failure modes.
- **Command** `/conway-init` — interview-driven team bootstrap.
- **Command** `/conway-session` — per-session team materialization via `TeamCreate` + named teammates.
- **Hook** `enforce-ownership.py` — PreToolUse path-scoped ownership enforcement.
- **Templates** under `templates/` — used by `/conway-init` to scaffold `AGENTS.md` files.

## Not yet implemented (planned for v0.2)

- `/conway-propose-agent` — coordinator-driven flow for adding a new domain to an existing team.
- `/conway-validate` — check `owned_paths` for overlap and other invariants outside of `/conway-init`.
- Pressure-tested `conway-method` skill via RED-GREEN-REFACTOR with subagents.
- Delegation log automation (currently the team's shared TaskList serves this).
