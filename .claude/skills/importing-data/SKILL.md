---
name: importing-data
description: Systematic CSV import process - discover structure, design schema, standardize formats, import to SQLite, detect quality issues (component skill for DataPeeker analysis sessions)
---

# Importing Data - Component Skill

## Purpose

Use this skill when:
- Starting a new analysis with CSV data files
- Need to import CSV into SQLite database systematically
- Want to ensure proper schema design and type inference
- Need quality assessment before cleaning/analysis begins
- Replacing ad-hoc "just import-csvs" workflow

This skill is a **prerequisite** for all DataPeeker analysis workflows and is referenced by all process skills.

## Prerequisites

- **CSV file accessible** on local filesystem
- **SQLite database** at `data/analytics.db` (or path specified by project)
- **Workspace created** for analysis session (via `just start-analysis` or equivalent)
- **Understanding** that this skill creates `raw_*` tables, not final tables (cleaning-data handles finalization)

## Data Import Process

Create a TodoWrite checklist for the 5-phase data import process:

```
Phase 1: CSV Discovery & Profiling - pending
Phase 2: Schema Design & Type Inference - pending
Phase 3: Basic Standardization - pending
Phase 4: Import Execution - pending
Phase 5: Quality Assessment & Reporting - pending
```

Mark each phase as you complete it. Document all findings in numbered markdown files (`01-csv-profile.md` through `05-quality-report.md`) within your analysis workspace directory.

---

## Phase 1: CSV Discovery & Profiling

**Goal:** Understand CSV file structure, detect encoding and delimiter, capture sample data for schema design.

### File Discovery

Identify the CSV file(s) to import:
- Ask user for CSV file path(s)
- Verify file exists and is readable
- Note file size for sampling strategy (>100K rows = sample-based profiling)

**Document:** Record CSV file path, size, timestamp in `01-csv-profile.md`

### Encoding Detection

Detect file encoding to prevent import errors:

```bash
file -I /path/to/file.csv
```

Common encodings:
- `charset=us-ascii` or `charset=utf-8` → Standard, no conversion needed
- `charset=iso-8859-1` or `charset=windows-1252` → May need conversion to UTF-8

**Document:** Record detected encoding. If non-UTF-8, note conversion requirement.

### Delimiter Detection

Analyze first few lines to detect delimiter:

```bash
head -n 5 /path/to/file.csv
```

Check for:
- Comma (`,`) - most common
- Tab (`\t`) - TSV files
- Pipe (`|`) - less common
- Semicolon (`;`) - European CSV files

**Document:** Record detected delimiter character.

### Header Detection

Determine if first row contains headers:
- Read first row
- Check if row contains text labels vs data values
- If ambiguous, ask user to confirm

**Document:** Record whether headers present, list header names if found.

### Sample Data Capture

Capture representative samples for schema inference:

```bash
# First 10 rows
head -n 11 /path/to/file.csv > /tmp/csv_head_sample.txt

# Last 10 rows
tail -n 10 /path/to/file.csv > /tmp/csv_tail_sample.txt

# Row count
wc -l /path/to/file.csv
```

**Document:** Include head and tail samples in `01-csv-profile.md` for reference during schema design.

### Phase 1 Documentation Template

Create `analysis/[session-name]/01-csv-profile.md` with:

```markdown
# CSV Profile: [filename]

## File Information
- **Source:** [absolute path to CSV]
- **Size:** [file size in MB]
- **Row count:** [total rows including header]
- **Encoding:** [detected encoding]
- **Delimiter:** [character]
- **Headers:** [Yes/No - list if yes]

## Sample Data

### First 10 Rows
```
[paste head output]
```

### Last 10 Rows
```
[paste tail output]
```

## Column Overview

[For each column detected in headers/first row:]
### [Column Name or Position]
- **Sample values (first 10):** [list unique values if reasonable]
- **Observed types:** [text, numbers, dates, mixed]
- **NULL indicators:** [empty cells, 'N/A', 'null', etc.]

## Notes
[Any observations about data quality, unusual patterns, concerns for import]

## Next Steps
Proceed to Phase 2: Schema Design & Type Inference
```

