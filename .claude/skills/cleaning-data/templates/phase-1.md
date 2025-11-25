# Cleaning Scope: [dataset_name]

## Data Source
- **Source Skill:** importing-data
- **Raw Table:** raw_[table_name]
- **Quality Report Reference:** 05-quality-report.md (from importing-data)
- **Rows in raw table:** [N]

## Quality Issues Summary

[Extracted from 05-quality-report.md:]

### Completeness Issues
- **Columns with >10% NULLs:**
  - [column_name]: [X]% NULL ([N] rows)
  - [column_name]: [X]% NULL ([N] rows)

### Duplicate Issues
- **Exact duplicates:** [N] rows ([X]% of total)
- **Near-duplicates:** [Estimated count if flagged]

### Outlier Issues
- **[Numeric column]:** [N] outliers (>3 MAD)
- **[Numeric column]:** [N] outliers (>3 MAD)

### Free Text Issues
- **[Text column]:** [N] unique values ([X]% uniqueness) - categorization candidate
- **[Text column]:** [N] unique values ([X]% uniqueness) - categorization candidate

### Referential Integrity Issues

[If multiple tables analyzed in importing-data:]

- **[child_table].[fk_column] → [parent_table].[pk_column]:**
  - Orphaned records: [N] ([X]% of child table)
  - Match confidence: [High/Medium/Low] ([XX]% integrity)
  - Relationship type: [One-to-one / Many-to-one / Many-to-many]
  - Recommended action: [Exclude orphans / Flag for review / Preserve with NULL / Create placeholder parent]

[If single table: "N/A - Single table analysis"]

## Issue Prioritization

| Issue | Impact | Severity | Effort | Priority | Rationale |
|-------|--------|----------|--------|----------|-----------|
| [Issue description] | High | Critical | Low | **CRITICAL** | [Why this matters] |
| [Issue description] | High | Significant | Medium | **HIGH** | [Why this matters] |
| [Issue description] | Medium | Significant | Low | **HIGH** | [Why this matters] |
| [Issue description] | Low | Minor | Low | **LOW** | [Can skip or document] |

## Cleaning Objectives

Based on prioritization, the cleaning objectives are:

1. **Address CRITICAL issues:** [List specific actions]
   - Expected impact: [% of rows affected, data quality improvement]

2. **Address HIGH priority issues:** [List specific actions]
   - Expected impact: [% of rows affected, data quality improvement]

3. **Document MEDIUM/LOW priority issues:** [List what won't be addressed and why]
   - Rationale: [Effort vs benefit trade-off]

## Success Criteria

After cleaning, the clean_[table_name] table MUST meet:
- [ ] All CRITICAL issues resolved
- [ ] All HIGH priority issues resolved
- [ ] All transformations documented with before/after counts
- [ ] All exclusions documented with rationale
- [ ] Verification queries confirm success

## Next Steps
Proceed to Phase 2: Issue Detection (Agent-Delegated) for deep-dive investigation of prioritized issues.
