---
name: using-ost-framework
description: Use when reading or writing OST (Outcome / Strategy / Tactic) graph data in the `agents` TypeDB database - covers the falsifiability rubric, the three-layer discipline, ID conventions, lifecycle transitions, and the structured Task fields that replace generic descriptions
user-invocable: false
---

# Using the OST Framework

You are working with the **OST (Outcome / Strategy / Tactic) Framework** as it is implemented in the `agents` TypeDB database on edge-01. OST is a goal-decomposition discipline. The point of encoding it as a graph is that **the links between layers carry falsifiable hypotheses** — not just arrows, but claims that could be wrong.

Announce: "I'm using the using-ost-framework skill to work with the OST graph."

**This skill assumes the [`using-typedb`](../../../semantic-db/skills/using-typedb/SKILL.md) substrate skill.** Use that for actual query mechanics, transaction types, and 3.x syntax. This skill covers what to model, what the rubric requires, and what to refuse.

> **Before anything else, run `typedb-database_schema(name="agents")` and read it.** The shape encoded here may have evolved; this skill captures the design intent, not a frozen snapshot.

## The three layers, with their gates

### Outcome — a state of being

Solution-agnostic. Must pass three gates:

- **Why? gate** — There is a concrete reason this matters beyond "the metric should go up." If the outcome reduces to "improve X," X needs to be something that matters in itself.
- **How else? gate** — At least one *other* plausible strategy could achieve it. If only one strategy fits, you are looking at a strategy in disguise, not an outcome.
- **Jira ticket test** — The outcome **must not** be expressible as a single closable ticket. If it can be closed by writing some code and shipping it, it is a tactic, not an outcome.