**CHECKPOINT:** Before proceeding to Phase 2, you MUST have:
- [ ] CSV file path confirmed and file accessible
- [ ] Encoding, delimiter, headers detected
- [ ] Sample data captured (head + tail)
- [ ] `01-csv-profile.md` created with all sections filled
- [ ] Column overview completed with initial observations

---

## Phase 2: Schema Design & Type Inference

**Goal:** Design SQLite schema by inferring types from CSV samples, propose table structure with rationale.

### Analyze Column Types

For each column from Phase 1 profiling, infer SQLite type:

**SQLite Type Inference Rules:**

1. **INTEGER** - Use when:
   - All non-NULL values are whole numbers
   - No decimal points observed
   - Typical for: IDs, counts, years, quantities

2. **REAL** - Use when:
   - Values contain decimal points
   - Monetary amounts, measurements, percentages
   - Example: 19.99, 0.05, 123.45

3. **TEXT** - Use when:
   - Mixed alphanumeric content
   - Dates/datetimes (store as ISO 8601: YYYY-MM-DD or YYYY-MM-DD HH:MM:SS)
   - Categories, names, descriptions
   - **Default choice when unsure**

**Document:** For each column, record inferred type with rationale and sample values.

### Handle NULL Representations

Identify NULL representations in CSV:
- Empty cells → `NULL` in SQLite
- Literal strings: "N/A", "null", "NULL", "None", "#N/A" → Convert to `NULL`
- Numeric codes: -999, -1 (if documented as NULL) → Convert to `NULL`

**Document:** List all NULL representations found and conversion strategy.

### Design Table Schema

Propose CREATE TABLE statement:

```sql
CREATE TABLE raw_[table_name] (
  [column_1_name] [TYPE],  -- Rationale for type choice
  [column_2_name] [TYPE],  -- Rationale for type choice
  ...
);
```

**Table naming convention:**
- Prefix with `raw_` to indicate unprocessed data
- Use lowercase with underscores: `raw_sales_data`, `raw_customers`
- Derive from CSV filename or ask user for preferred name

**Document:** Full CREATE TABLE statement with inline comments explaining each type choice.

### Present Schema to User

Use AskUserQuestion tool to present schema proposal:
- Show proposed table name
- Show each column with type and rationale
- Ask user to confirm or request changes

**Document:** User's approval and any requested modifications.

### Phase 2 Documentation Template

Create `analysis/[session-name]/02-schema-design.md`:

```markdown
# Schema Design: [dataset_name]

## Objective
Design SQLite schema for importing [CSV_filename] based on data profiling from Phase 1.

## Column Type Analysis

### [Column 1 Name]
- **Sample values:** [examples from 01-csv-profile.md]
- **Proposed type:** [INTEGER|REAL|TEXT]
- **Rationale:** [Why this type - reference inference rules above]
- **NULL handling:** [How NULL values will be handled]

### [Column 2 Name]
- **Sample values:** [examples]
- **Proposed type:** [INTEGER|REAL|TEXT]
- **Rationale:** [Explanation]
- **NULL handling:** [Approach]

[Continue for all columns...]

## NULL Representation Mapping

| CSV Representation | SQLite Value | Count in Sample |
|--------------------|--------------|-----------------|
| (empty cell)       | NULL         | [count]         |
| "N/A"              | NULL         | [count]         |
| [others]           | NULL         | [count]         |

## Proposed Schema

```sql
CREATE TABLE raw_[table_name] (
  [column_1] [TYPE],  -- [Rationale]
  [column_2] [TYPE],  -- [Rationale]
  ...
);
```

## User Confirmation

- **Proposed table name:** `raw_[name]`
- **Total columns:** [count]
- **User approval:** [Date/time of approval]
- **Modifications requested:** [None / List of changes made]

## Next Steps
Proceed to Phase 3: Basic Standardization
```

**CHECKPOINT:** Before proceeding to Phase 3, you MUST have:
- [ ] All columns analyzed with type inference rationale
- [ ] NULL representations identified and mapped
- [ ] CREATE TABLE statement drafted
- [ ] User approved schema (via AskUserQuestion)
- [ ] `02-schema-design.md` created with all sections filled

