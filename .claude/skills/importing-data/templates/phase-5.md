# Quality Assessment Report: [dataset_name]

## Objective
Systematically detect data quality issues in raw_[table_name] to inform cleaning-data skill.

## Import Summary
- **Source CSV:** [path to original CSV]
- **Raw table:** raw_[table_name]
- **Rows imported:** [count]
- **Import date:** [timestamp from Phase 4]

## Table Schema
```
[Paste PRAGMA table_info output from sub-agent]
```

## Data Completeness

### NULL Analysis

| Column | Non-NULL Count | NULL Count | NULL % |
|--------|----------------|------------|--------|
| [col1] | [count]        | [count]    | [%]    |
| [col2] | [count]        | [count]    | [%]    |
| ...    | ...            | ...        | ...    |

**Columns with >10% NULLs (require attention):**
- [column_name]: [%] NULL - [impact assessment]
- [column_name]: [%] NULL - [impact assessment]

## Duplicate Detection

**Exact duplicates found:** [count] rows

[If duplicates found:]
```
[Paste examples from sub-agent - first 5-10 duplicate groups]
```

**Assessment:** [Are these true duplicates or expected repeated values?]

## Outlier Detection

### [Numeric Column 1]
- **Mean:** [value]
- **MAD:** [value]
- **Min:** [value]
- **Max:** [value]
- **Outliers (>3 MAD):** [count] rows

[Repeat for each numeric column]

**Columns with outliers requiring investigation:**
- [column_name]: [count] outliers - [min/max values]
- [column_name]: [count] outliers - [min/max values]

## Free Text Candidates

**Columns with high uniqueness (>50%):**

| Column | Unique Values | Total Values | Uniqueness % | Categorization Priority |
|--------|---------------|--------------|--------------|-------------------------|
| [col]  | [count]       | [count]      | [%]          | [High/Medium/Low]       |

**Recommended for categorization:**
- [column_name]: [unique count] values - [brief description of content]

## Foreign Key Relationships

[If multiple tables exist, include FK detection results. If single table: "N/A - Single table analysis"]

### High Confidence Relationships (>95% integrity)

#### [child_table].[fk_column] → [parent_table].[pk_column]
- **Relationship Type:** [One-to-one / Many-to-one / Many-to-many]
- **Match Percentage:** [XX.X]%
- **Cardinality:** Avg [X.X] children per parent (min: [N], max: [N])
- **NULL FKs:** [count] rows ([X]%)
- **Orphaned FKs:** [count] rows ([X]%)
- **Join Recommendation:** [LEFT / INNER] JOIN
- **Cleaning Priority:** [HIGH / MEDIUM / LOW]

[Repeat for each high-confidence relationship]

### Medium Confidence Relationships (80-95% integrity)

[If any exist:]
#### [child_table].[fk_column] → [parent_table].[pk_column]
- **Match Percentage:** [XX.X]%
- **Orphaned FKs:** [count] rows ([X]%)
- **Issue:** [Description of integrity concerns]
- **Recommendation:** [Investigate / Validate / Review before joining]

### Referential Integrity Summary

**Total FK relationships detected:** [count]
- High confidence: [count]
- Medium confidence: [count]
- Low confidence / Unconfirmed: [count]

**Orphaned records across all relationships:** [count] ([X]% of total child records)

**Impact on Analysis:**
- [count] records will be excluded if using INNER JOINs
- Recommended approach: Use LEFT JOIN, filter NULLs in WHERE clause if needed

## Additional Quality Concerns

[List any other issues found by sub-agent:]
- Type inconsistencies
- Invalid values
- Date range issues
- Suspicious patterns

## Summary of Findings

**Critical issues (must address in cleaning-data):**
1. [Issue description with severity]
2. [Issue description with severity]

**Non-critical issues (address if time permits):**
1. [Issue description]
2. [Issue description]

## Recommended Actions for cleaning-data

1. **Phase 1 (Scope):** Review FK relationships and orphaned records from this report
2. **Phase 2 (Issue Detection):** Deep-dive investigation of [specific issues including FK orphans]
3. **Phase 3 (Strategy):** Decide approach for [duplicates/outliers/free text/FK orphans]
4. **Phase 4 (Execution):** Apply transformations including FK integrity enforcement and create clean_* tables

## Next Steps
Proceed to cleaning-data skill with this quality report as input.
