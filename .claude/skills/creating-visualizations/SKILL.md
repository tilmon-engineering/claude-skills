---
name: creating-visualizations
description: Component skill for creating effective text-based visualizations in DataPeeker analysis sessions
---

# Creating Visualizations

## Purpose

This component skill guides creation of clear, effective text-based visualizations for analytics documentation. Use it when:
- Presenting query results in a more visual format
- Need to reveal patterns that are hard to see in raw numbers
- Creating reports or documentation that will be read by stakeholders
- Referenced by process skills requiring data visualization

## Prerequisites

- Query results obtained and interpreted
- Understanding of patterns to highlight (use `interpreting-results` skill)
- Analysis documented in markdown files
- Clear communication goal for the visualization

## Visualization Creation Process

Create a TodoWrite checklist for the 4-phase visualization process:

```
Phase 1: Choose Visualization Type
Phase 2: Structure Data for Display
Phase 3: Create Visualization
Phase 4: Annotate with Context
```

Mark each phase as you complete it. Include visualizations in numbered markdown files alongside queries and interpretations.

---

## Phase 1: Choose Visualization Type

**Goal:** Select the right visualization format for your data and communication goal.

### Visualization Selection Decision Tree

Ask these questions in order:

**1. What type of data am I visualizing?**

- **Single summary statistic** → Callout box or highlighted metric
- **List of values** → Table or ranked list
- **Distribution across categories** → Bar chart (ASCII or markdown)
- **Time series** → Line chart (sparkline) or time table
- **Comparison between groups** → Side-by-side table or grouped bars
- **Part-to-whole relationship** → Percentage table or ASCII pie chart
- **Correlation or relationship** → Scatter (character plot) or correlation matrix

**2. What is my primary communication goal?**

- **Show exact values** → Table with clear formatting
- **Show relative magnitudes** → Bar chart or ranked list
- **Show trends over time** → Sparkline or time series table
- **Show distribution shape** → Histogram (ASCII)
- **Show ranking** → Ordered list or horizontal bars
- **Show proportions** → Percentage table with bars

**3. How many data points?**

- **1-5 values** → Callout boxes or simple list
- **6-20 values** → Table or bar chart
- **21-50 values** → Grouped table or histogram
- **50+ values** → Summary statistics + histogram, or top/bottom N

**4. Who is the audience?**

- **Technical analysts** → Full tables with precision
- **Business stakeholders** → Simplified visuals with key takeaways
- **Mixed audience** → Visual summary + detailed table

### Available Visualization Types

**For DataPeeker (markdown-based), we use text-based formats:**

1. **Markdown Tables** - Structured data with alignment
2. **ASCII Bar Charts** - Visual magnitude comparison
3. **Sparklines** - Compact trend indicators
4. **ASCII Histograms** - Distribution visualization
5. **Callout Boxes** - Highlighting key metrics
6. **Ranked Lists** - Ordered items with context
7. **Comparison Tables** - Side-by-side metrics
8. **Character Plots** - Simple scatter or time series

**Choose based on what best reveals the pattern you want to communicate.**

---

## Phase 2: Structure Data for Display

**Goal:** Organize and format data for effective visualization.

### Data Preparation Checklist

Before creating visualization:

**1. Sort appropriately:**
```markdown
For ranked data:
- Sort by the metric you want to emphasize (descending for "top N")
- Consider: Alphabetical only if order doesn't matter

For time series:
- Sort chronologically (oldest to newest, or newest first if recent matters)

For categorical:
- Sort by frequency, magnitude, or logical grouping
- Avoid: Random or database-default ordering
```

**2. Round to appropriate precision:**
```markdown
Examples:
- Revenue: Round to thousands or whole dollars (not $1,234.56789)
- Percentages: 1-2 decimal places (14.3%, not 14.285714%)
- Counts: Whole numbers only (1,234 not 1234.0)
- Ratios: 2-3 significant figures (2.4x not 2.3567x)

Rule: Show precision that matches the certainty of your data
```

**3. Add calculated columns:**
```markdown
Useful additions:
- Percentage of total
- Difference from average/baseline
- Rank or percentile
- Running totals or moving averages
- Year-over-year change
```

