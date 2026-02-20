# Marp: Markdown to Presentation Tool

Marp transforms Markdown documents into professional presentation slides. This guide covers installation, CLI usage, syntax, and best practices for data-driven presentations.

---

## Overview

**What is Marp?**
- Markdown Presentation Ecosystem for creating slides from Markdown
- Built on CommonMark specifications with presentation-specific extensions
- Supports PDF, HTML, PowerPoint (PPTX), and image exports
- Uses browser rendering engine (Chrome, Edge, or Firefox) for output

**When to Use Marp:**
- Executive summaries (5-10 slides)
- Meeting presentations and stakeholder updates
- Quick visual communication of findings
- When you need slides + ability to export to multiple formats

**When NOT to Use Marp:**
- Comprehensive technical documentation (use pandoc for whitepapers)
- Documents requiring academic citations (use pandoc with BibTeX)
- Complex cross-referencing (use pandoc-crossref)

---

## Installation

### Option 1: npx (Recommended for occasional use)

No installation required. Run directly:
```bash
npx @marp-team/marp-cli@latest slides.md -o slides.pdf
```

### Option 2: npm (Project-based installation)

Install as development dependency:
```bash
npm install --save-dev @marp-team/marp-cli
```

Add to `package.json` scripts:
```json
{
  "scripts": {
    "build:slides": "marp presentation.md -o presentation.pdf",
    "watch:slides": "marp -w -p presentation.md"
  }
}
```

Run via npm:
```bash
npm run build:slides
npm run watch:slides
```

### Option 3: Global Installation

```bash
npm install -g @marp-team/marp-cli

# Use directly
marp slides.md -o slides.pdf
```

### Verify Installation

```bash
# Check version
marp --version

# View help
marp --help
```

---

## CLI Usage

### Basic Conversions

**Convert to HTML** (default):
```bash
marp presentation.md
# Creates: presentation.html
```

**Convert to PDF**:
```bash
marp presentation.md -o presentation.pdf
```

**Convert to PowerPoint**:
```bash
marp presentation.md -o presentation.pptx

# Editable PowerPoint (experimental)
marp presentation.md --pptx-editable -o presentation.pptx
```

**Convert to Images**:
```bash
# PNG images (one per slide)
marp presentation.md --images png

# JPEG images
marp presentation.md --images jpeg

# Control image resolution
marp presentation.md --images png --image-scale 2
```

### Development Workflow

**Watch Mode** (auto-rebuild on file changes):
```bash
marp -w presentation.md
```

**Preview Mode** (opens browser preview):
```bash
marp -p presentation.md
```

**Watch + Preview Combined**:
```bash
marp -w -p presentation.md
```

**HTTP Server** (conversion server):
```bash
marp -s
# Server runs on http://localhost:8080
# Access: http://localhost:8080/presentation.md
```

### Advanced Options

**Custom Theme**:
```bash
marp presentation.md --theme-set custom-theme.css -o presentation.pdf
```

**Allow Local Files** (for security):
```bash
marp presentation.md --allow-local-files -o presentation.pdf
```

**Select Browser Engine**:
```bash
# Use Chrome (default)
marp presentation.md --browser chrome -o presentation.pdf

# Use Edge
marp presentation.md --browser edge -o presentation.pdf

# Use Firefox
marp presentation.md --browser firefox -o presentation.pdf
```

**Parallel Processing**:
```bash
# Set concurrency level (default: 5)
marp presentation.md --parallel 10 -o presentation.pdf
```

**Extract Presenter Notes**:
```bash
marp presentation.md --notes -o notes.txt
```

**Configuration File**:
```bash
# Use .marprc.yml or marp.config.js
marp --config-file custom-config.yml presentation.md
```

### Common Command Patterns

**Generate multiple formats at once**:
```bash
#!/bin/bash
# generate-all.sh

marp presentation.md -o presentation.pdf
marp presentation.md -o presentation.html
marp presentation.md -o presentation.pptx
marp presentation.md --images png

echo "Generated: PDF, HTML, PPTX, and PNG images"
```

**Watch mode with live reload**:
```bash
marp -w -p --browser firefox presentation.md
```

---

## Markdown Syntax for Slides

### Slide Separators

