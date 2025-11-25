---
name: comparative-analysis
description: Systematic comparison of segments, cohorts, or time periods - ensure fair apples-to-apples comparisons, identify meaningful differences, explain WHY differences exist
---

# Comparative Analysis Process

## Overview

This skill guides you through systematic comparison of two or more groups, segments, cohorts, or time periods. Unlike exploratory-analysis (where you discover patterns) or guided-investigation (where you answer broad questions), comparative analysis helps you **rigorously compare** specific groups and **explain** why they differ.

Comparative analysis is appropriate when:
- You need to compare performance between specific segments (regions, products, customer cohorts)
- You want to understand how groups differ across multiple dimensions
- You're evaluating changes before/after an intervention or between time periods
- The user asks "How does X compare to Y?" or "What's different about segment A vs B?"
- You need to make fair, apples-to-apples comparisons with controls for confounding factors

## Prerequisites

Before using this skill, you MUST:
1. Have data imported into SQLite database using the `importing-data` skill
2. Have data quality validated and cleaned using the `cleaning-data` skill (MANDATORY - never skip)
3. Have created an analysis workspace (`just start-analysis comparative-analysis <name>`)
4. Have clearly defined what you're comparing (user must specify comparison groups)
5. Be familiar with the component skills:
   - `understanding-data` - for data profiling
   - `writing-queries` - for SQL query construction
   - `interpreting-results` - for result analysis
   - `creating-visualizations` - for text-based visualizations

## Mandatory Process Structure

You MUST use TodoWrite to track progress through all 5 phases. Create todos at the start:

```markdown
- Phase 1: Define Comparison - pending
- Phase 2: Segment Definition - pending
- Phase 3: Metric Comparison - pending
- Phase 4: Difference Explanation - pending
- Phase 5: Conclusions and Recommendations - pending
```

Update status as you progress. Mark phases complete ONLY after checkpoint verification.

---

## Phase 1: Define Comparison

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Clarified what groups/segments/periods are being compared
- [ ] Identified the comparison objective (what question does this answer?)
- [ ] Determined comparison type (segments, cohorts, time periods, before/after)
- [ ] Established what metrics will be compared
- [ ] Documented the comparison framework
- [ ] Saved to `01 - comparison-definition.md`

### Instructions

1. **Clarify the comparison goal with the user**

Ask clarifying questions:
- What specific groups/segments do you want to compare?
- What's the purpose of this comparison? What decision will it inform?
- What differences would be meaningful or actionable?
- Are there specific metrics you care about most?
- What time period should the comparison cover?

2. **Define the comparison framework**

Create: `01 - comparison-definition.md`

