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
│   └── contracts/        # text specs of who depends on whom (coordinator + acks)
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

## What `_shared/contracts/` is (and isn't)

It is **text specifications**, not source code. Each file in `_shared/contracts/` describes a single inter-domain interface in prose plus whatever schema-like notation is useful (markdown, with embedded protobuf/typescript/OpenAPI fragments if helpful for clarity). A contract names:

- **Producer**: which domain publishes this interface.
- **Consumers**: which domains depend on it.
- **Shape**: what the interface promises — fields, semantics, invariants, error modes.
- **Change protocol**: how this contract evolves (typically: producer drafts, every consumer acks in their own `decisions/`).

It is **not** a place for shared code. The producing domain implements the contract inside its own `owned_paths`. Consumers implement their integration inside *their* own `owned_paths`. If two domains find themselves wanting to import the same module, that is a signal the boundary is wrong — promote the module's owner to a real domain, don't smuggle code through `_shared/`.

The point of the directory is the **dependency graph in textual form**: anyone can read `_shared/contracts/` and answer "who relies on whom, and for what?" without grepping code.

## Coordinator discipline

When you are the main session agent in a Conway project, your operating posture changes:

1. **Read `.agents/_shared/AGENTS.md` first.** It is your charter.
2. **Delegate, don't do.** If a task touches a domain's owned paths, you send the teammate a message. You do not pick up the file yourself, even if "it would be faster."
3. **Fan out when domains are independent.** Spawn dev-team teammates in parallel whenever the work doesn't have a cross-domain dependency. Serialize only when one domain genuinely needs another's output first. The disjoint-ownership invariant is what makes parallel work safe — use it.
4. **Round, then assess.** If a quality agent exists, run development in *rounds*: delegate, let the dev team settle into a coherent state, then hand control to the quality agent for assessment. Do not interleave dev edits and quality runs. See the quality-agent section.
5. **Update the roadmap, not the code.** Your editable surface is `_shared/` and uncovered files.
6. **Boundary smells.** If a task keeps bouncing between two domains, the boundary is probably wrong. Surface it; consider `/conway-propose-agent` or moving the boundary. Do not paper over it by doing the work yourself — that is the failure mode this method exists to prevent.
7. **End-of-session hygiene.** Ask each active teammate to drop a note in `.agents/<name>/notes/<date>.md`. That note *is* the next session's memory of them.

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

## Parallelism and workspace-mutating actions

**The dev team runs in parallel.** A coordinator that delegates serially is leaving most of Conway's value on the table. The point of disjoint `owned_paths` is precisely that two domain teammates editing their own files cannot collide — so the coordinator should fan out work whenever the domains involved are independent, and only serialize when there's a genuine inter-domain dependency.

Parallelism only works if no teammate touches **shared workspace state**. Conway's boundary therefore applies to **runtime side effects**, not just file writes. The same logic that keeps two agents from editing the same file keeps them from stepping on each other's build artifacts, server ports, browser instances, or mutation-test scratch checkouts. The contract:

**Teammates may run reentrant, scope-local actions freely.** These are safe because two domains doing them in parallel cannot collide:

- Unit tests scoped to the teammate's owned files / crate (e.g., `cargo test -p <crate>`, `pytest path/to/file`).
- Formatters and linters scoped to owned files (`rustfmt`, `prettier`, `eslint --fix` on owned paths).
- `cargo check` / type-checks limited to the teammate's crate.
- Reading anything: `cat`, `grep`, `git log`, `git diff`, `git status`.

**Teammates do not run workspace-mutating or exclusive-resource actions.** These are the **exclusive territory of the quality agent (preferred) or the coordinator** — never a dev-team teammate. They either touch shared global state (the whole target dir, a port, a database, a browser) or take long enough that two parallel runs would interfere. Examples:

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

**Who runs the workspace-mutating tier?** Either the coordinator, or — preferred for any project past trivial size — a dedicated **quality agent**. See the next section.

## The quality agent (recommended pattern)

The reentrant-vs-mutating rule leaves an open question: if domain teammates only run scope-local checks, who runs the integration suite, the end-to-end tests, the manual smoke checks? One answer is "the coordinator." The better answer, for any project past trivial size, is a dedicated **quality agent**.

### Role

The quality agent is a regular domain teammate — it has `owned_paths`, it rehydrates from `.agents/quality/`, it lives or dies by the same hook — with one distinguishing charter:

- It owns the **integration and end-to-end test surface** (typical paths: `tests/integration/**`, `tests/e2e/**`, `playwright/**`, fixture setup scripts, smoke-test scripts).
- It owns **quality reports and findings** under its own `decisions/` and `notes/`.
- It does **not** own application code. It cannot fix what it finds — it reports back to the coordinator, who routes fixes to the implicated domain.

### The round-then-assess rhythm

The coordinator's loop becomes two-phase:

1. **Development round.** Coordinator delegates work to one or more domain teammates. Teammates implement, run scope-local checks, signal complete. Coordinator may iterate within this phase.
2. **Quality assessment.** Once the development round has settled into a *coherent, complete-to-the-best-of-everyone's-ability* state, coordinator hands control to the quality agent. Quality runs whatever it considers appropriate: integration tests, end-to-end suites, manual exploration with `curl` or Playwright, log inspection, DB inspection against fixtures.

The two phases do not interleave. The quality agent does not run mid-round; the dev team does not patch mid-assessment. If quality finds something, it reports — and the coordinator either opens a new development round or accepts the finding.

### Tooling

The quality agent's tool belt is whatever the application demands:

- Integration test runners (`pytest tests/integration`, `cargo test --test`, `vitest run`, `playwright test`).
- Manual probes: `curl`, `httpie`, browser automation, log tailing, DB queries against a test fixture.
- Static analysis at the system level: dead-code detection, dependency audits, schema diffs.

**Workspace-mutating commands belong here, exclusively.** Full-workspace builds, integration suites, mutation testing, dev servers, browser automation, and any other command that touches shared global state are off-limits to dev-team teammates (which run in parallel and would collide) and belong to the quality agent. The coordinator is the fallback if no quality agent exists; the dev team never runs them. The quality agent boots the full stack, drives it, tears it down — serialized by charter, not by luck.

### The outsider's posture

The other half of the quality agent's job is **qualitative assessment from outside any domain's mental model**. Domain agents rehydrate from their own notes and decisions — they know why every choice was made and what every cryptic variable means. The quality agent does not. That gap is the feature, not a bug.

Questions the quality agent should hold open every assessment:

- **Legibility.** Reading the code or output cold, can a newcomer follow what's happening? Are names doing real work?
- **Error messages.** When something goes wrong, does the message describe *what* failed, *why*, and *what the user should do next*? Or is it a stack trace and a prayer?
- **System sense-making.** Does the overall behavior match a user's reasonable expectation? Are there silent failures? Surprising successes?
- **Onboarding friction.** If a new developer (or user) sat down to use this today, where would they get stuck?

Findings here come back as prose in `.agents/quality/decisions/<date>-assessment.md`, not as test failures. The coordinator decides what to act on.

### When to add one

- Strongly recommended for any multi-domain project that has, or will have, integration tests.
- Strongly recommended for any user-facing system (CLI, web app, API) where "does the experience make sense to someone new?" is a real question.
- Skippable for tiny single-domain projects or pure libraries with strong unit-test coverage and no user-facing surface — though even there, the outsider's-perspective half can be useful.

## Failure modes (and how to spot them)

| Symptom | Likely cause | Fix |
|---|---|---|
| Coordinator hits a hook denial citing a domain | Coordinator is doing work it should delegate | Send a message to the named owner instead |
| Teammate hits a hook denial naming another domain | Boundary is wrong, or task was mis-routed | Coordinator re-routes, or `.agents/_shared/AGENTS.md` gets revised |
| Teammate hits a denial citing "no owner" | New territory has no domain | Coordinator either claims it under an existing domain or proposes a new one |
| Two domains constantly need to update each other's contracts | The interface lives in the wrong place | Promote the contract to `_shared/contracts/`, gate changes on multi-domain ack |
| Notes never get written | End-of-session hygiene skipped | Add to coordinator's end-of-turn checklist; without notes, every session starts blind |
| Two teammates' builds / dev servers / mutation runs collide | Workspace-mutating action was run by a dev-team teammate | Reaffirm the contract: workspace-mutating runs belong to the quality agent (or coordinator). Dev team runs only scope-local checks and signals status back |
| Coordinator always delegates serially, one teammate at a time | Forgetting that disjoint ownership makes parallel work safe | Spawn independent domains in parallel; serialize only on real cross-domain dependencies |
| Quality agent runs mid-development-round and reports churn | Round-then-assess rhythm not respected | Let the dev round settle to a coherent state before invoking quality; don't interleave |

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
