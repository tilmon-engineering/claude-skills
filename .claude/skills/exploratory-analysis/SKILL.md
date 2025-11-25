---
name: exploratory-analysis
description: Systematic exploratory data analysis process - discover patterns in unfamiliar data, identify meaningful insights, formulate specific questions for deeper investigation
---

# Exploratory Analysis Process

## Overview

This skill guides you through systematic exploration of unfamiliar datasets when you don't yet have a specific question to answer. Unlike hypothesis-testing (where you test a specific claim) or guided-investigation (where you answer a specific question), exploratory analysis helps you **discover** what's interesting in the data and **identify** what questions you should be asking.

Exploratory analysis is appropriate when:
- You have a new dataset and need to understand what's in it
- The user says "Just see what's interesting" or "Tell me what stands out"
- You need to discover patterns before formulating specific questions
- You're looking for unexpected insights or anomalies
- You want to generate hypotheses for later testing

## Prerequisites

Before using this skill, you MUST:
1. Have data imported into SQLite database using the `importing-data` skill
2. Have data quality validated and cleaned using the `cleaning-data` skill (MANDATORY - never skip)
3. Have created an analysis workspace (`just start-analysis exploratory-analysis <name>`)
4. Have NO preconceived hypotheses or specific questions (if you do, use hypothesis-testing or guided-investigation instead)
5. Be familiar with the component skills:
   - `understanding-data` - for data profiling
   - `writing-queries` - for SQL query construction
   - `interpreting-results` - for result analysis
   - `creating-visualizations` - for text-based visualizations

## Mandatory Process Structure

You MUST use TodoWrite to track progress through all 5 phases. Create todos at the start:

```markdown
- Phase 1: Data Familiarization - pending
- Phase 2: Pattern Discovery - pending
- Phase 3: Anomaly Investigation - pending
- Phase 4: Insight Generation - pending
- Phase 5: Question Formulation - pending
```

Update status as you progress. Mark phases complete ONLY after checkpoint verification.

---

## Phase 1: Data Familiarization

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Catalogued all tables and their apparent purposes
- [ ] Documented schema (columns, types, relationships)
- [ ] Assessed data quality (completeness, ranges, distributions)
- [ ] Identified temporal coverage and granularity
- [ ] Saved to `01 - data-familiarization.md`

### Instructions

1. **Understand what data you have**

Create: `01 - data-familiarization.md`

```markdown
# Data Familiarization

## Exploration Context

**Dataset:** [Name or description]
**Source:** [Where data came from, if known]
**Exploration Goal:** [User's request, e.g., "Find interesting patterns in sales data"]

## Tables Overview

[List all tables with row counts and apparent purposes]

### Table: [table_name]
**Row count:** [count]
**Apparent purpose:** [What this table seems to represent]
**Grain:** [What one row represents, e.g., "one transaction", "one customer", "one daily summary"]

Example:
### Table: sales
**Row count:** 15,847
**Apparent purpose:** Transaction-level sales records
**Grain:** One row per individual sale transaction

### Table: [table_name_2]
...

## Schema Details

[For each table, document key columns]

### Table: sales
```sql
PRAGMA table_info(sales);
```

**Key columns identified:**
- `transaction_date` (TEXT) - when sale occurred
- `amount` (REAL) - sale value in currency
- `product_id` (INTEGER) - product identifier
- `customer_id` (INTEGER) - customer identifier
- `region` (TEXT) - geographic region

**Potential relationships:**
- `product_id` likely joins to products table
- `customer_id` likely joins to customers table

**Temporal coverage:**
- Earliest date: [result from MIN(transaction_date)]
- Latest date: [result from MAX(transaction_date)]
- Coverage: [X months/years of data]

## Data Quality Assessment

### Completeness

```sql
-- Check for NULL values in key columns
SELECT
  COUNT(*) as total_rows,
  COUNT(transaction_date) as non_null_dates,
  COUNT(amount) as non_null_amounts,
  COUNT(product_id) as non_null_products
FROM sales;
```

**Results:** [Paste results]

**Assessment:**
- [Column]: [% complete], [any concerns]
- [Column]: [% complete], [any concerns]

### Value Distributions

```sql
-- Check numeric column ranges
SELECT
  MIN(amount) as min_amount,
  MAX(amount) as max_amount,
  ROUND(AVG(amount), 2) as avg_amount,
  COUNT(DISTINCT customer_id) as unique_customers,
  COUNT(DISTINCT product_id) as unique_products
