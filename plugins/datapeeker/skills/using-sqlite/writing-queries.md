# Writing Queries - SQLite-Specific Patterns

## When to Use This Guidance

Use when you need:
- **SQLite-specific syntax** (STRFTIME, date handling)
- **DataPeeker query conventions** (NULL counting, percentage calculations)
- **Common verification patterns** used across DataPeeker skills

**Note:** For general SQL query formulation (applicable to Postgres, Athena, etc.), use the `writing-queries` skill. This guidance focuses on SQLite idioms and DataPeeker conventions.

## DataPeeker Query Conventions

### 1. NULL Counting (Efficient Pattern)

**DataPeeker Standard:**
```sql
SELECT
    COUNT(*) as total_rows,
    COUNT(column) as non_null_count,
    COUNT(*) - COUNT(column) as null_count,
    ROUND(100.0 * (COUNT(*) - COUNT(column)) / COUNT(*), 2) as null_percentage
FROM table_name;
```

**Why this pattern:**
- `COUNT(*) - COUNT(column)` is more efficient than CASE WHEN
- Consistently used across all DataPeeker skills
- Clear and readable

**Don't use:**
```sql
-- Less efficient
COUNT(CASE WHEN column IS NULL THEN 1 END)
```

---

### 2. Percentage Calculations (Float Division)

**DataPeeker Standard:**
```sql
SELECT
    category,
    COUNT(*) as count,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM table_name), 2) as percentage
FROM table_name
GROUP BY category;
```

**Critical:** Use `100.0` (not `100`) for float division

**Why:**
- `100 * x / y` does integer division, losing decimals
- `100.0 * x / y` does float division, preserving accuracy
- Subquery ensures correct total denominator

---

### 3. Empty String vs NULL Detection

```sql
SELECT COUNT(*) as problematic_rows
FROM table_name
WHERE TRIM(text_column) = '' OR text_column IS NULL;
```

**Pattern:** Always check BOTH empty strings and NULL for text columns

---

## SQLite Date/Time Handling

### STRFTIME - The Core Date Function

**Month grouping (most common):**
```sql
SELECT
    STRFTIME('%Y-%m', date_column) as year_month,
    COUNT(*) as count
FROM table_name
GROUP BY year_month
ORDER BY year_month;
```

**Common formats:**
```sql
STRFTIME('%Y-%m-%d', date_col)  -- Full date: 2025-01-15
STRFTIME('%Y-%m', date_col)      -- Year-month: 2025-01
STRFTIME('%Y', date_col)         -- Year only: 2025
STRFTIME('%m', date_col)         -- Month only: 01
STRFTIME('%d', date_col)         -- Day only: 15
STRFTIME('%w', date_col)         -- Day of week: 0-6 (0=Sunday)
STRFTIME('%Y-Q%q', date_col)     -- Quarter: 2025-Q1 (INVALID, see below)
```

