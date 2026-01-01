# Optimizing Performance

## When to Use This Guidance

Use when:
- Query takes >1 second to execute
- Loading or processing large datasets (>100k rows)
- Running repeated similar queries
- Bulk insert/update operations are slow
- Need to diagnose why a query is slow

**Don't optimize prematurely.** Diagnose first, then optimize based on evidence.

## Step 1: Measure Performance

### Enable Timing

```bash
sqlite3 data/analytics.db <<'EOF'
.timer on
SELECT COUNT(*) FROM large_table;
EOF
```

**Output:**
```
1500000
Run Time: real 0.123 user 0.089 system 0.034
```

**When to optimize:** If real time >1 second for typical analysis queries

---

## Step 2: Diagnose with EXPLAIN QUERY PLAN

### Run Query Plan Analysis

```bash
sqlite3 data/analytics.db <<'EOF'
EXPLAIN QUERY PLAN
SELECT * FROM orders WHERE customer_id = 1001;
EOF
```

**Good output (using index):**
```
SEARCH orders USING INDEX idx_customer_id (customer_id=?)
```

**Bad output (full table scan):**
```
SCAN orders
```

**Key terms:**
- **SEARCH** = Using index (fast)
- **SCAN** = Full table scan (slow)

---

### Common Query Plan Patterns

| Pattern | Meaning | Speed |
|---------|---------|-------|
| `SEARCH table USING INDEX idx_name` | Index used | Fast ✓ |
| `SEARCH table USING INTEGER PRIMARY KEY` | Primary key used | Very fast ✓ |
| `SCAN table` | Full table scan | Slow ✗ |
| `USE TEMP B-TREE FOR ORDER BY` | Sorting without index | Slow for large data ✗ |

---

## Step 3: Create Indexes

### When to Create an Index

Create index when:
- Column frequently used in WHERE clauses
- Column used in JOIN conditions
- Column used in ORDER BY (and result set is large)
- EXPLAIN shows SCAN instead of SEARCH

**Don't create index when:**
- Table is small (<1000 rows)
- Column has very few distinct values
- Column rarely queried

---

### Single Column Index

```sql
CREATE INDEX idx_customer_id ON orders(customer_id);
```

**Use for:** Foreign key columns, frequently filtered columns

---

### Compound Index

```sql
CREATE INDEX idx_customer_date ON orders(customer_id, order_date);
```

**Use for:** Queries that filter on multiple columns

**Order matters:**
```sql
-- Good for: WHERE customer_id = X AND order_date > Y
-- Good for: WHERE customer_id = X
-- NOT good for: WHERE order_date > Y (only)
```

**Rule:** Put most selective column first, columns from WHERE before ORDER BY

---

### Partial Index (SQLite 3.8.0+)

```sql
CREATE INDEX idx_active_orders ON orders(customer_id)
WHERE status = 'active';
```

**Use for:** Queries that always filter on specific value

**Benefit:** Smaller index, faster queries on subset

---

### Verify Index Created

```bash
sqlite3 data/analytics.db ".indexes orders"
```

**Or detailed:**
```bash
sqlite3 data/analytics.db "PRAGMA index_list(orders);"
```

---

### Re-run Query Plan After Index

```bash
sqlite3 data/analytics.db <<'EOF'
EXPLAIN QUERY PLAN
SELECT * FROM orders WHERE customer_id = 1001;
EOF
```

**Should now show:** `SEARCH orders USING INDEX idx_customer_id`

---

## Step 4: Analyze Statistics

### Update Query Planner Statistics

```sql
ANALYZE;
```

**Run after:**
- Creating new indexes
- Large data imports
- Significant data changes

**Why:** Helps query planner choose best index

---

## Step 5: Transaction Optimization

### For Bulk Inserts

**Without transaction (slow):**
```python
for row in data:
    cursor.execute("INSERT INTO table VALUES (?)", (row,))
    conn.commit()  # Commit each insert - SLOW!
```

**With transaction (100x faster):**
```python
cursor.execute("BEGIN TRANSACTION")
for row in data:
    cursor.execute("INSERT INTO table VALUES (?)", (row,))
conn.commit()  # Single commit - FAST!
```

**Speed improvement:** 100x for bulk operations

---

### Batch Commits for Very Large Imports

```python
BATCH_SIZE = 10000

cursor.execute("BEGIN TRANSACTION")
for i, row in enumerate(data):
    cursor.execute("INSERT INTO table VALUES (?)", (row,))

    if (i + 1) % BATCH_SIZE == 0:
        conn.commit()
        cursor.execute("BEGIN TRANSACTION")
        print(f"Processed {i+1} rows...")

conn.commit()
```

**Benefit:** Balance between speed and memory usage

---

## Step 6: PRAGMA Optimizations

### Essential PRAGMAs for Performance

```sql
-- Journal mode (faster for concurrent access)
PRAGMA journal_mode = WAL;

-- Increase cache size (default is often too small)
PRAGMA cache_size = -64000;  -- 64MB cache (negative = KB)

-- Memory-mapped I/O for large databases
PRAGMA mmap_size = 268435456;  -- 256MB

-- Synchronous mode (careful: affects durability)
PRAGMA synchronous = NORMAL;  -- Default is FULL (safer but slower)
```

**Warning:** `PRAGMA synchronous = OFF` is dangerous (data loss risk), only use for imports if you can re-import

---

### Check Current Settings

```bash
sqlite3 data/analytics.db <<'EOF'
PRAGMA journal_mode;
PRAGMA cache_size;
PRAGMA mmap_size;
PRAGMA synchronous;
EOF
```