FROM sales;
```

**Results:** [Paste results]

**Observations:**
- Amount range: $[min] to $[max] (average: $[avg])
- [Number] unique customers
- [Number] unique products
- [Any outliers or surprises]

### Temporal Distribution

```sql
-- Check temporal distribution
SELECT
  STRFTIME('%Y-%m', transaction_date) as month,
  COUNT(*) as transaction_count
FROM sales
GROUP BY month
ORDER BY month;
```

**Results:** [Paste results]

**Observations:**
- [Gaps in data?]
- [Seasonality visible?]
- [Growing or shrinking over time?]
- [Complete weeks/months or partial?]

## Initial Impressions

[Before exploring patterns, note your initial observations]

- Dataset covers [timeframe]
- [Number] transactions across [number] products/customers/regions
- Data quality appears [good/fair/poor] because [reasons]
- Potential areas of interest:
  1. [Something that caught your attention]
  2. [Another interesting aspect]
  3. [Third area to explore]

## Exploration Strategy

[Based on familiarization, what vectors will you explore?]

Will explore:
1. **Time-based patterns:** [What temporal analyses make sense?]
2. **Segmentation patterns:** [What groups/categories to compare?]
3. **Relationship patterns:** [What correlations or associations to check?]
```

2. **Use the understanding-data component skill**
   - Profile the database systematically
   - Don't skip quality checks - surprises are common
   - Look for obvious data issues that would affect exploration

3. **Resist premature pattern-hunting**
   - Don't start with "I wonder if weekends are different"
   - First understand WHAT data you have, THEN explore patterns
   - If you catch yourself forming hypotheses, note them for Phase 2 but finish familiarization first

**Common Rationalization:** "I can see the tables, I don't need detailed familiarization"
**Reality:** Skipping familiarization leads to missing important context about data quality, coverage, and structure.

**Common Rationalization:** "I'll explore patterns while I familiarize myself with the data"
**Reality:** Mixing familiarization and pattern-hunting creates confusion. Separate concerns.

---

## Phase 2: Pattern Discovery

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Explored temporal patterns (trends, seasonality, cycles)
- [ ] Explored segmentation patterns (groups, categories, clusters)
- [ ] Explored relationship patterns (correlations, associations)
- [ ] Documented each exploration with rationale, query, results, observations
- [ ] Created separate files for each exploration vector
- [ ] Files saved as `02-temporal-patterns.md`, `03-segmentation-patterns.md`, `04-relationship-patterns.md`

### Instructions

1. **Explore SYSTEMATICALLY along three vectors**

You MUST explore all three vectors, even if some seem less promising. Surprises often come from unexpected places.

#### Vector 1: Temporal Patterns

Create: `02-temporal-patterns.md`

```markdown
# Temporal Pattern Exploration

## Objective

Discover how the data varies over time - trends, seasonality, cycles, or irregular patterns.

## Exploration Approach

[Explain what temporal analyses you'll perform]

1. Overall trend (is metric growing/shrinking/stable?)
2. Seasonal patterns (day-of-week, month-of-year, etc.)
3. Period-over-period comparisons (YoY, MoM, etc.)
4. Irregular events or anomalies in time series

---

## Analysis 1: Overall Trend

### Rationale
[Why checking overall trend first]

Example: "Establish baseline understanding of whether sales are growing, declining, or stable over the dataset period"

### Query
```sql
-- Monthly aggregation to see trend
SELECT
  STRFTIME('%Y-%m', transaction_date) as month,
  COUNT(*) as transaction_count,
  SUM(amount) as total_sales,
  ROUND(AVG(amount), 2) as avg_transaction,
  COUNT(DISTINCT customer_id) as unique_customers
