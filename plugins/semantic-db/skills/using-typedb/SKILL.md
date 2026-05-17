---
name: using-typedb
description: Use when interacting with a TypeDB 3.x database via the typedb MCP tools (typedb-query, typedb-database_schema, etc.) - covers schema-first workflow, transaction types, TypeQL 3.x syntax (which differs materially from 2.x), and the most common failure modes
user-invocable: false
---

# Using TypeDB

You are about to interact with a TypeDB 3.x knowledge graph through the `typedb` MCP tool family. This skill exists because **most TypeQL knowledge in your training data is for TypeDB 2.x, and TypeQL 3.x is a different language**. Treat your priors as stale and verify against the live schema.

Announce: "I'm using the using-typedb skill to interact with the TypeDB database."

## The cardinal rules

1. **TypeDB 3.x is not 2.x.** If you remember TypeQL from training, assume it is wrong until verified. Notable changes: `get` is gone (use `fetch`), `sub entity`/`sub relation`/`sub attribute` is gone for top-level type declarations (you write `entity person` directly), `abstract` is now `@abstract`, `regex` is now `@regex(...)`, cardinality is `@card(...)`, enums are `@values(...)`.
2. **Always fetch the schema before writing a query.** Never write TypeQL from memory of "what the schema probably is." Use `typedb-database_schema` first.
3. **Pick the right transaction type or nothing works.** `read` for `match`/`fetch`, `write` for `insert`/`update`/`delete`, `schema` for `define`/`redefine`/`undefine`. The MCP error when you get this wrong is not always obvious — this is the #1 first failure for new agents.
4. **Verify every write.** After an insert or delete, run a small `match … fetch { $x.* };` to confirm the data actually lives. "Ran the write, didn't verify" is a failure mode, not a workflow.
5. **Never `database_delete` without explicit user permission**, and never run a `schema` transaction on a production database without first stating what you are about to change.

## Workflow

### Step 1 — read the schema

```
typedb-database_schema(name="<db>")
```

Returns the full `define` text. Read it. Identify the types, their attributes, their relations, the roles in each relation, and the cardinality/value annotations. Only then write a query.

### Step 2 — write the query against the actual schema

Use TypeQL 3.x. The patterns below are verified against the 3.x docs.

**Fetch all attributes of matched entities:**

```typeql
match $x isa person;
fetch { $x.* };
```

**Fetch specific attributes and nest sub-queries:**

```typeql
match
  $u isa user, has username $name;
fetch {
  "name": $name,
  "all_attributes": { $u.* },
  "friends": [
    match friendship ($u, $other);
    fetch { "friend": $other.username };
  ]
};
```

**Insert an entity:**

```typeql
insert
  $p isa person, has name "Alice", has email "alice@example.com";
```

**Insert a relation by binding role players:**

```typeql
insert
  $r isa friendship (friend: $a, friend: $b);
```

