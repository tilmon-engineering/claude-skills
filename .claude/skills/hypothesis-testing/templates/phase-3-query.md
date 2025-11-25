# [Query Purpose]

## Rationale
[Why this query is needed for the hypothesis test]

## Query
```sql
-- [Clear SQL with comments]
SELECT
  STRFTIME('%w', date_column) as day_of_week,  -- 0=Sunday, 6=Saturday
  COUNT(*) as transaction_count,
  SUM(amount) as total_sales,
  AVG(amount) as avg_sale,
  MIN(amount) as min_sale,
  MAX(amount) as max_sale
FROM sales
WHERE date_column IS NOT NULL
  AND amount IS NOT NULL
GROUP BY day_of_week
ORDER BY day_of_week;
```

## Results
[Paste actual query results here - raw output]

```
day_of_week | transaction_count | total_sales | avg_sale | min_sale | max_sale
0           | 1250              | 45890.50    | 36.71    | 5.00     | 299.99
1           | 2140              | 98234.20    | 45.90    | 5.00     | 450.00
...
```

## Initial Observations
[What do you see? NO INTERPRETATION YET, just facts]
- Day 0 (Sunday): 1,250 transactions, $36.71 average
- Day 1 (Monday): 2,140 transactions, $45.90 average
- [etc.]