FROM sales
GROUP BY month
ORDER BY month;
```

### Results
[Paste actual results]

### Observations
[What do you see? Facts only]

- First month: [stats]
- Last month: [stats]
- Overall direction: [growing/declining/stable/erratic]
- Growth rate: [approximate % change]
- Volatility: [stable or highly variable month-to-month]

### Text Visualization
[Use creating-visualizations skill to make a simple ASCII chart if helpful]

```
Month         Sales ($)
2024-01       ████████████████ 45,890
2024-02       ██████████████ 38,234
2024-03       ████████████████████ 52,145
```

---

## Analysis 2: Day-of-Week Patterns

### Rationale
[Why checking day-of-week]

### Query
```sql
SELECT
  CASE CAST(STRFTIME('%w', transaction_date) AS INTEGER)
    WHEN 0 THEN 'Sunday'
    WHEN 1 THEN 'Monday'
    WHEN 2 THEN 'Tuesday'
    WHEN 3 THEN 'Wednesday'
    WHEN 4 THEN 'Thursday'
    WHEN 5 THEN 'Friday'
    WHEN 6 THEN 'Saturday'
  END as day_name,
  CAST(STRFTIME('%w', transaction_date) AS INTEGER) as day_num,
  COUNT(*) as transaction_count,
  ROUND(AVG(amount), 2) as avg_amount,
  ROUND(SUM(amount), 2) as total_sales
FROM sales
GROUP BY day_num, day_name
ORDER BY day_num;
```

### Results
[Paste results]

### Observations
[Describe pattern - which days are high/low, by how much]

---

## Analysis 3: [Other temporal pattern]

[Repeat structure for month-of-year, hour-of-day if timestamps available, etc.]

---

## Temporal Patterns Summary

### Key Findings
1. **[Pattern 1]:** [Description with magnitude]
2. **[Pattern 2]:** [Description with magnitude]
3. **[Pattern 3]:** [Description with magnitude]

### Interesting Anomalies
- [Any unusual spikes or drops worth investigating]

### Questions Raised
- [What questions does this create for later investigation?]
```

#### Vector 2: Segmentation Patterns

Create: `03-segmentation-patterns.md`

```markdown
# Segmentation Pattern Exploration

## Objective

Discover how the data varies across natural groups - categories, segments, cohorts, or clusters.

## Exploration Approach

[Explain what segmentation dimensions you'll explore]

1. Categorical dimensions (region, product type, customer tier, etc.)
2. Derived segments (high/medium/low value, new/returning, etc.)
3. Cross-segments (region × product, etc.)

---

## Analysis 1: [Dimension] Distribution

### Rationale
[Why exploring this dimension]

Example: "Understand if sales are concentrated in certain regions or distributed evenly"

### Query
```sql
SELECT
  region,
  COUNT(*) as transaction_count,
  SUM(amount) as total_sales,
  ROUND(AVG(amount), 2) as avg_transaction,
  COUNT(DISTINCT customer_id) as unique_customers,
  -- Calculate percentage of total
  ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM sales), 1) as pct_of_transactions
FROM sales
WHERE region IS NOT NULL
GROUP BY region
ORDER BY total_sales DESC;
```

### Results
[Paste results]

### Observations
- [Top segment]: [stats] ([X]% of total)
- [Bottom segment]: [stats] ([X]% of total)
- Concentration: [How concentrated or distributed?]
- Differences: [Magnitude of differences between segments]

---

## Analysis 2: [Another dimension]

[Repeat structure for products, customer segments, etc.]

---

## Analysis 3: Cross-Segmentation

### Rationale
[Why looking at interaction of two dimensions]

Example: "Check if product preferences vary by region"

### Query
```sql
SELECT
  region,
  product_category,
  COUNT(*) as transaction_count,
  ROUND(SUM(amount), 2) as total_sales
FROM sales
  JOIN products ON sales.product_id = products.id
WHERE region IS NOT NULL AND product_category IS NOT NULL
GROUP BY region, product_category
ORDER BY region, total_sales DESC;
```

### Results
[Paste results]

### Observations
- [Pattern across segments]
- [Interesting variations]

---

## Segmentation Patterns Summary

### Key Findings
1. **[Finding 1]:** [Description]
2. **[Finding 2]:** [Description]

### Notable Differences
- [Biggest differences between segments]

### Questions Raised
- [What questions does this create?]
```

#### Vector 3: Relationship Patterns

Create: `04-relationship-patterns.md`

