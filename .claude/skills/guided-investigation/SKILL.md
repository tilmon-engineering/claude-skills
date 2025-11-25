---
name: guided-investigation
description: Systematic process for investigating open-ended questions - decompose vague questions into specific sub-questions, map to data, investigate incrementally, synthesize findings
---

# Guided Investigation Process

## Overview

This skill guides you through systematic investigation of open-ended or exploratory questions. Unlike hypothesis testing (where you test a specific claim), guided investigation helps you answer questions like "Why is X happening?" or "What's driving Y?" by breaking them into specific sub-questions and investigating each systematically.

Guided investigation is appropriate when:
- You have a broad question without a specific hypothesis
- You need to understand a complex phenomenon with multiple potential factors
- The user says "I want to understand..." or "What's causing..."
- You need to decompose a vague question into answerable parts
- You're investigating a business problem with unclear root causes

## Prerequisites

Before using this skill, you MUST:
1. Have data imported into SQLite database (`just import-csvs`)
2. Have created an analysis workspace (`just start-analysis guided-investigation <name>`)
3. Have a clear investigative goal from the user
4. Be familiar with the component skills:
   - `understanding-data` - for data profiling
   - `writing-queries` - for SQL query construction
   - `interpreting-results` - for result analysis
   - `creating-visualizations` - for text-based visualizations

## Mandatory Process Structure

You MUST use TodoWrite to track progress through all 5 phases. Create todos at the start:

```markdown
- Phase 1: Question Decomposition - pending
- Phase 2: Data Discovery - pending
- Phase 3: Systematic Investigation - pending
- Phase 4: Synthesis - pending
- Phase 5: Conclusions and Recommendations - pending
```

Update status as you progress. Mark phases complete ONLY after checkpoint verification.

---

## Phase 1: Question Decomposition

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Clarified the user's broad question
- [ ] Decomposed it into 3-5 specific, answerable sub-questions
- [ ] Prioritized sub-questions by importance/dependency
- [ ] Documented the investigative framework
- [ ] Saved to `01 - question-decomposition.md`

### Instructions

1. **Ask clarifying questions** to understand the user's goal

   - What's the core question you're trying to answer?
   - What decision will this inform?
   - What would constitute a satisfactory answer?
   - What do you already know or suspect?
   - What constraints exist (time, data, etc.)?

2. **Decompose the broad question** into specific sub-questions

Create: `01 - question-decomposition.md`

```markdown
# Question Decomposition

## Broad Investigative Question

[User's original question in plain language]

Example: "Why are our sales declining in the Northeast region?"

## Context and Motivation

[Why this question matters, what decision it informs]

Example: "Sales in Northeast have dropped 15% YoY. Need to understand root cause to determine if this is a market trend, competitive pressure, operational issue, or product problem."

## Sub-Questions

Break the broad question into specific, answerable components:

### Sub-Question 1: [Specific question]
**What we need to learn:** [Clear statement of what this answers]
**Why it matters:** [How this relates to the broad question]
**Success criteria:** [What would constitute an answer]

Example:
### Sub-Question 1: Is the decline uniform across all months or concentrated in specific periods?
**What we need to learn:** Temporal pattern of the decline
**Why it matters:** Helps distinguish seasonal effects from sustained trends
**Success criteria:** Monthly sales comparison showing when decline started and if it's accelerating

### Sub-Question 2: [Another specific question]
...

### Sub-Question 3: [Another specific question]
...

## Investigation Dependencies

[Which sub-questions need to be answered first? What's the logical order?]

Example:
1. Start with temporal patterns (SQ1) - establishes baseline understanding
2. Then segment analysis (SQ2, SQ3) - identifies which segments are affected
3. Finally product analysis (SQ4) - determines if specific products drive the pattern
4. Context analysis (SQ5) - checks for external factors

## Hypotheses to Consider

[What are possible explanations we should investigate?]

Note: Unlike hypothesis-testing skill, these are informal "things to check" not formal H0/H1

Example:
1. Competitive pressure: New competitor entered market in Q2
2. Product quality: Customer complaints increased starting March
3. Pricing: Prices increased 8% in January
4. Seasonality: Historical Q1 weakness
5. Sales team: Turnover in sales team in February

## Success Criteria for Overall Investigation

[What would make this investigation complete?]

Example: "Investigation complete when we can identify the top 2-3 factors driving the decline and quantify their relative impact."
```

