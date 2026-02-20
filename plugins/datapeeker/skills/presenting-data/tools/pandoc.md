# Pandoc: Universal Document Converter

Pandoc is a universal markup converter for creating publication-quality documents from Markdown. This guide covers installation, CLI usage, citations, cross-references, and best practices for data analysis whitepapers.

---

## Overview

**What is Pandoc?**
- Universal document converter supporting 50+ input/output formats
- Haskell-based with modular reader/writer architecture
- Industry-standard tool for academic and technical publishing
- Supports citations, cross-references, and professional formatting

**When to Use Pandoc:**
- Technical reports and whitepapers (20-50+ pages)
- Academic papers with citations and bibliography
- Comprehensive documentation requiring cross-references
- Professional documents needing LaTeX-quality typography

**When NOT to Use Pandoc:**
- Quick presentations (use marp for slides)
- Simple one-page documents (plain Markdown sufficient)
- Interactive web applications (use specialized web frameworks)

---

## Installation

### macOS

**Using Homebrew**:
```bash
brew install pandoc

# For PDF output, also install LaTeX
brew install --cask mactex
# Or minimal: brew install basictex
```

### Linux

**Ubuntu/Debian**:
```bash
sudo apt-get update
sudo apt-get install pandoc

# For PDF output
sudo apt-get install texlive-full
# Or minimal: sudo apt-get install texlive-latex-base
```

**Fedora**:
```bash
sudo dnf install pandoc

# For PDF output
sudo dnf install texlive-scheme-full
```

### Windows

**Download installer**: https://pandoc.org/installing.html

**For PDF output**, install MiKTeX or TeX Live:
- MiKTeX: https://miktex.org/download
- TeX Live: https://www.tug.org/texlive/windows.html

### Verify Installation

```bash
# Check pandoc version
pandoc --version

# Check LaTeX (for PDF)
pdflatex --version

# List supported formats
pandoc --list-input-formats
pandoc --list-output-formats
```

---

## CLI Usage: Basic Conversions

### Simple Conversions

**Markdown to HTML**:
```bash
pandoc input.md -o output.html
```

**Markdown to PDF**:
```bash
pandoc input.md -o output.pdf
```

**Markdown to DOCX**:
```bash
pandoc input.md -o output.docx
```

**Explicit Format Specification**:
```bash
pandoc -f markdown -t pdf input.md -o output.pdf
```

### Standalone Documents

**Include headers, footers, and formatting**:
```bash
pandoc -s input.md -o output.html
pandoc -s input.md -o output.pdf
pandoc -s input.md -o output.docx
```

Without `-s`, output contains only the converted content (no document structure).

---

## CLI Usage: Advanced Options

### Table of Contents

**Generate TOC**:
```bash
pandoc -s --toc input.md -o output.pdf
```

**Customize TOC depth**:
```bash
pandoc -s --toc --toc-depth=2 input.md -o output.pdf
```

**Custom TOC title**:
```markdown
---
toc-title: "Contents"
---
```

### Section Numbering

**Number sections automatically**:
```bash
pandoc -s --number-sections input.md -o output.pdf
```

**Combined with TOC**:
```bash
pandoc -s --toc --number-sections input.md -o output.pdf
```

### Variables and Metadata

**Set document variables**:
```bash
pandoc -V title="My Research Paper" \
  -V author="Jane Smith" \
  -V date="2025-11-25" \
  -s input.md -o output.pdf
```

**Common variables**:
- `-V geometry:margin=1in` - Page margins
- `-V fontsize=12pt` - Font size
- `-V linestretch=1.5` - Line spacing (1.5 = 1.5x)
- `-V papersize=letter` - Paper size
- `-V documentclass=article` - LaTeX document class
- `-V colorlinks=true` - Colored hyperlinks