```markdown
# Relationship Pattern Exploration

## Objective

Discover correlations, associations, or dependencies between variables.

## Exploration Approach

[Explain what relationships you'll explore]

1. Metric correlations (does X relate to Y?)
2. Sequential patterns (does event A precede event B?)
3. Cohort behaviors (do groups behave differently over time?)

---

## Analysis 1: [Relationship description]

### Rationale
[Why exploring this relationship]

Example: "Check if transaction size correlates with customer tenure"

### Query
```sql
-- Create tenure buckets and compare average transaction size
SELECT
  CASE
    WHEN tenure_days < 30 THEN '0-30 days'
    WHEN tenure_days < 90 THEN '30-90 days'
    WHEN tenure_days < 180 THEN '90-180 days'
    WHEN tenure_days < 365 THEN '180-365 days'
    ELSE '1+ years'
  END as tenure_bucket,
  COUNT(*) as transaction_count,
  ROUND(AVG(amount), 2) as avg_amount,
  COUNT(DISTINCT customer_id) as unique_customers
FROM (
  SELECT
    s.*,
    JULIANDAY(s.transaction_date) - JULIANDAY(c.signup_date) as tenure_days
  FROM sales s
  JOIN customers c ON s.customer_id = c.id
)
GROUP BY tenure_bucket
ORDER BY MIN(tenure_days);
```

### Results
[Paste results]

### Observations
- [Pattern description]
- [Magnitude of correlation if present]
- [Direction: positive/negative/no relationship]

---

## Analysis 2: [Another relationship]

[Repeat structure]

---

## Relationship Patterns Summary

### Key Findings
1. **[Finding 1]:** [Description]
2. **[Finding 2]:** [Description]

### Correlations Identified
- [List any meaningful correlations with magnitude]

### Questions Raised
- [What questions does this create?]
```

2. **Be systematic, not random**
   - Explore ALL three vectors (temporal, segmentation, relationship)
   - Don't skip a vector just because first query seems uninteresting
   - Patterns often hide in places you don't expect

3. **Separate observation from interpretation**
   - In each analysis, state FACTS (what the numbers show)
   - Save interpretation for Phase 4 (Insight Generation)
   - Resist the urge to explain patterns yet - just catalog them

4. **Use visualizations liberally**
   - Text-based tables, ASCII charts, markdown formatting
   - Help patterns become visible
   - Refer to `creating-visualizations` component skill

**Common Rationalization:** "I found an interesting pattern, I'll just focus on that"
**Reality:** Focusing on first interesting pattern causes you to miss better patterns elsewhere. Complete all three vectors.

**Common Rationalization:** "This dimension looks boring, I'll skip it"
**Reality:** "Boring" dimensions often hide surprising patterns. Explore systematically.

**Common Rationalization:** "I'll combine all patterns into one analysis file"
**Reality:** Separate files by vector creates structure and makes findings easy to locate.

---

## Phase 3: Anomaly Investigation

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Identified 3-5 specific anomalies, outliers, or unexpected patterns from Phase 2
- [ ] Investigated each anomaly with follow-up queries
- [ ] Determined if anomalies are data quality issues or real phenomena
- [ ] Documented findings
- [ ] Saved to `05 - anomaly-investigation.md`

### Instructions

1. **Review Phase 2 for anomalies**

Go back through temporal, segmentation, and relationship explorations and identify:
- Unexpected spikes or drops
- Outlier values or segments
- Counterintuitive patterns
- Violations of expected business logic
- Inconsistencies or irregularities

2. **Investigate each anomaly**

Create: `05 - anomaly-investigation.md`

```markdown
# Anomaly Investigation

## Anomalies Identified

[List anomalies found in Phase 2]

1. **[Anomaly description]** - found in [which analysis]
2. **[Anomaly description]** - found in [which analysis]
3. **[Anomaly description]** - found in [which analysis]

---

## Anomaly 1: [Description]

### Where Found
[Reference to Phase 2 analysis where this was spotted]

Example: "In temporal analysis (02-temporal-patterns.md), noticed sales spike of 300% on 2024-02-14"

### Why It's Anomalous
[What makes this unusual or unexpected]

Example: "February 14 sales were $45,890, compared to typical daily average of $15,200 - a 3x spike"

### Investigation Query

```sql
-- Drill into the anomalous period
SELECT
  transaction_date,
  COUNT(*) as transaction_count,
  SUM(amount) as total_sales,
  ROUND(AVG(amount), 2) as avg_transaction,
  MIN(amount) as min_amount,
  MAX(amount) as max_amount,
  COUNT(DISTINCT customer_id) as unique_customers,
  COUNT(DISTINCT product_id) as unique_products