3. **STOP and get user confirmation**
   - Review the sub-questions with the user
   - Confirm they address the core question
   - Adjust priorities if needed
   - Do NOT proceed until user confirms the framework

**Common Rationalization:** "The question is clear, I can just start querying data"
**Reality:** Vague questions lead to unfocused investigation. Decompose first, always.

**Common Rationalization:** "I'll figure out the sub-questions as I go"
**Reality:** Without a clear framework, you'll chase random patterns. Plan the investigation first.

---

## Phase 2: Data Discovery

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Mapped each sub-question to specific data tables/columns
- [ ] Identified what data exists vs what's missing
- [ ] Documented data limitations that will constrain the investigation
- [ ] Created a query plan for each sub-question
- [ ] Saved to `02 - data-discovery.md`

### Instructions

1. **Map sub-questions to data**

Create: `02 - data-discovery.md`

```markdown
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
```

2. **Run initial data quality checks**
   - Use `understanding-data` skill to verify table structures
   - Check for NULL values, date ranges, value distributions
   - Document any surprises or data quality issues

3. **Adjust investigation plan if needed**
   - If key data is missing, modify sub-questions
   - Reprioritize based on data availability
   - Document what questions cannot be answered with available data

**Common Rationalization:** "I'll just start with queries and see what the data shows"
**Reality:** Without mapping questions to data first, you'll waste time on unfocused queries.

**Common Rationalization:** "I can skip data quality checks since I know the data"
**Reality:** Assumptions about data often turn out wrong. Check systematically.

---

## Phase 3: Systematic Investigation

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Created one numbered markdown file per sub-question
- [ ] Executed all planned queries for each sub-question
- [ ] Documented rationale, query, results, and observations for each
- [ ] Tracked findings incrementally
- [ ] Files saved as `03-SQ1-*.md`, `04-SQ2-*.md`, etc.

### Instructions

1. **Investigate ONE sub-question at a time**

Important: **ONE FILE PER SUB-QUESTION**, not one file per query. Each sub-question file may contain multiple queries.

2. **For each sub-question, create a dedicated file:**

Create: `03-SQ1-[descriptive-name].md` (then 04-SQ2, 05-SQ3, etc.)

```markdown
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
```

3. **Investigation sequence**
   - Follow the dependency order from Phase 1
   - Complete each sub-question fully before moving to next
   - Build on findings: let earlier answers inform later queries
   - Update your investigation plan if findings suggest new directions

4. **Use component skills as needed**
   - `writing-queries` skill for complex SQL
   - `interpreting-results` skill for understanding patterns
   - `creating-visualizations` skill for markdown tables/text charts

5. **Document incrementally**
   - Don't wait until the end to document
   - Capture observations immediately after each query
   - Note surprises, anomalies, or unexpected patterns

**Common Rationalization:** "I'll run all queries first, then document everything at the end"
**Reality:** You'll forget context and rationale. Document as you go.

**Common Rationalization:** "I found something interesting, I'll chase it instead of finishing current sub-question"
**Reality:** Stay disciplined. Note the interesting finding, complete current sub-question, then decide if it warrants investigation.

**Common Rationalization:** "I can combine multiple sub-questions into one file"
**Reality:** One file per sub-question creates clear structure and makes findings easy to locate.

---