**Basic Separator** (three dashes):
```markdown
# Slide 1 Title
Content for first slide

---

# Slide 2 Title
Content for second slide
```

### Front Matter (Global Directives)

**YAML front matter** at document start:
```markdown
---
theme: gaia
paginate: true
backgroundColor: #ffffff
backgroundImage: url('background.jpg')
color: #333333
header: "DataPeeker Analysis"
footer: "Q4 2024 Report"
---

# My Presentation
First slide content
```

**Common Global Directives**:
- `theme`: Choose theme (`default`, `gaia`, `uncover`, or custom)
- `paginate`: Add page numbers (`true`/`false`)
- `backgroundColor`: Set background color (CSS color)
- `backgroundImage`: Set background image (CSS url)
- `color`: Set text color (CSS color)
- `header`: Add header to all slides
- `footer`: Add footer to all slides
- `size`: Slide dimensions (`16:9`, `4:3`)
- `class`: Apply CSS classes

### Per-Slide Directives

**Local Directives** (apply to following slide):
```markdown
---

<!-- theme: uncover -->
<!-- paginate: false -->
<!-- backgroundColor: #1a1a1a -->
<!-- color: #ffffff -->

# Dark Theme Slide
This slide has custom styling
```

**Scoped Directives** (underscore prefix - don't inherit):
```markdown
---

<!-- _paginate: false -->
<!-- _backgroundColor: #f5f5f5 -->

# Title Slide
No page number, custom background
```

**Important**: Directives must be HTML comments (`<!-- directive: value -->`)

### Text Formatting

**Standard Markdown**:
```markdown
# Heading 1
## Heading 2
### Heading 3

**Bold text**
*Italic text*
~~Strikethrough~~

- Bullet list
  - Nested item
- Another item

1. Numbered list
2. Second item

[Link text](https://example.com)

`inline code`
```

**Code Blocks with Syntax Highlighting**:
````markdown
```sql
SELECT
  region,
  SUM(sales) as total_sales
FROM sales_metrics
WHERE date >= '2024-10-01'
GROUP BY region
ORDER BY total_sales DESC
```
````

**Math Typesetting** (LaTeX syntax):
```markdown
Inline math: $E = mc^2$

Display math:
$$
\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}
$$
```

### Images

**Basic Image**:
```markdown
![Alt text](path/to/image.png)
```

**Sized Image**:
```markdown
![width:600px height:400px](chart.png)

# or
![w:600px h:400px](chart.png)

# or proportional
![width:80%](chart.png)
```

**Background Image**:
```markdown
![bg](background.jpg)

# Sized background
![bg width:100%](background.jpg)

# Positioned background
![bg left](left-image.jpg)
![bg right](right-image.jpg)
```

**Image Alignment**:
```markdown
![bg left:40%](left-image.jpg)
![bg right:60%](right-image.jpg)
```

**Supported Formats**: PNG, JPEG, SVG, GIF, WebP

### Slide Layouts

**Two-Column Layout**:
```markdown
<div class="columns">
<div>

## Left Column
- Point 1
- Point 2

</div>
<div>

## Right Column
- Point A
- Point B

</div>
</div>
```

**Split Content**:
```markdown
<!-- _class: split -->

# Split Slide

:::: {.columns}
::: {.column}
Left content
:::
::: {.column}
Right content
:::
::::
```

### Speaker Notes

**Add presenter notes** (visible in HTML presenter view):
```markdown
# Slide Title

Main slide content visible to audience

<!--
Speaker notes here:
- Remember to mention X
- Ask if anyone has questions about Y
- Transition to next topic: Z
-->
```

**View speaker notes**:
- HTML export includes presenter mode (press 'P' key)
- Extract to text file: `marp --notes presentation.md -o notes.txt`

---

## Themes

### Built-in Themes

**Default Theme**:
```markdown
---
theme: default
---
```

**Gaia Theme** (light, modern):
```markdown
---
theme: gaia
---
```

**Uncover Theme** (dark, minimalist):
```markdown
---
theme: uncover
---
```

### Custom Themes

**Create Custom Theme CSS**:
```css
/* custom-theme.css */
@import 'default';  /* Extend default theme */

@theme custom-data-theme

section {
  background-color: #f5f5f5;
  color: #333;
  font-family: 'Segoe UI', 'Arial', sans-serif;
  font-size: 28px;
  padding: 60px;
}

section h1 {
  color: #0066cc;
  font-size: 48px;
  font-weight: bold;
  border-bottom: 3px solid #0066cc;
  padding-bottom: 10px;
}

section h2 {
  color: #0088cc;
  font-size: 36px;
  margin-top: 40px;
}

section code {
  background-color: #e8e8e8;
  padding: 2px 6px;
  border-radius: 3px;
}

section pre {
  background-color: #1e1e1e;
  color: #d4d4d4;
  padding: 20px;
  border-radius: 5px;
}

section footer {
  font-size: 14px;
  color: #999;
}

section header {
  font-size: 14px;
  color: #666;
  text-align: right;
}

/* Title slide styling */
section.title-slide {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
}

section.title-slide h1 {
  color: white;
  border-bottom: none;
  font-size: 64px;
}

/* Data emphasis styles */
section .metric {
  font-size: 48px;
  font-weight: bold;
  color: #0066cc;
}

section .callout {
  background-color: #fff3cd;
  border-left: 5px solid #ffc107;
  padding: 15px;
  margin: 20px 0;
}
```

**Use Custom Theme**:
```bash
marp presentation.md --theme-set custom-theme.css -o presentation.pdf
```

**In Markdown**:
```markdown
---
theme: custom-data-theme
---

# Presentation
```

### Theme CSS Variables

**Customize via CSS variables**:
```css
:root {
  --color-background: #ffffff;
  --color-foreground: #333333;
  --color-highlight: #0066cc;
  --color-dimmed: #999999;
  --font-size-base: 28px;
}

section {
  background: var(--color-background);
  color: var(--color-foreground);
  font-size: var(--font-size-base);
}

section h1 {
  color: var(--color-highlight);
}
```

---

## DataPeeker Presentation Patterns

### Pattern 1: Executive Summary

```markdown
---
theme: gaia
paginate: true
footer: "DataPeeker Q4 Analysis"
---

# Q4 Sales Analysis
## Executive Summary

**Key Finding**: West Coast expansion delivered 23% YoY growth

---

## Data Sources

- **Database**: `analytics_prod.sales_metrics`
- **Period**: 2024-10-01 to 2024-12-31
- **Records**: 50,000 transactions
- **Query Timestamp**: 2025-11-25 14:30 UTC

---

## Finding 1: Revenue Growth

**West Coast Performance**:
- Revenue: $1.2M (Q4 2024)
- Growth: +$450K vs Q4 2023
- Target: $800K (**exceeded by 50%**)

![width:700px](revenue-chart.png)

---

## Finding 2: Customer Acquisition

**New Customer Metrics**:
- Total new accounts: 342 (Q2-Q4 2024)
- Market share: 28% of all new customers
- Tech sector concentration: 62%

![width:700px](customer-acquisition.png)

---

## Finding 3: Transaction Values

**Premium Pricing Validation**:
- West Coast avg: **$285** per transaction
- Company avg: $254 per transaction
- Premium: **+12%**

![width:700px](transaction-value-chart.png)

---

## Methodology

```sql
SELECT
  region,
  DATE_TRUNC('month', transaction_date) as month,
  SUM(amount) as revenue,
  COUNT(DISTINCT customer_id) as customers,
  AVG(amount) as avg_transaction
FROM analytics_prod.sales_metrics
WHERE DATE(transaction_date) BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY region, month
ORDER BY revenue DESC
```

<!--
Query execution:
- Time: 2.3 seconds
- Rows examined: 50,000
- Rows returned: 18 (3 regions × 6 months)
-->

---

## Conclusions

### Three Key Takeaways
1. ✅ Expansion exceeded targets (23% vs 10% projected)
2. ✅ Customer acquisition validates market fit
3. ✅ Premium pricing sustainable

### Recommendation
**Continue West Coast investment** - positive ROI within 18 months

---

## Next Steps

**Immediate Actions**:
1. Approve 2025 West Coast budget ($200K)
2. Pilot East Coast expansion (Q2 2025)
3. Monitor retention metrics monthly

**Follow-up Analysis**: Q2 2025 retention study

---

## Questions?

**Full Technical Report**: [Whitepaper](./whitepaper.pdf)

**Analysis Repository**: [github.com/example-org/q4-analysis](https://github.com/example-org/q4-analysis)

**Contact**: data-team@example.com

---

<!-- _paginate: false -->
<!-- _backgroundColor: #f5f5f5 -->

# Thank You

**DataPeeker Team**
Q4 2024 Analysis
```

### Pattern 2: Technical Walkthrough

```markdown
---
theme: default
paginate: true
header: "Technical Analysis Walkthrough"
---

# Data Quality Assessment
## Q4 Sales Data Analysis

---

## Agenda

1. Data Source Validation
2. Quality Metrics Review
3. Transformation Pipeline
4. Results & Findings
5. Reproducibility Documentation

---

## Data Source: `analytics_prod.sales_metrics`

**Schema Validation**:
```sql
DESCRIBE analytics_prod.sales_metrics;
```

| Column            | Type      | Nullable |
|-------------------|-----------|----------|
| transaction_id    | INTEGER   | NOT NULL |
| customer_id       | INTEGER   | NOT NULL |
| region            | VARCHAR   | NOT NULL |
| amount            | DECIMAL   | NOT NULL |
| transaction_date  | DATE      | NOT NULL |

---

## Quality Metrics

**Completeness**:
- NULL values: 0.02% (within tolerance)
- Missing dates: 0 records
- Invalid amounts: 0 records

**Consistency**:
- Duplicate transactions: 0 detected
- Date range validation: ✓ All within expected period
- Amount range: $5 - $5,000 (normal distribution)

---

## Outlier Detection

**Method**: 3 MAD (Median Absolute Deviation)

```sql
SELECT
  amount,
  ABS(amount - MEDIAN(amount) OVER ()) /
    (MAD(amount) OVER () * 1.4826) as outlier_score
FROM sales_metrics
HAVING outlier_score > 3
```

**Results**: 12 outliers identified (0.024%)

All outliers reviewed and validated as legitimate high-value transactions.

---

## Transformation Pipeline

![width:900px](data-pipeline-diagram.svg)

1. **Raw Data** → Quality validation
2. **Validated Data** → Aggregation by region/month
3. **Aggregated Data** → Visualization preparation
4. **Visualizations** → Presentation delivery

---

## Results

[Insert findings slides similar to Pattern 1]

---

## Reproducibility

**Environment**:
- DataPeeker: v2.1.0
- Python: 3.11.5
- pandas: 2.1.0
- plotext: 5.2.8

**Repository**: All queries and code version controlled
- Commit: `abc123def456`
- Branch: `main`
- Tag: `q4-2024-analysis-v1.0`

---

## Run the Analysis Yourself

```bash
# Clone repository
git clone github.com/example-org/q4-analysis

# Install dependencies
pip install -r requirements.txt

# Set database connection
export DB_CONN="postgresql://user@host/db"

# Run analysis
python scripts/q4_regional_analysis.py

# View results
open analysis/q4-2024/findings.md
```

---

## Questions & Discussion
```

---

## Best Practices for Data Presentations

### DO:

✅ **Use clear, descriptive slide titles**
```markdown
# Finding 1: West Coast Revenue Dominance
NOT: # Results
```

✅ **Include data provenance on every slide**
```markdown
**Source**: `analytics_prod.sales_metrics` (2024-10-01 to 2024-12-31)
```

✅ **Show SQL queries for key findings**
```markdown
```sql
SELECT region, SUM(sales) FROM metrics WHERE...
```
```

✅ **Use visualizations from `creating-visualizations` skill**
```markdown
![width:700px](revenue-chart.png)
```

✅ **Add speaker notes for context**
```markdown
<!--
Remember to mention: This growth exceeded our projections by 50%
-->
```

✅ **Link to detailed whitepaper**
```markdown
Full methodology: [Technical Whitepaper](./whitepaper.pdf)
```

✅ **Version control both source and output**
```bash
git add presentation.md presentation.pdf
git commit -m "Add Q4 analysis presentation"
```

### DON'T:

❌ **Overload slides with text**
- Keep bullet points concise (max 5-7 per slide)
- Use multiple slides instead of cramming

❌ **Skip data source documentation**
- Always include database, table, timestamp
- Link to query files or repository

❌ **Use manual visualizations**
- Use `creating-visualizations` skill to generate charts
- Export as PNG/SVG and embed

❌ **Forget accessibility**
- Ensure sufficient color contrast
- Don't rely solely on color to convey meaning
- Use alt text for images

❌ **Ignore file size**
- Optimize images before embedding
- Large presentations are slow to load

---

## Troubleshooting

### Issue: "Command not found: marp"

**Solution**: Install marp-cli
```bash
npm install -g @marp-team/marp-cli
```

### Issue: PDF export fails

**Solution**: Requires Chrome/Edge/Firefox. Install if missing:
```bash
# macOS
brew install --cask google-chrome

# Or specify different browser
marp presentation.md --browser firefox -o presentation.pdf
```

### Issue: Images not loading

**Solution**: Use `--allow-local-files` flag
```bash
marp presentation.md --allow-local-files -o presentation.pdf
```

### Issue: Theme not applying

**Solution**: Verify theme CSS syntax
```bash
# Check for CSS errors
marp presentation.md --theme-set custom-theme.css --dry-run
```

### Issue: Slow rendering

**Solution**: Increase parallel processing
```bash
marp presentation.md --parallel 10 -o presentation.pdf
```

---

## Configuration File

**Create `.marprc.yml`** in project root:
```yaml
allowLocalFiles: true
engine: ./custom-engine.js
html: true
inputDir: ./slides
output: ./dist
pdf: true
pdfNotes: false
pdfOutlines: false
theme: custom-theme.css
themeSet: ./themes
watch: false
server: false
```

**Or `marp.config.js`**:
```javascript
module.exports = {
  allowLocalFiles: true,
  inputDir: './slides',
  output: './dist',
  themeSet: './themes',
  pdf: true
}
```

**Use configuration**:
```bash
marp presentation.md  # Automatically loads .marprc.yml
```

---

## Integration with DataPeeker Workflow

### Workflow: Analysis → Presentation

```bash
#!/bin/bash
# generate-presentation.sh

# Step 1: Run analysis (generates data and charts)
python scripts/q4_analysis.py

# Step 2: Generate charts using creating-visualizations skill
python scripts/create_charts.py

# Step 3: Build presentation from markdown
marp analysis/presentation.md \
  --allow-local-files \
  --theme-set themes/data-theme.css \
  -o analysis/presentation.pdf

echo "Presentation created: analysis/presentation.pdf"
```

### Workflow: Watch Mode for Iterative Development

```bash
# Terminal 1: Run analysis and regenerate charts on data changes
watch -n 60 python scripts/q4_analysis.py

# Terminal 2: Watch presentation markdown and rebuild on changes
marp -w -p analysis/presentation.md
```

### Workflow: Multiple Format Generation

```bash
#!/bin/bash
# generate-all-formats.sh

PRESENTATION="analysis/presentation.md"
OUTPUT_DIR="analysis/deliverables"

mkdir -p "$OUTPUT_DIR"

# PDF for printing/distribution
marp "$PRESENTATION" -o "$OUTPUT_DIR/presentation.pdf"

# HTML for web viewing
marp "$PRESENTATION" -o "$OUTPUT_DIR/presentation.html"

# PPTX for editing
marp "$PRESENTATION" -o "$OUTPUT_DIR/presentation.pptx"

# PNG images for social media/slides
marp "$PRESENTATION" --images png --image-scale 2

echo "Generated all formats in $OUTPUT_DIR"
```

---

## References

**Official Documentation**:
- [Marp Official Website](https://marp.app/)
- [Marp CLI GitHub](https://github.com/marp-team/marp-cli)
- [Marpit Framework (Directives)](https://marpit.marp.app/directives)
- [Marp Theme CSS](https://marpit.marp.app/theme-css)
- [Awesome Marp Collection](https://github.com/marp-team/awesome-marp)

**Related DataPeeker Skills**:
- `creating-visualizations` - Generate charts for presentations
- `interpreting-results` - Develop findings to present
- `frameworks/3-paragraph-essay.md` - Structure your presentation
- `frameworks/narrative-structure.md` - Tell compelling data stories
- `tools/pandoc.md` - Create detailed whitepapers
