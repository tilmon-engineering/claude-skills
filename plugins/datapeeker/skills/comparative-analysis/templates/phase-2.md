# Segment Definition and Validation

## Objective

Verify that comparison groups are well-defined in the data, have adequate sample sizes, and are suitable for comparison.

---

## Group 1: [Name]

### Definition Query

[Query that identifies this group]

```sql
-- Example: Northeast region definition
SELECT DISTINCT region
FROM sales
WHERE region IS NOT NULL
ORDER BY region;

-- Verify 'Northeast' exists
```

**Results:** [Paste results]

**Validation:** [Confirm group identifier exists and is spelled consistently]

### Group Characteristics

```sql
-- Profile Group 1
SELECT
  COUNT(*) as total_transactions,
  COUNT(DISTINCT customer_id) as unique_customers,
  COUNT(DISTINCT product_id) as unique_products,
  MIN(transaction_date) as earliest_date,
  MAX(transaction_date) as latest_date,
  ROUND(SUM(amount), 2) as total_revenue,
  ROUND(AVG(amount), 2) as avg_transaction
FROM sales
WHERE region = 'Northeast'
  AND transaction_date BETWEEN '2024-01-01' AND '2024-03-31';
```

**Results:** [Paste results]

**Profile:**
- **Sample Size:** [Number of transactions, customers]
- **Temporal Coverage:** [Date range, any gaps?]
- **Revenue Scale:** [Total and average]
- **Product Diversity:** [Number of unique products]

### Data Quality Check

```sql
-- Check for NULL values or anomalies in Group 1
SELECT
  COUNT(*) as total_rows,
  COUNT(customer_id) as non_null_customers,
  COUNT(amount) as non_null_amounts,
  COUNT(CASE WHEN amount < 0 THEN 1 END) as negative_amounts,
  COUNT(CASE WHEN amount = 0 THEN 1 END) as zero_amounts,
  COUNT(CASE WHEN amount > 10000 THEN 1 END) as extreme_amounts
FROM sales
WHERE region = 'Northeast'
  AND transaction_date BETWEEN '2024-01-01' AND '2024-03-31';
```

**Results:** [Paste results]

**Quality Assessment:**
- Completeness: [% of records with required fields]
- Anomalies: [Any concerning patterns?]
- Outliers: [How many extreme values? Should they be excluded?]

---

## Group 2: [Name]

[Repeat same structure as Group 1]

### Definition Query
...

### Group Characteristics
...

### Data Quality Check
...

---

## Group 3: [If applicable]

[Repeat structure]

---

## Comparability Assessment

### Sample Size Comparison

| Group | Transactions | Customers | Date Range | Days of Data |
|-------|--------------|-----------|------------|--------------|
| [Group 1] | [count] | [count] | [range] | [days] |
| [Group 2] | [count] | [count] | [range] | [days] |

**Assessment:** [Are sample sizes adequate? Are they comparable? Any concerns?]

Example: "Both groups have >10,000 transactions and >2,000 customers. Sample sizes are adequate for comparison. Date ranges are identical (90 days), ensuring temporal comparability."

### Data Quality Comparison

| Group | Completeness % | Anomalies | Outliers |
|-------|----------------|-----------|----------|
| [Group 1] | [%] | [count/issues] | [count] |
| [Group 2] | [%] | [count/issues] | [count] |

**Assessment:** [Is data quality similar across groups? Any quality differences that could bias comparison?]

Example: "Data quality is comparable. Both groups have >99% completeness. Group 1 has 3 extreme values (>$10K), Group 2 has 5. Will include all data but note outlier sensitivity in analysis."

### Temporal Alignment

[Are time periods aligned? Any seasonal or calendar effects to consider?]

Example: "Both groups cover Q1 2024 (Jan 1 - Mar 31), so seasonality is controlled. Both include same number of weekends (13) and no major holidays affect one region more than the other."

### Fair Comparison Checklist

- [ ] Groups are clearly defined and non-overlapping
- [ ] Sample sizes are adequate (typically >1000 transactions or >100 customers per group)
- [ ] Time periods are aligned (same date range or controlled for seasonality)
- [ ] Data quality is comparable across groups
- [ ] Outliers are handled consistently
- [ ] No obvious confounds that would make comparison unfair

**Proceed to comparison?** [Yes/No - if No, explain what needs to be fixed]