## Phase 4: Synthesis

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Reviewed all sub-question findings together
- [ ] Identified patterns and connections across sub-questions
- [ ] Assessed which hypotheses from Phase 1 are supported/refuted
- [ ] Created a coherent narrative explaining the findings
- [ ] Saved to `XX - synthesis.md` (use next sequential number)

### Instructions

1. **Create synthesis file**

Create: `XX - synthesis.md`

```markdown
# Synthesis

## Investigation Summary

[One paragraph: What was the broad question and what did you investigate?]

Example: "Investigated why Northeast region sales declined 15% YoY by examining temporal patterns, regional segmentation, product mix, and customer behavior across 5 sub-questions."

## Sub-Question Findings Recap

### SQ1: [Question]
**Finding:** [One-sentence answer]

### SQ2: [Question]
**Finding:** [One-sentence answer]

### SQ3: [Question]
**Finding:** [One-sentence answer]

[etc.]

## Cross-Cutting Patterns

[What patterns emerged across multiple sub-questions?]

Example:
1. **Timing alignment:** Decline started in January 2024 across all regions and product categories
2. **Volume vs price:** All segments show volume decline with stable pricing
3. **Customer concentration:** 70% of decline comes from mid-tier customer segment

## Hypothesis Assessment

[From Phase 1, which hypotheses are supported by evidence?]

### Hypothesis: Competitive pressure
**Evidence:**
- Transaction volume dropped 15% starting January
- Average ticket size unchanged (no price competition)
- Decline concentrated in mid-tier customers

**Assessment:** **SUPPORTED** - pattern is consistent with new competitor targeting mid-market

### Hypothesis: Product quality issues
**Evidence:**
- No change in return rates
- Product mix stable
- No correlation between decline and specific product categories

**Assessment:** **NOT SUPPORTED** - if quality were the issue, we'd see product-specific effects

### Hypothesis: [Another hypothesis]
**Evidence:** [...]
**Assessment:** [SUPPORTED / PARTIALLY SUPPORTED / NOT SUPPORTED]

## Integrated Explanation

[Synthesize findings into a coherent story]

Example: "The 15% sales decline in Northeast is best explained by competitive pressure beginning in January 2024. The pattern shows:

1. Sudden onset (January start date) suggests market event, not gradual trend
2. Volume decline with stable pricing suggests customers switching to alternative, not reducing consumption
3. Mid-tier customer concentration matches known competitor's target market
4. Geographic concentration in Northeast aligns with competitor's initial market entry

While we cannot definitively prove causation without competitor data, the circumstantial evidence strongly points to competitive pressure as the primary driver."

## Confidence Assessment

[How confident are you in this explanation?]

**Confidence Level:** [High / Medium / Low]

**Reasoning:**
- Strengths: [What makes you confident?]
- Weaknesses: [What creates uncertainty?]
- Data gaps: [What data would increase confidence?]

Example:
**Confidence Level:** Medium-High

**Reasoning:**
- Strengths: Multiple independent lines of evidence point to same conclusion; timing and segmentation patterns are consistent with competitive hypothesis
- Weaknesses: No direct competitor data to confirm; cannot rule out other January 2024 events (promotion ending, marketing change, etc.)
- Data gaps: Competitor market entry dates, customer churn destination data, lost deal analysis would confirm hypothesis
```

2. **Build a coherent narrative**
   - Connect the dots between sub-question findings
   - Identify the most parsimonious explanation
   - Acknowledge where evidence is strong vs weak
   - Be honest about alternative explanations

3. **Check your logic**
   - Does the explanation account for ALL the findings?
   - Are there contradictions you're ignoring?
   - Are you cherry-picking evidence that fits your story?
   - What would someone skeptical say?

**Common Rationalization:** "The first sub-question gave me the answer, I don't need synthesis"
**Reality:** Individual findings need integration. Synthesis reveals connections and tests coherence.

**Common Rationalization:** "I'll just present the findings separately and let the user synthesize"
**Reality:** Your job is to synthesize. Don't pass the cognitive work to the user.

