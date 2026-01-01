# Explaining the Differences

## Differences to Explain

[List the key differences identified in Phase 3 that need explanation]

1. **[Difference 1]:** [Brief description with magnitude]
2. **[Difference 2]:** [Brief description with magnitude]
3. **[Difference 3]:** [Brief description with magnitude]

Example:
1. **Total Revenue:** Northeast 17% higher than Southeast ($66,780 difference)
2. **Customer Count:** Northeast 9% more customers than Southeast (232 customers)
3. **Product Mix:** Northeast skews 3pp more toward Electronics

---

## Difference 1: [Description]

### The Observed Difference

[Restate the finding from Phase 3]

Example: "Northeast region has 17% higher total revenue than Southeast ($458,920 vs $392,140)"

### Hypotheses for Why This Difference Exists

[List plausible explanations to investigate]

1. **[Hypothesis 1]:** [Explanation]
2. **[Hypothesis 2]:** [Explanation]
3. **[Hypothesis 3]:** [Explanation]

Example:
1. **Market size:** Northeast serves larger population / more potential customers
2. **Customer behavior:** Northeast customers purchase more frequently or at higher value
3. **Operational:** Northeast has more stores, longer hours, or better staffing
4. **Product availability:** Northeast carries different/better product mix
5. **Pricing:** Northeast has different pricing that drives more revenue

### Investigation: Hypothesis 1 - [Description]

**How to test:** [What query or analysis would confirm/refute this?]

```sql
-- Example: Test if customer count difference explains revenue difference
SELECT
  region,
  COUNT(DISTINCT customer_id) as customers,
  ROUND(SUM(amount), 2) as revenue,
  ROUND(SUM(amount) / COUNT(DISTINCT customer_id), 2) as revenue_per_customer
FROM sales
WHERE region IN ('Northeast', 'Southeast')
  AND transaction_date BETWEEN '2024-01-01' AND '2024-03-31'
GROUP BY region;
```

**Results:** [Paste results]

**Analysis:**

[Evaluate the hypothesis]

Example:
"Northeast has 232 more customers (8.9% more). If customer count were the ONLY difference, and per-customer revenue were equal, revenue difference would be:
- Expected: 8.9% revenue advantage
- Actual: 17.0% revenue advantage
- **Conclusion:** Customer count explains ~half the revenue gap. Other factors must explain the remaining 8pp."

**Verdict:** [Fully explains / Partially explains / Does not explain]

### Investigation: Hypothesis 2 - [Next hypothesis]

[Repeat structure]

### Investigation: Hypothesis 3 - [Next hypothesis]

[Repeat structure]

---

## Difference Decomposition: [Metric]

[Break down the difference into component factors]

### Mathematical Decomposition

[If applicable, show how metric can be broken into factors]

Example:
```
Total Revenue = Customers × Revenue per Customer
Total Revenue = Customers × Transactions per Customer × Revenue per Transaction

Northeast revenue advantage:
- Customer count effect: +8.9% (232 more customers)
- Revenue per customer effect: +7.5% ($11.22 more per customer)
- Combined multiplicative effect: ~17%

Conclusion: Both volume (more customers) AND value (higher per-customer) drive the difference
```

### Factor Contribution

[Quantify relative importance of factors]

Example:
| Factor | Contribution to Revenue Gap |
|--------|----------------------------|
| More customers | ~50% of gap |
| Higher revenue/customer | ~45% of gap |
| Interaction effect | ~5% of gap |

**Interpretation:** [What does this mean?]

Example: "Northeast advantage is roughly equally split between having more customers (volume) and extracting more value from each customer (intensity). This is a dual advantage."

---

## Difference 2: [Next Difference]

[Repeat full structure for next major difference]

---

## Confound Analysis

### Potential Confounds Checked

[List factors that could create spurious differences - revisit Phase 1 confounds]

1. **[Confound]:** [How you checked for this]
   - **Result:** [Found to be issue / Not an issue]

Example:
1. **Time period alignment:** Checked that both regions use identical date range (2024-01-01 to 2024-03-31)
   - **Result:** Confirmed aligned - not a confound

2. **Seasonality:** Checked if regions have different seasonal patterns
   - Query: Compared month-over-month growth for both regions
   - **Result:** Similar seasonal patterns - not a confound

3. **Holidays/Events:** Checked if regions had different holiday coverage
   - Analysis: Both regions include same holidays (New Year, Valentine's, etc.)
   - **Result:** Equal holiday exposure - not a confound

4. **Data quality:** Checked if one region has more NULL values or data issues
   - Reviewed Phase 2 quality checks
   - **Result:** Both regions >99% complete - not a confound

### Confounds That Could Not Be Ruled Out

[Factors that might affect comparison but can't be tested with available data]

Example:
1. **Store count:** No data on number of stores per region - Northeast might have more locations
2. **Operating hours:** No data on hours - differences could be operational rather than demand-based
3. **Marketing spend:** No data on regional marketing - could drive customer acquisition differences
4. **Competitive intensity:** No data on competitors - one region might have less competition

**Impact on conclusions:** [How does this limit your confidence?]

Example: "Cannot determine if Northeast advantage stems from market characteristics (larger market, less competition) or operational excellence (better execution). Causal interpretation is limited."

---

## Explanation Summary

### Key Findings

[Synthesize what you learned about WHY differences exist]

1. **[Finding 1]:** [Explanation with supporting evidence]
2. **[Finding 2]:** [Explanation with supporting evidence]
3. **[Finding 3]:** [Explanation with supporting evidence]

Example:
1. **Dual driver model:** Northeast revenue advantage comes from both more customers (+9%) AND higher value per customer (+7.5%)
2. **Product preference:** Northeast's 3pp skew toward Electronics (higher margin category) contributes to revenue/customer advantage
3. **Engagement similarity:** Transaction frequency is similar across regions - difference is not about customer engagement

### Causal vs Correlational

**What we can say with confidence:**
- [Patterns that are clearly demonstrated]

**What remains uncertain:**
- [Causal questions that can't be answered with available data]

Example:
**What we can say with confidence:**
- Northeast generates 17% more revenue through both volume and value advantages
- Product mix contributes modestly to per-customer revenue difference
- Customer engagement (transactions per customer) is similar

**What remains uncertain:**
- Whether Northeast advantage is due to market size, operations, or competitive dynamics
- Whether Southeast could achieve Northeast performance levels with operational changes
- Root cause of customer count difference (market size vs acquisition effectiveness)

### Alternative Explanations Not Ruled Out

[Acknowledge what else could explain the patterns]

Example:
1. Northeast might serve fundamentally different customer demographics (can't test without demographic data)
2. Regions might have different store footprints affecting convenience (no store location data)
3. Historical or seasonal factors beyond the Q1 window analyzed (limited to 3 months)
