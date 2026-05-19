# Changelog

## conway-architecture 0.1.0

First working release. Implements the Conway Architecture method: a persistent, domain-scoped subagent team whose communication boundaries become the system's architecture, enforced by a path-scoped `PreToolUse` hook. Empirically verified in v0.0.1 that hook input carries the teammate's `name` as `agent_type`, which makes path-scoped enforcement clean.

**New:**
- `conway-method` skill: vocabulary, decision table, coordinator/teammate discipline, failure modes. The headline artifact codifying the method.
- `/conway-init` command: interview-driven team bootstrap. Writes `.agents/<domain>/AGENTS.md` charters with `owned_paths` frontmatter, plus `.agents/_shared/{AGENTS.md, ROADMAP.md, contracts/}`.
- `/conway-session` command: materializes the team via `TeamCreate` and spawns each domain agent as a named teammate with a charter-loading prompt.
- `enforce-ownership.py` PreToolUse hook: parses `.agents/<domain>/AGENTS.md` frontmatter, intersects requested `file_path` with every domain's `owned_paths` globs, and blocks misrouted writes. No-op in projects without `.agents/`.
- Templates for domain AGENTS.md, shared roster, and ROADMAP — used by `/conway-init` and hand-authorable.

**Changed:**
- Removed v0.0.1 diagnostic scaffold (`/conway-probe`, stdin-dump hook). Their job — verify the hook's identity fields — is done.

**Known limitations (planned for v0.2):**
- The `conway-method` skill has not yet been pressure-tested via `writing-skills` RED-GREEN-REFACTOR with subagents.
- `/conway-propose-agent` (growth flow) and `/conway-validate` (standalone invariant check) are not yet implemented.

## conway-architecture 0.0.1

Initial diagnostic scaffold. Not yet a working method plugin — the v0.0.1 release is a probe used to empirically verify what identity fields a `PreToolUse` hook receives when invoked by a named teammate spawned via `TeamCreate` + `Agent(team_name=..., name=..., ...)`. The answer determines whether path-scoped enforcement of domain ownership is feasible before the real method plugin is designed.

**New:**
- `/conway-probe` command: spawns a named teammate, has it `Write` a file, captures the hook input alongside a main-agent baseline, and reports which field a future enforcement hook should key on.
- `PreToolUse` hook on `Write|Edit`: non-blocking stdin dump to `.conway-probe/pretooluse.jsonl`.

## semantic-db 0.1.0

Initial release. A substrate skill, `using-typedb`, teaching agents to interact with TypeDB 3.x databases through the `typedb` MCP tools.

**New:**
- `using-typedb` skill: schema-first workflow, transaction-type discipline (`read`/`write`/`schema`), TypeQL 3.x syntax (fetch, attribute subtyping, `@card`/`@regex`/`@values`), `define` vs `redefine` vs `undefine` rules, two-stage delete pattern under `@card(1..1)`, and the MCP→JSON→TypeQL regex double-escape gotcha.

## outcomes 0.1.0

Initial release. A domain skill, `using-ost-framework`, encoding the OST (Outcome / Strategy / Tactic) Framework as implemented in the `agents` TypeDB database on edge-01. Pairs with `semantic-db` for query mechanics.

**New:**
- `using-ost-framework` skill: three-layer rubric with diagnostic gates, falsifiability discipline (hypothesis + invalidation trigger + deadline + lifecycle on every link), structured Task fields, AssetTag URI conventions, ID allocation patterns, canonical read/write workflows, and an explicit refusal list for vague hypotheses, trade-off-free strategies, and asset-less tactics.

## autonomy 1.1.1

Reliability fix for the `journal-summarizer` subagent, which previously failed to write `summary.md` in many cases (Haiku returning prose instead of calling `Write`, ambiguous relative paths, and brittle "rewrite the whole summary" semantics).

**Changed:**
- Reframed `summary.md` as an append-only chronological log of 5-iteration windows. Each milestone (iterations 5, 10, 15, …) appends one ~2-paragraph section; older sections are never rewritten.
- `journal-summarizer` now uses Sonnet (was Haiku), gained the `Edit` tool, and has an explicit positive output contract: must end its turn with a successful `Edit`/`Write` tool call.
- `end-iteration` Step 4 now passes absolute paths for `summary.md` and the 5 window journal files to the subagent, plus an explicit create-vs-append fork.

## autonomy 1.1.0

Convert command wrappers to user-invocable skills. The 14 wrapper commands in `plugins/autonomy/commands/` were thin pass-throughs to skills with no additional logic; they have been removed and the underlying skills renamed to match the old slash names. User-facing slash names are unchanged (`/start-iteration`, `/slime`, `/fork-iteration`, etc.) but now resolve directly to skills.

**Changed:**
- Removed all 14 wrapper commands; renamed skills to match old command names (e.g. `starting-an-iteration` → `start-iteration`, `slime-strategy` → `slime`).
- Marked all autonomy skills `user-invocable: true` explicitly in frontmatter.
- Updated cross-references in skills, agents, and README to use new skill names.

## autonomy 1.0.0

Initial release of the autonomy plugin. Enables AI agents to iteratively self-direct in pursuit of open-ended goals with state continuity across conversations through iteration journals.

**New:**
- Core iteration workflow: `/create-goal`, `/start-iteration`, `/end-iteration`, `/checkpoint-iteration`, `/review-progress` for goal pursuit with journal-based state continuity.
- Git integration: automatic journal commits, 4-digit iteration numbering (0001-9999), branch-aware annotated tags (`autonomy/<branch>/iteration-NNNN`), structured commit metadata (status, metrics, blockers, next steps).
- Slime mold strategy: `/slime` one-command setup for parallel exploration workflows with cooperative branch genealogy.
- Branch management: `/list-branches`, `/fork-iteration`, `/branch-status`, `/compare-branches`, `/analyze-branch` for cross-branch learning and idea reincorporation.
- Worktree support: `/fork-worktree`, `/list-worktrees`, `/remove-worktree` for running parallel agents on different branches simultaneously.
- `branch-analyzer` agent (Haiku) for computational analysis of branch state via generated Python scripts.
- `journal-reader` and `journal-summarizer` agents for context loading and milestone summarization.
