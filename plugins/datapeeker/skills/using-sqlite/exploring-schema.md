# Exploring Schema

## When to Use This Guidance

Use when:
- Starting analysis of an unfamiliar database
- Before writing join queries (need to know foreign keys)
- Checking if a table exists before querying
- Understanding column types to avoid type errors
- Verifying table structure after import

**Always explore schema before writing queries.** You cannot write correct queries without understanding the structure.

## Essential Commands

### 1. List All Tables

```bash
sqlite3 data/analytics.db ".tables"
```

**Output:**
```
clean_customers  raw_customers    raw_transactions
clean_orders     raw_orders
```

**Tip:** Use pattern matching: `.tables raw_%` to see only raw_ tables

---

### 2. View Table Structure

```bash
# Quick overview
sqlite3 data/analytics.db ".schema raw_customers"

# Detailed column info
sqlite3 data/analytics.db "PRAGMA table_info(raw_customers);"
```

**PRAGMA table_info Output:**
```
cid  name           type     notnull  dflt_value  pk
---  -------------  -------  -------  ----------  --
0    customer_id    INTEGER  1        NULL        1
1    name           TEXT     0        NULL        0
2    email          TEXT     0        NULL        0
3    signup_date    TEXT     0        NULL        0
```

**Columns explained:**
- `cid`: Column ID (position)
- `name`: Column name
- `type`: Data type (INTEGER, REAL, TEXT, BLOB)
- `notnull`: 1 if NOT NULL constraint, 0 otherwise
- `pk`: 1 if primary key, 0 otherwise

---

### 3. Check for Indexes

```bash
sqlite3 data/analytics.db ".indexes raw_customers"

# Or detailed info
sqlite3 data/analytics.db "PRAGMA index_list(raw_customers);"
```

**Why it matters:** Knowing which columns are indexed helps understand query performance.

---

### 4. View All Schema Information

```bash
sqlite3 data/analytics.db ".fullschema"
```

**Use for:** Complete database documentation, understanding all constraints

---

## Common Patterns

### Verify Table Exists Before Querying

```bash
sqlite3 data/analytics.db <<'EOF'
SELECT name FROM sqlite_master
WHERE type='table' AND name='raw_customers';
EOF
```

If returns empty, table doesn't exist.

---

### Check Column Names for a Table

```bash
sqlite3 data/analytics.db "PRAGMA table_info(raw_sales);" | cut -f2
```

**Output:** Just column names, useful for scripts

---

### Find All Tables with Specific Prefix

```bash
sqlite3 data/analytics.db <<'EOF'
SELECT name FROM sqlite_master
WHERE type='table' AND name LIKE 'raw_%'
ORDER BY name;
EOF
```

---

### Understand Foreign Key Relationships

```bash
sqlite3 data/analytics.db <<'EOF'
-- Check unique values in potential foreign key column
SELECT COUNT(DISTINCT customer_id) FROM raw_orders;

-- Compare to primary key table
SELECT COUNT(*) FROM raw_customers;

-- Check for orphaned records
SELECT COUNT(*) FROM raw_orders o
LEFT JOIN raw_customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
EOF
```

**Purpose:** Understand join cardinality before writing complex queries.

---

## Step-by-Step Exploration Workflow

**When starting analysis of unfamiliar database:**

```bash
DB="data/analytics.db"

# Step 1: What tables exist?
echo "=== Tables ==="
sqlite3 $DB ".tables"

# Step 2: For each important table, understand structure
echo "=== raw_sales schema ==="
sqlite3 $DB ".schema raw_sales"

# Step 3: Check detailed column info
echo "=== Column details ==="
sqlite3 $DB "PRAGMA table_info(raw_sales);"

# Step 4: Sample the data
echo "=== Sample data ==="
sqlite3 -column -header $DB "SELECT * FROM raw_sales LIMIT 3;"

# Step 5: Check for indexes
echo "=== Indexes ==="
sqlite3 $DB ".indexes raw_sales"
```

---

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Querying without checking schema | Wrong column names, type errors | Always .tables and .schema first |
| Assuming column types | Silent type coercion, incorrect results | Check PRAGMA table_info |
| Forgetting raw_/clean_ prefix | Query fails with "no such table" | Use .tables to verify exact name |
| Not checking for indexes | Optimize wrong columns | Check .indexes before creating new ones |
| Ignoring primary keys | Duplicate issues, join problems | Note pk=1 columns in table_info |

---

## DataPeeker Conventions

### Table Naming

```
raw_*    = Imported, unprocessed data
clean_*  = Quality-assured, analysis-ready data
```

**Before querying:** Check which version (raw_ vs clean_) you need.

### Column Type Conventions

- **Dates:** Always TEXT in ISO 8601 format (YYYY-MM-DD)
- **IDs:** Always INTEGER
- **Amounts:** REAL for decimal precision
- **Categories:** TEXT

---

## Real-World Example

```bash
# Scenario: Need to join orders and customers, but unfamiliar with schema

# 1. Check tables exist
sqlite3 data/analytics.db ".tables" | grep -E "(order|customer)"
# Found: raw_orders, clean_orders, raw_customers, clean_customers

# 2. Understand clean_orders structure
sqlite3 data/analytics.db "PRAGMA table_info(clean_orders);"
# Found columns: order_id (PK), customer_id, order_date, amount

# 3. Understand clean_customers structure
sqlite3 data/analytics.db "PRAGMA table_info(clean_customers);"
# Found columns: customer_id (PK), name, email, signup_date

# 4. Verify relationship
sqlite3 -column -header data/analytics.db <<'EOF'
SELECT
    COUNT(*) as orders,
    COUNT(DISTINCT customer_id) as unique_customers
FROM clean_orders;
EOF
# 1000 orders, 250 unique customers → 1-to-many relationship

# 5. Now safe to write join query
sqlite3 -column -header data/analytics.db <<'EOF'
SELECT c.name, COUNT(*) as order_count, SUM(o.amount) as total_spent
FROM clean_orders o
JOIN clean_customers c ON o.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spent DESC
LIMIT 10;
EOF
```

---

## Quick Checklist

Before writing any query:
- [ ] Verified table exists (`.tables`)
- [ ] Checked table structure (`.schema` or `PRAGMA table_info`)
- [ ] Understood column types
- [ ] Sampled data to verify content (`LIMIT 5`)
- [ ] If joining: verified foreign key relationships

**Time investment:** 2-3 minutes exploring saves 20+ minutes debugging wrong queries.