---

## Phase 3: Basic Standardization

**Goal:** Define transformation rules for dates, numbers, whitespace, and text formatting to ensure clean, consistent data in raw_* table.

### Date Format Standardization

**Target format:** ISO 8601
- Dates: `YYYY-MM-DD` (e.g., 2025-01-15)
- Datetimes: `YYYY-MM-DD HH:MM:SS` (e.g., 2025-01-15 14:30:00)

**Common source formats to convert:**
- `MM/DD/YYYY` or `M/D/YYYY` → `YYYY-MM-DD`
- `DD/MM/YYYY` or `D/M/YYYY` → `YYYY-MM-DD` (verify with user which is month vs day)
- `YYYY/MM/DD` → `YYYY-MM-DD` (slash to hyphen)
- `Mon DD, YYYY` → `YYYY-MM-DD` (e.g., "Jan 15, 2025" → "2025-01-15")
- Timestamps with T separator: `YYYY-MM-DDTHH:MM:SS` → Keep as-is (valid ISO 8601)

**Document:** List each date column, source format detected, target format, conversion logic.

### Number Format Normalization

**Remove non-numeric characters:**
- Currency symbols: `$123.45` → `123.45`
- Comma separators: `1,234.56` → `1234.56`
- Percentage signs: `45%` → `45` or `0.45` (document choice)
- Units: `25kg`, `100m` → `25`, `100` (document unit in column name/comments)

**Decimal handling:**
- Preserve decimal points
- Convert European format if detected: `1.234,56` → `1234.56` (verify with user)

**Document:** List each numeric column, formatting issues found, normalization rules.

### Whitespace and Text Normalization

**Whitespace cleaning:**
- Trim leading/trailing whitespace from all TEXT columns
- Normalize internal whitespace: multiple spaces → single space
- Normalize line endings: `\r\n` or `\r` → `\n`

**Text case standardization** (optional, apply selectively):
- IDs/codes: Often uppercase for consistency
- Names: Title case or preserve original
- Free text: Preserve original case
- **Document choice per column type**

**Document:** Which columns get whitespace cleaning, which get case normalization.

### NULL Standardization

Apply NULL representation mapping from Phase 2:
- Convert all identified NULL representations to actual SQLite `NULL`
- Empty strings → `NULL` for numeric/date columns
- Empty strings → Preserve as empty string `''` for TEXT columns (document choice)

**Document:** NULL conversion applied, count of conversions per column.

### Phase 3 Documentation Template

Create `analysis/[session-name]/03-standardization-rules.md`:

```markdown
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
```

**CHECKPOINT:** Before proceeding to Phase 4, you MUST have:
- [ ] Date standardization rules defined for all date columns
- [ ] Number normalization rules defined for all numeric columns
- [ ] Whitespace/text rules defined
- [ ] NULL conversion mapping finalized
- [ ] `03-standardization-rules.md` created with verification queries

---

## Phase 4: Import Execution

**Goal:** Execute import with standardization rules, verify row count and data integrity.

### Generate CREATE TABLE Statement

From Phase 2 schema design, finalize CREATE TABLE statement:

```sql
CREATE TABLE IF NOT EXISTS raw_[table_name] (
  [column_1] [TYPE],
  [column_2] [TYPE],
  ...
);
```

**Execute:**
```bash
sqlite3 data/analytics.db < create_table.sql
```

**Verify table created:**
```sql
-- Check table exists
.tables

-- Inspect schema
PRAGMA table_info(raw_[table_name]);
```

**Document:** Paste table creation confirmation and schema output.

### Import CSV with Standardization

**Import method options:**

**Option 1: SQLite `.import` command** (for simple cases):
```bash
sqlite3 data/analytics.db <<EOF
.mode csv
.import /path/to/file.csv raw_[table_name]
EOF
```

