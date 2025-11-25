# Import Log: [dataset_name]

## Objective
Execute import of [CSV_filename] to raw_[table_name] with standardization rules applied.

## Table Creation

```sql
CREATE TABLE IF NOT EXISTS raw_[table_name] (
  [full schema from Phase 2]
);
```

**Execution result:** [Success / Error message]

**Schema verification:**
```
[Paste PRAGMA table_info output]
```

## Import Execution

**Method used:** [SQLite .import / Python script / Other]

**Import command:**
```bash
[Exact command or script used]
```

**Import results:**
- Start time: [timestamp]
- End time: [timestamp]
- Duration: [seconds]
- Warnings: [Any warnings encountered]
- Errors: [Any errors and how resolved]

## Import Verification

### Row Count Check
```sql
SELECT COUNT(*) as row_count FROM raw_[table_name];
```

**Result:** [N rows]
**Expected (from CSV):** [N rows]
**Status:** ✓ Match / ✗ Mismatch - [Explanation]

### Sample Data
```sql
SELECT * FROM raw_[table_name] LIMIT 5;
```

**Results:**
```
[Paste first 5 rows]
```

### Column Completeness
```sql
SELECT
  COUNT(*) as total_rows,
  [column completeness query from above]
FROM raw_[table_name];
```

**Results:**
```
[Paste counts]
```

## Standardization Verification

### Date Format Check
```sql
[Verification query from 03-standardization-rules.md]
```

**Result:** [0 rows = success / N rows with issues]

### Number Format Check
```sql
[Verification query from 03-standardization-rules.md]
```

**Result:** [0 rows = success / N rows with issues]

### Whitespace Check
```sql
[Verification query from 03-standardization-rules.md]
```

**Result:** [0 rows = success / N rows with issues]

## Issues Encountered

[Document any issues found during verification and resolution approach]

## Import Summary

- **Status:** ✓ Success / ⚠ Success with caveats / ✗ Failed
- **Table:** `raw_[table_name]`
- **Rows imported:** [N]
- **Columns:** [N]
- **Standardization rules applied:** [Date/Number/Whitespace/NULL]
- **Verification status:** [All checks passed / Issues documented above]

## Next Steps
Proceed to Phase 5: Quality Assessment & Reporting