---

## Common Performance Patterns

### Pattern 1: Optimize Common Filter Column

```sql
-- Before (slow)
SELECT * FROM orders WHERE customer_id = 1001;
-- Query plan: SCAN orders

-- Create index
CREATE INDEX idx_customer_id ON orders(customer_id);

-- After (fast)
-- Query plan: SEARCH orders USING INDEX idx_customer_id
```

---

### Pattern 2: Optimize JOIN Performance

```sql
-- Diagnose
EXPLAIN QUERY PLAN
SELECT o.*, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id;

-- If showing SCAN, create indexes
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_customers_id ON customers(id);  -- Usually PK, already indexed

-- Re-check query plan
EXPLAIN QUERY PLAN ...
```

---

### Pattern 3: Optimize Sorted Queries

```sql
-- Before (slow with large result set)
SELECT * FROM orders WHERE customer_id = 1001 ORDER BY order_date DESC;
-- Query plan: USE TEMP B-TREE FOR ORDER BY

-- Create compound index
CREATE INDEX idx_customer_date ON orders(customer_id, order_date);

-- After (fast)
-- Query plan: SEARCH orders USING INDEX idx_customer_date
```

---

### Pattern 4: Optimize Aggregations

```sql
-- Slow for large tables
SELECT customer_id, COUNT(*) FROM orders GROUP BY customer_id;

-- Create index on GROUP BY column
CREATE INDEX idx_customer_id ON orders(customer_id);

-- Much faster with index
```

---

## Performance Troubleshooting

| Symptom | Likely Cause | Fix |
|---------|--------------|-----|
| Query takes >10 seconds | Full table scan | Add index on WHERE columns |
| JOIN is slow | Missing indexes on join keys | Index both sides of JOIN |
| Bulk insert is slow | Auto-commit each row | Wrap in transaction |
| ORDER BY is slow | Sorting large result set | Create index on sort columns |
| Queries slower after import | Stale statistics | Run ANALYZE |
| Multiple queries slow | Small cache | Increase PRAGMA cache_size |

---

## Real-World Example

```bash
# Scenario: Slow customer order history query

DB="data/analytics.db"

# Step 1: Measure baseline
echo "=== Baseline (no optimization) ==="
sqlite3 $DB <<'EOF'
.timer on
SELECT o.order_id, o.order_date, o.amount
FROM orders o
WHERE o.customer_id = 1001
ORDER BY o.order_date DESC
LIMIT 100;
EOF
# Result: 2.5 seconds

# Step 2: Diagnose
echo "=== Query Plan Analysis ==="
sqlite3 $DB <<'EOF'
EXPLAIN QUERY PLAN
SELECT o.order_id, o.order_date, o.amount
FROM orders o
WHERE o.customer_id = 1001
ORDER BY o.order_date DESC
LIMIT 100;
EOF
# Result: SCAN orders (no index)

# Step 3: Create compound index (customer_id + order_date)
echo "=== Creating Index ==="
sqlite3 $DB <<'EOF'
CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date);
EOF

# Step 4: Update statistics
echo "=== Updating Statistics ==="
sqlite3 $DB "ANALYZE;"

# Step 5: Re-measure
echo "=== After Optimization ==="
sqlite3 $DB <<'EOF'
.timer on
SELECT o.order_id, o.order_date, o.amount
FROM orders o
WHERE o.customer_id = 1001
ORDER BY o.order_date DESC
LIMIT 100;
EOF
# Result: 0.008 seconds (300x faster!)

# Step 6: Verify query plan
echo "=== Verify Query Plan ==="
sqlite3 $DB <<'EOF'
EXPLAIN QUERY PLAN
SELECT o.order_id, o.order_date, o.amount
FROM orders o
WHERE o.customer_id = 1001
ORDER BY o.order_date DESC
LIMIT 100;
EOF
# Result: SEARCH orders USING INDEX idx_orders_customer_date
```

---

## Optimization Checklist

Before creating indexes:
- [ ] Measured query time with .timer on
- [ ] Ran EXPLAIN QUERY PLAN
- [ ] Identified SCAN operations that should be SEARCH
- [ ] Determined which columns are filtered/joined/sorted most

After creating indexes:
- [ ] Verified index created (.indexes table_name)
- [ ] Ran ANALYZE to update statistics
- [ ] Re-ran EXPLAIN QUERY PLAN (should show SEARCH with index)
- [ ] Re-measured query time (should be significantly faster)
- [ ] Documented optimization in analysis notes

---

## When NOT to Optimize

**Don't optimize when:**
- Query runs in <1 second (fast enough)
- Table has <1000 rows (insignificant)
- Index would be larger than table (overhead not worth it)
- Column has only 2-3 distinct values (index not selective)
- One-time query (won't be repeated)

**Remember:** Premature optimization wastes time. Measure first, optimize only what matters.

---

## Quick Reference

### Diagnose
```sql
EXPLAIN QUERY PLAN SELECT ...;  -- See if using indexes
.timer on                       -- Measure query time
```

### Optimize
```sql
CREATE INDEX idx_name ON table(column);  -- Single column
CREATE INDEX idx_name ON table(col1, col2);  -- Compound
ANALYZE;  -- Update statistics
```

### Verify
```sql
.indexes table_name  -- List indexes
EXPLAIN QUERY PLAN SELECT ...;  -- Verify using index
```

### Bulk Operations
```python
cursor.execute("BEGIN TRANSACTION")
# ... many inserts ...
conn.commit()
```

**Rule of thumb:** If query takes >1 second and runs frequently, investigate with EXPLAIN QUERY PLAN.