FROM sales
WHERE transaction_date BETWEEN '2024-02-13' AND '2024-02-15'
GROUP BY transaction_date
ORDER BY transaction_date;
```

### Results
[Paste results]

### Deeper Investigation

[If needed, more queries to understand the anomaly]

```sql
-- Check if specific products drove the spike
SELECT
  p.product_name,
  p.category,
  COUNT(*) as transaction_count,
  SUM(s.amount) as total_sales
FROM sales s
JOIN products p ON s.product_id = p.id
WHERE s.transaction_date = '2024-02-14'
GROUP BY p.product_name, p.category
ORDER BY total_sales DESC
LIMIT 10;
```

### Results
[Paste results]

### Explanation

**Determination:** [Data quality issue / Real phenomenon / Unclear]

**Reasoning:** [Explain what caused this anomaly]

Example: "Real phenomenon - Valentine's Day (Feb 14) drove 3x spike in flower and chocolate sales. Pattern is legitimate seasonal effect, not data error."

**Action:** [Should this be excluded from other analyses? Noted as special case? Investigated further?]

---

## Anomaly 2: [Next anomaly]

[Repeat structure]

---

## Anomalies Summary

### Real Phenomena
[List anomalies that are legitimate patterns worthy of insight]

1. **[Anomaly]:** [Brief explanation]
2. **[Anomaly]:** [Brief explanation]

### Data Quality Issues
[List anomalies that are data errors or artifacts]

1. **[Issue]:** [What's wrong and how it affects analysis]

### Unexplained
[List anomalies you couldn't fully explain]

1. **[Anomaly]:** [What remains unclear]

### Implications for Pattern Discovery

[How do these anomalies affect your Phase 2 findings?]

- [Anomaly] explains [pattern from Phase 2]
- [Data issue] invalidates [finding from Phase 2]
- [Real phenomenon] is interesting enough to become a standalone insight
```

3. **Distinguish data quality from real patterns**
   - NULL values, duplicates, data entry errors → data quality issues
   - Seasonal events, one-time promotions, external shocks → real phenomena
   - When unclear, state that explicitly

4. **Don't ignore anomalies**
   - Anomalies are often where the most interesting insights hide
   - Investigate thoroughly, don't dismiss as "probably nothing"
   - Data quality issues found now save headaches later

**Common Rationalization:** "That spike is probably a holiday, I'll ignore it"
**Reality:** VERIFY your assumption. "Probably" isn't good enough. Check.

**Common Rationalization:** "This anomaly is a data quality issue, I'll just exclude it"
**Reality:** Document what you're excluding and why. Future analysts need to know.

**Common Rationalization:** "I found 20 anomalies, I'll investigate them all"
**Reality:** Focus on the 3-5 most significant. You're exploring, not auditing every data point.

---

## Phase 4: Insight Generation

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Reviewed all patterns and anomalies from Phases 2-3
- [ ] Identified 3-5 insights that are actionable, surprising, or meaningful
- [ ] For each insight, documented: finding, significance, context, caveats
- [ ] Assessed confidence level for each insight
- [ ] Saved to `06 - insights.md`

### Instructions

1. **Extract insights from patterns**

Not every pattern is an insight. An insight must be:
- **Actionable:** Suggests a decision or further investigation
- **Surprising:** Non-obvious, counter to expectations, or revealing hidden structure
- **Meaningful:** Materially significant magnitude or impact

2. **Document insights systematically**

Create: `06 - insights.md`