---

## Phase 5: Conclusions and Recommendations

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Written clear answer to the original broad question
- [ ] Provided specific, actionable recommendations
- [ ] Listed concrete next steps or follow-up investigations
- [ ] Documented key limitations and caveats
- [ ] Saved to `XX - conclusions.md` (use next sequential number)
- [ ] Updated `00 - overview.md` with summary

### Instructions

1. **Create conclusions file**

Create: `XX - conclusions.md`

```markdown
# Conclusions and Recommendations

## Answer to Broad Question

[Clear, direct answer to the user's original question]

Example: "Northeast sales declined 15% due to competitive pressure from a new market entrant targeting mid-tier customers starting in January 2024."

## Detailed Conclusion

[2-3 paragraphs providing full answer with key evidence]

Example: "The investigation identified competitive pressure as the primary driver of the Northeast sales decline. Several lines of evidence support this conclusion:

First, the timing and pattern of decline suggest a market disruption rather than internal operational issues. The decline started suddenly in January 2024 and has been consistent at ~15% month-over-month, affecting all product categories proportionally.

Second, the customer segmentation analysis reveals that 70% of the volume loss comes from mid-tier customers (those spending $50-200/month), while high-value and low-value customers are relatively stable. This concentration matches the known target market of Competitor X, who entered the Northeast market in Q4 2023.

Third, the nature of the decline - pure volume loss with stable average transaction values - indicates customers are switching to an alternative provider rather than reducing overall consumption or responding to pricing changes."

## Actionable Recommendations

[Specific actions based on findings - prioritized]

### Immediate Actions (1-2 weeks)

1. **[Specific recommendation]**
   - What to do: [Concrete action]
   - Why: [How this addresses the findings]
   - Owner: [Who should do this]
   - Success metric: [How to measure impact]

Example:
1. **Conduct competitive pricing analysis**
   - What: Survey mid-tier customers to understand why they switched; analyze competitor pricing and offerings
   - Why: Findings suggest competitive pressure but we lack direct competitor intelligence
   - Owner: Marketing/Strategy team
   - Success metric: Competitive intelligence report identifying 3-5 key differentiators

2. **Launch mid-tier customer retention program**
   - What: Create targeted offers for customers in $50-200/month segment
   - Why: This segment represents 70% of the decline and is most at-risk
   - Owner: Sales team with Marketing support
   - Success metric: Reduce churn rate in mid-tier by 20% within 2 months

### Short-term Actions (1-3 months)

[Recommendations for next 3 months]

### Long-term Strategic Implications

[What does this mean for strategy?]

Example: "This investigation reveals vulnerability to focused competition in the mid-market segment. Long-term strategic response should include:
- Develop clear mid-market value proposition
- Improve competitive intelligence capabilities
- Consider geographic expansion to diversify risk"

## Follow-up Investigations

[What additional analysis would be valuable?]

1. **[Follow-up question]**
   - Why investigate: [What this would clarify]
   - Data needed: [What data required]
   - Suggested approach: [How to investigate]
   - Priority: [High/Medium/Low]

Example:
1. **Customer churn destination analysis**
   - Why: Would definitively confirm competitive pressure hypothesis
   - Data needed: Customer exit interviews, win/loss data, market research
   - Approach: Survey churned customers from January-present; analyze reasons for leaving
   - Priority: HIGH - directly validates core conclusion

2. **Product-by-product competitive positioning**
   - Why: Would identify which products are most vulnerable to competition
   - Data needed: Product-level sales trends, competitive product catalog
   - Approach: Guided-investigation focused on product mix changes
   - Priority: MEDIUM - helps refine competitive response

3. **Geographic expansion of competitive threat**
   - Why: Need to know if pattern will spread to other regions
   - Data needed: Sales data from other regions, competitor location data
   - Approach: Comparative-analysis of Northeast vs other regions
   - Priority: HIGH - informs defensive strategy

## Key Limitations

[Important caveats about the conclusion]

1. **[Limitation]:** [Explanation and impact]

Example:
1. **No direct competitor data:** Conclusion is based on circumstantial evidence (timing, segmentation, behavior patterns) but lacks direct confirmation of customer switching to specific competitor
2. **Three-month window:** Analysis covers Jan-Mar 2024; pattern may evolve over time
3. **Cannot rule out coincidental factors:** Other January 2024 events (internal changes, marketing shifts, external events) could contribute to decline
4. **Northeast-only focus:** Did not investigate whether similar patterns exist in other regions

## Confidence Level

**Overall confidence:** [High / Medium / Low]

**Rationale:** [Why this confidence level?]

Example:
**Overall confidence:** Medium-High

**Rationale:** Multiple independent findings point consistently to competitive pressure explanation. Timing, segmentation, and behavioral patterns all align. Primary uncertainty stems from lack of direct competitor data and limited time window. Would upgrade to High confidence with customer churn destination data or extended time series showing persistent pattern.
```

