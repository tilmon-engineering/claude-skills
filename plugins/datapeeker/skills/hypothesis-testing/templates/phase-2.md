# Test Design

## Metrics

### Primary Metric
[What you'll measure - be specific about calculation]

Example: "Average daily sales amount, calculated as SUM(amount) grouped by day_of_week"

### Supporting Metrics
- [Additional metrics that provide context]
- [Sample sizes, variance measures, etc.]

## Comparison Structure

[How you'll compare groups/periods]

Example: "Compare average sales across all 7 days of the week"

## Data Requirements

### Required Tables/Columns
- Table: `sales`
  - `date` or `transaction_date` (date column)
  - `amount` or `total` (numeric sales value)
  - [Any other required columns]

### Data Quality Checks
1. **Missing values:** Check for NULL dates or amounts
2. **Date range:** Verify we have complete weeks (not partial data)
3. **Sample size:** Ensure adequate transactions per day-of-week
4. **Outliers:** Identify and decide how to handle extreme values

### Queries Needed (design, don't execute yet)
1. Schema check: Verify table structure
2. Data quality: Check for NULLs, ranges, counts
3. Main analysis: Calculate metric by segment
4. Supporting analysis: Calculate sample sizes, variance

## Statistical Considerations

[How you'll assess significance - note: we can't do formal statistical tests, but we can assess practical significance]

Example: "Look for differences >20% from average, check if driven by small sample sizes"