```markdown
# Insights

## Insight Criteria

For this exploration, an insight must be:
- **Actionable:** Informs a decision or next investigation
- **Surprising:** Non-obvious or counter-intuitive
- **Meaningful:** Magnitude is significant enough to matter

---

## Insight 1: [Concise insight statement]

### The Finding

[Describe the pattern or relationship in specific terms]

Example: "Weekend sales are 40% lower than weekday sales, driven entirely by transaction volume (not ticket size)"

### Why It's Significant

[Explain why this matters - business impact, decision relevance, strategic importance]

Example: "If pattern is due to operational constraints (reduced hours), there's significant untapped revenue potential. If due to customer behavior, staffing/inventory strategies should shift toward weekdays."

### Supporting Evidence

[Reference specific analyses from Phases 2-3]

- Found in: [file reference]
- Key data points:
  - [Specific metric 1]
  - [Specific metric 2]
- Magnitude: [Quantify the effect]
- Consistency: [Is pattern consistent across time/segments?]

### Context and Interpretation

[Provide business context, possible explanations]

Example: "Could be explained by:
1. Store hours (reduced weekend hours)
2. Customer behavior (fewer weekend shoppers)
3. Product availability (limited weekend inventory)

Need operational data to distinguish these explanations."

### Caveats and Limitations

[What reduces confidence or limits applicability?]

Example:
- Based on 3 months of data (Jan-Mar); seasonal effects unknown
- Cannot distinguish operational constraints from demand patterns
- No control for holidays or special events

### Confidence Level

**Confidence:** [High / Medium / Low]

**Reasoning:** [Why this confidence level?]

Example:
**Confidence:** Medium

**Reasoning:** Pattern is clear and consistent across 13 weeks (strengthens confidence), but cannot determine causation without operational data (weakens confidence). Sample size is adequate.

### Recommended Action

[What should be done with this insight?]

- [ ] Further investigation: [What to investigate]
- [ ] Business decision: [What decision this informs]
- [ ] Data collection: [What additional data would help]

Example:
- [ ] Investigate store hours by day-of-week to test operational constraint hypothesis
- [ ] Run A/B test: extend Sunday hours and measure sales per operating hour
- [ ] Collect weekend vs weekday customer surveys to understand behavioral differences

---

## Insight 2: [Next insight]

[Repeat structure]

---

## Insight 3: [Next insight]

[Repeat structure]

---

## Non-Insights (Patterns That Didn't Qualify)

[List patterns found that were interesting but didn't meet insight criteria]

### Pattern: [Description]
**Why not an insight:** [Too small magnitude / Not actionable / Expected/obvious]

Example:
### Pattern: Sales increased 2% from January to March
**Why not an insight:** Magnitude too small to be meaningful (within normal variance); also could be seasonal effect of moving from winter to spring

---

## Insights Summary

### Highest Priority Insights
[Rank insights by importance/actionability]

1. **[Insight]:** [One sentence summary]
2. **[Insight]:** [One sentence summary]
3. **[Insight]:** [One sentence summary]

### Cross-Cutting Themes

[Are there themes that connect multiple insights?]

Example: "Multiple insights point to a customer segmentation issue - mid-tier customers behaving very differently from high/low tiers across time, product, and geography dimensions."

### Strategic Implications

[What do these insights collectively suggest about strategy, operations, or priorities?]

Example: "Dataset reveals significant untapped potential in weekend/Sunday operations and mid-tier customer retention. Both represent high-impact opportunities for revenue growth."
```

3. **Be selective**
   - Don't try to turn every pattern into an insight
   - 3-5 high-quality insights beat 20 marginal observations
   - If you have more than 5, rank them and focus on top 5

4. **Quantify magnitude**
   - "Sales vary by region" is not enough
   - "Top region has 3x sales of bottom region" is specific
   - Numbers make insights actionable

5. **Assess confidence honestly**
   - High confidence: Strong evidence, large sample, consistent pattern, clear interpretation
   - Medium confidence: Clear pattern but causation unclear OR limited time window OR potential confounds
   - Low confidence: Interesting but small sample OR inconsistent OR multiple plausible explanations

**Common Rationalization:** "Every pattern I found is an insight"
**Reality:** Most patterns are noise or expected. Be selective. Insights must clear the bar: actionable, surprising, meaningful.

**Common Rationalization:** "I'll just state the pattern and let the user figure out if it matters"
**Reality:** Your job is to interpret. Explain WHY the pattern matters and WHAT it suggests.

**Common Rationalization:** "I'm very confident in this insight"
**Reality:** Exploratory analysis rarely produces high confidence. Be honest about uncertainty and limitations.

---

## Phase 5: Question Formulation

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Generated 3-5 specific, answerable questions based on insights
- [ ] For each question, identified: what process to use, what data is needed, why it matters
- [ ] Prioritized questions by potential value
- [ ] Saved to `07 - next-questions.md`
- [ ] Updated `00 - overview.md` with exploration summary

### Instructions

1. **Convert insights into questions**

Each insight should suggest 1-2 follow-up questions. Good questions:
- Build on what you learned in exploration
- Are specific enough to be answerable
- Have clear business value
- Can be addressed with available (or obtainable) data

2. **Document questions for follow-up**

Create: `07 - next-questions.md`

