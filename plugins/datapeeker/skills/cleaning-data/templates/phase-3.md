# Cleaning Strategy: [dataset_name]

## Objective
Define cleaning approach for all detected issues, with user-approved decisions for execution in Phase 4.

## Issue Summary from Phase 2

[Brief recap of issues detected]

- Exact duplicates: [N]
- Near-duplicates: [N]
- Outliers: [N per column]
- Free text columns: [N]
- Business rule violations: [N if applicable]

---

## Strategy 1: Duplicate Handling

### Exact Duplicates
**Chosen Approach:** [Option A/B/C]

**Rationale:** [Why this approach fits the data and use case]

**Implementation:**
- [Specific steps for execution]
- Expected exclusions: [N] rows ([X]%)

### Near-Duplicates
**Chosen Approach:** [Option A/B/C]

**Rationale:** [Why this approach]

**Implementation:**
- [Specific steps, including which groups to merge]
- Expected exclusions/merges: [N] rows

---

## Strategy 2: Outlier Handling

### [Numeric Column 1]
**Chosen Approach:** [Option A/B/C/D]

**Rationale:** [Why this approach for this column]

**Threshold:** [3 MAD or other value]

**Implementation:**
- [Specific SQL approach]
- Expected exclusions/caps: [N] rows ([X]%)

[Repeat for each numeric column]

---

## Strategy 3: Free Text Categorization

### [Text Column 1]
**Chosen Approach:** [Option A/B/C/D]

**Agent Proposal Review:**
- Categories proposed: [N]
- High confidence mappings: [N]
- Manual review needed: [N]

**Final Category Schema:**

| Category | Definition | Value Count |
|----------|------------|-------------|
| [Cat 1] | [Definition] | [N] |
| [Cat 2] | [Definition] | [N] |
| Other | [Uncategorized] | [N] |

**Implementation:**
- [SQL CASE statement or mapping table approach]
- Ambiguous values: [How handled]

[Repeat for each text column]

---

## Strategy 4: Referential Integrity (if multiple tables)

### [Relationship 1]: [child_table].[fk_column] → [parent_table].[pk_column]

**Orphaned Records:** [N] ([X]% of child table)

**Chosen Approach:** [Option A/B/C/D]

**Rationale:** [Why this approach for this relationship]

**Implementation:**
- [Specific SQL approach - filter, NULL update, flag addition, or placeholder insertion]
- Expected exclusions: [N] rows ([X]%) [if Option A]
- JOIN behavior impact: [How this affects downstream queries]

**Verification:**
- [How to confirm approach worked correctly]

[Repeat for each FK relationship]

[If single table: "N/A - Single table analysis"]

---

## Strategy 5: Business Rules (if applicable)

### Rule 1: [Rule Name]
**Validation:** [Constraint description]

**Violations Found:** [N] ([X]%)

**Chosen Approach:** [Option A/B/C]

**Implementation:** [How violations will be handled]

[Repeat for each rule]

---

## Exclusion Projections

**Estimated total exclusions:**

| Reason | Count | % of Dataset |
|--------|-------|--------------|
| Duplicates | [N] | [X]% |
| Outliers | [N] | [X]% |
| FK orphans (if excluded) | [N] | [X]% |
| Business rule violations | [N] | [X]% |
| Uncategorizable free text | [N] | [X]% |
| **TOTAL** | **[N]** | **[X]%** |

**Expected clean table size:** [raw count] - [exclusions] = [clean count] rows

---

## User Confirmation

- **Date:** [Timestamp]
- **Confirmed by:** [User]
- **Modifications from agent proposals:** [None / List changes]

## Next Steps
Proceed to Phase 4: Cleaning Execution with approved strategies.
