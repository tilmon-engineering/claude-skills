# Data Discovery

## Available Data

[Use understanding-data skill to profile the database]

### Tables Overview
[List all tables and their purposes]

Example:
- `sales`: Transaction-level sales data
- `customers`: Customer demographics and segments
- `products`: Product catalog with categories
- `regions`: Geographic region definitions

### Relevant Columns by Sub-Question

#### Sub-Question 1: Temporal patterns
**Required data:**
- `sales.transaction_date` - for time series analysis
- `sales.amount` or `sales.revenue` - for sales metrics

**Data check needed:**
- Date range coverage
- Completeness of historical data
- Date format consistency

#### Sub-Question 2: [Next question]
**Required data:**
- [List columns needed]

**Data check needed:**
- [Quality checks to perform]

## Data Gaps and Limitations

[What data is NOT available that would be useful?]

Example:
1. **No competitor data:** Cannot directly measure competitive pressure
2. **No promotion history:** Cannot control for promotional effects
3. **No store hours data:** Cannot distinguish operational changes from demand changes
4. **Customer satisfaction scores:** Only available from Q2 onward, not for historical comparison

## Query Plan

For each sub-question, define what queries will be needed:

### Sub-Question 1: Temporal patterns
1. **Monthly sales trend:** GROUP BY month, calculate total and YoY change
2. **Week-over-week analysis:** Check for sudden drops vs gradual decline
3. **Same-period-last-year comparison:** Control for seasonality

### Sub-Question 2: [Next question]
1. **[Query description]**
2. **[Query description]**

## Investigation Strategy

[Based on data availability, what order will we investigate?]

Example:
1. Start with SQ1 (temporal) - data is complete, establishes baseline
2. Then SQ2 (regional) - data is good, will narrow focus
3. Skip SQ4 temporarily (data gap: no competitor data available)
4. End with SQ3 (product) - most granular, build on earlier findings
