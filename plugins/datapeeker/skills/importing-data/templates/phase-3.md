# Standardization Rules: [dataset_name]

## Objective
Define transformation rules to standardize CSV data before import to raw_[table_name].

## Date Standardization

### [Date Column Name]
- **Source format:** [e.g., "MM/DD/YYYY"]
- **Target format:** YYYY-MM-DD (ISO 8601)
- **Conversion logic:**
  ```
  Parse MM, DD, YYYY components
  Reformat as YYYY-MM-DD
  ```
- **Verification query:**
  ```sql
  -- After import, verify all dates are ISO format
  SELECT [column_name], COUNT(*) as count
  FROM raw_[table_name]
  WHERE [column_name] NOT GLOB '[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]'
    AND [column_name] IS NOT NULL;
  ```

[Repeat for each date column]

## Number Normalization

### [Numeric Column Name]
- **Issues found:** [e.g., "Comma separators, dollar signs"]
- **Normalization rules:**
  - Remove: `$`, `,`
  - Keep: `.` (decimal point)
- **Example transformation:** `$1,234.56` → `1234.56`
- **Verification query:**
  ```sql
  -- After import, verify all values are numeric
  SELECT [column_name], COUNT(*) as count
  FROM raw_[table_name]
  WHERE CAST([column_name] AS REAL) IS NULL
    AND [column_name] IS NOT NULL;
  ```

[Repeat for each numeric column]

## Whitespace Standardization

**Columns affected:** [List TEXT columns]
**Rules:**
- Trim leading/trailing whitespace
- Collapse multiple internal spaces to single space
- Normalize line endings to LF (`\n`)

**Verification query:**
```sql
-- Check for leading/trailing whitespace after import
SELECT [column_name], COUNT(*) as count
FROM raw_[table_name]
WHERE [column_name] != TRIM([column_name])
  AND [column_name] IS NOT NULL;
```

## NULL Standardization

**Conversions applied:**

| Original Value | Converted To | Affected Columns | Count |
|----------------|--------------|------------------|-------|
| (empty)        | NULL         | [All columns]    | [N]   |
| "N/A"          | NULL         | [List]           | [N]   |
| [Others]       | NULL         | [List]           | [N]   |

## Implementation Notes

[Any special cases, ambiguities resolved, user decisions made]

## Next Steps
Proceed to Phase 4: Import Execution