(You'll need a `match` clause before `insert` to bind `$a` and `$b` to existing entities.)

**Delete an attribute (inverted `has`):**

```typeql
match $p isa person, has email $e;
delete has $e of $p;
```

**Delete an entity:**

```typeql
match $p isa person, has name "Alice";
delete $p;
```

### Step 3 — verify

After any write, run a read query that would observe what you just wrote. If the row isn't there, the transaction didn't commit or your match pattern is wrong — investigate before continuing.

## Transaction types — table

| Operation | `transaction_type` |
|---|---|
| `match … fetch …;` | `read` |
| `match … return …;` (aggregations) | `read` |
| `insert …;` | `write` |
| `match … insert …;` | `write` |
| `match … delete …;` | `write` |
| `define …;` / `redefine …;` / `undefine …;` | `schema` |

Running a `define` under `write` fails. Running an `insert` under `schema` fails. There is no auto-detection.

## Schema changes — `define` vs `redefine` vs `undefine`

- **`define`** adds new types, attributes, or relations. Idempotent for additions.
- **`redefine`** can change *annotations only* (e.g. swap `@card(0..1)` for `@card(1..1)`, change `@regex`). It **cannot** change structural declarations like `sub`, `owns`, `plays`, or `relates`.
- **`undefine`** removes a declaration. To change a structural declaration, you must `undefine` it and then `define` the new shape — in that order, in separate statements (often in two separate schema transactions if data depends on the old shape).

If you find yourself wanting `redefine entity foo, owns bar;` to change the cardinality of `bar`, you actually want to redefine the annotation on the `owns` line — not the structural relationship.

## The 3.x gotchas that bite

### Naming conventions

TypeDB convention is **kebab-case for types** (`asset-tag`, `strategy-outcome-link`, `ost-node`) and **snake_case for attributes** (`hypothesis_text`, `created_at`, `lifecycle_state`). LLMs default to camelCase; do not. Match the casing in the live schema exactly.

### Attribute subtyping

In 3.x, attributes can be subtyped to enforce ID-shape distinctions:

```typeql
attribute ost_id @abstract, value string;
attribute outcome_id, sub ost_id, value string @regex("^O_[0-9]{4}$");
attribute tactic_id,  sub ost_id, value string @regex("^T_[0-9]{4}$");
```

An entity that `owns outcome_id` cannot accidentally `has tactic_id "O_0001"` — the type system enforces shape. This is intentional. Honor it: when inserting, use the right subtype's value, and trust regex enforcement to catch mistakes.

### Regex double-escaping through MCP

Regexes pass through MCP → JSON → TypeQL and get **double-escaped**. A regex containing `\s` will arrive at TypeDB as `\\\\s` if you escape naively. Test patterns end-to-end before relying on them, and **prefer permissive patterns** (`.+`, `.*`) over character classes that need escapes. This is a real bug we've hit.

### Cardinality on relation roles

Relations declare per-role cardinality:

```typeql
relation tactic-task,
  relates tactic @card(1..1),
  relates task   @card(1..1);
```

`@card(1..1)` means exactly one role player. To delete an entity that plays a `@card(1..1)` role, you must **delete the relation first, then the entity** — otherwise the cardinality constraint is violated mid-delete. Two-stage delete:

```typeql
# Stage 1: remove the relation
match
  $t isa task, has task_id "K_00000001";
  $r isa tactic-task (task: $t);
delete $r;

# Stage 2: remove the entity
match $t isa task, has task_id "K_00000001";
delete $t;
```

### `@values(...)` enums

```typeql
attribute lifecycle_state, value string @values("hypothetical", "validated", "falsified");
```

Inserting any other string fails. Don't invent new states — extend the schema deliberately if you need a new one, and surface that decision to the human user.

### Roles are scoped to relations

A role like `outcome` in `strategy-outcome-link` is not the same thing as a role `outcome` in some other relation. When binding role players in an `insert`, the relation type determines which role names are legal:

```typeql
insert $link isa strategy-outcome-link (strategy: $s, outcome: $o), ... ;
```

Use the role names exactly as declared in `relates` clauses in the schema.

## Reading the schema critically

When `typedb-database_schema` returns, scan for:

- **Subtype hierarchies** (`entity foo @abstract` with concrete subtypes) — the abstract type can't be instantiated; queries for `$x isa foo` will return all subtypes.
- **`@key` vs `@card(1..1)`** — `@key` is unique and required; `@card(1..1)` is required but not unique.
- **Role-relation graph** — list every `plays X:Y` on entities and every `relates Y` on relations. That tells you the legal shape of inserts.
- **`@regex` on IDs** — your generated IDs must match, or insert fails.
- **`@values` enums** — your strings must be in the allowed set.

## When you don't know

- "I don't know what type to use here — let me read the schema first" is correct.
- "The schema doesn't have a place for this concept" is a real answer; surface it to the user rather than inventing types.
- "I tried this and the MCP returned an error" — paste the actual error to the user; do not paper over it with a different query.

## Don'ts

- Don't `database_delete` without explicit permission.
- Don't run `schema` transactions on production without stating the diff first.
- Don't write queries from memory of the schema.
- Don't assume 2.x syntax works.
- Don't claim a write succeeded without a verifying read.
- Don't invent new enum values or asset kinds — extend the schema deliberately.