**4. Consider grouping:**
```markdown
For large datasets:
- Show Top N + "Other" row
- Group by logical categories
- Use ranges/buckets for continuous data
- Separate outliers from main distribution
```

**5. Format for readability:**
```markdown
Best practices:
- Add thousand separators (1,234 not 1234)
- Use consistent decimal places within columns
- Align numbers right, text left
- Include units in headers ($, %, units)
```

---

## Phase 3: Create Visualization

**Goal:** Build the actual visualization using text-based formats.

### Format 1: Markdown Tables

**Use for:** Structured data with multiple columns, exact values matter

**Basic table:**
```markdown
| Category    | Orders | Revenue    | Avg Order Value |
|-------------|-------:|:----------:|----------------:|
| Electronics | 1,523  | $345,678   | $226.89         |
| Home        | 2,341  | $298,432   | $127.48         |
| Clothing    | 3,456  | $234,567   | $67.89          |
```

**Best practices:**
- Align numbers right, text left (use `:---:` or `---:` in header separator)
- Include totals row when appropriate
- Use bold for emphasis: `**$345,678**`
- Add percentage columns for context
- Keep columns to 5-7 maximum for readability

**Table with percentages:**
```markdown
| Category    | Revenue    | % of Total | Growth YoY |
|-------------|:----------:|-----------:|-----------:|
| Electronics | $345,678   |      42.5% |    +23.4%  |
| Home        | $298,432   |      36.8% |    +15.2%  |
| Clothing    | $234,567   |      28.9% |     -8.1%  |
| **Total**   | **$811,677** | **100.0%** |  **+12.3%** |
```

### Format 2: ASCII Bar Charts

**Use for:** Visual magnitude comparison, relative sizes matter more than exact values

**Horizontal bars:**
```markdown
## Sales by Category

Electronics  [████████████████████████████] 345,678  (42.5%)
Home & Garden [████████████████████████]     298,432  (36.8%)
Clothing      [███████████████████]          234,567  (28.9%)
Sports        [██████████]                   134,234  (16.5%)
Toys          [████]                          56,789   (7.0%)
```

**How to create:**
1. Calculate max value (scale endpoint)
2. Determine bar length: `(value / max_value) * bar_width`
3. Use █ or = characters for filled portions
4. Include value and percentage after bar
5. Keep bar width consistent (typically 30-50 characters)

**Example with script:**
```python
# Helper for bar generation
def generate_bar(value, max_value, width=30):
    filled = int((value / max_value) * width)
    return '█' * filled + ' ' * (width - filled)

# Usage in markdown
for category, value in sorted_data:
    bar = generate_bar(value, max_value)
    pct = (value / total) * 100
    print(f"{category:15} [{bar}] {value:,} ({pct:.1f}%)")
```

**Vertical bars (for smaller datasets):**
```markdown
## Daily Sales Pattern

Day        Sales
Mon        ████████ 1,234
Tue        ██████████ 1,567
Wed        ████████████ 1,890
Thu        ██████████████ 2,134
Fri        ████████████████ 2,456
Sat        ████████ 1,123
Sun        ██████ 945
```

### Format 3: Sparklines

**Use for:** Compact trend visualization, showing direction and volatility

**Simple sparklines using Unicode characters:**
```markdown
## Monthly Revenue Trends

Q1 2024: ▁▂▃▄▅▆▇█  (Strong growth, $1.2M total)
Q2 2024: ████████  (Plateau, $1.8M total)
Q3 2024: ████▇▆▅▄  (Decline, $1.5M total)
Q4 2024: ▄▅▆▇███▉  (Recovery, $1.9M total)
```

**Sparkline characters (smallest to largest):**
- ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

**How to create:**
1. Normalize values to 0-8 range
2. Map to corresponding block character
3. Place inline with context text

**Alternative with ASCII:**
```markdown
## Customer Acquisition Trend (12 months)

Jan-Dec 2024:  .-'^~*^"~-._  (Peak in July, recovering in December)
Target line:   ------------
```

**When to use:**
- Space is limited
- Showing multiple trends for comparison
- Trend direction matters more than exact values
- Inline with text narrative

### Format 4: ASCII Histograms

**Use for:** Distribution visualization, showing shape and spread

