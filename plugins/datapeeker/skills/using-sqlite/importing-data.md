# Importing Data

## When to Use This Guidance

Use when:
- Loading CSV files into SQLite tables
- Verifying import success
- Deciding between CLI .import vs Python sqlite3
- Handling import errors or mismatched row counts

**Note:** For the full 5-phase import workflow (discovery, schema design, standardization, import, quality assessment), use the `importing-data` skill. This guidance focuses specifically on SQLite CLI import mechanics.

## Two Import Methods

### Method 1: CLI .import (Simple Cases)

**Use when:**
- CSV is well-formed (consistent delimiters, proper quotes)
- No row-level transformations needed
- Data matches table schema directly

### Method 2: Python sqlite3 (Complex Cases)

**Use when:**
- Need row-level transformations (date parsing, text cleaning)
- Complex standardization rules
- Conditional logic during import
- CSV has inconsistent formatting

---

## Method 1: CLI .import

### Pattern 1: Basic Import with Heredoc

```bash
sqlite3 data/analytics.db <<'EOF'
.mode csv
.import /path/to/file.csv raw_table_name
EOF
```

**Critical:** Use absolute path or path relative to where sqlite3 is invoked

---

### Pattern 2: Import with Table Pre-Creation

```bash
# Step 1: Create table with correct schema
sqlite3 data/analytics.db < create_table.sql

# Step 2: Import data
sqlite3 data/analytics.db <<'EOF'
.mode csv
.import /path/to/file.csv raw_table_name
EOF
```

**Benefit:** Explicit control over column types and constraints

---

### Pattern 3: Skip Header Row (SQLite 3.32+)

```bash
sqlite3 data/analytics.db <<'EOF'
.mode csv
.import --skip 1 /path/to/file.csv raw_table_name
EOF
```

**Note:** Older SQLite versions don't support --skip, table creation infers from header

---

### Complete Import Example

```bash
DB="data/analytics.db"
CSV_FILE="data/raw/sales.csv"

# Step 1: Create table
sqlite3 $DB <<'EOF'
CREATE TABLE IF NOT EXISTS raw_sales (
    sale_id INTEGER,
    customer_id INTEGER,
    sale_date TEXT,
    amount REAL,
    product TEXT
);
EOF

# Step 2: Import
sqlite3 $DB <<'EOF'
.mode csv
.import data/raw/sales.csv raw_sales
EOF

# Step 3: Verify row count
echo "=== Row Count ==="
sqlite3 $DB "SELECT COUNT(*) as row_count FROM raw_sales;"

# Step 4: Sample data
echo "=== Sample Data ==="
sqlite3 -column -header $DB "SELECT * FROM raw_sales LIMIT 5;"

# Step 5: Check for NULLs
echo "=== NULL Check ==="
sqlite3 $DB <<'EOF'
SELECT
    COUNT(*) - COUNT(sale_id) as sale_id_nulls,
    COUNT(*) - COUNT(customer_id) as customer_id_nulls,
    COUNT(*) - COUNT(sale_date) as sale_date_nulls,
    COUNT(*) - COUNT(amount) as amount_nulls
FROM raw_sales;
EOF
```

---

## Method 2: Python sqlite3

### When CLI .import Is Insufficient

**Use Python when you need:**
- Date format conversion (MM/DD/YYYY → YYYY-MM-DD)
- Text cleaning (trim whitespace, normalize case)
- Number format fixes (remove $, commas from currency)
- NULL representation mapping (empty string → NULL)
- Conditional logic (skip rows, transform values)

---

### Basic Python Import Pattern

```python
import sqlite3
import csv

conn = sqlite3.connect('data/analytics.db')
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS raw_sales (
        sale_id INTEGER,
        customer_id INTEGER,
        sale_date TEXT,
        amount REAL,
        product TEXT
    )
""")

# Import with transformation
with open('data/raw/sales.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("""
            INSERT INTO raw_sales (sale_id, customer_id, sale_date, amount, product)
            VALUES (?, ?, ?, ?, ?)
        """, (
            int(row['sale_id']) if row['sale_id'] else None,
            int(row['customer_id']) if row['customer_id'] else None,
            row['sale_date'],  # Already YYYY-MM-DD in this example
            float(row['amount'].replace('$', '').replace(',', '')) if row['amount'] else None,
            row['product'].strip()
        ))

conn.commit()
conn.close()
```

