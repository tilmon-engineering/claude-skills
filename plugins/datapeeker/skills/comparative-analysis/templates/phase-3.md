# Metric Comparison

## Objective

Compare all defined metrics across groups to identify meaningful differences.

**Materiality Threshold:** [Restate from Phase 1]

Example: "Differences >10% in primary metrics or >20% in secondary metrics are considered meaningful"

---

## Primary Metric 1: [Metric Name]

### Rationale

[Why this metric matters for the comparison]

### Query

```sql
-- Calculate [metric] for each group
SELECT
  region as group_name,
  COUNT(*) as transaction_count,
  ROUND(SUM(amount), 2) as total_revenue,
  ROUND(AVG(amount), 2) as avg_transaction_size,
  COUNT(DISTINCT customer_id) as unique_customers,
  ROUND(SUM(amount) / COUNT(DISTINCT customer_id), 2) as revenue_per_customer
FROM sales
WHERE region IN ('Northeast', 'Southeast')
  AND transaction_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY region
ORDER BY total_revenue DESC;
```

### Results

[Paste actual results]

### Comparison Table

| Metric | Northeast | Southeast | Difference | % Difference |
|--------|-----------|-----------|------------|--------------|
| Total Revenue | $458,920 | $392,140 | +$66,780 | +17.0% |
| Avg Transaction | $94.50 | $89.25 | +$5.25 | +5.9% |
| Customers | 2,847 | 2,615 | +232 | +8.9% |
| Revenue/Customer | $161.20 | $149.98 | +$11.22 | +7.5% |

### Observations

**Magnitude:** [Describe the difference with specific numbers]

Example: "Northeast has 17% higher total revenue ($66,780 more), driven by both more customers (+8.9%) and slightly higher revenue per customer (+7.5%)."

**Materiality:** [Meets threshold? Meaningful?]

Example: "Total revenue difference (17%) exceeds materiality threshold (10%). This is a meaningful difference worthy of explanation."

**Pattern:** [What does this tell us?]

Example: "Northeast advantage is multi-factorial: more customers AND higher per-customer value. Not just volume-driven."

### Visualization

[Use creating-visualizations skill for clarity]

```
Group          Total Revenue
Northeast      ████████████████████ $458,920
Southeast      ████████████████ $392,140
                                    (83% of NE)
```

---

## Primary Metric 2: [Next Metric]

[Repeat structure for each primary metric]

---

## Secondary Metrics

[Compare all secondary metrics using same structure]

### Product Mix Comparison

```sql
SELECT
  region,
  product_category,
  COUNT(*) as transactions,
  ROUND(SUM(amount), 2) as revenue,
  ROUND(100.0 * SUM(amount) / SUM(SUM(amount)) OVER (PARTITION BY region), 1) as pct_of_region_revenue
FROM sales
  JOIN products ON sales.product_id = products.id
WHERE region IN ('Northeast', 'Southeast')
  AND transaction_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY region, product_category
ORDER BY region, revenue DESC;
```

**Results:** [Paste results]

**Comparison:**

| Category | NE Revenue | NE % | SE Revenue | SE % | Difference |
|----------|------------|------|------------|------|------------|
| Electronics | $182,450 | 39.7% | $145,200 | 37.0% | +2.7pp |
| Apparel | $135,890 | 29.6% | $128,340 | 32.7% | -3.1pp |
| Home Goods | $98,120 | 21.4% | $75,890 | 19.4% | +2.0pp |
| Other | $42,460 | 9.3% | $42,710 | 10.9% | -1.6pp |

**Observations:** [What product mix differences exist?]

---

## Metrics Summary

### Meaningful Differences (Exceed Materiality Threshold)

[List all metrics where difference meets threshold]

1. **Total Revenue:** Northeast +17.0% (meaningful)
2. **Revenue per Customer:** Northeast +7.5% (below threshold but notable)
3. **[Metric]:** [Group] [+/- %] ([meaningful/not meaningful])

### Similar Metrics (Below Materiality Threshold)

[List metrics that are similar between groups]

1. **Average Transaction Size:** Only 5.9% difference (below 10% threshold)
2. **[Metric]:** [% difference] (groups are similar on this dimension)

### Directional Summary

[High-level summary of how groups compare]

Example:
"Northeast outperforms Southeast on volume metrics (customers, transactions, total revenue) by 8-17%. Per-customer and per-transaction metrics show smaller differences (6-8%), suggesting advantage is primarily scale-driven rather than fundamental behavior differences. Product mix is similar, with minor preferences for Electronics and Home Goods in Northeast."

### Comparison Visualization

[Overall summary table or chart]

| Dimension | Winner | Magnitude |
|-----------|--------|-----------|
| Total Revenue | Northeast | +17% |
| Customer Base | Northeast | +9% |
| Transaction Size | Northeast | +6% |
| Product Mix | Similar | <3pp diff |
| Engagement | Similar | <5% diff |