**Distribution of order values:**
```markdown
## Order Value Distribution

 $0-24    [████████████████████]           2,345 orders (34.5%)
 $25-49   [██████████████████████████]     3,012 orders (44.3%)
 $50-74   [████████████]                   1,456 orders (21.4%)
 $75-99   [██████]                           678 orders  (10.0%)
$100-149  [████]                             456 orders   (6.7%)
$150-199  [██]                               234 orders   (3.4%)
$200+     [█]                                123 orders   (1.8%)

Total: 6,789 orders | Median: $42 | Mean: $58 | Std Dev: $47
```

**Best practices:**
- Use 5-10 buckets (not too many, not too few)
- Equal bucket widths when possible
- Include bucket for outliers ($200+)
- Show summary statistics below
- Label axes clearly

**Vertical histogram (for presentations):**
```markdown
## Page Load Time Distribution

3000ms  |
        |
2500ms  |          █
        |          █
2000ms  |     █    █
        |     █    █    █
1500ms  |     █    █    █    █
        |     █    █    █    █    █
1000ms  |     █    █    █    █    █    █
        |     █    █    █    █    █    █    █
 500ms  |     █    █    █    █    █    █    █    █
        |___________________________________
         0-   200- 400- 600- 800- 1000- 1200- 1400- 1600+
         200  400  600  800  1000  1200  1400  1600  (ms)

Most common: 600-800ms | 95th percentile: 1,400ms
```

### Format 5: Callout Boxes

**Use for:** Highlighting single key metrics or insights

**Simple callout:**
```markdown
---
**KEY FINDING**

Revenue increased **23.4%** from Q3 to Q4
($1.5M → $1.9M, +$400K absolute growth)

---
```

**Multi-metric dashboard:**
```markdown
---
## Q4 2024 Summary

📊 **Total Revenue:** $1,876,543 (↑ 23.4% QoQ)
🛒 **Orders:** 12,345 (↑ 18.2% QoQ)
💵 **Avg Order Value:** $152.14 (↑ 4.4% QoQ)
👥 **Active Customers:** 8,934 (↑ 15.7% QoQ)

---
```

**Comparison callout:**
```markdown
---
## Treatment vs Control Comparison

**Treatment Group (n=1,234)**
- Conversion Rate: **3.2%** (↑0.8pp vs control)
- Revenue: **$156,789** (+$23,456)
- AOV: **$127.14** (+$4.23)

**Control Group (n=1,198)**
- Conversion Rate: 2.4%
- Revenue: $133,333
- AOV: $122.91

**Statistical Significance:** p < 0.05 ✓

---
```

### Format 6: Ranked Lists

**Use for:** Top/bottom N, ordered items with narrative

**Simple ranked list:**
```markdown
## Top 5 Products by Revenue (Q4 2024)

1. **Widget Pro** — $234,567 (18.2% of total)
   - Units sold: 2,345 | AOV: $100.03
   - Growth: +45% vs Q3

2. **Gadget Plus** — $198,432 (15.4% of total)
   - Units sold: 4,567 | AOV: $43.44
   - Growth: +23% vs Q3

3. **Doohickey Elite** — $176,543 (13.7% of total)
   - Units sold: 876 | AOV: $201.52
   - Growth: +12% vs Q3

4. **Thingamajig** — $145,678 (11.3% of total)
   - Units sold: 3,456 | AOV: $42.16
   - Growth: -5% vs Q3

5. **Whatsit Standard** — $123,456 (9.6% of total)
   - Units sold: 2,678 | AOV: $46.11
   - Growth: +8% vs Q3

**Top 5 represent 68.2% of total revenue**
```

**Comparative ranked list:**
```markdown
## Best and Worst Performing Regions

### Top 3 (by growth)
1. 🔥 **West Region** — +34.5% growth | $456K revenue
2. 📈 **South Region** — +28.2% growth | $389K revenue
3. ✓ **Central Region** — +15.7% growth | $312K revenue

### Bottom 3 (by growth)
1. ⚠️ **Northeast Region** — -8.3% decline | $278K revenue
2. 📉 **Mid-Atlantic** — -4.1% decline | $234K revenue
3. → **Northwest** — +1.2% growth | $198K revenue

**Note:** All regions increased in absolute terms, but growth rates varied widely.
```

