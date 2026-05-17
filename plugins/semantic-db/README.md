# semantic-db

A Claude Code plugin teaching agents how to interact with **TypeDB 3.x** semantic databases through the `typedb` MCP tools.

It is the substrate layer: it does not encode any particular schema. It pairs naturally with domain plugins like [`outcomes`](../outcomes) that describe specific schemas living inside a TypeDB database.

## What's in here

- `skills/using-typedb/SKILL.md` — the only skill. Auto-invoked (`user-invocable: false`) whenever an agent appears to be reaching for the `typedb-*` MCP tools.

## What it covers

- TypeDB 3.x ≠ 2.x — verified syntax for `fetch`, attribute subtyping, annotations.
- Schema-first workflow: fetch the live schema before writing queries.
- Transaction type discipline (`read` / `write` / `schema`) — the most common first failure.
- `define` vs `redefine` vs `undefine` — what each can change.
- Two-stage deletes under `@card(1..1)` constraints.
- The MCP → JSON → TypeQL regex double-escape gotcha.
- Verification-after-write as a workflow norm.

## Composition

Domain plugins (e.g. `outcomes`) should depend on this one in spirit: their skill text can say "use `using-typedb` for the actual queries" and link to a relation/entity in their schema, without re-explaining TypeQL itself.