If a proposed outcome fails any gate, **refuse to insert it**. Surface the failure to the user and propose either reframing it upward (to a real outcome) or pushing it downward (it's actually a strategy or tactic).

### Strategy — a systemic hypothesis with explicit trade-offs

A strategy must **name what it is giving up**. "Be excellent at everything" is not a strategy. Good strategies look like:

> "Prioritize latency over throughput on the inference path by routing all requests through a single hot replica; we are accepting reduced fault tolerance to do this."

If the description has no trade-off, the strategy is not a strategy. Refuse to insert it.

### Tactic — an asset-specific deliverable

A tactic must point at one or more **AssetTags** (`tactic-targets-asset-tag` relation). If you cannot name the asset (repository, microservice, endpoint, config, hardware, contract, design, workflow), the tactic is not a tactic — it is a strategy in disguise.

### Task — implementation work under a tactic

One task serves exactly one tactic (`tactic-task` relation, `@card(1..1)` on both sides). Tasks use **structured fields**, not generic descriptions:

- `problem_statement` (required, `@card(1..1)`) — what is wrong now.
- `solution_statement` (optional) — what we plan to do.
- `acceptance_criteria` (optional, but strongly preferred) — observable conditions for success.
- `definition_of_done` (optional, strongly preferred) — checklist for completeness.
- `kanban_state` — one of `backlog | ready | in_progress | in_review | blocked | done | cancelled`.

**Tasks do NOT carry hypotheses.** Falsifiability lives strictly at the strategic layer (the two link relations). Tasks validate via `acceptance_criteria` and `definition_of_done`. If you find yourself wanting to attach a hypothesis to a task, the falsifiability belongs one level up, on the tactic→strategy link.

Refuse to insert a task without `problem_statement`, and warn loudly if `acceptance_criteria` is missing.

## Falsifiability — the heart of OST

Every `strategy-outcome-link` and every `tactic-strategy-link` carries four mandatory attributes (all `@card(1..1)`):

| Attribute | What it must contain |
|---|---|
| `hypothesis_text` | A concrete, falsifiable claim. "Doing X will move Y by Z within N." |
| `invalidation_trigger_text` | The specific observation that would force abandonment. Name a number where possible. |
| `evaluation_deadline` | A `datetime`. Far enough out that real evidence can accumulate; near enough that the link does not drift. |
| `lifecycle_state` | One of `hypothetical \| validated \| falsified`. New links start `hypothetical`. |

### What gets refused

- "This will help things." — Not falsifiable. Refuse.
- "We expect improvement in user satisfaction." — Not specific. Demand a number and a deadline.
- A hypothesis without an invalidation trigger. — Refuse. Without the trigger you cannot ever falsify the link, which means it isn't a hypothesis.
- An evaluation deadline of "TBD" or far past. — Refuse. Pick a real date.

If the user cannot write a falsifiable hypothesis for the link, **that is the signal that the strategy isn't really a strategy**. Surface it. Do not paper over by writing a soft hypothesis.

### Lifecycle transitions

- `hypothetical` → `validated` — only with stated evidence that the hypothesis held. A human decides; agents do not auto-validate. Ask the user explicitly: "I have evidence X, Y, Z that this link held. Mark it `validated`?"
- `hypothetical` → `falsified` — when the `invalidation_trigger_text` condition is observed, or the `evaluation_deadline` passes without supporting evidence. Again, human-confirmed.
- Once `validated` or `falsified`, a link is a historical record. Do not flip it back to `hypothetical`.

## The schema cheat-sheet (verify against the live one)

Entity types: `outcome`, `strategy`, `tactic`, `task`, `asset-tag`, `prd`, `adr`.
All of `outcome / strategy / tactic / task` are subtypes of the abstract `ost-node` and own `label @card(1..1)`, `description @card(0..1)`, `created_at @card(1..1)`, plus their typed id.

Relations:

- `strategy-outcome-link` — relates `outcome` (1..1) and `strategy` (1..1); owns the four falsifiability attributes plus `strategy_outcome_link_id @key`.
- `tactic-strategy-link` — relates `strategy` (1..1) and `tactic` (1..1); same falsifiability attributes plus `tactic_strategy_link_id @key`.
- `tactic-targets-asset-tag` — relates `tactic` (1..) and `asset_tag` (1..). Many-to-many.
- `tactic-task` — relates `tactic` (1..1) and `task` (1..1). Strictly 1:1.
- `prd-documents-strategy` — relates `prd` (1..1) and `strategy` (1..1). Optional documentation.
- `adr-documents-tactic` — relates `adr` (1..1) and `tactic` (1..1). Optional documentation.

ID regex (enforced by `@regex` on subtyped id attributes):

| Entity | Pattern |
|---|---|
| outcome | `^O_[0-9]{4}$` |
| strategy | `^S_[0-9]{4}$` |
| tactic | `^T_[0-9]{4}$` |
| task | `^K_[0-9]{8}$` |
| strategy-outcome-link | `^LINK_S_[0-9]{4}-O_[0-9]{4}$` |
| tactic-strategy-link | `^LINK_T_[0-9]{4}-S_[0-9]{4}$` |
| asset-tag | `^(repository\|microservice\|endpoint\|config\|hardware\|contract\|design\|workflow)://.+$` |
| prd | `^PRD_[0-9]{4}$` |
| adr | `^ADR_[0-9]{4}$` |

Asset-tag `asset_tag_kind` is a fixed enum: `repository, microservice, endpoint, config, hardware, contract, design, workflow`. **Do not invent new kinds.** If the asset doesn't fit, surface that to the user — extending the enum is a deliberate schema change.

## ID allocation

Before inserting a new node, query for the highest existing id of that type, then increment. Example for outcomes:

```typeql
match $o isa outcome, has outcome_id $id;
fetch { "id": $id };
```

Sort client-side, take the max, increment, format with the right zero-padding (`O_0001` → `O_0042` → `O_0100`).

For links, the id is derived: `LINK_<strategy_id>-<outcome_id>` or `LINK_<tactic_id>-<strategy_id>`. Build it deterministically from the endpoints; do not allocate a counter.

## Reading workflow — common queries

### Traverse from an outcome down to its open tasks

```typeql
match
  $o isa outcome, has outcome_id "O_0001";
  $sol isa strategy-outcome-link (outcome: $o, strategy: $s);
  $tsl isa tactic-strategy-link  (strategy: $s, tactic: $t);
  $tt  isa tactic-task           (tactic: $t,  task: $k);
  $k has kanban_state $state;
  $state != "done"; $state != "cancelled";
fetch {
  "outcome": { $o.* },
  "strategy": { $s.* },
  "tactic": { $t.* },
  "task": { $k.* }
};
```

### Find overdue hypothetical links

```typeql
match
  $l isa strategy-outcome-link,
    has lifecycle_state "hypothetical",
    has evaluation_deadline $d;
  $d < 2026-05-17T00:00:00;
fetch { "link": { $l.* } };
```

Run with today's date. The same pattern works for `tactic-strategy-link`. Surface results to the user for triage — do not auto-flip lifecycle.

### Find orphan nodes (smell)

A tactic with no `tactic-strategy-link`, or a strategy with no `strategy-outcome-link`, is usually a modeling mistake. Query for entities without their expected upward relation and surface them.

### Find all tactics targeting a given asset

```typeql
match
  $a isa asset-tag, has asset_tag_id "microservice://typedb";
  $r isa tactic-targets-asset-tag (asset_tag: $a, tactic: $t);
fetch { "tactic": { $t.* } };
```

This is the bridge: rich data about `microservice://typedb` lives in **other** TypeDB databases keyed by the same URI. Do not duplicate asset data into the OST graph.

## Writing workflow — full Outcome→Strategy→Tactic→Task chain

Each of these is a separate `write` transaction (and the schema must already be in place). Use `using-typedb` for the actual mechanics. Sketch:

1. **Insert outcome.** Allocate `O_NNNN`, write `label`, `description`, `created_at`.
2. **Insert strategy.** Allocate `S_NNNN`, write fields. Description must name a trade-off.
3. **Insert `strategy-outcome-link`** binding the two, with `hypothesis_text`, `invalidation_trigger_text`, `evaluation_deadline`, `lifecycle_state="hypothetical"`, and id `LINK_S_NNNN-O_NNNN`.
4. **Insert tactic.** Allocate `T_NNNN`, write fields.
5. **Insert `tactic-strategy-link`** with full falsifiability quad.
6. **Insert/locate asset-tag(s)** and bind via `tactic-targets-asset-tag`.
7. **Insert task.** Allocate `K_NNNNNNNN`, write `problem_statement` (required), `acceptance_criteria`, `definition_of_done`, `kanban_state="backlog"`.
8. **Insert `tactic-task`** relation.
9. **Verify** by running the downward-traversal query above with the new `O_NNNN` — confirm the whole chain comes back.

## Cross-database linkage

AssetTag URIs (`microservice://typedb`, `repository://prediction-trader`, `design://ost-rubric-v1`) are how OST refers to assets whose rich data lives in **other** databases on the same TypeDB instance. Keep OST narrow:

- An asset-tag in OST owns `asset_tag_id @key`, `asset_tag_kind`, `created_at`, and optionally `description` and `label`. That is it.
- Resist the urge to add asset-detail attributes (versions, ports, owners, dashboards) onto asset-tag. Those belong in the asset's home database, keyed by the same URI.

## What this skill refuses

| Refused thing | Why |
|---|---|
| Outcome that passes the Jira ticket test | It's a tactic, not an outcome. |
| Strategy description with no trade-off | Not a strategy. |
| Link without falsifiable `hypothesis_text` | Defeats the entire framework. |
| Link without `invalidation_trigger_text` | Hypothesis cannot be falsified → not a hypothesis. |
| Link with `evaluation_deadline` in the past or "TBD" | Deadline must be real. |
| Tactic without at least one `tactic-targets-asset-tag` binding | Not a tactic. |
| Task without `problem_statement` | Required by schema; also: violates task discipline. |
| Task carrying its own hypothesis | Falsifiability lives at the strategic layer. AC + DoD are the task's test. |
| New `asset_tag_kind` value | Enum is fixed in schema; extension is a deliberate schema change. |
| Auto-flipping a link to `validated` | Humans validate. Always ask. |

## When in doubt

- "I don't know what level this belongs at" — fine answer. Walk through the gates with the user.
- "The user described a tactic but is calling it an outcome" — flag it gently before writing anything.
- "There is no good asset-tag for this tactic" — surface it. Maybe a new asset needs to exist first.
- "The hypothesis the user gave isn't falsifiable" — say so directly. Propose a sharper one.