### Format 7: Comparison Tables

**Use for:** Side-by-side metric comparison across segments or time periods

**Period-over-period comparison:**
```markdown
## Q4 2024 vs Q4 2023 Performance

| Metric               | Q4 2023   | Q4 2024   | Change     | % Change |
|----------------------|----------:|----------:|-----------:|---------:|
| Revenue              | $1.52M    | $1.88M    | +$360K     |  +23.7%  |
| Orders               | 10,234    | 12,345    | +2,111     |  +20.6%  |
| Avg Order Value      | $148.52   | $152.14   | +$3.62     |   +2.4%  |
| Active Customers     | 7,456     | 8,934     | +1,478     |  +19.8%  |
| Customer Acq Cost    | $42.15    | $38.76    | -$3.39     |   -8.0%  |
| Customer LTV         | $456.78   | $523.12   | +$66.34    |  +14.5%  |
```

**Segment comparison:**
```markdown
## B2B vs B2C Customer Behavior

| Metric                    | B2B        | B2C       | B2B/B2C Ratio |
|---------------------------|:----------:|:---------:|--------------:|
| Avg Order Value           | $1,234.56  | $87.23    |         14.2x |
| Orders per Customer       | 8.4        | 2.1       |          4.0x |
| Annual Customer Value     | $10,370    | $183      |         56.7x |
| Purchase Frequency        | Monthly    | Quarterly |             — |
| Repeat Purchase Rate      | 87%        | 34%       |          2.6x |
| Customer Support Tickets  | 0.8/order  | 0.2/order |          4.0x |

**Insight:** B2B customers are higher value but require more support resources.
```

### Format 8: Character Plots

**Use for:** Simple scatter plots or relationships when trend matters

**Scatter plot (relationship between two variables):**
```markdown
## Relationship: Order Value vs Shipping Speed

High Value |
($200+)    |                               * *
           |                          *   * * *
           |                       *  * * *
Med Value  |                   *  * * *
($100-199) |               * * * * *
           |           * * * * *
           |       * * * * *
Low Value  |   * * * * *
($0-99)    | * * *
           |_________________________________
             1-day   2-day   3-day   5-day   7-day
                    Shipping Speed

**Pattern:** Customers choosing faster shipping tend to have higher order values.
```

**Time series plot:**
```markdown
## Daily Order Volume (Last 30 Days)

3000 |                            *
     |                         *     *
2500 |                      *
     |                   *        *
2000 |                *                 *
     |             *                       *
1500 |          *                             *
     |       *                                   *
1000 |    *                                         *
     |_________________________________________________
      1    5    10   15   20   25   30
                    Days Ago

**Trend:** Volume peaked mid-month during promotion, returning to baseline.
```

---

## Phase 4: Annotate with Context

**Goal:** Add context and guidance so visualization is self-explanatory.

### Annotation Checklist

Every visualization should include:

**1. Title/Caption:**
```markdown
## [Clear, descriptive title that states what is being shown]

Example:
✓ Good: "Monthly Revenue by Product Category (Jan-Dec 2024)"
✗ Bad: "Revenue Chart"
```

**2. Data source and date:**
```markdown
**Data source:** analytics.db, orders table
**Time period:** Q4 2024 (Oct 1 - Dec 31)
**Last updated:** 2025-11-18
```

**3. Key takeaway (above or below visualization):**
```markdown
**Key Finding:** Electronics drove 42.5% of Q4 revenue despite representing
only 15% of order volume, indicating premium product performance.
```

**4. Units and scale:**
```markdown
- Include $ or % symbols
- Clarify if values are in thousands: ($000s)
- Note if values are indexed or normalized
- Specify timezone for timestamps
```

**5. Context for interpretation:**
```markdown
**Context notes:**
- Q4 includes Black Friday/Cyber Monday (Nov 24-27)
- New product line launched Oct 15, affecting Electronics category
- Shipping delays in December may have suppressed orders
```

**6. Limitations and caveats:**
```markdown
**Caveats:**
- Data excludes returns and cancellations
- International orders converted to USD at average quarterly exchange rate
- First week of October had incomplete data due to system migration
```