2. **Update overview file**

Update: `00 - overview.md`

Add at the end:

```markdown
## Investigation Summary

**Broad Question:** [Original question]

**Answer:** [One-sentence conclusion]

**Confidence:** [High/Medium/Low]

**Key Finding:** [Most important discovery]

**Primary Recommendation:** [Top priority action]

**Critical Limitation:** [Most important caveat]

**Recommended Follow-up:** [Most valuable next investigation]

---

## File Index

- 01 - Question Decomposition
- 02 - Data Discovery
- 03-SQ1 - [Sub-question 1 name]
- 04-SQ2 - [Sub-question 2 name]
- 05-SQ3 - [Sub-question 3 name]
- [etc. - list all files]
- XX - Synthesis
- XX - Conclusions
```

3. **Final verification checklist**
   - [ ] All sub-questions answered
   - [ ] Synthesis creates coherent narrative
   - [ ] Recommendations are specific and actionable
   - [ ] Limitations honestly stated
   - [ ] Follow-ups identified
   - [ ] Overview updated
   - [ ] User informed of conclusions

**Common Rationalization:** "I found interesting patterns, that's enough"
**Reality:** Patterns aren't conclusions. Synthesize findings into clear answer to original question.

**Common Rationalization:** "I'll let the user decide what to do with the findings"
**Reality:** Provide specific recommendations. Don't make them do all the strategic thinking.

**Common Rationalization:** "I'll skip the limitations section since the conclusion is solid"
**Reality:** Every investigation has limitations. Acknowledging them increases credibility.

---

## Complete Example: Customer Churn Investigation

### Example Scenario
User asks: "Why are we losing customers in the premium segment?"

### Phase 1: Question Decomposition (01 - question-decomposition.md)

