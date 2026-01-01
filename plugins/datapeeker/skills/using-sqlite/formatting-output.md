# Formatting Output

## When to Use This Guidance

Use when:
- Query results are hard to read or interpret
- Need specific format for export (CSV, JSON, Markdown)
- Preparing results for reports or documentation
- Column alignment is poor or headers are missing
- Redirecting output to files for further analysis

**Readable output is critical for data analysis.** Poorly formatted results lead to misinterpretation.

## Quick Format Selection

| Use Case | Mode | Command |
|----------|------|---------|
| **Human reading (terminal)** | column | `.mode column` + `.headers on` |
| **Export to spreadsheet** | csv | `.mode csv` + `.headers on` |
| **API/programming** | json | `.mode json` |
| **Documentation/reports** | markdown | `.mode markdown` + `.headers on` |
| **Copy to another DB** | insert | `.mode insert table_name` |
| **Debugging/inspection** | line | `.mode line` |

## Essential Output Modes

### 1. Column Mode (Human-Readable)

**Best for:** Terminal output, quick exploration

```bash
sqlite3 data/analytics.db <<'EOF'
.mode column
.headers on
.width 15 25 10
SELECT customer_id, name, order_count FROM top_customers LIMIT 5;
EOF
```

**Output:**
```
customer_id     name                      order_count
--------------  ------------------------  -----------
1001            Alice Johnson             42
1002            Bob Smith                 38
1003            Carol Williams            35
```

**Key settings:**
- `.mode column` - Align in columns
- `.headers on` - Show column names
- `.width 15 25 10` - Set column widths (optional)

---

### 2. CSV Mode (Export to Spreadsheet)

**Best for:** Excel, Google Sheets, data transfer

```bash
sqlite3 data/analytics.db <<'EOF'
.mode csv
.headers on
.output results.csv
SELECT * FROM monthly_sales;
.output stdout
EOF
```

**Output file (results.csv):**
```csv
month,revenue,order_count
2025-01,125000,450
2025-02,132000,478
```

**Critical:** Always use `.headers on` for CSV exports

---

### 3. JSON Mode (APIs/Programming)

**Best for:** Web APIs, JavaScript, Python processing

```bash
sqlite3 -json data/analytics.db "SELECT * FROM customers LIMIT 3;" > customers.json
```

**Output:**
```json
[
  {"customer_id":1001,"name":"Alice Johnson","email":"alice@example.com"},
  {"customer_id":1002,"name":"Bob Smith","email":"bob@example.com"},
  {"customer_id":1003,"name":"Carol Williams","email":"carol@example.com"}
]
```

**One-liner:** `sqlite3 -json` flag sets mode automatically

---

### 4. Markdown Mode (Reports/Documentation)

**Best for:** GitHub, documentation, analysis reports

```bash
sqlite3 data/analytics.db <<'EOF'
.mode markdown
.headers on
SELECT category, COUNT(*) as products, AVG(price) as avg_price
FROM products
GROUP BY category
LIMIT 5;
EOF
```

**Output:**
```markdown
| category    | products | avg_price |
|-------------|----------|-----------|
| Electronics | 145      | 299.99    |
| Books       | 523      | 15.99     |
| Clothing    | 234      | 45.50     |
```

**Perfect for:** Copying into markdown analysis documents

---

### 5. Line Mode (Debugging)

**Best for:** Inspecting individual records, debugging

```bash
sqlite3 data/analytics.db <<'EOF'
.mode line
SELECT * FROM customers WHERE customer_id = 1001;
EOF
```

**Output:**
```
customer_id = 1001
       name = Alice Johnson
      email = alice@example.com
signup_date = 2024-01-15
```

**Use when:** Need to see all fields of one record clearly

---

## Header Control

### Show Headers (Recommended)

```bash
.headers on
```

**Always use for:**
- CSV exports
- Column mode
- Markdown mode
- Any output someone else will read

### Hide Headers

```bash
.headers off
```

**Only use for:**
- Piping to scripts that expect no header
- Counting or single-value queries

---

## Redirecting Output

### To File

```bash
sqlite3 data/analytics.db <<'EOF'
.mode csv
.headers on
.output analysis_results.csv
SELECT * FROM monthly_metrics;
.output stdout
EOF
```

**Critical:** Always reset to stdout after: `.output stdout`

### Single Query to File

```bash
sqlite3 data/analytics.db <<'EOF'
.mode markdown
.headers on
.once report.md
SELECT * FROM summary_stats;
EOF
```

**Benefit:** `.once` auto-resets to stdout after one query

---

## Common Formatting Patterns

### Pattern 1: Quick Terminal Check

```bash
# Readable output for quick exploration
sqlite3 -column -header data/analytics.db "SELECT * FROM table LIMIT 10;"
```

---

### Pattern 2: Export for Spreadsheet

```bash
sqlite3 data/analytics.db <<'EOF'
.mode csv
.headers on
.output monthly_report.csv
SELECT
    STRFTIME('%Y-%m', order_date) as month,
    COUNT(*) as orders,
    SUM(amount) as revenue
FROM orders
GROUP BY month
ORDER BY month;
.output stdout
EOF
```

---