**7. What to look for:**
```markdown
**What to notice:**
- Electronics peak in November (holiday season)
- Clothing shows consistent decline (investigate seasonality)
- Sports category smallest but growing fastest (+45% QoQ)
```

### Full Annotated Example

```markdown
## Top 10 Products by Revenue — Q4 2024

**Key Finding:** Top 10 products generated $1.2M (64% of total revenue), with Widget Pro alone accounting for nearly 1 in 5 dollars.

| Rank | Product           | Revenue    | % of Total | Units Sold | Avg Price |
|-----:|:------------------|:----------:|-----------:|-----------:|----------:|
|   1. | Widget Pro        | $234,567   |      18.2% |      2,345 |   $100.03 |
|   2. | Gadget Plus       | $198,432   |      15.4% |      4,567 |    $43.44 |
|   3. | Doohickey Elite   | $176,543   |      13.7% |        876 |   $201.52 |
|   4. | Thingamajig       | $145,678   |      11.3% |      3,456 |    $42.16 |
|   5. | Whatsit Standard  | $123,456   |       9.6% |      2,678 |    $46.11 |
|   6. | Contraption       | $98,765    |       7.7% |      1,987 |    $49.71 |
|   7. | Apparatus         | $87,654    |       6.8% |      1,234 |    $71.04 |
|   8. | Gizmo             | $76,543    |       5.9% |      3,456 |    $22.15 |
|   9. | Mechanism         | $65,432    |       5.1% |        987 |    $66.29 |
|  10. | Device            | $54,321    |       4.2% |      2,134 |    $25.46 |
| **Total Top 10** | **—**    | **$1,261,391** | **63.5%** | **23,720** | **$53.18** |
| All Other Products | —      | $726,152   |      36.5% |     34,281 |    $21.18 |

**Data notes:**
- Source: analytics.db, aggregated from orders and order_items tables
- Time period: October 1 - December 31, 2024 (92 days)
- Excludes returns, refunds, and cancelled orders (47 orders excluded)

**What this shows:**
- Revenue concentration: Top 10 products = 64% of revenue but only 41% of units
- Price segmentation: Widget Pro and Doohickey Elite are premium products (avg >$100)
- Volume products: Gadget Plus and Thingamajig drive revenue through volume
- Long tail: "All Other" represents 127 products with lower individual sales

**Implications:**
- Inventory: Prioritize stock of top 10 products to avoid stockouts
- Marketing: Feature Widget Pro prominently (highest revenue per SKU)
- Risk: Revenue concentration in top 10 creates dependency risk
- Opportunity: Investigate why "All Other" products have lower AOV

**Follow-up questions:**
- How has top 10 list changed vs Q3? (product ranking stability)
- What's the profit margin profile of top 10 vs others? (revenue ≠ profit)
- Are top 10 products also highest rated? (quality vs marketing driven)
```

---

## Visualization Best Practices

### DO:

1. **Choose format based on communication goal, not convenience**
   - Ask: "What do I want the reader to notice first?"
   - Match visualization to insight you're highlighting

2. **Make visualizations self-contained**
   - Reader should understand without reading entire document
   - Include title, units, source, key takeaway

3. **Use consistent formatting within analysis**
   - Same bar width for all bar charts
   - Same precision for similar metrics
   - Consistent color/symbol conventions (if using)

4. **Highlight what matters**
   - Use **bold** for most important values
   - Put key finding at top or bottom
   - Add 🔥, ⚠️, ✓ symbols sparingly for emphasis

5. **Test readability**
   - View in markdown preview (not just raw markdown)
   - Check alignment and spacing
   - Ensure visualization works in different font sizes

6. **Layer detail progressively**
   - Summary visualization first (bar chart, key metrics)
   - Detailed table second (full data)
   - Technical notes third (methodology, caveats)

7. **Combine formats when helpful**
   - Bar chart + exact values table
   - Sparkline + summary statistics
   - Visualization + narrative interpretation

### DON'T:

1. **Don't create visualizations for their own sake**
   - If a simple table is clearer, use the table
   - Visualization should reveal patterns, not obscure them

2. **Don't use excessive precision**
   - Revenue in dollars, not cents ($1,234 not $1,234.56)
   - Percentages to 1 decimal place (14.3% not 14.285714%)