**Critical:** Always use parameterized queries (`?`) to prevent SQL injection

---

### Python Import with Date Standardization

```python
import sqlite3
import csv
from datetime import datetime

conn = sqlite3.connect('data/analytics.db')
cursor = conn.cursor()

with open('data/raw/sales.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Convert MM/DD/YYYY to YYYY-MM-DD
        date_obj = datetime.strptime(row['sale_date'], '%m/%d/%Y')
        iso_date = date_obj.strftime('%Y-%m-%d')

        cursor.execute("""
            INSERT INTO raw_sales (sale_id, customer_id, sale_date, amount, product)
            VALUES (?, ?, ?, ?, ?)
        """, (
            int(row['sale_id']),
            int(row['customer_id']),
            iso_date,  # Now ISO 8601 format
            float(row['amount']),
            row['product']
        ))

conn.commit()
conn.close()
```

---

## Verification Patterns (Mandatory)

### Pattern 1: Row Count Verification

```bash
# Get CSV row count (minus header)
CSV_ROWS=$(tail -n +2 data/raw/sales.csv | wc -l | tr -d ' ')

# Get database row count
DB_ROWS=$(sqlite3 data/analytics.db "SELECT COUNT(*) FROM raw_sales;")

echo "CSV rows: $CSV_ROWS"
echo "DB rows: $DB_ROWS"

if [ "$CSV_ROWS" != "$DB_ROWS" ]; then
    echo "ERROR: Row count mismatch!"
    exit 1
fi
```

**Always verify:** Import success doesn't guarantee all rows imported

---

### Pattern 2: Sample Data Inspection

```bash
sqlite3 -column -header data/analytics.db <<'EOF'
SELECT * FROM raw_sales LIMIT 5;
EOF
```

**Check for:**
- Column values look correct
- No obvious truncation
- Data types appropriate

---

### Pattern 3: NULL Detection

```bash
sqlite3 data/analytics.db <<'EOF'
SELECT
    COUNT(*) as total_rows,
    COUNT(*) - COUNT(sale_id) as sale_id_nulls,
    COUNT(*) - COUNT(customer_id) as customer_id_nulls,
    COUNT(*) - COUNT(sale_date) as sale_date_nulls,
    COUNT(*) - COUNT(amount) as amount_nulls
FROM raw_sales;
EOF
```

**Identify:** Unexpected NULL values from import issues

---

### Pattern 4: Schema Verification

```bash
sqlite3 data/analytics.db "PRAGMA table_info(raw_sales);"
```

**Verify:** Table structure matches design

---

## Transaction Handling

### For Bulk Imports (Python)

```python
conn = sqlite3.connect('data/analytics.db')
cursor = conn.cursor()

# Start transaction
cursor.execute("BEGIN TRANSACTION")

try:
    # Multiple inserts...
    for row in data:
        cursor.execute("INSERT INTO table VALUES (?)", (row,))

    # Commit all at once
    conn.commit()
except Exception as e:
    # Rollback on error
    conn.rollback()
    print(f"Import failed: {e}")
finally:
    conn.close()
```

**Benefit:** 100x faster than individual commits, atomic operation

---

## Common Import Errors

| Error | Cause | Fix |
|-------|-------|-----|
| "Error: table already exists" | .import creates table if missing | Pre-create table with correct schema |
| Row count mismatch | Header miscounted, empty rows | Verify with tail -n +2 CSV count |
| "Error: wrong number of columns" | CSV columns ≠ table columns | Check .schema, verify CSV format |
| Silent data truncation | Column width limits (rare in SQLite) | Check MAX(LENGTH(column)) |
| Incorrect NULL handling | Empty string vs NULL confusion | Use Python for explicit NULL mapping |
| "UNIQUE constraint failed" | Duplicate primary key | Check CSV for duplicates first |

---

## DataPeeker Import Workflow

**From importing-data skill Phase 4:**