**Option 2: Python script** (for complex standardization):
```python
import csv
import sqlite3
from datetime import datetime

conn = sqlite3.connect('data/analytics.db')
cursor = conn.cursor()

with open('/path/to/file.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Apply standardization rules from Phase 3
        row['date_column'] = standardize_date(row['date_column'])
        row['amount_column'] = standardize_number(row['amount_column'])
        # ... apply other rules ...

        cursor.execute("""
            INSERT INTO raw_[table_name]
            ([columns]) VALUES ([placeholders])
        """, tuple(row.values()))

conn.commit()
conn.close()
```

**Document:** Which method used, any import warnings/errors encountered and resolved.

### Verify Import Success

**Row count verification:**
```sql
-- Count rows in table
SELECT COUNT(*) as row_count FROM raw_[table_name];
```

Compare to CSV row count from Phase 1. Should match (or CSV count - 1 if CSV had header row).

**Sample data inspection:**
```sql
-- View first 5 rows
SELECT * FROM raw_[table_name] LIMIT 5;

-- View last 5 rows
SELECT * FROM raw_[table_name]
ORDER BY rowid DESC LIMIT 5;
```

**Column completeness check:**
```sql
-- Check NULL counts per column
SELECT
  COUNT(*) as total_rows,
  COUNT([column_1]) as [column_1]_non_null,
  COUNT([column_2]) as [column_2]_non_null,
  ...
FROM raw_[table_name];
```

**Document:** Paste actual results showing row counts, sample rows, NULL counts.

### Run Verification Queries from Phase 3

Execute all verification queries defined in `03-standardization-rules.md`:
- Date format verification
- Number format verification
- Whitespace verification

**Expected:** All verification queries return 0 rows (no violations).

**If violations found:** Document count and examples, decide whether to:
1. Re-import with adjusted rules
2. Document as acceptable edge cases
3. Flag for cleaning-data phase

**Document:** Results of all verification queries.

### Phase 4 Documentation Template

Create `analysis/[session-name]/04-import-log.md`:

```markdown
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
```

**CHECKPOINT:** Before proceeding to Phase 5, you MUST have:
- [ ] raw_* table created in data/analytics.db
- [ ] CSV data imported with standardization applied
- [ ] Row count verified matches CSV (accounting for headers)
- [ ] Sample data inspected and looks correct
- [ ] All Phase 3 verification queries executed
- [ ] `04-import-log.md` created with all results documented

---

## Phase 5: Quality Assessment & Reporting

**Goal:** Systematically detect data quality issues using sub-agent to prevent context pollution, document findings for cleaning-data skill.

**CRITICAL:** This phase MUST use sub-agent delegation. DO NOT analyze data in main agent context.

### Delegate Quality Assessment to Sub-Agent

**Use dedicated quality-assessment agent**

Invoke the `quality-assessment` agent (defined in `.claude/agents/quality-assessment.md`):

```
Task tool with agent: quality-assessment
Parameters:
- table_name: raw_[actual_table_name]
- columns: [list of all columns from schema]
- numeric_columns: [list of numeric columns for outlier detection]
- text_columns: [list of text columns for uniqueness analysis]
```

The agent will execute all quality checks (NULL analysis, duplicates, outliers, free text) and return structured findings.

**Document agent findings in `05-quality-report.md` using template below.**

### Create Quality Report for cleaning-data

Create `analysis/[session-name]/05-quality-report.md`:

```markdown
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

1. **Phase 2 (Issue Detection):** Deep-dive investigation of [specific issues]
2. **Phase 3 (Strategy):** Decide approach for [duplicates/outliers/free text]
3. **Phase 4 (Execution):** Apply transformations and create clean_* tables

## Next Steps
Proceed to cleaning-data skill with this quality report as input.
```

**CHECKPOINT:** Before concluding importing-data skill, you MUST have:
- [ ] Sub-agent completed quality assessment (NOT done in main context)
- [ ] NULL percentages documented for all columns
- [ ] Duplicates detected and examples captured
- [ ] Outliers identified in all numeric columns
- [ ] Free text columns identified for categorization
- [ ] `05-quality-report.md` created with all sections filled
- [ ] Quality report ready for cleaning-data skill to consume

---

## Common Rationalizations