3. **Don't hide important caveats**
   - Data quality issues must be visible
   - Exclusions and filters must be noted
   - Sample size and time period must be clear

4. **Don't use misleading scales**
   - Bar charts should start at zero (not truncated y-axis)
   - Be explicit if using non-zero baseline

5. **Don't over-format**
   - Too many symbols/colors creates visual noise
   - Keep it simple and professional

6. **Don't assume reader knows context**
   - Define abbreviations
   - Explain what metrics mean
   - Note if using non-standard calculations

7. **Don't forget the "so what?"**
   - Every visualization needs an interpretation
   - State implications, not just observations

---

## Common Visualization Patterns

### Pattern 1: Before/After Comparison

```markdown
## Impact of Pricing Change (Oct 15, 2024)

### Before Pricing Change (Oct 1-14)
- Average Order Value: **$145.67**
- Daily Orders: **234**
- Daily Revenue: **$34,087**

### After Pricing Change (Oct 15-31)
- Average Order Value: **$127.23** (↓ $18.44, -12.7%)
- Daily Orders: **289** (↑ 55, +23.5%)
- Daily Revenue: **$36,769** (↑ $2,682, +7.9%)

**Net effect:** Lower prices increased volume enough to grow total revenue.
```

### Pattern 2: Distribution Summary

```markdown
## Customer Lifetime Value Distribution

```
      |                          █
      |                          █
      |                    █     █
      |               █    █     █
      |          █    █    █     █    █
      |     █    █    █    █     █    █    █
      |___________________________________
        $0-   $100- $250- $500- $1K-  $2K-  $5K+
        100   250   500   1K    2K    5K

**Summary Statistics:**
- Median LTV: **$423** (50% of customers below this)
- Mean LTV: **$687** (pulled up by high-value customers)
- 75th percentile: **$892**
- 95th percentile: **$2,145**
- Top 5%: **>$5,000** (only 234 customers, 18% of revenue)

**Interpretation:** Right-skewed distribution shows small number of high-value
customers drive disproportionate revenue. Retention focus should target
customers crossing $500 threshold (top 25%).
```

### Pattern 3: Segmentation Analysis

```markdown
## Customer Segmentation by Purchase Behavior

| Segment         | Customers | Avg Orders | Avg LTV | % of Revenue | Strategy      |
|:----------------|----------:|-----------:|--------:|-------------:|:--------------|
| **Champions**   |       234 |       18.3 |  $2,145 |        18.2% | VIP treatment |
| **Loyal**       |     1,456 |        8.7 |    $892 |        47.3% | Retain & grow |
| **Potential**   |     3,678 |        2.4 |    $287 |        38.5% | Nurture       |
| **At Risk**     |       892 |        1.2 |    $156 |         5.1% | Win-back      |
| **Lost**        |     2,134 |        1.0 |     $87 |         6.8% | Low priority  |

**Visual breakdown:**
Champions    [███]                234 customers → $501,030 revenue
Loyal        [█████████████]    1,456 customers → $1,299,552 revenue
Potential    [████████████████] 3,678 customers → $1,055,586 revenue
At Risk      [██]                 892 customers → $139,152 revenue
Lost         [██]               2,134 customers → $185,658 revenue

**Key insight:** Top two segments (Champions + Loyal) are only 18% of customer
base but generate 66% of revenue. These 1,690 customers should receive majority
of retention investment.
```

### Pattern 4: Time Series with Annotations

```markdown
## Monthly Revenue Trend with Key Events

$2.0M |                                           *
      |                                      * *
$1.8M |                                   *
      |                              * *
$1.6M |                         * *               ← New product launch
      |                    * *
$1.4M |               * *
      |          * *                              ← Pricing change
$1.2M |     * *
      |  *                                        ← Q4 start
$1.0M |________________________________________________
       Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec

**Key Events:**
- **Oct 1:** Q4 begins, seasonal uptick expected
- **Oct 15:** Pricing change (-10% on popular items)
- **Nov 1:** New product line launched (premium segment)
- **Nov 24-27:** Black Friday/Cyber Monday surge

**Analysis:** Revenue growth accelerated after new product launch (Nov),
suggesting demand for premium options. Pricing change impact unclear due to
seasonal overlap.
```

### Pattern 5: Funnel Analysis

```markdown
## Purchase Funnel Conversion Rates