```bash
# Assuming Phase 1-3 complete (discovery, schema design, standardization)

DB="data/analytics.db"

# Step 1: Create table from schema design
sqlite3 $DB < 04-import-execution.sql

# Step 2: Verify table created
echo "=== Table Schema ==="
sqlite3 $DB "PRAGMA table_info(raw_sales);"

# Step 3: Import CSV
sqlite3 $DB <<'EOF'
.mode csv
.import data/raw/sales.csv raw_sales
EOF

# Step 4: Verify import
echo "=== Row Count ==="
sqlite3 $DB "SELECT COUNT(*) FROM raw_sales;"

echo "=== Sample Data ==="
sqlite3 -column -header $DB "SELECT * FROM raw_sales LIMIT 5;"

echo "=== NULL Analysis ==="
sqlite3 $DB <<'EOF'
SELECT
    COUNT(*) as total,
    COUNT(*) - COUNT(sale_id) as sale_id_nulls,
    COUNT(*) - COUNT(customer_id) as customer_id_nulls,
    COUNT(*) - COUNT(sale_date) as sale_date_nulls,
    COUNT(*) - COUNT(amount) as amount_nulls
FROM raw_sales;
EOF
```

**Document all results in Phase 4 markdown file**

---

## Handling Special Cases

### CSV with Spaces in Path

```bash
# Use quotes around path
sqlite3 data/analytics.db <<'EOF'
.mode csv
.import "data/raw/sales report 2025.csv" raw_sales
EOF
```

---

### CSV with Non-Standard Delimiter

```bash
# For TSV (tab-separated)
sqlite3 data/analytics.db <<'EOF'
.mode tabs
.import data/raw/sales.tsv raw_sales
EOF

# For custom delimiter (use Python)
```

---

### Large CSV Files (>100MB)

```python
# Use batched commits
import sqlite3
import csv

conn = sqlite3.connect('data/analytics.db')
cursor = conn.cursor()

BATCH_SIZE = 1000

cursor.execute("BEGIN TRANSACTION")
count = 0

with open('large_file.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute("INSERT INTO table VALUES (?)", (row['value'],))
        count += 1

        if count % BATCH_SIZE == 0:
            conn.commit()
            cursor.execute("BEGIN TRANSACTION")
            print(f"Imported {count} rows...")

conn.commit()
conn.close()
```

---

## Verification Checklist

After every import:
- [ ] Row count matches expectation (CSV count vs DB count)
- [ ] Sample data looks correct (LIMIT 5 inspection)
- [ ] No unexpected NULLs (NULL count query)
- [ ] Schema matches design (PRAGMA table_info)
- [ ] Documented results in analysis artifact

**Skipping verification = silent data loss risk**

---

## Real-World Example

```bash
#!/bin/bash

# Scenario: Import sales data with verification

DB="data/analytics.db"
CSV="data/raw/sales_2025_q1.csv"

echo "=== Import Starting ==="
date

# 1. Get expected row count
CSV_ROWS=$(tail -n +2 "$CSV" | wc -l | tr -d ' ')
echo "CSV has $CSV_ROWS rows (excluding header)"

# 2. Create table
echo "=== Creating Table ==="
sqlite3 $DB <<'EOF'
CREATE TABLE IF NOT EXISTS raw_sales_q1 (
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    sale_date TEXT,
    amount REAL,
    product TEXT
);
EOF

# 3. Import
echo "=== Importing ==="
sqlite3 $DB <<EOF
.mode csv
.import "$CSV" raw_sales_q1
EOF

# 4. Verify row count
DB_ROWS=$(sqlite3 $DB "SELECT COUNT(*) FROM raw_sales_q1;")
echo "Database has $DB_ROWS rows"

if [ "$CSV_ROWS" != "$DB_ROWS" ]; then
    echo "ERROR: Row count mismatch!"
    echo "Expected: $CSV_ROWS, Got: $DB_ROWS"
    exit 1
fi

# 5. Sample data
echo "=== Sample Data ==="
sqlite3 -column -header $DB "SELECT * FROM raw_sales_q1 LIMIT 5;"

# 6. NULL check
echo "=== NULL Analysis ==="
sqlite3 $DB <<'EOF'
SELECT
    COUNT(*) as total,
    COUNT(*) - COUNT(sale_id) as sale_id_nulls,
    COUNT(*) - COUNT(customer_id) as customer_id_nulls,
    COUNT(*) - COUNT(sale_date) as sale_date_nulls,
    COUNT(*) - COUNT(amount) as amount_nulls
FROM raw_sales_q1;
EOF

echo "=== Import Complete ==="
date
```

**Result:** Verified import with audit trail for reproducibility.
