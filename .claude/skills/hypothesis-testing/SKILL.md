---
name: hypothesis-testing
description: Rigorous hypothesis testing process for data analysis - formulate hypotheses before looking at data, design tests, analyze systematically, interpret with skepticism
---

# Hypothesis Testing Process

## Overview

This skill guides you through rigorous hypothesis testing in data analysis. The core principle is **scientific rigor**: formulate your hypotheses BEFORE looking at the data to avoid p-hacking and confirmation bias.

Hypothesis testing is appropriate when:
- You have a specific claim or belief to test
- You want to avoid confirmation bias
- The question can be framed as "Does X affect Y?"
- You need defensible, reproducible conclusions

## Prerequisites

Before using this skill, you MUST:
1. Have data imported into SQLite database using the `importing-data` skill
2. Have data quality validated and cleaned using the `cleaning-data` skill (MANDATORY - never skip)
3. Have created an analysis workspace (`just start-analysis hypothesis-testing <name>`)
4. Understand the basic structure of your data tables
5. Be familiar with the component skills:
   - `understanding-data` - for data profiling
   - `writing-queries` - for SQL query construction
   - `interpreting-results` - for result analysis
   - `creating-visualizations` - for text-based visualizations

## Mandatory Process Structure

You MUST use TodoWrite to track progress through all 5 phases. Create todos at the start:

```markdown
- Phase 1: Hypothesis Formulation (H0/H1) - pending
- Phase 2: Test Design - pending
- Phase 3: Data Analysis - pending
- Phase 4: Result Interpretation - pending
- Phase 5: Conclusion and Follow-up - pending
```

Update status as you progress. Mark phases complete ONLY after checkpoint verification.

---

## Phase 1: Hypothesis Formulation

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Written null hypothesis (H0) - specific, testable statement
- [ ] Written alternative hypothesis (H1) - specific, directional or non-directional
- [ ] Documented WHY you're testing this (user goal, business context)
- [ ] Saved to `01 - hypothesis-formulation.md`

### Instructions

1. **Ask clarifying questions** about the user's analytical goal
   - What belief or claim needs testing?
   - What would constitute evidence for/against this belief?
   - What's the practical significance threshold?

2. **Write hypotheses in `01 - hypothesis-formulation.md`** with: ./templates/phase-1.md

3. **STOP and get user confirmation**
   - Read the hypotheses back to the user
   - Confirm this is what they want to test
   - Do NOT proceed to Phase 2 until confirmed

**Common Rationalization:** "I'll just peek at the data to refine the hypothesis"
**Reality:** This creates confirmation bias. Formulate hypothesis FIRST, always.

---

## Phase 2: Test Design

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Defined exact metrics to calculate
- [ ] Specified comparison method (segments, time periods, etc.)
- [ ] Listed required data checks (missing values, outliers, sample sizes)
- [ ] Written test plan WITHOUT executing any queries yet
- [ ] Saved to `02 - test-design.md`

### Instructions

1. **Design your test in `02 - test-design.md`** with: ./templates/phase-2.md

2. **STOP and verify test design**
   - Does this test actually answer the hypothesis?
   - Are there simpler/better ways to test it?
   - Have you planned for data quality issues?
   - Get user confirmation before proceeding

**Common Rationalization:** "I'll just run one quick query to see if the data exists"
**Reality:** That's looking at data before test design is complete. Finish design FIRST.

---

## Phase 3: Data Analysis

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Executed schema/data quality checks
- [ ] Documented any data issues found
- [ ] Executed main analysis query
- [ ] Executed supporting analysis queries
- [ ] Saved all queries and results to numbered files (03-*, 04-*, etc.)

### Instructions

1. **Execute queries in order, one file per query**

Create separate numbered files:
- `03 - schema-check.md`
- `04 - data-quality-check.md`
- `05 - main-analysis.md`
- `06 - supporting-analysis.md` (if needed)

2. **For each query file, use this structure:** ./templates/phase-3-query.md