Step                     Count      Conversion    Drop-off
────────────────────────────────────────────────────────────
1. Site Visitors        100,000         100.0%        —
                           ↓
2. Product Viewers       45,000          45.0%     55.0% ← High bounce rate
                           ↓
3. Add to Cart           12,000          26.7%     73.3%
                           ↓
4. Begin Checkout         8,500          70.8%     29.2% ← Cart abandonment
                           ↓
5. Complete Purchase      3,200          37.6%     62.4% ← Payment issues?
────────────────────────────────────────────────────────────
**Overall Conversion:**   3.2%

**Visualization:**
Visitors    [████████████████████████████████████] 100,000
Viewers     [██████████████████]                    45,000
Cart        [█████]                                 12,000
Checkout    [███]                                    8,500
Purchase    [█]                                      3,200

**Problem areas:**
1. **Bounce rate (55%):** Half of visitors leave without viewing products
   - Action: Improve landing page, clearer value proposition

2. **Cart abandonment (29%):** Losing 3,500 potential customers at checkout
   - Action: Simplify checkout, add progress indicator

3. **Checkout failure (62%):** Massive drop-off at payment
   - Action: URGENT — investigate payment gateway, error messages

**Quick win:** Fixing checkout issues could 2.6x conversion (3.2% → 8.4%)
```

---

## Integration with Process Skills

Process skills reference this component skill with:

```markdown
Use the `creating-visualizations` component skill to present query results
visually, making patterns and insights more accessible to stakeholders.
```

When creating visualizations during analysis:
1. Choose format based on communication goal (Phase 1)
2. Structure data for clarity (Phase 2)
3. Build visualization with appropriate text format (Phase 3)
4. Annotate with context and interpretation (Phase 4)

This ensures analysis outputs are not just technically correct but also
effectively communicated and actionable.

---

## When to Visualize

**Visualize when:**
- Pattern is easier to see visually than in raw numbers
- Presenting to stakeholders who need quick understanding
- Comparing multiple segments, time periods, or metrics
- Distribution shape matters (histograms)
- Trend direction matters (sparklines, time series)

**Use tables when:**
- Exact values are critical
- Reader needs to reference specific numbers
- Data is already structured and scannable
- Audience is technical and prefers precision

**Use both when:**
- Visualization reveals pattern, table provides detail
- Different audiences (executive summary + appendix)
- Building progressive disclosure (overview → detail)

---

## Text-Based Visualization Tools

While DataPeeker uses manual markdown visualization, these tools can help
generate visualizations from data:

**For Python users:**
```python
# ASCII histogram
from ascii_graph import Pyasciigraph
graph = Pyasciigraph()
data = [('Cat A', 345), ('Cat B', 298), ('Cat C', 234)]
for line in graph.graph('Sales by Category', data):
    print(line)

# Terminal tables
from tabulate import tabulate
data = [['Electronics', 1523, 345678], ['Home', 2341, 298432]]
print(tabulate(data, headers=['Category', 'Orders', 'Revenue'],
               tablefmt='pipe', numalign='right'))
```

**For direct SQL output:**
```sql
-- Generate simple text bars in SQL
SELECT
  category,
  revenue,
  REPEAT('█', CAST(revenue / 10000 AS INTEGER)) as bar
FROM category_sales
ORDER BY revenue DESC;
```

**For manual creation:**
- Use spreadsheet to calculate bar lengths
- Copy formatted tables from SQL tools
- Verify alignment in markdown preview before committing

---

## Quality Checklist

Before finalizing any visualization, verify:

- [ ] Visualization has clear, descriptive title
- [ ] Units are labeled ($ , %, etc.)
- [ ] Data source and time period documented
- [ ] Key takeaway stated explicitly
- [ ] Appropriate precision (not over-rounded or over-precise)
- [ ] Scale is appropriate (bars from zero, etc.)
- [ ] Annotations explain what to notice
- [ ] Caveats and limitations noted
- [ ] Visualization renders correctly in markdown preview
- [ ] Numbers match source query results
- [ ] Format matches communication goal
- [ ] Audience can understand without additional context

**If any checklist item fails, revise before including in analysis.**
