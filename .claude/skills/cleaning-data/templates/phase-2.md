# Detected Issues Report: [dataset_name]

## Objective
Deep-dive investigation of data quality issues identified in Phase 1 scope using sub-agent delegation.

## Detection 1: Duplicate Records

### Exact Duplicates

**Detection Method:** GROUP BY all key columns, COUNT(*) > 1

**Summary:**
- **Total duplicate groups:** [N]
- **Total duplicate records:** [N] (excludes first occurrence in each group)
- **Percentage of dataset:** [X%]

**Top Duplicate Groups:**

| Group # | Key Values | Occurrence Count | Example IDs |
|---------|------------|------------------|-------------|
| 1 | [values] | [N] | [IDs] |
| 2 | [values] | [N] | [IDs] |
| ... | ... | ... | ... |

**Analysis:**
[Are these true duplicates or expected repeated values? Pattern observations?]

### Near-Duplicates (Fuzzy Matching)

**Detection Method:** Python fuzzy string matching (>90% similarity threshold)

**Summary:**
- **Fuzzy groups found:** [N]
- **High confidence (>95%):** [N groups]
- **Medium confidence (90-95%):** [N groups]

**High Confidence Groups (Likely Merge Candidates):**

| Group # | Values | Similarity | IDs | Recommended Action |
|---------|--------|------------|-----|---------------------|
| 1 | "[value1]" vs "[value2]" | 97% | [IDs] | Merge to "[canonical]" |
| 2 | "[value1]" vs "[value2]" | 95% | [IDs] | Merge to "[canonical]" |

**Medium Confidence Groups (Manual Review Needed):**

| Group # | Values | Similarity | IDs | Recommended Action |
|---------|--------|------------|-----|---------------------|
| 1 | "[value1]" vs "[value2]" | 92% | [IDs] | Review - may be distinct |

**Analysis:**
[Which fuzzy groups should be merged? Which need manual review?]

---

## Detection 2: Outliers (MAD-Based)

### [Numeric Column 1]

**Statistics:**
- **Median:** [value]
- **MAD:** [value]
- **Min:** [value]
- **Max:** [value]
- **3 MAD threshold:** [value]

**Outlier Summary:**
- **Total outliers (>3 MAD):** [N]
- **Extreme (>5 MAD):** [N]
- **Significant (3-5 MAD):** [N]

**Top Outlier Examples:**

| Row ID | Value | MAD Distance | Context/Pattern |
|--------|-------|--------------|-----------------|
| [ID] | [value] | [X] MAD | [e.g., "Dec 2024 spike"] |
| [ID] | [value] | [X] MAD | [context] |

**Analysis:**
[Are these data errors or legitimate? Pattern observed? Recommended action?]

[Repeat for each numeric column flagged in Phase 1]

---

## Detection 3: Free Text Issues

[If free text columns were in scope:]

### [Text Column Name]

**Unique Values:** [N]
**Total Values:** [N]
**Uniqueness:** [X%]

**Categorization Assessment:**
[Can values be grouped into categories? Natural groupings identified?]

[If sub-agent analyzed free text for categorization, include findings here]

---

## Detection 4: Referential Integrity Violations

[If multiple tables with FK relationships:]

### [child_table].[fk_column] → [parent_table].[pk_column]

**Relationship Confirmation:**
- Match percentage: [XX.X]% (from importing-data: [XX.X]%)
- Relationship type: [One-to-one / Many-to-one / Many-to-many]
- Cardinality: Avg [X.X] children per parent

**Orphaned Records:**
- Total orphaned: [N] rows ([X]% of child table)
- Sample orphaned values:
  - [value1]: [count] occurrences
  - [value2]: [count] occurrences

**Orphan Pattern Analysis:**
- **Recency:** [Most orphans are <recent/old>, detailed breakdown:]
  - Last 7 days: [N] orphans
  - Last 30 days: [N] orphans
  - Older than 90 days: [N] orphans
- **Pattern observed:** [e.g., "All orphans are from Q1 2024", "No clear pattern"]
- **Potential cause:** [e.g., "Parent records deleted", "Data entry lag", "Import order issue"]

**Impact Assessment:**
- **INNER JOIN impact:** [N] child records excluded ([X]% of total)
- **LEFT JOIN impact:** [N] child records will have NULL parent fields
- **Analysis affected:** [Which queries/analyses depend on this relationship?]

**Recommended Action:**
- [Exclude orphans / Flag for review / Preserve with NULL / Create placeholder parent]
- Rationale: [Why this approach based on pattern analysis]

[Repeat for each FK relationship requiring attention]

[If single table: "N/A - Single table analysis"]

---

## Cross-Issue Analysis

### Records with Multiple Issues

[Do any records have BOTH duplicates AND outliers? List overlaps.]

| Row ID | Issues | Impact |
|--------|--------|--------|
| [ID] | Duplicate + Outlier | [Decision needed] |

---

## Summary of All Findings

### Issue Counts by Type

| Issue Type | Count | % of Dataset | Severity Assessment |
|-----------|-------|--------------|---------------------|
| Exact Duplicates | [N] | [X%] | [High/Medium/Low] |
| Near-Duplicates | [N] | [X%] | [High/Medium/Low] |
| Outliers ([col]) | [N] | [X%] | [High/Medium/Low] |
| Free Text | [N unique] | [X%] | [High/Medium/Low] |
| FK Orphans ([relationship]) | [N] | [X%] | [High/Medium/Low] |

### Records Flagged for Manual Review

**High Priority Review:**
- [Row IDs and reasons]

**Medium Priority Review:**
- [Row IDs and reasons]

---

## Implications for Phase 3 (Strategy Design)

Based on detected issues, Phase 3 must address:

1. **Duplicate Strategy:**
   - Exact duplicates: [Keep first / Keep most complete / Merge approach]
   - Near-duplicates: [Auto-merge high confidence / Manual review medium confidence]

2. **Outlier Strategy:**
   - [Column]: [Exclude / Cap at threshold / Flag for review / Keep as-is]
   - [Column]: [approach]

3. **Free Text Strategy:**
   - [Column]: [Categorization schema / Manual mapping / Keep as-is]

4. **FK Orphan Strategy (if multiple tables):**
   - [Relationship]: [Exclude orphans / Preserve with NULL / Flag for review / Create placeholder parent]
   - [Relationship]: [approach]

5. **Records to Exclude:**
   - [List specific IDs or criteria for exclusion]

6. **User Decisions Needed:**
   - [Which issues require user input in Phase 3?]

## Next Steps
Proceed to Phase 3: Cleaning Strategy Design with user confirmation on approaches.