3. **Execute queries using appropriate tool**
   - Use SQLite CLI or database tool
   - Copy EXACT results (don't summarize or round)
   - If query fails, document error and revise

4. **Handle data quality issues**
   - If quality checks reveal problems, document them
   - Decide: exclude bad data, transform it, or note as limitation
   - Update test design if needed (document why)

**Common Rationalization:** "I'll skip data quality checks since the data looks fine"
**Reality:** ALWAYS check data quality. Surprises happen. Document what you checked.

**Common Rationalization:** "I'll combine all queries into one file to save time"
**Reality:** Separate files create clear audit trail. One query, one file.

---

## Phase 4: Result Interpretation

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Described what the data shows (facts only)
- [ ] Calculated relevant comparisons (% differences, ratios)
- [ ] Considered alternative explanations
- [ ] Assessed confounding factors identified in Phase 1
- [ ] Stated whether results support/reject H0
- [ ] Saved to `07 - interpretation.md` (or next number)

### Instructions

1. **Create interpretation file: `XX - interpretation.md`** with: ./templates/phase-4.md

2. **Be intellectually honest**
   - State limitations clearly
   - Don't overstate conclusions
   - Acknowledge uncertainty
   - Suggest what additional data would help

**Common Rationalization:** "The pattern is obvious, I don't need to consider alternatives"
**Reality:** Always consider alternatives. Obvious patterns often have surprising explanations.

**Common Rationalization:** "I'll downplay limitations so the conclusion looks stronger"
**Reality:** Stating limitations INCREASES credibility. Be honest about uncertainty.

---

## Phase 5: Conclusion and Follow-up

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Written clear, actionable conclusion
- [ ] Listed 2-3 specific follow-up questions
- [ ] Suggested concrete next steps
- [ ] Saved to `08 - conclusion.md` (or next number)
- [ ] Updated `00 - overview.md` with summary

### Instructions

1. **Create conclusion file: `XX - conclusion.md`** with: ./templates/phase-5.md

2. **Update overview file: `00 - overview.md`**

Add summary section with: ./templates/overview-summary.md

3. **Final checklist before marking complete**
   - [ ] All phases documented in numbered files
   - [ ] Queries and results included
   - [ ] Limitations acknowledged
   - [ ] Follow-up questions specified
   - [ ] Overview updated
   - [ ] User informed of conclusions

**Common Rationalization:** "I found the answer, I'm done"
**Reality:** Good analysis always identifies the NEXT question. List follow-ups.

**Common Rationalization:** "I'll skip updating the overview since it's all in the detailed files"
**Reality:** Overview provides navigational summary. Always update it.

---

## Complete Example: Day-of-Week Analysis

### Example Scenario
User wants to test: "Do we get more sales on weekends?"

### Phase 1: Hypothesis Formulation (01 - hypothesis-formulation.md)

```markdown
# Hypothesis Formulation

## Analytical Goal
Determine if weekend days (Saturday, Sunday) have higher sales than weekday days (Monday-Friday)

## Context
Business wants to optimize staffing and inventory. If weekends are significantly busier, we should staff up. If not, we can balance resources across the week.

## Hypotheses

### Null Hypothesis (H0)
Weekend days and weekday days have equal average sales. Any observed differences are due to random variation.

### Alternative Hypothesis (H1)
Weekend days have significantly different average sales compared to weekday days.

## Success Criteria
- Difference >25% would be practically meaningful (enough to justify staffing changes)
- Pattern should be consistent across multiple weeks

## Potential Confounds
- Holidays: Holiday Monday might inflate weekday averages
- Promotions: Weekend promotions might inflate weekend sales
- Store hours: Different hours on weekends might affect opportunity
- Seasonality: Analysis period might not be representative of full year
```

### Phase 2: Test Design (02 - test-design.md)

```markdown
# Test Design

## Metrics

### Primary Metric
Average daily sales amount: SUM(amount) / COUNT(DISTINCT date) for weekend vs weekday groups

### Supporting Metrics
- Total transaction count per day-of-week (to assess sample size)
- Median sales per transaction (to check if average is representative)
- Week-over-week consistency (to see if pattern is stable)

## Comparison Structure
Group days into two categories:
- Weekend: Saturday (day 6), Sunday (day 0)
- Weekday: Monday-Friday (days 1-5)

Calculate average daily sales for each group, compare the ratio.

## Data Requirements

### Required Tables/Columns
- Table: `sales` (or similar)
  - `transaction_date` (DATE or TEXT in ISO format)
  - `amount` (NUMERIC)

### Data Quality Checks
1. Check for NULL dates or amounts
2. Verify date range covers complete weeks
3. Confirm adequate sample size (>100 transactions per day-of-week)
4. Identify any outlier days (holidays, system outages)

### Queries Needed
1. Schema check: PRAGMA table_info(sales)
2. Data quality: NULL checks, date range, outlier detection
3. Main analysis: Daily sales by day-of-week
4. Supporting: Transaction counts, weekly pattern consistency

## Statistical Considerations
Look for differences >25% between weekend and weekday averages. Check if pattern is consistent across multiple weeks (not just one unusual weekend).
```

### Phase 3: Data Analysis (03-06 files)

**03 - schema-check.md:**
```markdown
# Schema Check

## Rationale
Verify the sales table exists and has the required columns for date and amount

## Query
```sql
PRAGMA table_info(sales);
```

## Results
```
cid | name              | type    | notnull | dflt_value | pk
0   | transaction_id    | INTEGER | 0       | NULL       | 1
1   | transaction_date  | TEXT    | 0       | NULL       | 0
2   | amount            | REAL    | 0       | NULL       | 0
3   | product_id        | INTEGER | 0       | NULL       | 0
```

## Initial Observations
- Table `sales` exists
- Has `transaction_date` column (TEXT type - will need STRFTIME to extract day-of-week)
- Has `amount` column (REAL type - good for calculations)
- Columns allow NULLs - need to check data quality
```

**04 - data-quality-check.md:**
```markdown
# Data Quality Check

## Rationale
Verify data completeness and identify any issues before main analysis

## Query
```sql
SELECT
  COUNT(*) as total_rows,
  COUNT(CASE WHEN transaction_date IS NULL THEN 1 END) as null_dates,
  COUNT(CASE WHEN amount IS NULL THEN 1 END) as null_amounts,
  MIN(transaction_date) as earliest_date,
  MAX(transaction_date) as latest_date,
  MIN(amount) as min_amount,
  MAX(amount) as max_amount
FROM sales;
```

## Results
```
total_rows | null_dates | null_amounts | earliest_date | latest_date | min_amount | max_amount
15847      | 0          | 0            | 2024-01-01    | 2024-03-31  | 5.00       | 899.99
```

## Initial Observations
- 15,847 total transactions
- No NULL dates or amounts (clean data)
- 3 months of data (Jan-Mar 2024)
- 13 complete weeks (91 days / 7)
- Amount range: $5 to $899.99 (no obvious outliers)
```

**05 - main-analysis.md:**
```markdown
# Main Analysis: Sales by Day of Week

## Rationale
Calculate average sales by day of week to test if weekend days differ from weekdays

## Query
```sql
SELECT
  CAST(STRFTIME('%w', transaction_date) AS INTEGER) as day_of_week,
  CASE
    WHEN CAST(STRFTIME('%w', transaction_date) AS INTEGER) IN (0, 6) THEN 'Weekend'
    ELSE 'Weekday'
  END as day_type,
  COUNT(DISTINCT transaction_date) as days_count,
  COUNT(*) as transaction_count,
  SUM(amount) as total_sales,
  ROUND(SUM(amount) / COUNT(DISTINCT transaction_date), 2) as avg_daily_sales,
  ROUND(AVG(amount), 2) as avg_transaction_amount
FROM sales
GROUP BY day_of_week, day_type
ORDER BY day_of_week;
```

## Results
```
day_of_week | day_type | days_count | transaction_count | total_sales | avg_daily_sales | avg_transaction_amount
0           | Weekend  | 13         | 1456              | 52389.44    | 4030.00        | 35.98
1           | Weekday  | 13         | 2234              | 102345.67   | 7872.90        | 45.81
2           | Weekday  | 13         | 2198              | 98234.55    | 7556.50        | 44.70
3           | Weekday  | 13         | 2301              | 105678.90   | 8129.15        | 45.93
4           | Weekday  | 13         | 2345              | 108901.23   | 8377.02        | 46.44
5           | Weekday  | 13         | 2456              | 115432.11   | 8879.39        | 47.00
6           | Weekend  | 13         | 2857              | 98765.43    | 7597.34        | 34.56
```

## Initial Observations
- Sunday (0): $4,030 avg daily sales, 1,456 transactions, $35.98 avg transaction
- Monday-Friday (1-5): $7,800-$8,800 avg daily sales, 2,200-2,500 transactions, $44-47 avg transaction
- Saturday (6): $7,597 avg daily sales, 2,857 transactions, $34.56 avg transaction
- Saturday has HIGH transaction count but LOW per-transaction amount
- Sunday has both low transaction count AND low per-transaction amount
```

**06 - supporting-analysis.md:**
```markdown
# Supporting Analysis: Weekend vs Weekday Comparison

## Rationale
Aggregate weekend and weekday categories to test the hypothesis directly

## Query
```sql
SELECT
  CASE
    WHEN CAST(STRFTIME('%w', transaction_date) AS INTEGER) IN (0, 6) THEN 'Weekend'
    ELSE 'Weekday'
  END as day_type,
  COUNT(DISTINCT transaction_date) as days_count,
  COUNT(*) as transaction_count,
  SUM(amount) as total_sales,
  ROUND(SUM(amount) / COUNT(DISTINCT transaction_date), 2) as avg_daily_sales,
  ROUND(AVG(amount), 2) as avg_transaction_amount
FROM sales
GROUP BY day_type;
```

## Results
```
day_type | days_count | transaction_count | total_sales | avg_daily_sales | avg_transaction_amount
Weekday  | 65         | 11534             | 530592.46   | 8163.00         | 46.01
Weekend  | 26         | 4313              | 151154.87   | 5813.65         | 35.04
```

## Initial Observations
- Weekday average: $8,163 per day
- Weekend average: $5,814 per day
- Difference: $2,349 (29% lower on weekends)
- Weekend has 62% fewer transactions per day
- Weekend transactions are 24% smaller on average
```

### Phase 4: Interpretation (07 - interpretation.md)

```markdown
# Result Interpretation

## Summary of Findings

### Primary Metric Results
Weekends have significantly LOWER sales than weekdays:
- Weekday avg: $8,163 per day
- Weekend avg: $5,814 per day
- Difference: 29% lower on weekends

This contradicts the original hypothesis that weekends would have higher sales.

### Statistical Assessment
- Magnitude: 29% difference is both statistically meaningful (large sample) and practically significant (>25% threshold)
- Consistency: Pattern holds across 13 weeks of data
- Practical importance: This magnitude justifies different staffing/inventory approaches

## Alternative Explanations

1. **Store hours:** Maybe stores close earlier on weekends
   - Evidence: Transaction count is 62% lower on weekends, suggesting operational constraint
   - Impact: Could fully explain lower daily totals if hours are reduced

2. **Customer behavior:** Maybe weekend shoppers buy smaller items
   - Evidence: Average transaction is 24% smaller on weekends ($35 vs $46)
   - Impact: Explains some but not all of the difference

3. **Product mix:** Maybe high-value products aren't available on weekends
   - Evidence: Would need product category data to verify
   - Impact: Unknown

4. **Sunday effect:** Maybe Sunday drags down weekend average
   - Evidence: Sunday has only $4,030 avg (47% lower than Saturday's $7,597)
   - Impact: If we exclude Sunday, Saturday is closer to weekdays but still 7% lower

## Hypothesis Test Result

### Null Hypothesis (H0)
Weekend days and weekday days have equal average sales.

### Decision
**REJECT H0**

### Rationale
The 29% difference between weekend and weekday average sales is large, consistent across 13 weeks, and exceeds our 25% practical significance threshold. The pattern is clear: weekends have lower sales than weekdays.

HOWEVER: This is the OPPOSITE of what we hypothesized. The alternative hypothesis stated "weekend days have significantly different sales" which is true, but we expected higher, not lower.

## Limitations

1. **Cannot determine causation:** Data shows weekends are lower but doesn't explain why
2. **Store operational factors unknown:** Don't have data on hours, staffing, inventory availability
3. **Sunday is dramatically lower:** Weekend average is heavily influenced by very low Sunday sales
4. **Seasonal effects:** 3 months (Jan-Mar) may not represent full year (could be post-holiday slump)
5. **No control for promotions/holidays:** Any holidays in the period could skew results
```

### Phase 5: Conclusion (08 - conclusion.md)

```markdown
# Conclusion and Follow-up

## Main Conclusion

Weekends have 29% lower average daily sales than weekdays, contradicting the initial hypothesis that weekends would be busier. This pattern is consistent across 13 weeks and appears driven by both fewer transactions (62% lower) and smaller average purchases (24% lower).

## Actionable Insights

**DO NOT increase weekend staffing based on this data.** The hypothesis that weekends are busier is not supported.

Instead:

1. **Investigate Sunday specifically:** With only $4,030 avg daily sales (vs $7,600 on Saturday), Sunday operations may not be profitable. Consider:
   - Reduced hours on Sunday
   - Sunday-specific promotions to drive traffic
   - Or closing on Sundays if fixed costs exceed contribution margin

2. **Understand operational constraints:** Before making staffing decisions, determine:
   - Are weekend hours reduced? (This might explain lower transaction counts)
   - Is weekend inventory limited? (This might explain smaller purchases)
   - Are certain high-value products unavailable on weekends?

3. **Focus weekday resources:** If pattern holds year-round, optimize for Monday-Friday peak demand

## Follow-up Questions

1. **What are actual store operating hours by day?**
   - Data needed: Store hours table, or time-of-day in transaction timestamps
   - Approach: Calculate sales per operating hour rather than per day
   - Why: Would distinguish "fewer hours" from "fewer customers per hour"

2. **Does the weekend pattern hold across all seasons?**
   - Data needed: Full year of transaction data
   - Approach: Repeat this analysis for each quarter
   - Why: Jan-Mar might be post-holiday slump; need to verify pattern is year-round

3. **Are there product category differences on weekends?**
   - Data needed: Product category or department in transaction records
   - Approach: Analyze category mix and average prices by day-of-week
   - Why: Would explain the 24% smaller average transaction on weekends

4. **How do weekends compare if we exclude Sunday?**
   - Data needed: Current dataset (already have this)
   - Approach: Re-run analysis treating Sunday separately
   - Why: Sunday is so dramatically lower it may be distorting the weekend average

## Confidence Level

**Medium confidence** in the finding that weekends are lower, but **low confidence** in the explanation.

Reasoning:
- Pattern is clear and consistent across 13 weeks (strengthens confidence)
- Sample sizes are adequate (4,313 weekend transactions is plenty)
- BUT: Cannot distinguish operational constraints from customer behavior (weakens confidence)
- AND: Only 3 months of data may not represent full year (weakens confidence)

**Next step:** Investigate store hours and expand to full year data before making operational changes.
```

---

## Common Rationalizations

### "I'll just look at the data first to understand it better"
**Why this is wrong:** Looking at data before formulating hypotheses creates confirmation bias. You'll unconsciously form hypotheses that match what you see, then "test" them. This isn't science.

**Do instead:** Formulate hypothesis from domain knowledge, business context, or theory. Then look at data.

### "The hypothesis is obvious from the results, I don't need to write it down"
**Why this is wrong:** Hindsight bias makes everything seem obvious after you see the answer. Writing hypothesis first creates accountability.

**Do instead:** Always write H0 and H1 in Phase 1 before any query execution.

### "I'll skip data quality checks since the data looks clean"
**Why this is wrong:** You can't know data is clean until you check. Surprises happen often.

**Do instead:** ALWAYS run data quality queries. Document what you checked and what you found (even if it's "no issues").

### "The pattern is clear, I don't need to consider alternative explanations"
**Why this is wrong:** Obvious patterns often have non-obvious causes. Confounding factors are common.

**Do instead:** Always list 2-3 alternative explanations in Phase 4, even if you think they're unlikely.

### "I'll combine multiple queries into one file for efficiency"
**Why this is wrong:** One file per query creates clear audit trail and makes analysis reproducible.

**Do instead:** One query, one file. Use consistent numbering (03-, 04-, etc.).

### "I found the answer, analysis is complete"
**Why this is wrong:** Good analysis always identifies the next question. Every conclusion should raise new questions.

**Do instead:** Always list 2-3 follow-up questions in Phase 5.

### "I'll downplay limitations so the conclusion looks stronger"
**Why this is wrong:** Acknowledging limitations increases credibility. Readers trust honest uncertainty more than false certainty.

**Do instead:** State limitations clearly. Be honest about what you don't know.

### "I'll skip updating the overview since everything is in detailed files"
**Why this is wrong:** Overview provides navigation and quick summary. Future readers (including you) will thank you.

**Do instead:** Always update `00 - overview.md` with results summary in Phase 5.

---

## Summary

This skill ensures rigorous, reproducible hypothesis testing by:

1. **Preventing confirmation bias:** Formulate hypothesis BEFORE looking at data
2. **Ensuring thoughtful design:** Plan your test before executing queries
3. **Creating audit trail:** One query per file, with rationale and results
4. **Demanding intellectual honesty:** Consider alternatives, state limitations
5. **Identifying next questions:** Every analysis should suggest follow-up investigations

Follow this process and you'll produce defensible, credible analysis that stands up to scrutiny.