### "The CSV looks clean, I can skip profiling and go straight to import"
**Why this is wrong:** Hidden issues (encoding, delimiters, NULL representations) cause import failures or silent data corruption. Even "clean" CSVs have edge cases.

**Do instead:** Always complete Phase 1 profiling. Takes 5 minutes and prevents hours of debugging broken imports.

### "I'll just guess the schema types, they're obvious from the column names"
**Why this is wrong:** Column named "year" might contain "2023-Q1" (TEXT). "amount" might have "$" symbols. Type inference prevents silent casting failures.

**Do instead:** Complete Phase 2 type inference with sample analysis. Document rationale for each type choice.

### "Dates look fine, I don't need standardization rules"
**Why this is wrong:** Mixed formats ("01/15/2025", "2025-01-15", "Jan 15 2025") break date arithmetic and sorting. Standardization is mandatory.

**Do instead:** Complete Phase 3 with explicit date format conversion rules. Verify with queries after import.

### "I'll do the import manually, don't need to document it"
**Why this is wrong:** Undocumented imports can't be reproduced. When re-importing updated data, you'll forget the transformations applied.

**Do instead:** Complete Phase 4 import log with commands, results, and verification. Future-you will thank present-you.

### "The data looks good after import, quality assessment is overkill"
**Why this is wrong:** Duplicates, outliers, and NULL patterns are invisible without systematic checks. These surface as bugs during analysis.

**Do instead:** ALWAYS complete Phase 5 with sub-agent delegation. Quality report saves time in cleaning-data phase.

### "I'll run quality checks in the main agent, it's faster than delegating"
**Why this is wrong:** Analyzing thousands of rows pollutes main agent context, degrading performance for entire session. Sub-agents prevent this.

**Do instead:** ALWAYS delegate Phase 5 to sub-agent with exact sqlite3 commands provided.

### "This CSV has 100K rows, I should skip some profiling steps for speed"
**Why this is wrong:** Large files are MORE likely to have quality issues, not less. Sampling strategies exist for large files.

**Do instead:** Use head/tail sampling (Phase 1) and query-based profiling (Phase 5 sub-agent). Don't skip phases.

### "The import succeeded, I don't need to verify row counts"
**Why this is wrong:** Silent data loss happens. Header rows miscounted, empty rows skipped, encoding issues truncating data.

**Do instead:** Always verify row count matches (Phase 4). If mismatch, investigate before proceeding.

### "I'll clean the data during import, don't need separate cleaning-data skill"
**Why this is wrong:** Import handles technical standardization (formats). Cleaning handles semantic issues (business rules, categorization). Mixing them creates confusion.

**Do instead:** Keep importing-data focused on standardization. Let cleaning-data handle deduplication, outliers, free text.

### "Quality report shows no issues, I can skip cleaning-data"
**Why this is wrong:** cleaning-data is ALWAYS mandatory per design. Even "clean" data needs business rule validation and final verification.

**Do instead:** Proceed to cleaning-data even if quality report shows minimal issues. Document "no cleaning needed" if appropriate.

---

## Summary

This skill ensures systematic, documented CSV import with quality assessment by:

1. **Profiling before importing:** Understand encoding, delimiters, headers, and sample data before designing schema - prevents import failures and silent corruption.

2. **Explicit type inference:** Analyze samples to infer INTEGER/REAL/TEXT types with documented rationale - prevents type casting failures and ensures correct data representation.

3. **Mandatory standardization:** Convert dates to ISO 8601, normalize numbers, clean whitespace, map NULL representations - creates consistent data foundation for analysis.

4. **Verified import execution:** Document CREATE TABLE statements, import methods, row count verification - ensures reproducibility and data integrity.

5. **Systematic quality assessment:** Delegate NULL detection, duplicate finding, outlier identification, and free text discovery to sub-agent - prevents context pollution while ensuring comprehensive quality checks.

6. **Audit trail maintenance:** Create numbered markdown files (01-05) documenting every decision - provides full traceability from raw CSV to raw_* tables.

Follow this process and you'll create clean, well-documented raw_* tables ready for the cleaning-data skill, avoid silent data corruption, and maintain complete audit trail for reproducible imports.

---