```markdown
# Comparison Definition

## Comparison Objective

[Clear statement of what you're comparing and why]

Example: "Compare sales performance between Northeast and Southeast regions to understand regional differences and identify growth opportunities."

## Comparison Type

**Type:** [Select one: Segment Comparison / Cohort Comparison / Time Period Comparison / Before-After Comparison]

**Explanation:** [Brief description of comparison type]

Examples:
- **Segment Comparison:** Comparing naturally-occurring groups (regions, product categories, customer tiers)
- **Cohort Comparison:** Comparing groups defined by shared timing (signup month, first purchase year)
- **Time Period Comparison:** Comparing same metrics across different time ranges (Q1 vs Q2, 2024 vs 2025)
- **Before-After Comparison:** Comparing metrics before and after an event/intervention (pre-launch vs post-launch)

## Groups Being Compared

### Group 1: [Name/Description]
**Definition:** [How this group is defined in the data]
**Size/Scope:** [Expected magnitude - approximate # of records, customers, transactions]
**Time Period:** [What time range for this group]

Example:
### Group 1: Northeast Region
**Definition:** Customers where `region = 'Northeast'`
**Size/Scope:** ~15,000 transactions from approximately 2,500 customers
**Time Period:** January 2024 - March 2024 (Q1)

### Group 2: [Name/Description]
**Definition:** [How this group is defined]
**Size/Scope:** [Expected magnitude]
**Time Period:** [What time range]

### Group 3: [If comparing more than 2 groups]
...

## Comparison Metrics

[What specific metrics will be compared across groups?]

**Primary Metrics:**
1. **[Metric name]:** [Definition, why it matters]
2. **[Metric name]:** [Definition, why it matters]
3. **[Metric name]:** [Definition, why it matters]

Example:
**Primary Metrics:**
1. **Total Revenue:** Total sales dollars - measures overall volume
2. **Average Transaction Size:** Revenue per transaction - measures customer purchasing behavior
3. **Customer Count:** Unique customers - measures market penetration
4. **Transactions per Customer:** Average purchases per customer - measures engagement/loyalty

**Secondary Metrics:**
[Additional metrics that provide context]

1. **[Metric name]:** [Why this is useful context]
2. **[Metric name]:** [Why this is useful context]

Example:
**Secondary Metrics:**
1. **Product Mix:** Distribution of sales across categories - helps explain revenue differences
2. **Temporal Distribution:** Day-of-week patterns - checks for operational differences

## Fair Comparison Principles

[What controls or adjustments are needed for fair comparison?]

**Potential Confounds to Address:**
1. **[Confound]:** [How to control for this]
2. **[Confound]:** [How to control for this]

Example:
**Potential Confounds to Address:**
1. **Time period differences:** Ensure both regions use same date range
2. **Sample size:** Normalize metrics (per customer, per day) rather than raw totals
3. **Seasonality:** If comparing different time periods, control for seasonal effects
4. **Operational differences:** Check store hours, staffing levels if available

**What constitutes "different enough to matter":**
- [Define materiality threshold]

Example: "Difference of >10% in primary metrics or >20% in secondary metrics will be considered meaningful"

## Success Criteria

[What would make this comparison complete and useful?]

Example:
- Identify which metrics differ significantly (>10%) between regions
- Quantify the magnitude of key differences
- Explain the top 2-3 drivers of differences
- Provide actionable recommendations based on findings

## Questions to Answer

[Specific questions this comparison should answer]

1. [Question 1]
2. [Question 2]
3. [Question 3]

Example:
1. Which region has higher revenue, and by how much?
2. Is revenue difference due to more customers, higher transaction size, or both?
3. Do regions differ in product preferences or purchasing patterns?
4. What explains the observed differences?
```

3. **Get user confirmation before proceeding**
   - Review comparison definition with user
   - Confirm groups are defined correctly
   - Verify metrics align with user's goals
   - Adjust framework if needed

**Common Rationalization:** "The comparison is obvious, I'll just start querying"
**Reality:** Without explicit definition, you'll make unstated assumptions about what "fair" means.

**Common Rationalization:** "I'll compare everything and see what's different"
**Reality:** Unfocused comparison produces noise. Define specific metrics and materiality thresholds.

---

## Phase 2: Segment Definition

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Verified that comparison groups exist in the data
- [ ] Validated group definitions with actual queries
- [ ] Checked for data quality issues within each group
- [ ] Documented group characteristics and sample sizes
- [ ] Confirmed groups are comparable (similar data quality, coverage)
- [ ] Saved to `02 - segment-definition.md`

### Instructions

1. **Validate that groups exist and are well-defined**

Create: `02 - segment-definition.md`

```markdown
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
```

2. **Handle segment definition issues**

If groups are not comparable:
- **Sample size too small:** Consider combining groups, expanding time window, or adjusting comparison
- **Different time periods:** Either align periods or explicitly control for temporal effects
- **Data quality differs:** Document the difference and consider if it invalidates comparison
- **Overlapping groups:** Redefine to ensure groups are mutually exclusive

3. **Document any exclusions or adjustments**

If you exclude outliers, filter dates, or adjust definitions, document clearly:
```markdown
## Adjustments Made for Fair Comparison

1. **Outlier handling:** Excluded 8 transactions >$50,000 as data entry errors (confirmed with field validation)
2. **Date alignment:** Limited both groups to Feb 1 - Apr 30 to match shorter group's coverage
3. **Null handling:** Excluded 127 transactions with NULL customer_id from both groups
```

**Common Rationalization:** "The groups look fine, I'll skip validation"
**Reality:** Unstated data quality issues or sample size problems will invalidate your comparison.

**Common Rationalization:** "Sample sizes are different but that's okay"
**Reality:** Large sample size differences require per-capita normalization. Raw totals are misleading.

---

