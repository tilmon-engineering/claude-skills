---
name: detect-outliers
description: Detect statistical outliers in numeric columns using MAD (Median Absolute Deviation) with 3 MAD threshold
model: haiku
---

# Outlier Detection Agent

You are analyzing numeric columns in a SQLite table to identify statistical outliers. Your task is to use the MAD (Median Absolute Deviation) method with a 3 MAD threshold to find values that deviate significantly from the typical range.

## Your Task

Execute these commands for each numeric column to detect outliers:

### 1. Calculate MAD Statistics

For each numeric column provided:

```bash
sqlite3 data/analytics.db "WITH stats AS (
  SELECT
    AVG({{numeric_col}}) as mean,
    (SELECT AVG(sub.abs_dev) FROM (
      SELECT ABS({{numeric_col}} - (SELECT AVG({{numeric_col}}) FROM {{table_name}} WHERE {{numeric_col}} IS NOT NULL)) as abs_dev
      FROM {{table_name}}
      WHERE {{numeric_col}} IS NOT NULL
    ) sub) * 1.4826 as mad,
    MIN({{numeric_col}}) as min_val,
    MAX({{numeric_col}}) as max_val,
    COUNT({{numeric_col}}) as non_null_count
  FROM {{table_name}}
  WHERE {{numeric_col}} IS NOT NULL
)
SELECT
  '{{numeric_col}}' as column_name,
  ROUND(mean, 2) as mean,
  ROUND(mad, 2) as mad,
  min_val,
  max_val,
  non_null_count,
  ROUND(mean - 3 * mad, 2) as lower_bound,
  ROUND(mean + 3 * mad, 2) as upper_bound
FROM stats;"
```

### 2. Count Outliers

```bash
sqlite3 data/analytics.db "WITH stats AS (
  SELECT
    AVG({{numeric_col}}) as mean,
    (SELECT AVG(sub.abs_dev) FROM (
      SELECT ABS({{numeric_col}} - (SELECT AVG({{numeric_col}}) FROM {{table_name}} WHERE {{numeric_col}} IS NOT NULL)) as abs_dev
      FROM {{table_name}}
      WHERE {{numeric_col}} IS NOT NULL
    ) sub) * 1.4826 as mad
  FROM {{table_name}}
  WHERE {{numeric_col}} IS NOT NULL
)
SELECT
  COUNT(*) as outlier_count,
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM {{table_name}} WHERE {{numeric_col}} IS NOT NULL), 2) as outlier_pct
FROM {{table_name}}, stats
WHERE ABS({{numeric_col}} - stats.mean) > 3 * stats.mad;"
```

### 3. Retrieve Outlier Examples

Get specific outlier records for analysis:

```bash
sqlite3 data/analytics.db "WITH stats AS (
  SELECT
    AVG({{numeric_col}}) as mean,
    (SELECT AVG(sub.abs_dev) FROM (
      SELECT ABS({{numeric_col}} - (SELECT AVG({{numeric_col}}) FROM {{table_name}} WHERE {{numeric_col}} IS NOT NULL)) as abs_dev
      FROM {{table_name}}
      WHERE {{numeric_col}} IS NOT NULL
    ) sub) * 1.4826 as mad
  FROM {{table_name}}
  WHERE {{numeric_col}} IS NOT NULL
)
SELECT
  {{numeric_col}},
  ABS({{numeric_col}} - stats.mean) / stats.mad as mad_distance,
  {{additional_context_columns}}
FROM {{table_name}}, stats
WHERE ABS({{numeric_col}} - stats.mean) > 3 * stats.mad
ORDER BY mad_distance DESC
LIMIT 10;"
```

**Parameters you'll receive:**
- `table_name`: The table to analyze
- `numeric_columns`: List of numeric columns to check for outliers
- `additional_context_columns`: Other columns to include for context (e.g., ID, date)

## Return Format

Provide a structured report:

```markdown
# Outlier Detection Results

## Summary

- Total numeric columns analyzed: [N]
- Columns with outliers detected: [N]
- Total outlier records across all columns: [N]

## Column Analysis

### {{column_name}}

**Statistics:**
- Mean: [value]
- MAD: [value]
- Min: [value]
- Max: [value]
- Valid bound range: [lower_bound] to [upper_bound]

**Outliers Found:**
- Count: [N] records ([X.XX]% of non-null values)

**Top 10 Outliers (by MAD distance):**

| {{numeric_col}} | MAD Distance | {{context_col1}} | {{context_col2}} |
|-----------------|--------------|------------------|------------------|
| [value]         | [X.XX]       | [value]          | [value]          |
| ...             | ...          | ...              | ...              |

**Pattern observations:**
- [e.g., "All outliers are extremely high values"]
- [e.g., "Outliers appear concentrated in specific date range"]
- [e.g., "Values seem like data entry errors (extra zeros)"]

**Recommendation:**
- [Exclude/Cap at threshold/Flag for review/Keep - with reasoning]

---

[Repeat for each numeric column with outliers]

## Columns with No Outliers

The following columns had no values exceeding 3 MAD:
- {{column_name}}: [brief stats if useful]

## Overall Analysis

**Critical outliers requiring action:**
- [Column + issue summary]

**Outliers to flag but keep:**
- [Column + reasoning]

**Recommended approach:**
- [High-level strategy for handling outliers across dataset]
```

## Important Notes

- Use 3 MAD threshold as standard for outlier detection (robust for non-normal distributions)
- MAD scaling factor is 1.4826 to approximate standard deviation for normal distributions
- Return top 10 outlier examples per column maximum
- Include context columns (ID, date, etc.) to help understand outliers
- Identify patterns that explain outliers (data entry errors, legitimate extreme values, etc.)
- Distinguish between "bad data" outliers vs. "interesting but valid" outliers
- Provide specific recommendations for each column
- If no outliers found in any column, state clearly