**Example with multiple variables**:
```bash
pandoc -s input.md \
  -V geometry:margin=1in \
  -V fontsize=12pt \
  -V linestretch=1.5 \
  -V colorlinks=true \
  -V linkcolor=blue \
  --toc --number-sections \
  -o output.pdf
```

### Merging Multiple Files

**Concatenate multiple markdown files**:
```bash
pandoc intro.md methods.md results.md conclusion.md \
  -s --toc --number-sections \
  -o complete-paper.pdf
```

**With metadata file**:
```bash
pandoc metadata.yaml intro.md methods.md results.md \
  -s --toc --number-sections \
  -o complete-paper.pdf
```

---

## Metadata in Markdown

### YAML Front Matter

**At the beginning of markdown file**:
```yaml
---
title: "Data Analysis Whitepaper: Q4 2024 Sales Performance"
author:
  - Jane Smith
  - John Doe
date: "2025-11-25"
institute: "Tilmon Engineering"
abstract: |
  This whitepaper presents a comprehensive analysis of Q4 2024 sales
  data, revealing 23% year-over-year growth driven primarily by West
  Coast expansion. We examine customer acquisition patterns, transaction
  values, and regional performance using reproducible SQL-based
  methodology.
keywords: "data analysis, SQL, reproducibility, sales analysis"
toc-title: "Table of Contents"
lof: true  # List of figures
lot: true  # List of tables
bibliography: references.bib
csl: ieee.csl
---

# Introduction

Document content starts here...
```

**Metadata Fields**:
- `title` - Document title
- `author` - Author(s), single string or list
- `date` - Publication date
- `institute` - Institution/organization
- `abstract` - Abstract paragraph(s)
- `keywords` - Comma-separated keywords
- `toc-title` - Custom TOC heading
- `lof` - Generate list of figures (true/false)
- `lot` - Generate list of tables (true/false)
- `bibliography` - Path to BibTeX file
- `csl` - Citation style (CSL file)
- `link-citations` - Make citations clickable (true/false)

---

## Citations and Bibliography

### Using BibTeX

**Step 1: Create BibTeX file** (`references.bib`):
```bibtex
@article{smith2024,
  author = {Smith, John and Johnson, Mary},
  title = {Advanced Data Analysis Techniques},
  journal = {Journal of Data Science},
  year = {2024},
  volume = {15},
  number = {3},
  pages = {123-145},
  doi = {10.1234/jds.2024.15.3}
}

@misc{example2025,
  author = {Tilmon Engineering},
  title = {DataPeeker: SQL Analysis Tool},
  year = {2025},
  version = {2.1.0},
  url = {https://github.com/example-org/datapeeker},
  note = {Accessed: 2025-11-25}
}

@misc{production_db2025,
  author = {Tilmon Engineering},
  title = {Production Sales Metrics Database},
  year = {2025},
  howpublished = {analytics\_prod.sales\_metrics},
  note = {Query timestamp: 2025-11-25 14:30:00 UTC}
}
```

**Step 2: Cite in Markdown**:
```markdown
According to recent research [@smith2024], data quality is crucial.

Multiple citations [@smith2024; @example2025] can be combined.

Cite with page numbers [@smith2024, pp. 45-47].

Suppress author name: [-@smith2024] showed that...
```

**Step 3: Convert with citations**:
```bash
pandoc input.md \
  --citeproc \
  --bibliography references.bib \
  -s -o output.pdf
```

### Citation Styles (CSL)

**Use specific citation style**:
```bash
pandoc input.md \
  --citeproc \
  --bibliography references.bib \
  --csl ieee.csl \
  -s -o output.pdf
```

**Common CSL styles**:
- `chicago-author-date.csl` - Chicago (default if no CSL specified)
- `ieee.csl` - IEEE numbered citations
- `apa.csl` - APA 7th edition
- `modern-language-association.csl` - MLA style
- `harvard-cite-them-right.csl` - Harvard style
- `nature.csl` - Nature journal style
- `vancouver.csl` - Vancouver style