## Phase 3: Metric Comparison

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Calculated all primary metrics for each group
- [ ] Calculated all secondary metrics for each group
- [ ] Computed differences (absolute and percentage) between groups
- [ ] Created comparison visualizations (tables, charts)
- [ ] Identified which metrics differ meaningfully (per materiality threshold)
- [ ] Documented all comparisons with queries and results
- [ ] Saved to `03 - metric-comparison.md`

### Instructions

1. **Compare groups systematically across all metrics**

Create: `03 - metric-comparison.md`

```markdown
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
```

2. **Be rigorous about normalization**

Compare apples-to-apples:
- Use per-customer or per-day metrics, not raw totals (unless groups are identical size)
- Calculate percentages within group (e.g., % of group's revenue by category)
- Use rate metrics (transactions per customer, revenue per transaction)

Wrong: "Northeast has $458K revenue vs Southeast's $392K"
Right: "Northeast has $161/customer vs Southeast's $150/customer (7.5% higher)"

3. **Compute statistical and practical significance**

**Statistical significance:** Is difference larger than random variation would explain?
- With large samples (>1000), small differences can be statistically significant
- Document sample sizes to provide context

**Practical significance:** Is difference large enough to matter for decisions?
- Use materiality threshold from Phase 1
- 5% difference in revenue might be huge for a billion-dollar company, trivial for a startup

4. **Use visualization to make differences clear**

- Side-by-side tables with difference columns
- ASCII bar charts showing relative magnitudes
- Percentage difference callouts

**Common Rationalization:** "I'll just show the raw numbers and let the user interpret"
**Reality:** Your job is interpretation. Show differences clearly and explain what they mean.

**Common Rationalization:** "Northeast has more revenue, that's the answer"
**Reality:** Explain WHY - more customers? Higher spend per customer? Different product mix? Dig deeper.

**Common Rationalization:** "These differences are statistically significant, so they matter"
**Reality:** Statistical significance ≠ practical significance. A 1% difference might be "significant" but not meaningful.

---

## Phase 4: Difference Explanation

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Identified the 2-3 most important differences from Phase 3
- [ ] For each difference, investigated potential causes
- [ ] Analyzed confounding factors
- [ ] Ruled out alternative explanations where possible
- [ ] Quantified relative contribution of different factors
- [ ] Documented explanation analysis with supporting queries
- [ ] Saved to `04 - difference-explanation.md`

### Instructions

1. **Focus on the most meaningful differences**

Don't try to explain every small difference. Focus on:
- Differences that exceed materiality threshold
- Differences that are surprising or counter-intuitive
- Differences that inform the comparison objective

2. **Investigate WHY differences exist**

Create: `04 - difference-explanation.md`

```markdown
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
```

3. **Be intellectually honest about causation**

Comparative analysis shows WHAT differs, not always WHY:
- With observational data, you usually can't prove causation
- Multiple explanations may fit the data
- Acknowledge uncertainty and alternative explanations

4. **Decompose complex differences**

When metrics differ, break them into components:
- Revenue = Customers × Revenue per Customer
- Revenue per Customer = Transactions per Customer × Revenue per Transaction
- Identify which component drives the overall difference

**Common Rationalization:** "I found the difference, that's enough"
**Reality:** Finding the difference is half the job. Explaining WHY is equally important.

**Common Rationalization:** "This factor correlates with the difference, so it's the cause"
**Reality:** Correlation ≠ causation. Multiple factors may correlate. Be cautious about causal claims.

**Common Rationalization:** "I'll ignore confounds since I can't measure them"
**Reality:** Acknowledge unmeasured confounds explicitly. They limit your conclusions but shouldn't be ignored.

---

## Phase 5: Conclusions and Recommendations

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Summarized key differences and their magnitudes
- [ ] Explained most likely drivers of differences
- [ ] Assessed confidence in findings
- [ ] Identified actionable insights
- [ ] Made specific recommendations based on comparison
- [ ] Documented limitations and caveats
- [ ] Saved to `05 - conclusions-and-recommendations.md`
- [ ] Updated `00 - overview.md` with comparison summary

### Instructions

1. **Synthesize findings into clear conclusions**

Create: `05 - conclusions-and-recommendations.md`

```markdown
# Conclusions and Recommendations

## Comparison Summary

**Groups Compared:** [List groups]

**Time Period:** [Date range]

**Sample Sizes:** [Transactions, customers per group]

Example:
**Groups Compared:** Northeast vs Southeast regions

**Time Period:** Q1 2024 (January 1 - March 31)

**Sample Sizes:** Northeast: 4,857 transactions, 2,847 customers | Southeast: 4,393 transactions, 2,615 customers

---

## Key Findings

### Finding 1: [Concise finding statement]

**Magnitude:** [Quantify the difference]

**Explanation:** [Why this difference exists]

**Confidence:** [High / Medium / Low]

Example:
### Finding 1: Northeast generates 17% more revenue than Southeast

**Magnitude:** $66,780 higher revenue in Q1 ($458,920 vs $392,140)

**Explanation:** Revenue advantage stems from two factors:
1. Larger customer base (+232 customers, +8.9%)
2. Higher revenue per customer (+$11.22, +7.5%)

Product mix contributes modestly - Northeast's 3pp preference for Electronics adds ~$8K to the gap.

**Confidence:** High - robust sample sizes, consistent across metrics, confounds controlled

### Finding 2: [Next finding]

[Repeat structure]

### Finding 3: [Next finding]

[Repeat structure]

---

## Directional Summary

[High-level takeaway from the comparison]

Example:
"Northeast outperforms Southeast on nearly all metrics, with advantages concentrated in customer acquisition (9% more customers) and per-customer value (8% higher). The regions show similar customer engagement patterns (transactions per customer within 5%), suggesting behavioral similarity despite outcome differences. This points to market or operational factors rather than customer behavior as drivers of regional performance gap."

---

## Confidence Assessment

### High Confidence Conclusions

[What you can state with strong evidence]

1. [Conclusion with reasoning]
2. [Conclusion with reasoning]

Example:
1. **Northeast revenue advantage is real and substantial (17%):** Based on 90 days of data, >9,000 transactions, robust across multiple metrics
2. **Advantage is dual-source (volume + value):** Mathematical decomposition clearly shows both factors contribute ~equally

### Medium Confidence Conclusions

[What is likely but has some uncertainty]

1. [Conclusion with caveat]
2. [Conclusion with caveat]

Example:
1. **Product mix contributes modestly:** Electronics preference explains ~$8K of $67K gap, but product-level data has some attribution uncertainty
2. **Regions have similar customer engagement:** Similar transaction frequency, but limited to 3-month window

### Low Confidence / Uncertain

[What remains unclear or speculative]

1. [Uncertainty with explanation]
2. [Uncertainty with explanation]

Example:
1. **Root cause of customer count difference:** Could be market size, acquisition effectiveness, or historical factors - cannot determine from available data
2. **Sustainability of patterns:** Only 3 months of data - unclear if patterns hold year-round

---

## Limitations and Caveats

### Data Limitations

[What data constraints limit conclusions?]

1. **[Limitation]:** [Impact on analysis]
2. **[Limitation]:** [Impact on analysis]

Example:
1. **No operational data:** Cannot determine if differences stem from store count, hours, or staffing
2. **Limited time window:** 3 months may not capture full seasonal patterns or year-round dynamics
3. **No customer demographics:** Cannot control for population characteristics that might differ by region

### Analytical Limitations

[What methodological constraints exist?]

1. **[Limitation]:** [Impact]
2. **[Limitation]:** [Impact]

Example:
1. **Observational data only:** Cannot make causal claims about WHY regions differ
2. **No statistical testing:** Differences described but not tested for statistical significance
3. **Potential unmeasured confounds:** Store characteristics, competitive landscape, marketing spend not available

### Scope Limitations

[What was excluded from comparison?]

Example:
1. **Costs not included:** Compared revenue only, not profitability
2. **Other regions excluded:** Binary comparison (NE vs SE) - West and Midwest not analyzed
3. **Customer lifetime value:** Single quarter snapshot, not long-term value

---

## Actionable Insights

[What can be done with these findings?]

### Insight 1: [Actionable statement]

**The Opportunity:** [What this insight suggests is possible]

**Why It Matters:** [Business impact or value]

**Supporting Evidence:** [Reference to findings]

Example:
### Insight 1: Southeast has potential to close 17% revenue gap with Northeast

**The Opportunity:** If Southeast could achieve Northeast's performance levels, it would generate additional $66K per quarter ($265K annually)

**Why It Matters:** Material revenue growth opportunity (~17% increase) from existing operations

**Supporting Evidence:** Northeast demonstrates that $161/customer revenue is achievable; Southeast currently at $150/customer

### Insight 2: [Next insight]

[Repeat structure]

---

## Recommendations

### Priority 1: [High-priority recommendation]

**Recommendation:** [Specific action to take]

**Rationale:** [Why this matters, based on comparison findings]

**Expected Impact:** [What change would this drive]

**Implementation:** [How to do this]

**Data/Analysis Needed:** [What additional investigation would help]

Example:
### Priority 1: Investigate root cause of customer count difference

**Recommendation:** Conduct deep-dive analysis to understand why Northeast has 9% more customers than Southeast

**Rationale:** Customer acquisition accounts for ~50% of revenue gap. Understanding whether this stems from market size, operational factors, or acquisition effectiveness is critical to determining if Southeast can close the gap.

**Expected Impact:** If gap is operational/tactical (not market size), could guide strategies to boost Southeast customer base by up to 232 customers (~$36K quarterly revenue)

**Implementation:**
1. Gather data on: store count, market population, marketing spend, competitive intensity per region
2. Use guided-investigation skill to answer: "Why does Northeast have more customers?"
3. If operational factors identified, pilot interventions in Southeast to test effectiveness

**Data/Analysis Needed:**
- Store locations and square footage by region
- Regional population and demographics
- Marketing spend by region
- Customer acquisition cost and channel mix

### Priority 2: [Next recommendation]

[Repeat structure]

### Priority 3: [Next recommendation]

[Repeat structure]

---

## Follow-Up Questions

[What questions does this comparison raise for future investigation?]

1. **[Question]:** [Why this matters]
   - **Suggested process:** [hypothesis-testing / guided-investigation / comparative-analysis / exploratory-analysis]
   - **Data required:** [What you'd need]

Example:
1. **Why does Northeast have more customers?**
   - **Suggested process:** `guided-investigation` - decompose into market, operational, and acquisition factors
   - **Data required:** Store count, market demographics, marketing spend, acquisition channels

2. **Can Southeast replicate Northeast's product mix?**
   - **Suggested process:** `hypothesis-testing` - test if shifting SE toward Electronics would improve revenue/customer
   - **Data required:** Product availability by region, Electronics demand elasticity

3. **Do patterns hold year-round?**
   - **Suggested process:** `comparative-analysis` - repeat comparison for Q2, Q3, Q4 to check consistency
   - **Data required:** Full year of transaction data

---

## Comparison Validity

[Final assessment of how fair and valid the comparison was]

**Fair Comparison Checklist:**
- [x] Groups clearly defined and non-overlapping
- [x] Time periods aligned (both Q1 2024)
- [x] Sample sizes adequate (>2,500 customers per group)
- [x] Data quality comparable (>99% complete both groups)
- [x] Known confounds controlled (time, seasonality, data quality)
- [ ] All potential confounds addressed (operational factors unknown)

**Overall Validity:** [High / Medium / Low]

**Reasoning:** [Explain validity assessment]

Example:
**Overall Validity:** Medium-High

**Reasoning:** Comparison is well-controlled for temporal and data quality factors. Sample sizes are robust. Primary limitation is inability to control for operational differences (store count, hours, staffing) which may explain some or all of observed differences. Comparison validly describes WHAT differs but has limited ability to determine WHY.
```

2. **Update overview document**

Update: `00 - overview.md`

Add at the end:

```markdown
## Comparison Summary

**Groups Compared:** [Groups]

**Time Period:** [Date range]

**Comparison Completed:** [Date]

---

## Key Differences Identified

1. **[Difference 1]:** [Brief description with magnitude]
   - Driver: [Primary explanation]
   - Confidence: [High/Medium/Low]

2. **[Difference 2]:** [Brief description with magnitude]
   - Driver: [Primary explanation]
   - Confidence: [High/Medium/Low]

3. **[Difference 3]:** [Brief description with magnitude]
   - Driver: [Primary explanation]
   - Confidence: [High/Medium/Low]

---

## Top Recommendations

1. **[Recommendation 1]:** [One sentence]
   - Expected impact: [Magnitude]

2. **[Recommendation 2]:** [One sentence]
   - Expected impact: [Magnitude]

---

## File Index

- 01 - Comparison Definition
- 02 - Segment Definition
- 03 - Metric Comparison
- 04 - Difference Explanation
- 05 - Conclusions and Recommendations
```

3. **Communicate findings to user**

Present conclusions clearly:
- Lead with directional summary (which group "wins" and why)
- Quantify key differences with specific numbers
- Explain drivers of differences
- Acknowledge uncertainty and limitations
- Provide actionable recommendations
- Suggest follow-up questions

**Common Rationalization:** "I'll just present all the numbers and let the user draw conclusions"
**Reality:** Your job is to interpret and synthesize. Provide clear conclusions, not just data dumps.

**Common Rationalization:** "I'm 100% confident in these conclusions"
**Reality:** Be honest about confidence levels and limitations. Overconfidence undermines credibility.

**Common Rationalization:** "Comparison complete, no follow-up needed"
**Reality:** Comparisons often raise more questions than they answer. Identify high-value follow-up investigations.

---

## Common Rationalizations

### "The groups are obviously different, I'll skip formal definition"
**Why this is wrong:** "Obvious" differences often have unstated assumptions. Explicit definition prevents misunderstandings and ensures you're answering the right question.

**Do instead:** Complete Phase 1 fully. Define groups, metrics, and materiality thresholds explicitly.

### "Sample sizes look fine, I'll skip validation"
**Why this is wrong:** Sample size is only one aspect. Data quality, temporal alignment, and outliers can invalidate comparisons even with large samples.

**Do instead:** Validate groups thoroughly in Phase 2. Check quality, coverage, and comparability.

### "I'll just compare raw totals"
**Why this is wrong:** Raw totals are misleading when groups have different sizes. $500K vs $400K tells you nothing if one group is 2x the size of the other.

**Do instead:** Normalize by customers, days, or transactions. Compare per-capita or rate metrics.

### "Northeast has higher revenue, that's the finding"
**Why this is wrong:** Stating WHAT differs without explaining WHY provides limited value. The explanation is where actionable insights live.

**Do instead:** Decompose differences. Explain whether higher revenue comes from more customers, higher per-customer value, different mix, etc.

### "These groups are different, so one must be better"
**Why this is wrong:** Different doesn't mean better. Context matters. Lower-revenue group might serve a different market, have different goals, or optimize for different metrics.

**Do instead:** Interpret differences in context. Consider whether "better" is even the right framing.

### "I found a correlation, so that's the cause"
**Why this is wrong:** Correlation ≠ causation. Many factors correlate with outcomes without causing them.

**Do instead:** Be cautious with causal language. Say "associated with" or "correlated with" rather than "caused by" unless you have experimental evidence.

### "I'll ignore the confounds I can't measure"
**Why this is wrong:** Unmeasured confounds don't disappear by ignoring them. They limit what you can conclude.

**Do instead:** Explicitly acknowledge unmeasured confounds in Phase 4. Explain how they limit causal interpretation.

### "I'll recommend that Southeast copy Northeast exactly"
**Why this is wrong:** You don't know if differences are due to replicable practices or immutable characteristics (market size, demographics, etc.).

**Do instead:** Recommend further investigation to understand whether differences are actionable or structural.

### "This comparison answered the question completely"
**Why this is wrong:** Comparisons typically reveal new questions about root causes, generalizability, and interventions.

**Do instead:** Identify high-value follow-up questions in Phase 5. Guide next investigations.

### "Statistical significance means it matters"
**Why this is wrong:** With large samples, tiny differences can be statistically significant but practically meaningless.

**Do instead:** Focus on practical significance (materiality threshold). A 1% difference might be "significant" but not meaningful.

---

## Summary

This skill ensures rigorous, fair comparisons by:

1. **Defining comparisons explicitly:** Clear groups, metrics, and materiality thresholds prevent unstated assumptions
2. **Validating segment quality:** Ensuring groups are comparable prevents invalid comparisons
3. **Comparing systematically:** Multi-metric analysis reveals patterns that single metrics miss
4. **Explaining differences:** Understanding WHY groups differ is as important as knowing WHAT differs
5. **Acknowledging limitations:** Honest assessment of confounds and causation builds credibility
6. **Providing actionable insights:** Converting findings into recommendations and follow-up questions

Follow this process and you'll deliver fair, rigorous comparisons that explain not just WHAT differs but WHY, identify actionable opportunities, and guide follow-up investigations.
