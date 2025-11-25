# Invoking CLI

## When to Use This Guidance

Use when you need to decide:
- Which method to run sqlite3 commands (interactive, heredoc, file, one-liner)
- How to structure multi-command scripts
- When to use command-line flags vs dot commands
- How to handle paths with spaces or special characters

**Choose the right invocation method for the task.** Each has specific use cases.

## Four Invocation Methods

| Method | Best For | Example |
|--------|----------|---------|
| **Interactive** | Exploration, debugging, learning | `sqlite3 data.db` then type commands |
| **Heredoc** | Multi-command scripts, imports | `sqlite3 data.db <<'EOF' ... EOF` |
| **File Redirect** | SQL files, schema creation | `sqlite3 data.db < script.sql` |
| **One-liner** | Quick checks, single queries | `sqlite3 data.db "SELECT COUNT(*) FROM table;"` |

---

## Method 1: Interactive Mode

### When to Use

**Use for:**
- Exploring unfamiliar database
- Testing queries before scripting
- Learning SQLite commands
- Debugging query issues

**Don't use for:**
- Automated scripts (not reproducible)
- Multi-step workflows (can't document easily)
- Analysis artifacts (no audit trail)

---

### Starting Interactive Mode

```bash
sqlite3 data/analytics.db
```

**Prompt:**
```
SQLite version 3.X.X
Enter ".help" for usage hints.
sqlite>
```

---

### Common Interactive Commands

```sql
sqlite> .tables                    -- List tables
sqlite> .schema customers          -- View schema
sqlite> SELECT COUNT(*) FROM customers;  -- Run query
sqlite> .mode column               -- Set output format
sqlite> .headers on                -- Show headers
sqlite> SELECT * FROM customers LIMIT 5;  -- Formatted output
sqlite> .quit                      -- Exit
```

---

### Setting Defaults for Interactive Sessions

Create `~/.sqliterc`:
```sql
.mode column
.headers on
.nullvalue NULL
.timer on
```

**Benefit:** Every interactive session starts with readable defaults

---

## Method 2: Heredoc (Most Common for Scripts)

### When to Use

**Use for:**
- Multi-command workflows
- Import operations with configuration
- Scripts that need multiple SQL statements
- Setting output modes before queries

**DataPeeker standard:** Heredoc for most scripted operations

---

### Basic Heredoc Pattern

```bash
sqlite3 data/analytics.db <<'EOF'
.mode column
.headers on
SELECT * FROM customers LIMIT 10;
EOF
```

**Key:** Single quotes around `'EOF'` prevent variable expansion (safer)

---

### Multi-Command Heredoc

```bash
sqlite3 data/analytics.db <<'EOF'
-- Configure output
.mode column
.headers on
.width 15 30 20

-- Multiple queries
SELECT 'Customer Count:' as metric, COUNT(*) as value FROM customers;
SELECT 'Order Count:' as metric, COUNT(*) as value FROM orders;
SELECT 'Total Revenue:' as metric, SUM(amount) as value FROM orders;
EOF
```

---

### Import with Heredoc (Standard Pattern)

```bash
sqlite3 data/analytics.db <<'EOF'
.mode csv
.import data/raw/sales.csv raw_sales
EOF
```

---

### Output Redirection with Heredoc

```bash
sqlite3 data/analytics.db <<'EOF'
.mode markdown
.headers on
.output analysis_results.md
SELECT category, COUNT(*) as count FROM products GROUP BY category;
.output stdout
EOF
```

---

### Variable Expansion in Heredoc

**Without quotes (variables expanded):**
```bash
TABLE_NAME="customers"
sqlite3 data/analytics.db <<EOF
SELECT COUNT(*) FROM $TABLE_NAME;
EOF
```

**With quotes (no expansion, safer):**
```bash
sqlite3 data/analytics.db <<'EOF'
SELECT COUNT(*) FROM customers;
EOF
```

**Recommendation:** Use `'EOF'` unless you specifically need variable expansion

---

## Method 3: File Redirect

### When to Use

**Use for:**
- Schema creation (CREATE TABLE statements)
- Pre-written SQL scripts
- Complex queries stored in files
- Separating SQL from shell logic

---

### Basic File Redirect

```bash
sqlite3 data/analytics.db < create_schema.sql
```

**create_schema.sql:**
```sql
CREATE TABLE IF NOT EXISTS raw_sales (
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    sale_date TEXT,
    amount REAL
);

CREATE INDEX idx_customer_id ON raw_sales(customer_id);
```

---

### With Output Capture

```bash
sqlite3 data/analytics.db < queries.sql > results.txt
```

---

### DataPeeker Pattern: Schema Creation

```bash
# Phase 4: Import execution

# Step 1: Create table from SQL file
sqlite3 data/analytics.db < 04-create-table.sql

# Step 2: Verify
sqlite3 data/analytics.db "PRAGMA table_info(raw_sales);"
```

---

## Method 4: One-Liner

### When to Use

**Use for:**
- Quick checks (row counts, existence checks)
- Single query results
- Shell script conditionals
- Fast verification

**Don't use for:**
- Multiple related queries
- Queries needing output formatting
- Complex queries (hard to read on one line)

---

### Basic One-Liner

```bash
sqlite3 data/analytics.db "SELECT COUNT(*) FROM customers;"
```

**Output:** Just the result (no headers, no formatting)

---

### With Output Formatting

```bash
sqlite3 -column -header data/analytics.db "SELECT * FROM customers LIMIT 5;"
```

**Flags:**
- `-column` = Column-aligned output
- `-header` = Show column names

---

### With Output Mode

```bash
# CSV output
sqlite3 -csv data/analytics.db "SELECT * FROM customers;" > customers.csv

# JSON output
sqlite3 -json data/analytics.db "SELECT * FROM customers;" > customers.json

# Markdown output
sqlite3 -markdown data/analytics.db "SELECT * FROM customers;" > customers.md
```

---

### In Shell Conditionals

```bash
ROW_COUNT=$(sqlite3 data/analytics.db "SELECT COUNT(*) FROM raw_sales;")

if [ "$ROW_COUNT" -eq 0 ]; then
    echo "ERROR: No data imported!"
    exit 1
fi
```

---

### Quick Existence Check

```bash
# Check if table exists
TABLE_EXISTS=$(sqlite3 data/analytics.db "SELECT name FROM sqlite_master WHERE type='table' AND name='customers';")

if [ -z "$TABLE_EXISTS" ]; then
    echo "Table does not exist"
fi
```

---

## Common Patterns by Use Case

### Pattern 1: Quick Row Count Check

```bash
sqlite3 data/analytics.db "SELECT COUNT(*) FROM table_name;"
```

---

### Pattern 2: Exploration with Formatting

```bash
sqlite3 data/analytics.db <<'EOF'
.mode column
.headers on
.width 20 30 15
SELECT * FROM customers WHERE status = 'active' LIMIT 10;
EOF
```

---

### Pattern 3: Import with Verification

```bash
# Import
sqlite3 data/analytics.db <<'EOF'
.mode csv
.import data/raw/sales.csv raw_sales
EOF

# Verify
sqlite3 data/analytics.db "SELECT COUNT(*) FROM raw_sales;"
```

---

### Pattern 4: Schema Creation from File

```bash
# Create
sqlite3 data/analytics.db < schema.sql

# Verify
sqlite3 data/analytics.db ".schema raw_sales"
```

---

### Pattern 5: Multi-Format Export

```bash
DB="data/analytics.db"
QUERY="SELECT * FROM monthly_summary"

# CSV for spreadsheet
sqlite3 -csv -header $DB "$QUERY" > summary.csv

# JSON for API
sqlite3 -json $DB "$QUERY" > summary.json

# Markdown for docs
sqlite3 -markdown -header $DB "$QUERY" > summary.md
```

---

## Handling Special Cases

### Paths with Spaces

```bash
# Use quotes
sqlite3 "data/analytics database.db" "SELECT COUNT(*) FROM table;"

# Heredoc (safer)
sqlite3 "data/analytics database.db" <<'EOF'
SELECT COUNT(*) FROM table;
EOF
```

---

### Multi-Line Queries (Readability)

**Heredoc (recommended):**
```bash
sqlite3 data/analytics.db <<'EOF'
SELECT
    customer_id,
    COUNT(*) as order_count,
    SUM(amount) as total_spent
FROM orders
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
EOF
```

**One-liner (hard to read):**
```bash
sqlite3 data/analytics.db "SELECT customer_id, COUNT(*) as order_count, SUM(amount) as total_spent FROM orders GROUP BY customer_id ORDER BY total_spent DESC LIMIT 10;"
```

---

### Passing Shell Variables Safely

```bash
TABLE_NAME="customers"
LIMIT=10

# Heredoc without quotes (variables expanded)
sqlite3 data/analytics.db <<EOF
SELECT * FROM $TABLE_NAME LIMIT $LIMIT;
EOF
```

**Warning:** Avoid user input in SQL (SQL injection risk). For programmatic access, use Python with parameterized queries.

---

## Command-Line Flags Reference

| Flag | Purpose | Example |
|------|---------|---------|
| `-header` | Show column headers | `sqlite3 -header db.db "SELECT * FROM t;"` |
| `-column` | Column-aligned output | `sqlite3 -column db.db "SELECT * FROM t;"` |
| `-csv` | CSV output | `sqlite3 -csv db.db "SELECT * FROM t;" > out.csv` |
| `-json` | JSON output | `sqlite3 -json db.db "SELECT * FROM t;" > out.json` |
| `-markdown` | Markdown table | `sqlite3 -markdown db.db "SELECT * FROM t;"` |
| `-readonly` | Open read-only | `sqlite3 -readonly db.db` |
| `-init FILE` | Run FILE on startup | `sqlite3 -init setup.sql db.db` |
| `-cmd CMD` | Run CMD before other | `sqlite3 -cmd ".mode csv" db.db` |

---

## Decision Tree

```
Need to run SQLite command?
│
├─ Just exploring/learning?
│  └─ Use: Interactive mode
│
├─ Single quick query?
│  └─ Use: One-liner (with -column -header if needed)
│
├─ Multiple commands or import?
│  └─ Use: Heredoc
│
└─ Complex SQL in separate file?
   └─ Use: File redirect (<)
```

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Interactive for scripts | Not reproducible | Use heredoc or file redirect |
| One-liner for complex query | Hard to read, maintain | Use heredoc for multi-line |
| Heredoc without EOF quotes | Variables expanded accidentally | Use `<<'EOF'` (with quotes) |
| Forgetting -header flag | No column names in output | Add `-header` to one-liners |
| File paths without quotes | Breaks with spaces | Quote paths: `"path/to/file.db"` |
| Using one-liner for imports | Can't set .mode easily | Use heredoc for imports |

---

## DataPeeker Standards

### For Analysis Workflows

**Use heredoc:**
```bash
sqlite3 data/analytics.db <<'EOF'
.mode column
.headers on
SELECT ...;
EOF
```

---

### For Verification

**Use one-liner:**
```bash
sqlite3 data/analytics.db "SELECT COUNT(*) FROM table;"
```

---

### For Schema Creation

**Use file redirect:**
```bash
sqlite3 data/analytics.db < schema.sql
```

---

## Real-World Example

```bash
#!/bin/bash

DB="data/analytics.db"

# Quick check (one-liner)
echo "=== Row Count ==="
sqlite3 $DB "SELECT COUNT(*) FROM orders;"

# Exploration (heredoc with formatting)
echo "=== Top Customers ==="
sqlite3 $DB <<'EOF'
.mode column
.headers on
.width 15 30 15 15
SELECT
    customer_id,
    name,
    order_count,
    total_spent
FROM customer_summary
ORDER BY total_spent DESC
LIMIT 10;
EOF

# Export (one-liner with mode flag)
echo "=== Exporting to CSV ==="
sqlite3 -csv -header $DB "SELECT * FROM monthly_summary;" > monthly_report.csv

# Schema creation (file redirect)
echo "=== Creating New Table ==="
sqlite3 $DB < create_temp_table.sql

# Verification (one-liner)
echo "=== Verify Table Created ==="
sqlite3 $DB ".schema temp_analysis"

echo "=== Complete ==="
```

**Result:** Each method used for its optimal purpose - readable, maintainable, reproducible.

---

## Quick Reference

**Interactive:** `sqlite3 db.db` (exploration)
**Heredoc:** `sqlite3 db.db <<'EOF' ... EOF` (scripts)
**File:** `sqlite3 db.db < file.sql` (schema)
**One-liner:** `sqlite3 db.db "SELECT ..."` (quick checks)

**With formatting:** Add `-column -header` to one-liners
**With mode:** Add `-csv`, `-json`, or `-markdown` to one-liners

**Recommendation:** Default to heredoc for DataPeeker workflows (reproducible, readable, flexible).
