# Verification Report: [dataset_name]

## Objective
Validate cleaning transformations, quantify quality improvements, document complete audit trail.

## Executive Summary
- Raw table: [N] rows
- Clean table: [N] rows
- Total exclusions: [N] ([X]%)
- Verification status: ✓ All validations passed

## Row Count Reconciliation

**Critical validation - MUST match exactly:**

```sql
-- Count raw table
SELECT COUNT(*) as raw_count FROM raw_[table_name];
-- Result: [N]

-- Count clean table
SELECT COUNT(*) as clean_count FROM clean_[table_name];
-- Result: [N]

-- Calculate exclusions from Phase 4 log
-- Expected: raw_count = clean_count + total_exclusions
```

**Reconciliation Status:** ✓ Pass / ✗ Fail - [Explanation if fail]

## Transformation Verification

### Duplicate Removal Verification

```sql
-- Confirm no duplicates remain
SELECT [key_columns], COUNT(*) as occurrences
FROM clean_[table_name]
GROUP BY [key_columns]
HAVING COUNT(*) > 1;
-- Expected: 0 rows returned
```

**Result:** [Pass/Fail with details]

### Outlier Handling Verification

```sql
-- For Exclude approach: confirm no outliers remain
WITH stats AS ([median/MAD calculation])
SELECT COUNT(*) as remaining_outliers
FROM clean_[table_name], stats
WHERE ABS([numeric_col] - median) > 3 * mad;
-- Expected: 0 rows
```

**Result:** [Pass/Fail with details]

### Free Text Categorization Verification

```sql
-- Confirm all values categorized
SELECT COUNT(*) as uncategorized
FROM clean_[table_name]
WHERE [column]_category IS NULL;
-- Expected: 0 (unless "keep uncategorized" was strategy)

-- Verify category distribution
SELECT [column]_category, COUNT(*) as count,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (), 2) as pct
FROM clean_[table_name]
GROUP BY [column]_category
ORDER BY count DESC;
```

**Result:** [Distribution matches Phase 4 expectations]

### Business Rule Verification (if applicable)

```sql
-- Confirm no violations remain
SELECT COUNT(*) as violations
FROM clean_[table_name]
WHERE NOT ([rule_1_condition] AND [rule_2_condition] ...);
-- Expected: 0 rows
```

**Result:** [Pass/Fail with details]

## Data Quality Improvements

### Before vs After Comparison

| Metric | Raw Table | Clean Table | Improvement |
|--------|-----------|-------------|-------------|
| Total rows | [N] | [N] | -[X]% (exclusions) |
| Completeness ([col1]) | [X]% | [X]% | +[X] pct points |
| Duplicate groups | [N] | 0 | -[N] (100%) |
| Outliers ([col2]) | [N] | 0 | -[N] (100%) |
| Free text unique values | [N] | [N categories] | -[X]% (categorization) |

## Exclusion Accounting

**Complete exclusion summary from Phase 4:**

| Reason | Count | % of Raw Dataset |
|--------|-------|------------------|
| Duplicates | [N] | [X]% |
| Outliers ([col1]) | [N] | [X]% |
| Outliers ([col2]) | [N] | [X]% |
| FK orphans (if excluded) | [N] | [X]% |
| Uncategorizable free text | [N] | [X]% |
| Business rule violations | [N] | [X]% |
| **TOTAL EXCLUDED** | **[N]** | **[X]%** |

## Spot Check Sample Records

### Records from Duplicate Groups

```sql
SELECT * FROM clean_[table_name] WHERE rowid IN ([IDs from Phase 2]);
```

**Verification:** [Correct record kept per strategy - details]

### Records with Outliers (if flagged/capped)

```sql
SELECT * FROM clean_[table_name] WHERE [numeric_col]_outlier_flag = 1;
```

**Verification:** [Flag accurate, values capped if applicable - details]

### Records with Categorized Free Text

```sql
SELECT [original_col], [col]_category FROM clean_[table_name] LIMIT 20;
```

**Verification:** [Categories make sense, mapping correct - details]

## Confidence Assessment

### High Confidence Transformations
- [Transformation]: [Why high confidence]
- Example: "Exact duplicate removal" - Clear validation, deterministic

### Medium Confidence Transformations
- [Transformation]: [Why medium confidence, some subjectivity]
- Example: "Free text categorization" - Agent-proposed with review

### Low Confidence / Needs Review
- [Transformation]: [Why needs domain expertise review]
- Example: "Outliers might be legitimate seasonal patterns"

## Limitations

**Scope limitations - What this cleaning did NOT address:**
- [Issues identified but not addressed]: [Reason not addressed]
- Example: "Date range not validated - requires domain knowledge"

**Data coverage:**
- Time periods covered: [Range]
- Geographies/categories not covered: [List if applicable]

**Assumptions made:**
- [Business rule assumed]: [Without domain validation]
- Example: "Assumed age >120 is invalid - may not apply to historical data"

**Edge cases:**
- [Unusual value handling]: [How handled]
- Example: "NULL FKs preserved - may need review based on analysis needs"

## Clean Table Readiness

**Status:** ✓ clean_[table_name] ready for analysis / ✗ Not ready - [Issues to resolve]

**Table details:**
- Location: data/analytics.db
- Row count: [N]
- Columns: [N] (including [N] new category/flag columns)

**Next steps:**
- Proceed to analysis process skills (exploratory-analysis, guided-investigation, etc.)
- Use this verification report to understand data transformations and limitations