**Download CSL styles**:
- [Zotero Style Repository](https://www.zotero.org/styles) (10,000+ styles)
- [CSL GitHub](https://github.com/citation-style-language/styles)

**Example with IEEE style**:
```bash
# Download IEEE style
curl -o ieee.csl \
  https://raw.githubusercontent.com/citation-style-language/styles/master/ieee.csl

# Use in conversion
pandoc input.md \
  --citeproc \
  --bibliography references.bib \
  --csl ieee.csl \
  -s -o output.pdf
```

### CSL JSON Format (Alternative to BibTeX)

**Create `references.json`**:
```json
[
  {
    "id": "smith2024",
    "type": "article-journal",
    "author": [
      {"family": "Smith", "given": "John"},
      {"family": "Johnson", "given": "Mary"}
    ],
    "title": "Advanced Data Analysis Techniques",
    "container-title": "Journal of Data Science",
    "issued": {"date-parts": [[2024]]},
    "volume": 15,
    "issue": 3,
    "page": "123-145",
    "DOI": "10.1234/jds.2024.15.3"
  }
]
```

**Use JSON bibliography**:
```bash
pandoc input.md \
  --citeproc \
  --bibliography references.json \
  -s -o output.pdf
```

---

## Cross-References (Figures, Tables, Equations)

### Using pandoc-crossref Filter

**Install pandoc-crossref**:
```bash
# Download from: https://github.com/lierdakil/pandoc-crossref/releases
# Or on some systems:
brew install pandoc-crossref  # macOS
```

**Syntax for Cross-References**:

**Sections**:
```markdown
# Introduction {#sec:intro}

As discussed in @sec:intro, data quality matters.

# Methodology {#sec:methods}

See @sec:methods for details.
```

**Figures**:
```markdown
![Data pipeline diagram](diagram.png){#fig:pipeline}

Figure @fig:pipeline shows the data processing workflow.

As shown in @fig:pipeline, the process has three stages.
```

**Tables**:
```markdown
| Region | Sales |
|--------|-------|
| North  | 45000 |
| South  | 32000 |

: Sales by region {#tbl:sales}

Table @tbl:sales summarizes regional performance.

Results (see @tbl:sales) demonstrate clear trends.
```

**Equations**:
```markdown
$$
E = mc^2
$$ {#eq:einstein}

Equation @eq:einstein is foundational to physics.

As @eq:einstein shows, energy and mass are related.
```

**Convert with cross-references**:
```bash
pandoc input.md \
  -F pandoc-crossref \
  --citeproc \
  --bibliography references.bib \
  -s --toc --number-sections \
  -o output.pdf
```

**Important**: `-F pandoc-crossref` must come **before** `--citeproc`

### Cross-Reference Customization

**Customize prefix text**:
```markdown
---
figPrefix: "Figure"
tblPrefix: "Table"
eqnPrefix: "Equation"
secPrefix: "Section"
---
```

**Custom numbering**:
```markdown
---
numberSections: true
figureTitle: "Figure"
tableTitle: "Table"
---
```

---

## Templates

### Extract Default Templates

**LaTeX template**:
```bash
pandoc -D latex > my-template.tex
```

**HTML template**:
```bash
pandoc -D html5 > my-template.html
```

**DOCX reference document**:
```bash
pandoc -D docx > reference.docx
```

### Using Custom Templates

**Apply custom LaTeX template**:
```bash
pandoc -s --template=my-template.tex input.md -o output.pdf
```

**Apply custom HTML template**:
```bash
pandoc -s --template=my-template.html input.md -o output.html
```

### Template Variables

**Available variables** (use in templates as `$variable$`):
- `$title$` - Document title
- `$author$` - Author name(s)
- `$date$` - Document date
- `$abstract$` - Abstract text
- `$toc$` - Table of contents
- `$body$` - Document body
- `$bibliography$` - Bibliography section

**Example LaTeX template snippet**:
```latex
\documentclass[12pt]{article}

\title{$title$}
\author{$author$}
\date{$date$}

\begin{document}

\maketitle

\begin{abstract}
$abstract$
\end{abstract}

\tableofcontents

$body$

\end{document}
```

---

## PDF Generation (LaTeX)

### LaTeX Engine Options

**Default (pdflatex)**:
```bash
pandoc input.md -o output.pdf
```

**XeLaTeX** (better Unicode support):
```bash
pandoc --pdf-engine=xelatex input.md -o output.pdf
```

**LuaLaTeX** (modern, fast):
```bash
pandoc --pdf-engine=lualatex input.md -o output.pdf
```

### PDF-Specific Variables

**Page geometry**:
```bash
pandoc -s input.md \
  -V geometry:margin=1in \
  -V geometry:paperwidth=8.5in \
  -V geometry:paperheight=11in \
  -o output.pdf
```

**Document class**:
```bash
pandoc -s input.md \
  -V documentclass=article \
  -V fontsize=12pt \
  -V papersize=letter \
  -o output.pdf
```

**Line spacing**:
```bash
pandoc -s input.md \
  -V linestretch=1.5 \
  -o output.pdf
```

**Colors and links**:
```bash
pandoc -s input.md \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V citecolor=blue \
  -V urlcolor=blue \
  -o output.pdf
```

### Include LaTeX in Header

**Create `preamble.tex`**:
```latex
\usepackage{fancyhdr}
\pagestyle{fancy}
\fancyhead[L]{My Document}
\fancyhead[R]{\thepage}
\fancyfoot[C]{Confidential}
```

**Include in conversion**:
```bash
pandoc -s input.md \
  -H preamble.tex \
  -o output.pdf
```

---

## Word Documents (DOCX)

### Basic DOCX Conversion

```bash
pandoc input.md -o output.docx
```

### Using Reference Document (Template)

**Extract reference document**:
```bash
pandoc -D docx > reference.docx
```

**Customize `reference.docx`**:
1. Open in Microsoft Word
2. Modify styles (Heading 1, Heading 2, Body Text, etc.)
3. Save

**Use customized template**:
```bash
pandoc input.md --reference-doc=reference.docx -o output.docx
```

### DOCX with Citations

```bash
pandoc input.md \
  --citeproc \
  --bibliography references.bib \
  --reference-doc=reference.docx \
  -o output.docx
```

---

## HTML Export

### Basic HTML

```bash
pandoc -s input.md -o output.html
```

### HTML with CSS

**External CSS**:
```bash
pandoc -s -c style.css input.md -o output.html
```

**Inline CSS** (self-contained):
```bash
pandoc -s --self-contained -c style.css input.md -o output.html
```

### HTML with MathJax (for equations)

```bash
pandoc -s --mathjax input.md -o output.html
```

---

## DataPeeker Whitepaper Patterns

### Pattern 1: Complete Technical Report

**File Structure**:
```
analysis/
├── q4-2024/
│   ├── whitepaper.md (main document)
│   ├── references.bib (bibliography)
│   ├── ieee.csl (citation style)
│   ├── metadata.yaml (optional separate metadata)
│   ├── queries/
│   │   └── q4_analysis.sql
│   └── visualizations/
│       ├── revenue-chart.png
│       └── customer-acquisition.png
```

**`whitepaper.md`**:
```yaml
---
title: "West Coast Expansion Analysis: Q4 2024 Performance Evaluation"
author:
  - name: "Data Analytics Team"
    affiliation: "Tilmon Engineering"
date: "2025-11-25"
institute: "Tilmon Engineering"
abstract: |
  This whitepaper presents a comprehensive analysis of Q4 2024 sales
  performance following the April 2024 West Coast expansion initiative.
  Using reproducible SQL-based methodology, we examine 50,000
  transactions to determine whether the expansion delivered measurable
  results. Key findings include 23% year-over-year revenue growth,
  342 new customer acquisitions, and sustainable +12% transaction value
  premium. Analysis validates continuation of West Coast operations and
  supports piloting similar expansion in East Coast markets.
keywords: "data analysis, SQL, sales analysis, geographic expansion, reproducibility"
toc-title: "Table of Contents"
lof: true
lot: true
bibliography: references.bib
csl: ieee.csl
link-citations: true
colorlinks: true
linkcolor: blue
citecolor: blue
urlcolor: blue
---

# Introduction

## Business Context

In April 2024, Tilmon Engineering initiated a strategic expansion into
West Coast markets, investing $200K and committing 3 sales FTE. By
October 2024, stakeholders required data-driven evaluation to determine
whether to continue, scale, or redirect these resources.

## Research Question

This analysis addresses: **Did the West Coast expansion deliver
measurable results that justify continued investment?**

## Thesis Statement

Six months of sales data (Q2-Q4 2024) demonstrate that West Coast
expansion exceeded projections across three key metrics: revenue growth
(23% YoY vs 10% target), customer acquisition (342 new accounts), and
transaction value premium (+12%). These findings support continued
investment and potential replication in similar markets.

## Document Overview

Section @sec:methodology details data sources and analytical approach.
Section @sec:results presents findings with supporting visualizations.
Section @sec:discussion interprets implications and addresses
limitations. Section @sec:conclusions provides recommendations and next
steps. Appendix A documents reproducibility information.

# Methodology {#sec:methodology}

## Data Sources

Data was extracted from the production analytics database using
standardized SQL queries documented in Appendix B.

**Database**: `analytics_prod.sales_metrics`
**Table Structure**: See @tbl:schema for schema details.

| Column            | Type      | Description                    |
|-------------------|-----------|--------------------------------|
| transaction_id    | INTEGER   | Unique transaction identifier  |
| customer_id       | INTEGER   | Customer identifier            |
| region            | VARCHAR   | Geographic region              |
| amount            | DECIMAL   | Transaction amount (USD)       |
| transaction_date  | DATE      | Date of transaction            |

: Database schema for sales_metrics table {#tbl:schema}

**Data Period**: October 1, 2024 - December 31, 2024
**Query Timestamp**: 2025-11-25 14:30:00 UTC
**Records Examined**: 50,000 transactions

## Analysis Framework

Our analysis follows established data quality frameworks [@jones2024]
and reproducible research standards [@smith2023]. Query methodology
builds on best practices from prior regional expansion studies
[@williams2024].

## Data Quality Assessment

**Completeness**: NULL values detected in 0.02% of records (10 of
50,000), all in non-critical columns. All critical fields (transaction
amount, date, region) complete.

**Consistency**: Zero duplicate transactions detected. Date ranges
validated against expected period. Amount ranges ($5-$5,000) follow
normal distribution.

**Outliers**: 12 outliers detected using 3 MAD threshold. All reviewed
and validated as legitimate high-value transactions.

## Query Methodology

Primary analysis query extracted regional performance metrics:

\```sql
SELECT
  region,
  DATE_TRUNC('month', transaction_date) as month,
  SUM(amount) as total_revenue,
  COUNT(DISTINCT customer_id) as unique_customers,
  AVG(amount) as avg_transaction,
  COUNT(*) as transaction_count
FROM analytics_prod.sales_metrics
WHERE DATE(transaction_date) BETWEEN '2024-10-01' AND '2024-12-31'
GROUP BY region, month
ORDER BY month, total_revenue DESC
\```

**Execution Details**:
- Runtime: 2.3 seconds
- Rows examined: 50,000
- Rows returned: 18 (3 regions × 6 months)
- Indexes used: date_region_idx

Full query text available in Appendix B.

# Results {#sec:results}

## Finding 1: Revenue Growth Concentration {#sec:revenue}

West Coast region demonstrated significantly higher revenue growth
compared to other regions.

![Q4 Revenue by Region](visualizations/revenue-chart.png){#fig:revenue width=80%}

Figure @fig:revenue shows quarterly revenue comparison across regions.
West Coast growth substantially exceeds other regions.

### Evidence

@tbl:revenue presents detailed revenue breakdown:

| Region      | Q4 2023 | Q4 2024 | Growth  | % of Growth |
|-------------|---------|---------|---------|-------------|
| West Coast  | $750K   | $1,200K | +$450K  | 69%         |
| East Coast  | $800K   | $900K   | +$100K  | 15%         |
| Central     | $650K   | $750K   | +$100K  | 15%         |
| **Total**   | $2,200K | $2,850K | +$650K  | 100%        |

: Regional revenue breakdown Q4 2023 vs Q4 2024 {#tbl:revenue}

West Coast revenue reached $1.2M in Q4 2024, representing $450K increase
(+60%) vs Q4 2023. All other regions combined grew $200K (+12%) over
same period.

### Analysis

Concentration of growth in West Coast region aligns with Q2 2024
expansion strategy targeting high-value customers in tech-heavy markets.
Finding consistent with prior research on geographic market penetration
[@jones2024].

### Caveats

Several factors may contribute to observed pattern:
1. West Coast expansion received higher marketing budget allocation
2. Seasonal factors (tech industry Q4 spending cycles)
3. Customer base differences (B2B vs B2C mix varies by region)

Further analysis (Section @sec:retention) examines sustainability.

## Finding 2: Customer Acquisition {#sec:customers}

[Additional findings follow same pattern...]

# Discussion {#sec:discussion}

[Interpretation of findings, comparison to prior research, alternative explanations...]

# Conclusions {#sec:conclusions}

[Summary, recommendations, limitations, future directions...]

# References

<!-- Bibliography automatically generated here -->

# Appendix A: Reproducibility Information {#sec:appendix-a}

## Environment

**Analysis Tools**:
- DataPeeker: v2.1.0
- Python: 3.11.5
- pandas: 2.1.0
- plotext: 5.2.8
- Operating System: macOS 14.6.0

**Database Connection**:
- Host: analytics-prod-db.example.com
- Database: analytics_prod
- Schema: public
- Table: sales_metrics

## Reproducibility Instructions

1. Clone analysis repository:
   \```bash
   git clone github.com/example-org/q4-analysis
   cd q4-analysis
   \```

2. Install dependencies:
   \```bash
   pip install -r requirements.txt
   \```

3. Set database credentials:
   \```bash
   export DB_CONN="postgresql://user@host/analytics_prod"
   \```

4. Run analysis:
   \```bash
   python scripts/q4_regional_analysis.py
   \```

5. Generate report:
   \```bash
   pandoc whitepaper.md \
     --citeproc \
     --bibliography references.bib \
     --csl ieee.csl \
     -F pandoc-crossref \
     -s --toc --number-sections \
     -V geometry:margin=1in \
     -o whitepaper.pdf
   \```

# Appendix B: SQL Queries {#sec:appendix-b}

## Query 1: Regional Revenue Analysis

\```sql
-- Purpose: Compare regional revenue Q4 2023 vs Q4 2024
-- Execution time: 2.3 seconds
-- Rows returned: 6

SELECT
  region,
  EXTRACT(year FROM transaction_date) as year,
  EXTRACT(quarter FROM transaction_date) as quarter,
  SUM(amount) as total_revenue,
  COUNT(DISTINCT customer_id) as unique_customers,
  COUNT(*) as transaction_count
FROM analytics_prod.sales_metrics
WHERE EXTRACT(quarter FROM transaction_date) = 4
  AND EXTRACT(year FROM transaction_date) IN (2023, 2024)
GROUP BY region, year, quarter
ORDER BY year, total_revenue DESC
\```

[Additional queries...]
```

**Build Whitepaper**:
```bash
#!/bin/bash
# build-whitepaper.sh

cd analysis/q4-2024

pandoc whitepaper.md \
  --citeproc \
  --bibliography references.bib \
  --csl ieee.csl \
  -F pandoc-crossref \
  -s --toc --number-sections \
  -V geometry:margin=1in \
  -V fontsize=11pt \
  -V linestretch=1.15 \
  -V colorlinks=true \
  -V linkcolor=blue \
  -V citecolor=blue \
  -V urlcolor=blue \
  --pdf-engine=xelatex \
  -o whitepaper.pdf

echo "Whitepaper generated: whitepaper.pdf"
```

---

## Best Practices

### DO:

✅ **Use metadata YAML for all documents**
```yaml
---
title: "Document Title"
author: "Your Name"
date: "2025-11-25"
bibliography: references.bib
---
```

✅ **Cite data sources in BibTeX**
```bibtex
@misc{production_db2025,
  author = {Company Name},
  title = {Production Database},
  year = {2025},
  note = {Query timestamp: 2025-11-25 14:30:00 UTC}
}
```

✅ **Use cross-references with pandoc-crossref**
```markdown
See Figure @fig:chart1 and Table @tbl:results.
```

✅ **Document SQL queries in appendix**
```markdown
# Appendix: SQL Queries

\```sql
SELECT * FROM table WHERE...
\```
```

✅ **Version control source and build scripts**
```bash
git add whitepaper.md references.bib build.sh
git commit -m "Add Q4 analysis whitepaper"
```

### DON'T:

❌ **Skip bibliography** - Always cite data sources
❌ **Forget cross-references** - Use pandoc-crossref for figures/tables
❌ **Hardcode formatting** - Use variables and templates instead
❌ **Ignore reproducibility** - Document environment and queries
❌ **Skip validation** - Review PDF output before distribution

---

## Troubleshooting

### Issue: "pandoc: command not found"

**Solution**: Install pandoc
```bash
brew install pandoc  # macOS
sudo apt-get install pandoc  # Linux
```

### Issue: PDF generation fails

**Solution**: Install LaTeX
```bash
brew install --cask mactex  # macOS
sudo apt-get install texlive-full  # Linux
```

### Issue: Bibliography not appearing

**Solution**: Ensure `--citeproc` flag is used and bibliography file exists
```bash
pandoc input.md \
  --citeproc \
  --bibliography references.bib \
  -s -o output.pdf
```

### Issue: Cross-references showing ??

**Solution**: Use pandoc-crossref filter BEFORE --citeproc
```bash
pandoc input.md \
  -F pandoc-crossref \
  --citeproc \
  --bibliography references.bib \
  -s -o output.pdf
```

### Issue: Citations showing [@citation_key] instead of numbers

**Solution**: Use `--citeproc` flag (or `-C` shorthand)
```bash
pandoc input.md -C --bibliography refs.bib -s -o output.pdf
```

---

## References

**Official Documentation**:
- [Pandoc Official Website](https://pandoc.org/)
- [Pandoc User's Guide](https://pandoc.org/MANUAL.html)
- [pandoc-crossref Documentation](https://lierdakil.github.io/pandoc-crossref/)
- [CSL Style Repository](https://github.com/citation-style-language/styles)
- [Zotero Style Repository](https://www.zotero.org/styles)

**Related DataPeeker Skills**:
- `creating-visualizations` - Generate figures for whitepapers
- `interpreting-results` - Develop findings to document
- `frameworks/3-paragraph-essay.md` - Structure your whitepaper
- `frameworks/narrative-structure.md` - Tell compelling data stories
- `tools/marp.md` - Create presentations (complementary to pandoc)
- `formats/citations.md` - Citing data sources properly
- `formats/reproducibility.md` - Documenting reproducible research
