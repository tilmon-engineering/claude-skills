# Terminal-Based Visualization Formats

This document provides detailed implementation guidance for creating text-based visualizations in terminal/markdown environments. Referenced by the main `creating-visualizations` skill when creating visualizations for DataPeeker analysis sessions.

---

## ⚠️ CRITICAL PRINCIPLE: Use Visualization Tools, Not Manual Creation

**NEVER manually create data visualizations** (bar charts, line plots, histograms, sparklines, scatter plots). Manual ASCII art introduces errors, misalignments, and scaling mistakes. **ALWAYS use established visualization tools.**

### What This Means

**✅ ALLOWED - Manual Creation:**
- **Tables with exact values** - Markdown tables showing query results with precise numbers
- **Callout boxes** - Formatted text highlighting key metrics
- **Ranked lists** - Numbered/bulleted lists with exact values from queries

**❌ PROHIBITED - Manual Creation:**
- Bar charts (ASCII or Unicode bars like `████`)
- Line plots or time series (character plots with `*` or `-`)
- Histograms (distribution visualizations)
- Sparklines (trend indicators with ▁▂▃▄▅▆▇█)
- Scatter plots or correlation visualizations
- Any visualization requiring scaling, normalization, or computed positioning

### Why This Matters

Manual visualization creation fails because:
1. **Scaling errors** - Bar lengths don't match proportions
2. **Alignment issues** - Characters don't line up correctly
3. **Calculation mistakes** - Wrong values mapped to visual elements
4. **Maintenance burden** - Manual updates when data changes
5. **Lack of reproducibility** - No clear process to regenerate

### The Rule

**If it involves visual representation of relative magnitudes, trends, or distributions: USE A TOOL.**

**If it's exact numbers in a structured format: Tables are fine.**

---

## Quick Start: Recommended Visualization Tools

Install these tools to create terminal visualizations programmatically:

### Python (Recommended for DataPeeker)

**For most use cases:**
```bash
pip install plotext asciichartpy termgraph sparklines rich
```

**Individual tools by use case:**

| Use Case | Tool | Install Command | Key Features |
|----------|------|-----------------|--------------|
| All-purpose (best choice) | plotext | `pip install plotext` | 9 chart types, no dependencies, 2.3M+ downloads/month |
| Line charts | asciichartpy | `pip install asciichartpy` | Simple, zero dependencies, fast |
| Bar charts | termgraph | `pip install termgraph` | Multiple chart types, data from stdin/files |
| Sparklines | sparklines | `pip install sparklines` | Tiny trend indicators, one-line install |
| Tables + formatting | rich | `pip install rich` | Beautiful tables, progress bars, text formatting |
| Histograms | plotext | `pip install plotext` | Built-in histogram support |

### Other Languages (if needed)

**Node.js:**
```bash
npm install asciichart
```

**Go:**
```bash
go install github.com/guptarohit/asciigraph@latest
```

**Rust:**
```toml
# Add to Cargo.toml
textplots = "0.8"
```

### Quick Verification

Test your installation:

```python
# Test plotext (most comprehensive)
python3 -c "import plotext as plt; plt.bar(['A', 'B', 'C'], [10, 20, 15]); plt.show()"

# Test asciichartpy (line charts)
python3 -c "from asciichartpy import plot; print(plot([1, 2, 5, 3, 4]))"

# Test sparklines (tiny trends)
python3 -c "from sparklines import sparklines; print(''.join(sparklines([1, 2, 5, 3, 4])))"
```

**If any test fails, see the troubleshooting guide in the research documentation.**

---

## Format 1: Markdown Tables

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

---

## Format 2: ASCII Bar Charts

**Use for:** Visual magnitude comparison, relative sizes matter more than exact values

**⚠️ DO NOT CREATE MANUALLY - Use a tool instead**

### Using plotext (Recommended)

```python
import plotext as plt

categories = ['Electronics', 'Home & Garden', 'Clothing', 'Sports', 'Toys']
values = [345678, 298432, 234567, 134234, 56789]

plt.simple_bar(categories, values, width=50, title='Sales by Category')
plt.show()
```

### Using termgraph

```python
from termgraph import termgraph as tg

categories = ['Electronics', 'Home & Garden', 'Clothing', 'Sports', 'Toys']
values = [[345678], [298432], [234567], [134234], [56789]]

data = list(zip(categories, values))
args = {
    'width': 50,
    'format': '{:<5.2f}',
    'suffix': '',
    'no_labels': False,
}
tg.chart(colors=[91], data=data, args=args)
```

### From SQLite Query

```python
import sqlite3
import plotext as plt

conn = sqlite3.connect('analytics.db')
cursor = conn.execute("""
    SELECT category, SUM(revenue) as total_revenue
    FROM sales
    GROUP BY category
    ORDER BY total_revenue DESC
""")

categories, revenues = zip(*cursor.fetchall())

plt.simple_bar(categories, revenues, title='Revenue by Category')
plt.show()
```

**Output includes proper scaling, alignment, and exact values automatically.**

---

## Format 3: Sparklines

**Use for:** Compact trend visualization, showing direction and volatility

**⚠️ DO NOT CREATE MANUALLY - Use the sparklines library**

### Using sparklines (Recommended)

```python
from sparklines import sparklines

# Monthly revenue data (in thousands)
q1_revenue = [300, 350, 420, 450]
q2_revenue = [450, 455, 460, 450]
q3_revenue = [450, 420, 380, 340]
q4_revenue = [340, 380, 440, 490]

print(f"Q1 2024: {''.join(sparklines(q1_revenue))}  (Strong growth, $1.2M total)")
print(f"Q2 2024: {''.join(sparklines(q2_revenue))}  (Plateau, $1.8M total)")
print(f"Q3 2024: {''.join(sparklines(q3_revenue))}  (Decline, $1.5M total)")
print(f"Q4 2024: {''.join(sparklines(q4_revenue))}  (Recovery, $1.9M total)")
```