**Quarter calculation (SQLite doesn't have %q):**
```sql
SELECT
    STRFTIME('%Y', date_col) ||
    '-Q' ||
    CAST(((CAST(STRFTIME('%m', date_col) AS INTEGER) - 1) / 3) + 1 AS TEXT) as quarter,
    COUNT(*) as count
FROM table_name
GROUP BY quarter;
```

---

### Weekend vs Weekday Pattern

```sql
SELECT
    CASE
        WHEN CAST(STRFTIME('%w', date_column) AS INTEGER) IN (0, 6)
        THEN 'Weekend'
        ELSE 'Weekday'
    END as day_type,
    COUNT(*) as count,
    SUM(amount) as total
FROM table_name
GROUP BY day_type;
```

**Note:** `%w` returns 0 for Sunday, 6 for Saturday

---

### Date Range Filtering

```sql
-- Single date
WHERE DATE(date_column) = '2025-01-15'

-- Date range
WHERE DATE(date_column) BETWEEN '2025-01-01' AND '2025-01-31'

-- Last 30 days
WHERE DATE(date_column) >= DATE('now', '-30 days')
```

---

## Common Verification Queries

### After Import: Row Count Verification

```sql
SELECT COUNT(*) as row_count FROM raw_table_name;
```

**Always run after .import command**

---

### After Import: Sample Data Check

```sql
SELECT * FROM raw_table_name LIMIT 5;
```

**Purpose:** Verify data looks correct

---

### Column Completeness Check

```sql
SELECT
    'column1' as column_name,
    COUNT(*) as total,
    COUNT(column1) as non_null,
    COUNT(*) - COUNT(column1) as nulls
UNION ALL
SELECT
    'column2',
    COUNT(*),
    COUNT(column2),
    COUNT(*) - COUNT(column2)
FROM table_name;
```

**Use when:** Checking multiple columns for completeness

---

### Schema Verification After Table Creation

```sql
PRAGMA table_info(raw_table_name);
```

**Purpose:** Confirm table structure matches design

---

## Relationship Validation Patterns

### Foreign Key Value Overlap

```sql
SELECT
    COUNT(DISTINCT fk_column) as fk_values_in_table_a,
    (SELECT COUNT(DISTINCT id_column) FROM table_b) as pk_values_in_table_b,
    (SELECT COUNT(DISTINCT fk_column)
     FROM table_a
     WHERE fk_column IN (SELECT id_column FROM table_b)) as matching_values
FROM table_a;
```

**Purpose:** Assess referential integrity before joining

---

### Join Cardinality Assessment

```sql
SELECT
    COUNT(*) as rows_in_a,
    COUNT(DISTINCT b.id_column) as matched_in_b,
    COUNT(*) - COUNT(b.id_column) as unmatched_rows
FROM table_a a
LEFT JOIN table_b b ON a.fk_column = b.id_column;
```

**Purpose:** Understand join behavior (1-1 vs 1-many)

---

## Data Distribution Patterns

### Categorical Distribution with Percentage

```sql
SELECT
    category_column,
    COUNT(*) as frequency,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM table_name), 2) as percentage
FROM table_name
GROUP BY category_column
ORDER BY frequency DESC;
```

---

### Numeric Range Analysis

```sql
SELECT
    MIN(numeric_column) as min_value,
    MAX(numeric_column) as max_value,
    AVG(numeric_column) as avg_value,
    ROUND(AVG(numeric_column), 2) as avg_rounded,
    COUNT(CASE WHEN numeric_column < 0 THEN 1 END) as negative_count,
    COUNT(CASE WHEN numeric_column = 0 THEN 1 END) as zero_count
FROM table_name;
```

**Purpose:** Detect impossible values, identify outliers

---

### Temporal Distribution

```sql
SELECT
    STRFTIME('%Y-%m', date_column) as month,
    COUNT(*) as row_count,
    MIN(date_column) as earliest_date,
    MAX(date_column) as latest_date
FROM table_name
GROUP BY month
ORDER BY month;
```

**Purpose:** Analyze temporal coverage, detect gaps

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| `100 * COUNT(*) / total` | Integer division, lose decimals | Use `100.0` for float division |
| `COUNT(CASE WHEN x IS NULL...)` | Less efficient NULL counting | Use `COUNT(*) - COUNT(x)` |
| Not trimming text before empty check | Miss whitespace-only values | Use `TRIM(col) = ''` |
| Using `%q` for quarter | SQLite doesn't support | Calculate from month number |
| Forgetting CAST on STRFTIME | String comparison, not numeric | `CAST(STRFTIME(...) AS INTEGER)` |
| Not specifying DATE() in WHERE | Compares timestamps, not dates | Use `DATE(col) = '2025-01-15'` |

---

## DataPeeker-Specific Patterns

### Import Verification (Standard Pattern)

```sql
-- 1. Row count
SELECT COUNT(*) FROM raw_table;

-- 2. Sample data
SELECT * FROM raw_table LIMIT 5;

-- 3. Column completeness
SELECT
    COUNT(*) - COUNT(critical_col1) as col1_nulls,
    COUNT(*) - COUNT(critical_col2) as col2_nulls
FROM raw_table;

-- 4. Schema verification
PRAGMA table_info(raw_table);
```

**Always run all four after import**

---

### Quality Assessment Queries

**Common data profiling patterns:**

```sql
-- NULL distribution
SELECT
    'critical_column' as column_name,
    COUNT(*) - COUNT(critical_column) as null_count,
    ROUND(100.0 * (COUNT(*) - COUNT(critical_column)) / COUNT(*), 2) as null_pct
FROM table_name;

-- Value ranges
SELECT
    MIN(numeric_col) as min,
    MAX(numeric_col) as max,
    AVG(numeric_col) as avg
FROM table_name;

-- Date ranges (SQLite-specific)
SELECT
    MIN(DATE(date_col)) as earliest,
    MAX(DATE(date_col)) as latest,
    JULIANDAY(MAX(DATE(date_col))) - JULIANDAY(MIN(DATE(date_col))) as days_span
FROM table_name;
```

**Note:** These patterns align with database-agnostic data profiling best practices.

---

## Real-World Example

```sql
-- Scenario: Analyze sales patterns by day of week

SELECT
    CASE
        WHEN CAST(STRFTIME('%w', transaction_date) AS INTEGER) IN (0, 6)
        THEN 'Weekend'
        ELSE 'Weekday'
    END as day_type,
    COUNT(*) as transaction_count,
    SUM(amount) as total_sales,
    ROUND(AVG(amount), 2) as avg_transaction,
    ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM sales), 2) as pct_of_transactions,
    ROUND(SUM(amount) / COUNT(DISTINCT DATE(transaction_date)), 2) as avg_daily_sales
FROM sales
WHERE DATE(transaction_date) BETWEEN '2025-01-01' AND '2025-03-31'
GROUP BY day_type;
```

**Demonstrates:**
- STRFTIME date handling
- Weekend/weekday CASE pattern
- Float division percentage (100.0)
- Multiple aggregations
- DATE filtering
- Average per day calculation

---

## Quick Reference

### NULL Handling
```sql
COUNT(*) - COUNT(col)  -- NULL count (efficient)
ROUND(100.0 * (COUNT(*) - COUNT(col)) / COUNT(*), 2)  -- NULL percentage
```

### Percentages
```sql
ROUND(100.0 * value / total, 2)  -- Always 100.0 for float division
```

### Date Grouping
```sql
STRFTIME('%Y-%m', date_col)  -- Month: 2025-01
STRFTIME('%w', date_col)     -- Day of week: 0-6
```

### Empty String Check
```sql
WHERE TRIM(text_col) = '' OR text_col IS NULL
```

### Verification After Import
```sql
SELECT COUNT(*) FROM raw_table;  -- Row count
SELECT * FROM raw_table LIMIT 5;  -- Sample
PRAGMA table_info(raw_table);     -- Schema
```

---

## Checklist

Before finalizing a query:
- [ ] Used 100.0 (not 100) for percentages
- [ ] Used COUNT(*) - COUNT(col) for NULL counting
- [ ] Checked both TRIM(col) = '' AND col IS NULL for text
- [ ] Used STRFTIME for date formatting
- [ ] Cast STRFTIME results to INTEGER if comparing numerically
- [ ] Used DATE(col) in WHERE clause for date filtering
- [ ] Rounded percentages to 2 decimals

**Following these patterns:** Ensures consistency with all DataPeeker skills and verified best practices.
