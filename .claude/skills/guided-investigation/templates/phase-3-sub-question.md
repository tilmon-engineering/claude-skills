# Sub-Question 1: [Question text]

## Objective

[Restate what this sub-question is trying to determine]

Example: "Determine if the sales decline is concentrated in specific months or spread evenly across the year."

## Approach

[Explain how you'll answer this question - what queries/analysis steps]

Example:
1. Calculate monthly sales for current year and prior year
2. Compute YoY percentage change by month
3. Visualize the trend to identify when decline started
4. Check if decline is accelerating, stable, or improving

---

## Query 1: Monthly Sales Comparison

### Rationale
[Why this specific query is needed]

### Query
```sql
-- [Clear SQL with comments explaining logic]
SELECT
  STRFTIME('%Y-%m', transaction_date) as month,
  COUNT(*) as transaction_count,
  SUM(amount) as total_sales,
  ROUND(AVG(amount), 2) as avg_transaction
FROM sales
WHERE transaction_date >= '2023-01-01'
GROUP BY month
ORDER BY month;
```

### Results
[Paste actual query results - raw output]

```
month   | transaction_count | total_sales | avg_transaction
2023-01 | 4523             | 203450.67   | 44.97
2023-02 | 4234             | 189234.22   | 44.70
...
2024-01 | 3845             | 172389.45   | 44.82
2024-02 | 3623             | 162145.88   | 44.76
```

### Observations
[What do you see? Facts only, interpretation comes later]

- 2023-01: 4,523 transactions, $203,451 total
- 2024-01: 3,845 transactions, $172,389 total (15% decline in transactions, 15.3% decline in revenue)
- Average transaction size is stable (~$45) - decline is driven by volume, not ticket size

---

## Query 2: [Next query for this sub-question]

[Repeat the same structure: Rationale, Query, Results, Observations]

---

## Sub-Question Answer

[After all queries for this sub-question, synthesize the answer]

### Key Findings
[What did you learn? Answer the specific sub-question]

Example: "The sales decline began in January 2024 and has been consistent month-over-month (~15% vs prior year). The decline is driven entirely by transaction volume, not by changes in average purchase size."

### Implications
[What does this mean for the broader investigation?]

Example: "Since ticket size is stable, this suggests a customer traffic problem rather than a pricing or product mix issue. Need to investigate customer acquisition/retention in subsequent sub-questions."

### Follow-up Questions Raised
[What new questions does this create?]

1. Why did transaction volume drop in January specifically?
2. Are we losing customers or are existing customers buying less frequently?
3. Is this pattern consistent across all customer segments?
