# outcomes

A Claude Code plugin teaching agents how to read and write the **OST (Outcome / Strategy / Tactic) Framework** as it lives in the `agents` TypeDB database on edge-01.

This is the domain layer. It pairs with [`semantic-db`](../semantic-db), which covers the TypeDB 3.x substrate itself. Install both: `outcomes` describes *what* the OST schema means and what discipline to enforce; `semantic-db` describes *how* to actually query a TypeDB database without making 2.x-vs-3.x mistakes.

## What's in here

- `skills/using-ost-framework/SKILL.md` — the only skill. Auto-invoked (`user-invocable: false`) when an agent is reading or writing OST data.

## What it covers

- The three layers (Outcome / Strategy / Tactic) and their diagnostic gates.
- The falsifiability rubric on `strategy-outcome-link` and `tactic-strategy-link` — hypothesis + invalidation trigger + deadline + lifecycle.
- Structured Task fields (`problem_statement`, `acceptance_criteria`, `definition_of_done`) — no generic descriptions.
- AssetTag URI conventions and how they bridge to *other* TypeDB databases.
- ID allocation (`O_NNNN`, `S_NNNN`, `T_NNNN`, `K_NNNNNNNN`) and link-id derivation.
- Canonical read queries (downward traversal, overdue-hypothetical-links, orphan smell).
- Canonical write workflow for a full Outcome→Strategy→Tactic→Task chain.
- A refusal list — vague hypotheses, Jira-ticket-shaped outcomes, trade-off-free strategies, asset-less tactics, AC-less tasks.

## Composition

This skill assumes `using-typedb` is available and links to it for query mechanics rather than re-explaining TypeQL 3.x. Install both plugins together.

## Source of truth

The skill's schema cheat-sheet was generated from the live `agents` database schema as of 2026-05-17. **The skill instructs agents to fetch the live schema themselves before writing** — when the schema evolves, the cheat-sheet may lag, but the live schema is always authoritative.