### From SQLite Query

```python
import sqlite3
from sparklines import sparklines

conn = sqlite3.connect('analytics.db')
cursor = conn.execute("""
    SELECT strftime('%Y-%m', order_date) as month,
           SUM(revenue) as monthly_revenue
    FROM orders
    WHERE order_date >= '2024-01-01'
    GROUP BY month
    ORDER BY month
""")

months, revenues = zip(*cursor.fetchall())
spark = ''.join(sparklines(revenues))

print(f"2024 Revenue Trend: {spark}")
print(f"Months: {months[0]} to {months[-1]}")
print(f"Total: ${sum(revenues):,.0f}")
```

**When to use:**
- Space is limited
- Showing multiple trends for comparison
- Trend direction matters more than exact values
- Inline with text narrative

**Sparkline characters (smallest to largest):** ▁ ▂ ▃ ▄ ▅ ▆ ▇ █

---

## Format 4: ASCII Histograms

**Use for:** Distribution visualization, showing shape and spread

**⚠️ DO NOT CREATE MANUALLY - Use plotext**

### Using plotext (Recommended)

```python
import plotext as plt
import statistics

# Order values from query
order_values = [23, 45, 67, 42, 89, 34, 56, 78, 45, 67, ...]  # Your data

plt.hist(order_values, bins=7, label='Order Values')
plt.title('Order Value Distribution')
plt.xlabel('Order Value ($)')
plt.ylabel('Frequency')

# Add summary statistics
median_val = statistics.median(order_values)
mean_val = statistics.mean(order_values)
stdev_val = statistics.stdev(order_values)

plt.show()
print(f"\nTotal: {len(order_values):,} orders")
print(f"Median: ${median_val:.0f} | Mean: ${mean_val:.0f} | Std Dev: ${stdev_val:.0f}")
```

### From SQLite Query

```python
import sqlite3
import plotext as plt

conn = sqlite3.connect('analytics.db')
cursor = conn.execute("SELECT order_value FROM orders")
order_values = [row[0] for row in cursor.fetchall()]

plt.hist(order_values, bins=10)
plt.title('Order Value Distribution')
plt.xlabel('Order Value ($)')
plt.ylabel('Number of Orders')
plt.show()

# Show summary stats
print(f"\nTotal orders: {len(order_values):,}")
```

**Best practices:**
- Let plotext calculate optimal bin widths
- Use 5-10 bins for most distributions
- Show summary statistics below the histogram
- Label axes with units

---

## Format 5: Callout Boxes

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

---

## Format 6: Ranked Lists

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

---

## Format 7: Comparison Tables

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

---

## Format 8: Line Plots and Scatter Plots

**Use for:** Time series, trends, relationships between variables

**⚠️ DO NOT CREATE MANUALLY - Use plotext or asciichartpy**

### Line Plot with plotext

```python
import plotext as plt

# Daily order volumes
days = list(range(1, 31))
volumes = [1234, 1567, 1890, 2134, 2456, ...]  # 30 days of data

plt.plot(days, volumes, label='Order Volume')
plt.title('Daily Order Volume (Last 30 Days)')
plt.xlabel('Days Ago')
plt.ylabel('Orders')
plt.show()
```

### Line Plot with asciichartpy

```python
from asciichartpy import plot

volumes = [1234, 1567, 1890, 2134, 2456, 1123, 945, ...]
print(plot(volumes, {'height': 15}))
print("\nDaily Order Volume - Last 30 Days")
```

### Scatter Plot with plotext

```python
import plotext as plt
import sqlite3

conn = sqlite3.connect('analytics.db')
cursor = conn.execute("""
    SELECT shipping_days, order_value
    FROM orders
    WHERE shipping_days IS NOT NULL
""")

shipping, values = zip(*cursor.fetchall())

plt.scatter(shipping, values)
plt.title('Order Value vs Shipping Speed')
plt.xlabel('Shipping Speed (days)')
plt.ylabel('Order Value ($)')
plt.show()
```

### Multiple Series

```python
import plotext as plt

days = list(range(1, 13))  # 12 months
revenue_2023 = [120, 130, 145, 150, 160, 170, 165, 175, 180, 190, 210, 230]
revenue_2024 = [140, 155, 170, 180, 190, 210, 220, 240, 260, 280, 310, 340]

plt.plot(days, revenue_2023, label='2023')
plt.plot(days, revenue_2024, label='2024')
plt.title('Monthly Revenue Comparison')
plt.xlabel('Month')
plt.ylabel('Revenue ($K)')
plt.show()
```

---

## Full Annotated Example

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

## Additional Resources

**For comprehensive tool documentation, installation troubleshooting, and code examples, see:**
- `INDEX_TERMINAL_VISUALIZATION.md` - Main navigation document
- `ASCII_TERMINAL_VISUALIZATION_GUIDE.md` - Detailed tool reference
- `TERMINAL_VISUALIZATION_QUICK_START.md` - 30+ ready-to-run examples

**For tables:**
Use the `rich` library for beautifully formatted tables:
```python
from rich.console import Console
from rich.table import Table

table = Table(title="Sales by Category")
table.add_column("Category", style="cyan")
table.add_column("Revenue", justify="right", style="green")

table.add_row("Electronics", "$345,678")
table.add_row("Home", "$298,432")

Console().print(table)
```
