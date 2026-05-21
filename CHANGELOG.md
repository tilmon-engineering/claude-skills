# Changelog

## conway-architecture 0.2.0

Adds the **quality agent** as a recommended pattern: a dedicated domain teammate that owns the integration/e2e test surface, runs workspace-mutating commands the dev team can't safely run in parallel, and brings an outsider's perspective on legibility, error messages, and onboarding friction. Codifies a **round-then-assess** rhythm — the coordinator delegates a development round in parallel, lets the dev team settle into a coherent state, then hands control to the quality agent for assessment, with no interleaving.

**New:**
- `conway-method` skill: new "The quality agent (recommended pattern)" section covering role, round-then-assess rhythm, tool belt, outsider's posture, and when-to-add criteria.
- `conway-method` skill: workspace-mutating commands now explicitly claimed as the quality agent's territory (coordinator as fallback), off-limits to dev-team teammates.
- `conway-method` skill: coordinator discipline now includes "fan out when domains are independent" and "round, then assess" as numbered rules.
- `conway-method` skill: three new failure-mode entries covering workspace-collision attribution, serial-by-default coordination, and mid-round quality runs.
- `/conway-init`: interview step 4 prompts the user to opt into a quality agent with default `owned_paths` proposed from repo structure (`tests/integration/**`, `tests/e2e/**`, `playwright/**`, etc.).

**Changed:**
- "Reentrant vs workspace-mutating actions" renamed to "Parallelism and workspace-mutating actions" — leads with the parallelism invariant that makes the rest of the contract necessary.

## conway-architecture 0.1.2

Removes the `model: sonnet` pin from `/conway-init` and `/conway-session` commands. The pin was causing 1M-context dispatch failures for users running the commands from a 1M-context session, because session capability flags appear to propagate to pinned model invocations (`sonnet` got invoked as `sonnet[1m]`, which requires usage credits). Commands now inherit the session's model.

**Changed:**
- `commands/conway-init.md`: dropped `model: sonnet` frontmatter field.
- `commands/conway-session.md`: dropped `model: sonnet` frontmatter field.

## conway-architecture 0.1.1

Clarifies what `.agents/_shared/contracts/` is. The directory holds **text specifications** describing inter-domain interfaces — producer, consumers, shape, change protocol — not source code. Each domain implements its side of a contract inside its own `owned_paths`. The directory's purpose is to expose the dependency graph in human-readable form, not to share code across domains.

**Changed:**
- `conway-method` skill: new "What `_shared/contracts/` is (and isn't)" section; updated file-tree comment.
- `templates/shared-AGENTS.md.template`: rewrote "Cross-domain contracts" section accordingly.
- `templates/domain-AGENTS.md.template`: tightened "Contracts I rely on" / "Contracts I expose" to clarify spec lives in `_shared/`, implementation lives in `owned_paths`.
- `README.md`: one-line clarification on `_shared/contracts/`.

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