```markdown
# Question Decomposition

## Broad Investigative Question

"Why are we losing customers in the premium segment?"

## Context and Motivation

Premium customers (>$500/month) have historically been our most stable segment with <5% annual churn. In Q1 2024, churn rate jumped to 12%. Need to understand root cause to stem the losses.

## Sub-Questions

### Sub-Question 1: When did the churn increase begin?
**What we need to learn:** Precise timing of when churn accelerated
**Why it matters:** Helps identify triggering events (pricing change, product issue, competitor launch)
**Success criteria:** Month-by-month churn rate showing inflection point

### Sub-Question 2: Are churned customers concentrated in specific product lines?
**What we need to learn:** Whether churn is product-specific or segment-wide
**Why it matters:** Product-specific churn suggests product issues; broad churn suggests market/competitive factors
**Success criteria:** Churn rate by product category with statistical significance

### Sub-Question 3: What was the tenure of churned customers?
**What we need to learn:** Are we losing new customers or long-tenured ones?
**Why it matters:** New customer churn suggests onboarding issues; long-tenure churn suggests value erosion
**Success criteria:** Distribution of churned customers by tenure (0-6mo, 6-12mo, 12-24mo, 24mo+)

### Sub-Question 4: Did churned customers show usage decline before churning?
**What we need to learn:** Whether churn was preceded by disengagement
**Why it matters:** Usage decline signals value realization problems; sudden churn suggests competitive switching
**Success criteria:** Usage metrics 30/60/90 days before churn vs stable customers

### Sub-Question 5: Are there geographic patterns to churn?
**What we need to learn:** Whether churn is concentrated in specific regions
**Why it matters:** Geographic concentration suggests regional competitive or operational factors
**Success criteria:** Churn rate by region with sample size validation

## Investigation Dependencies

1. SQ1 first (timing) - establishes when to focus detailed analysis
2. SQ2 and SQ5 parallel (product and geography) - identify concentration
3. SQ3 (tenure) - requires churn cohort identified from SQ1
4. SQ4 last (usage) - most complex, builds on understanding from others

## Hypotheses to Consider

1. **Price increase impact:** 8% price increase in January may have pushed customers over threshold
2. **Competitor launches:** Competitor Y launched enterprise tier in December
3. **Product quality:** Premium features had stability issues in Q4 2023
4. **Support degradation:** Support team had high turnover in Q1
5. **Contract renewal timing:** Many premium contracts up for renewal in Q1

## Success Criteria for Overall Investigation

Investigation complete when we can identify:
1. Primary driver of increased churn (with 70%+ confidence)
2. Quantified impact of that driver
3. Actionable recommendations to reduce churn
```

### Phase 2: Data Discovery (02 - data-discovery.md)

```markdown
# Data Discovery

## Available Data

### Tables Overview

- `customers`: Customer master data (id, signup_date, segment, region)
- `subscriptions`: Subscription details (customer_id, product_id, start_date, end_date, status)
- `usage_metrics`: Daily usage stats (customer_id, date, login_count, feature_usage)
- `products`: Product catalog (id, name, category, tier)
- `support_tickets`: Customer support interactions

### Relevant Columns by Sub-Question

#### Sub-Question 1: Timing of churn increase
**Required data:**
- `subscriptions.end_date` - when subscription ended
- `subscriptions.status` - to identify churns vs active
- `customers.segment` - to filter to premium

**Data check needed:**
- Definition of "churn" - is end_date populated for all churns?
- Completeness of historical data - how far back do we have data?

#### Sub-Question 2: Product concentration
**Required data:**
- `subscriptions.product_id` - what they were subscribed to
- `products.category` - to group products

**Data check needed:**
- Are multi-product customers handled correctly?
- Do we have category mapping for all products?

#### Sub-Question 3: Customer tenure
**Required data:**
- `customers.signup_date` - when they joined
- `subscriptions.end_date` - when they churned

**Data check needed:**
- Consistency between signup_date and first subscription start_date

#### Sub-Question 4: Usage decline
**Required data:**
- `usage_metrics.login_count` - engagement measure
- `usage_metrics.feature_usage` - specific feature adoption

**Data check needed:**
- Is usage data complete for all customers?
- What's the grain (daily, weekly)?

#### Sub-Question 5: Geographic patterns
**Required data:**
- `customers.region` - geographic identifier

**Data check needed:**
- Region data completeness
- Region definition granularity (country, state, city?)

## Data Gaps and Limitations

1. **No explicit churn reason:** Don't have exit interview data or cancellation reasons
2. **No competitor data:** Cannot directly measure competitive switching
3. **No pricing history:** Cannot analyze individual price points or grandfathered rates
4. **Limited support quality metrics:** Have ticket count but not resolution time or satisfaction scores

## Query Plan

### Sub-Question 1: Timing
1. Monthly churn count and rate for premium segment (last 12 months)
2. Comparison to prior year same period
3. Weekly granularity for Q1 2024 to identify precise inflection point

### Sub-Question 2: Product concentration
1. Churn rate by product category
2. Expected vs actual churn by category (chi-square test approach)

### Sub-Question 3: Tenure
1. Distribution of churned customers by tenure bucket
2. Churn rate by tenure bucket (churned / total in bucket)

### Sub-Question 4: Usage patterns
1. Average usage metrics 30/60/90 days before churn
2. Comparison to stable premium customers in same timeframe

### Sub-Question 5: Geography
1. Churn count and rate by region
2. Statistical significance test for regions

## Investigation Strategy

1. Start with SQ1 (timing) - will identify the specific churn cohort to analyze
2. Then SQ2 (product) and SQ5 (geography) in parallel - both straightforward, high-value
3. Then SQ3 (tenure) - quick analysis once cohort is identified
4. Finally SQ4 (usage) - most complex, requires time-series analysis
```