```markdown
# Questions for Further Investigation

## Purpose

Exploratory analysis has identified patterns and insights. This document translates those insights into specific, answerable questions for deeper investigation.

---

## Question 1: [Specific question]

### What We Learned in Exploration

[Reference the insight that led to this question]

Example: "Exploration revealed that weekend sales are 40% lower than weekdays (Insight 1), but we cannot determine if this is due to operational constraints or customer behavior."

### The Question

[State the specific question to investigate]

Example: "Is the weekend sales decline caused by reduced operating hours, or do customers simply shop less on weekends when given equal opportunity?"

### Why It Matters

[Explain business value of answering this question]

Example: "If caused by reduced hours, extending weekend hours could capture ~$50K additional monthly revenue. If caused by customer behavior, we should optimize staffing for weekday peaks and reduce weekend overhead."

### Recommended Process

**Process Skill:** [Which DataPeeker process would answer this?]

- [ ] `hypothesis-testing` - if you have a specific claim to test
- [ ] `guided-investigation` - if you need to systematically explore the question
- [ ] `comparative-analysis` - if you need to compare specific segments

Example: **`comparative-analysis`** - compare weekend vs weekday sales controlling for operating hours

### Data Required

[What data would you need to answer this?]

- Current data: [What you already have]
- Additional data needed: [What you'd need to collect]

Example:
- Current data: Transaction timestamps (if available - check if we have hour-of-day data)
- Additional data needed: Store operating hours by day-of-week

### Investigation Approach

[Brief outline of how to investigate]

Example:
1. Extract hour-of-day from transaction timestamps
2. Calculate sales per operating hour for weekend vs weekday
3. Compare: if sales/hour are equal, it's an hours issue; if sales/hour are lower on weekends, it's a demand issue

### Priority

**Priority:** [High / Medium / Low]

**Reasoning:** [Why this priority level?]

Example:
**Priority:** High

**Reasoning:** Potential $50K/month revenue impact and requires minimal data collection (may already have timestamp data). Quick investigation with high-value outcome.

---

## Question 2: [Next question]

[Repeat structure]

---

## Question 3: [Next question]

[Repeat structure]

---

## Questions Summary

### High Priority Questions
[List high-priority questions in recommended investigation order]

1. **[Question]** - Expected value: [impact], Estimated effort: [time/data required]
2. **[Question]** - Expected value: [impact], Estimated effort: [time/data required]

### Medium Priority Questions
[Questions that would be valuable but less urgent]

### Questions Deferred
[Questions that can't be answered with available data or aren't worth the effort]

**[Question]:** [Why deferred]

### Investigation Roadmap

[If someone wanted to investigate all high-priority questions, what order makes sense?]

Example:
1. Start with Q1 (weekend sales) - quick win, uses existing data
2. Then Q3 (customer segmentation) - builds on Q1 findings
3. Finally Q2 (product mix) - most complex, benefits from context from Q1 and Q3

## Data Collection Priorities

[What new data sources would unlock multiple questions?]

Example: "Adding customer segment identifier to transaction data would enable investigation of Q2, Q4, and Q5. High-value data enrichment."
```

3. **Update exploration overview**

Update: `00 - overview.md`

Add at the end:

```markdown
## Exploration Summary

**Dataset:** [Name/description]

**Time Period:** [Coverage]

**Data Quality:** [Overall assessment]

**Exploration Completed:** [Date]

---

## Key Insights Discovered

1. **[Insight 1 title]:** [One sentence]
   - Magnitude: [Quantify]
   - Confidence: [High/Medium/Low]

2. **[Insight 2 title]:** [One sentence]
   - Magnitude: [Quantify]
   - Confidence: [High/Medium/Low]

3. **[Insight 3 title]:** [One sentence]
   - Magnitude: [Quantify]
   - Confidence: [High/Medium/Low]

---

## Recommended Next Steps

**Highest Priority:**
1. [Question] - investigate using [process skill]
2. [Question] - investigate using [process skill]

**Data Collection:**
- [Data source to add] - would enable [questions]

---

## File Index

- 01 - Data Familiarization
- 02 - Temporal Patterns
- 03 - Segmentation Patterns
- 04 - Relationship Patterns
- 05 - Anomaly Investigation
- 06 - Insights
- 07 - Next Questions
```