### Pattern 3: Multiple Outputs, Different Formats

```bash
sqlite3 data/analytics.db <<'EOF'
-- CSV for spreadsheet
.mode csv
.headers on
.output data.csv
SELECT * FROM results;

-- JSON for API
.mode json
.output data.json
SELECT * FROM results;

-- Markdown for report
.mode markdown
.output report.md
SELECT category, COUNT(*) as count FROM results GROUP BY category;

.output stdout
EOF
```

---

### Pattern 4: Report with Multiple Sections

```bash
sqlite3 data/analytics.db <<'EOF'
.mode markdown
.headers on
.output analysis_report.md

.print "# Sales Analysis Report"
.print ""
.print "## Total Sales by Category"
SELECT category, SUM(amount) as total FROM sales GROUP BY category;

.print ""
.print "## Monthly Trends"
SELECT STRFTIME('%Y-%m', sale_date) as month, COUNT(*) FROM sales GROUP BY month;

.output stdout
EOF
```

**Tip:** Use `.print` to add markdown headings and text between queries

---

## Width and Separator Control

### Set Column Widths (Column Mode)

```bash
.width 10 20 15 30
```

**Order:** Left to right, matches SELECT column order

### Custom Separator

```bash
.mode list
.separator "|"
```

**Output:** `value1|value2|value3`

---

## Null Value Display

### Show NULL as String

```bash
.nullvalue "NULL"
```

**Before:**
```
customer_id  email
1001
```

**After:**
```
customer_id  email
1001         NULL
```

**Benefit:** Distinguish NULL from empty string

---

## Box Mode (Pretty Tables)

```bash
sqlite3 -box data/analytics.db "SELECT * FROM summary LIMIT 5;"
```

**Output:**
```
┌─────────────┬──────────────┬─────────┐
│ customer_id │ name         │ orders  │
├─────────────┼──────────────┼─────────┤
│ 1001        │ Alice        │ 42      │
│ 1002        │ Bob          │ 38      │
└─────────────┴──────────────┴─────────┘
```

**Use for:** Presentation-quality terminal output

---

## Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| CSV export without headers | Columns unlabeled in spreadsheet | Always `.headers on` before export |
| Forgetting `.output stdout` | All subsequent output goes to file | Reset after each redirect |
| Using column mode for exports | Not machine-readable | Use csv/json for exports |
| No width settings in column mode | Truncated or misaligned data | Set `.width` for important columns |
| JSON mode with aggregates | Complex nesting | Use csv or markdown for aggregate results |

---

## DataPeeker Best Practices

### For Analysis Sessions

```bash
# Start every session with readable defaults
sqlite3 data/analytics.db <<'EOF'
.mode column
.headers on
.nullvalue "NULL"
.timer on
EOF
```

### For Exporting Results

```bash
# Always: mode, headers, output, query, reset
.mode csv
.headers on
.output filename.csv
SELECT ...;
.output stdout
```

### For Documentation

```bash
# Use markdown mode for analysis artifacts
.mode markdown
.headers on
.once 03-hypothesis-results.md
SELECT ...;
```

---

## Verification Checklist

Before finalizing output:
- [ ] Headers visible (unless intentionally hidden)
- [ ] Columns aligned/readable
- [ ] NULL values distinguishable from empty strings
- [ ] File output reset to stdout (if used)
- [ ] Format matches intended use (csv for spreadsheet, markdown for docs)

---

## Real-World Example

```bash
# Scenario: Generate monthly sales report for stakeholders

DB="data/analytics.db"

# 1. Readable terminal check
echo "=== Preview ==="
sqlite3 -column -header $DB <<'EOF'
SELECT
    STRFTIME('%Y-%m', order_date) as month,
    COUNT(*) as orders,
    SUM(amount) as revenue,
    ROUND(AVG(amount), 2) as avg_order
FROM orders
WHERE order_date >= '2025-01-01'
GROUP BY month
ORDER BY month DESC
LIMIT 3;
EOF

# 2. Export to CSV for stakeholder
echo "=== Exporting to CSV ==="
sqlite3 $DB <<'EOF'
.mode csv
.headers on
.output monthly_sales_2025.csv
SELECT
    STRFTIME('%Y-%m', order_date) as month,
    COUNT(*) as total_orders,
    SUM(amount) as total_revenue,
    ROUND(AVG(amount), 2) as average_order_value
FROM orders
WHERE order_date >= '2025-01-01'
GROUP BY month
ORDER BY month;
.output stdout
EOF

# 3. Add to analysis documentation
echo "=== Documenting ==="
sqlite3 $DB <<'EOF'
.mode markdown
.headers on
.output analysis_results.md
.print "# Monthly Sales Analysis - 2025"
.print ""
SELECT
    STRFTIME('%Y-%m', order_date) as month,
    COUNT(*) as orders,
    SUM(amount) as revenue
FROM orders
WHERE order_date >= '2025-01-01'
GROUP BY month
ORDER BY month;
.output stdout
EOF

echo "=== Complete ==="
ls -lh monthly_sales_2025.csv analysis_results.md
```

**Result:** Three formats from one query - terminal preview, spreadsheet export, markdown documentation.