### Phases 3-5

[Would continue with actual queries and findings, following the same detailed structure as the hypothesis-testing example. For brevity in this skill documentation, showing structure rather than complete worked example.]

---

## Common Rationalizations

### "The question is vague, I'll just explore the data and see what I find"
**Why this is wrong:** Unfocused exploration leads to random pattern-chasing and analysis paralysis.

**Do instead:** Decompose the vague question into specific sub-questions in Phase 1. Structure the investigation.

### "I'll skip question decomposition since I know what to investigate"
**Why this is wrong:** Your initial instinct about what to investigate often misses important angles. Systematic decomposition reveals blind spots.

**Do instead:** Always do Phase 1. Writing down sub-questions forces you to think comprehensively.

### "I found an interesting pattern, I'll investigate that instead of my planned sub-questions"
**Why this is wrong:** Chasing tangents destroys investigation coherence. You end up with fragments, not a complete answer.

**Do instead:** Note interesting patterns for potential follow-up, but complete your current sub-question first.

### "I'll combine multiple sub-questions into one analysis"
**Why this is wrong:** Mixing sub-questions creates confusion and makes findings hard to locate later.

**Do instead:** One file per sub-question. Keep them separate and focused.

### "The data shows X, so the answer must be Y"
**Why this is wrong:** Correlation isn't causation. Data patterns have multiple possible explanations.

**Do instead:** Use Phase 4 synthesis to consider multiple explanations. Test competing hypotheses.

### "I have some findings, I'll just list them for the user"
**Why this is wrong:** Raw findings without synthesis don't answer the original question. You're not a data printer, you're an analyst.

**Do instead:** Synthesize findings into a coherent narrative in Phase 4. Answer the actual question asked.

### "I'll make strong recommendations even though I'm not confident"
**Why this is wrong:** Overconfident recommendations based on weak evidence damage credibility and lead to bad decisions.

**Do instead:** Calibrate recommendations to confidence level. If confidence is medium, say so and explain what would increase it.

### "I found the answer, I don't need to identify follow-up questions"
**Why this is wrong:** Every investigation should identify what to investigate next. Good analysis always reveals new questions.

**Do instead:** Always list 2-3 follow-up investigations in Phase 5. Show what the next layer of analysis would be.

### "I'll skip documenting limitations since it weakens my conclusion"
**Why this is wrong:** Hiding limitations destroys trust. Readers find them anyway, and then they distrust everything.

**Do instead:** Explicitly document limitations. Honest uncertainty is more credible than false certainty.

---

## Summary

This skill ensures systematic, comprehensive investigation of open-ended questions by:

1. **Decomposing vague questions:** Break broad questions into specific, answerable sub-questions
2. **Mapping questions to data:** Verify what data exists before diving into analysis
3. **Investigating systematically:** One sub-question at a time, building incrementally
4. **Synthesizing findings:** Connect the dots to create coherent explanations
5. **Providing actionable conclusions:** Answer the original question with specific recommendations
6. **Identifying next questions:** Every investigation reveals what to investigate next

Follow this process and you'll produce thorough, defensible investigations that answer complex business questions.