4. **Final verification checklist**
   - [ ] Explored all three vectors (temporal, segmentation, relationship)
   - [ ] Investigated significant anomalies
   - [ ] Generated 3-5 qualified insights (actionable, surprising, meaningful)
   - [ ] Formulated specific follow-up questions
   - [ ] Prioritized questions by value
   - [ ] Updated overview with summary
   - [ ] Communicated findings to user

**Common Rationalization:** "I found interesting patterns, I'm done"
**Reality:** Exploration isn't complete until you've formulated what to investigate next. Always end with questions.

**Common Rationalization:** "I'll just suggest broad areas to explore further"
**Reality:** Be specific. "Investigate customer behavior" is not actionable. "Compare weekend vs weekday sales per operating hour using comparative-analysis skill" is actionable.

**Common Rationalization:** "I'll list every possible question I can think of"
**Reality:** Focus on the 3-5 highest-value questions. Too many options create decision paralysis.

---

## Common Rationalizations

### "I can see interesting patterns already, I'll skip data familiarization"
**Why this is wrong:** Without understanding data quality, coverage, and structure, your pattern discoveries may be artifacts or noise.

**Do instead:** Complete Phase 1 fully. Familiarization prevents false discoveries and wasted effort.

### "This exploration vector looks boring, I'll skip it"
**Why this is wrong:** The most surprising insights often come from places you didn't expect. "Boring" dimensions frequently hide interesting patterns.

**Do instead:** Explore ALL three vectors (temporal, segmentation, relationship) systematically. Be comprehensive.

### "I found one great insight, that's enough"
**Why this is wrong:** One insight doesn't exhaust a dataset. You likely missed other valuable patterns.

**Do instead:** Continue systematic exploration. Aim for 3-5 insights across different dimensions.

### "Every pattern I found is an insight"
**Why this is wrong:** Most patterns are noise, expected, or immaterial. Calling everything an insight dilutes the valuable discoveries.

**Do instead:** Apply strict criteria: actionable, surprising, meaningful. Be selective.

### "I'll just describe patterns and let the user decide if they're important"
**Why this is wrong:** Your job is interpretation, not just data reporting. Users expect you to identify what matters and why.

**Do instead:** Assess significance, provide context, explain business implications. Do the analytical thinking.

### "I'm very confident in these exploratory findings"
**Why this is wrong:** Exploratory analysis generates hypotheses, not confirmations. Patterns need validation through targeted investigation.

**Do instead:** Be honest about confidence levels. Exploratory findings are typically medium-low confidence until validated.

### "I found interesting patterns, analysis is complete"
**Why this is wrong:** Exploration is the beginning, not the end. The goal is to identify what to investigate deeply.

**Do instead:** Always complete Phase 5. Convert insights into specific, answerable questions for follow-up.

### "I'll combine all patterns into one big report"
**Why this is wrong:** Mixing temporal, segmentation, and relationship analyses creates confusion and makes findings hard to locate.

**Do instead:** Separate files by exploration vector (02-temporal, 03-segmentation, 04-relationship). Clear structure aids comprehension.

### "This anomaly is probably a data error, I'll just exclude it"
**Why this is wrong:** Assumptions about anomalies are often wrong. "Probably" isn't good enough. Also, excluding data without documentation creates reproducibility issues.

**Do instead:** Investigate anomalies in Phase 3. Document what you exclude and why. Verify your assumptions.

### "I have 15 follow-up questions, I'll list them all"
**Why this is wrong:** Too many options create decision paralysis. Not all questions are equally valuable.

**Do instead:** Prioritize ruthlessly. Focus on 3-5 highest-value questions. Help the user know where to start.

---

## Summary

This skill ensures systematic, thorough exploration of unfamiliar datasets by:

1. **Familiarizing with data first:** Understand structure, quality, and coverage before pattern-hunting
2. **Exploring systematically:** Three vectors (temporal, segmentation, relationship) ensure comprehensive discovery
3. **Investigating anomalies:** Surprises and outliers often contain the most valuable insights
4. **Generating selective insights:** Apply strict criteria (actionable, surprising, meaningful) to separate signal from noise
5. **Formulating specific questions:** Convert insights into answerable questions for deeper investigation
6. **Prioritizing next steps:** Help users know what to investigate first and why

Follow this process and you'll discover what's truly interesting in unfamiliar data, avoid random pattern-chasing, and identify high-value questions for targeted investigation.
