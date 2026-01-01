# Citations for Data Analysis

Proper citation of data sources, queries, and tools ensures reproducibility, enables validation, and provides intellectual credit. This guide covers citation formats for data analysis contexts.

---

## Why Cite in Data Analysis?

**Reproducibility**: Citations enable others to access the same data sources and validate findings.

**Traceability**: Document provenance from raw data to final conclusions.

**Intellectual Credit**: Acknowledge prior research, methodology frameworks, and tool developers.

**Professional Credibility**: Demonstrates rigorous scholarship and attention to detail.

---

## What to Cite in Data Analysis

### 1. Data Sources
- Databases (production, analytics, external)
- Files (CSV, JSON, Excel)
- APIs and web services
- Surveys and data collection instruments

### 2. SQL Queries and Scripts
- Analysis queries
- Data transformation scripts
- ETL pipelines

### 3. Analysis Tools and Software
- DataPeeker, Jupyter, R, Python
- Libraries and packages (pandas, plotext, etc.)
- Visualization tools

### 4. Prior Research
- Published papers
- Internal reports
- Methodology frameworks

### 5. Statistical Methods
- Test procedures
- Modeling approaches
- Algorithms

---

## BibTeX Format

BibTeX is the standard format for academic and technical publications. Use with pandoc for automatic bibliography generation.

### Database Citations

**Pattern for production databases**:
```bibtex
@misc{database_identifier,
  author = {Organization Name},
  title = {Database Name},
  year = {2025},
  howpublished = {database.schema.table},
  note = {Query timestamp: YYYY-MM-DD HH:MM:SS UTC}
}
```

**Example**:
```bibtex
@misc{tilmon_sales_db_2025,
  author = {Tilmon Engineering},
  title = {Production Sales Metrics Database},
  year = {2025},
  howpublished = {analytics\_prod.sales\_metrics},
  note = {Query timestamp: 2025-11-25 14:30:00 UTC. Records examined: 50,000}
}
```

**Cite in text**:
```markdown
Data was extracted from the production database [@tilmon_sales_db_2025].
```

### File-Based Data Sources

**CSV Files**:
```bibtex
@misc{dataset_csv_2024,
  author = {Smith, Jane and Doe, John},
  title = {Q4 2024 Sales Transactions Dataset},
  year = {2024},
  howpublished = {CSV file},
  url = {https://example.com/data/q4_sales.csv},
  note = {Downloaded: 2025-11-25. 50,000 records}
}
```

**Excel Files**:
```bibtex
@misc{financial_data_2024,
  author = {Finance Department},
  title = {2024 Financial Report Data},
  year = {2024},
  howpublished = {Microsoft Excel file},
  note = {File: financial_report_2024.xlsx, Sheet: Q4_Summary}
}
```

### API and Web Data Sources

**REST API**:
```bibtex
@misc{stripe_api_2025,
  author = {Stripe, Inc.},
  title = {Stripe Payments API},
  year = {2025},
  url = {https://stripe.com/docs/api},
  note = {API version v2025-01-01. Accessed: 2025-11-25}
}
```

**Web Scraping**:
```bibtex
@misc{competitor_pricing_2025,
  author = {Competitor Analysis Team},
  title = {Competitor Pricing Data},
  year = {2025},
  url = {https://example.com/pricing},
  note = {Scraped: 2025-11-25 10:00 UTC. Data reflects public pricing as of scrape date}
}
```

### SQL Queries

**Cite specific queries**:
```bibtex
@misc{q4_revenue_query_2025,
  author = {Analytics Team},
  title = {Q4 Regional Revenue Analysis Query},
  year = {2025},
  howpublished = {SQL query},
  note = {File: queries/q4\_revenue.sql. Execution time: 2.3s. Repository: github.com/tilmon/analysis}
}
```

**Cite in text**:
```markdown
Regional revenue was calculated using a standardized query [@q4_revenue_query_2025]
that aggregates transactions by geographic region.
```

### Software and Tools

**DataPeeker**:
```bibtex
@software{datapeeker_2025,
  author = {Tilmon Engineering},
  title = {DataPeeker: SQL Analysis Tool},
  year = {2025},
  version = {2.1.0},
  url = {https://github.com/tilmon/datapeeker},
  note = {MIT License}
}
```

**Python Libraries**:
```bibtex
@software{pandas_2024,
  author = {{pandas development team}},
  title = {pandas: Powerful data structures for data analysis},
  year = {2024},
  version = {2.1.0},
  url = {https://pandas.pydata.org/},
  doi = {10.5281/zenodo.3509134}
}

@software{plotext_2024,
  author = {Piccolo, Savino},
  title = {plotext: Terminal plotting library for Python},
  year = {2024},
  version = {5.2.8},
  url = {https://github.com/piccolomo/plotext}
}
```

**R Packages**:
```bibtex
@manual{dplyr_2024,
  title = {dplyr: A Grammar of Data Manipulation},
  author = {Wickham, Hadley and François, Romain and Henry, Lionel and Müller, Kirill},
  year = {2024},
  note = {R package version 1.1.3},
  url = {https://CRAN.R-project.org/package=dplyr}
}
```

### Published Research

**Journal Articles**:
```bibtex
@article{jones2024,
  author = {Jones, Michael and Williams, Sarah},
  title = {Geographic Market Penetration Strategies for B2B SaaS},
  journal = {Journal of Sales Research},
  year = {2024},
  volume = {15},
  number = {3},
  pages = {234--256},
  doi = {10.1234/jsr.2024.15.3}
}
```

**Conference Papers**:
```bibtex
@inproceedings{smith2023,
  author = {Smith, Jane},
  title = {Reproducibility Standards for Business Analytics},
  booktitle = {Proceedings of the Data Science Conference},
  year = {2023},
  pages = {112--128},
  publisher = {ACM},
  address = {New York, NY},
  doi = {10.1145/3511234.3512345}
}
```

**Books**:
```bibtex
@book{wickham2023,
  author = {Wickham, Hadley and Grolemund, Garrett},
  title = {R for Data Science},
  edition = {2nd},
  year = {2023},
  publisher = {O'Reilly Media},
  address = {Sebastopol, CA},
  isbn = {978-1-492-09740-2}
}
```

### Internal Reports

**Company Reports**:
```bibtex
@techreport{tilmon_strategy_2024,
  author = {Strategic Planning Team},
  title = {2024 Geographic Expansion Strategy},
  institution = {Tilmon Engineering},
  year = {2024},
  type = {Internal Report},
  note = {Report ID: SPT-2024-003. Confidential}
}
```

**Working Papers**:
```bibtex
@unpublished{doe_analysis_2024,
  author = {Doe, John},
  title = {Preliminary Analysis of Customer Retention Patterns},
  year = {2024},
  note = {Working paper. Available from author}
}
```

### Methodology Frameworks

**Statistical Methods**:
```bibtex
@article{wilcoxon1945,
  author = {Wilcoxon, Frank},
  title = {Individual Comparisons by Ranking Methods},
  journal = {Biometrics Bulletin},
  year = {1945},
  volume = {1},
  number = {6},
  pages = {80--83},
  doi = {10.2307/3001968}
}
```

**Data Quality Frameworks**:
```bibtex
@article{batini2009,
  author = {Batini, Carlo and Cappiello, Cinzia and Francalanci, Chiara and Maurino, Andrea},
  title = {Methodologies for Data Quality Assessment and Improvement},
  journal = {ACM Computing Surveys},
  year = {2009},
  volume = {41},
  number = {3},
  pages = {1--52},
  doi = {10.1145/1541880.1541883}
}
```

---

## CSL JSON Format

Alternative to BibTeX, useful for web-based tools and JSON workflows.

### Database Citation (CSL JSON)

```json
{
  "id": "tilmon_sales_db_2025",
  "type": "dataset",
  "author": [
    {"literal": "Tilmon Engineering"}
  ],
  "title": "Production Sales Metrics Database",
  "issued": {"date-parts": [[2025]]},
  "URL": "analytics_prod.sales_metrics",
  "note": "Query timestamp: 2025-11-25 14:30:00 UTC. Records examined: 50,000"
}
```

### Software Citation (CSL JSON)

```json
{
  "id": "datapeeker_2025",
  "type": "software",
  "author": [
    {"literal": "Tilmon Engineering"}
  ],
  "title": "DataPeeker: SQL Analysis Tool",
  "version": "2.1.0",
  "issued": {"date-parts": [[2025]]},
  "URL": "https://github.com/tilmon/datapeeker"
}
```

### Journal Article (CSL JSON)

```json
{
  "id": "jones2024",
  "type": "article-journal",
  "author": [
    {"family": "Jones", "given": "Michael"},
    {"family": "Williams", "given": "Sarah"}
  ],
  "title": "Geographic Market Penetration Strategies for B2B SaaS",
  "container-title": "Journal of Sales Research",
  "volume": 15,
  "issue": 3,
  "page": "234-256",
  "issued": {"date-parts": [[2024]]},
  "DOI": "10.1234/jsr.2024.15.3"
}
```

---

## Citation in Markdown

### Basic Citations

**Single citation**:
```markdown
According to recent research [@jones2024], market penetration requires...
```

**Multiple citations**:
```markdown
Prior studies [@jones2024; @smith2023; @williams2022] have examined...
```

**Page numbers**:
```markdown
As noted by Jones [-@jones2024, pp. 45-47], the key factors include...
```

**Suppress author** (shows only year/number):
```markdown
Recent research [-@jones2024] demonstrates...
```

### Citations for Data Sources

**Database**:
```markdown
Data was extracted from the production database [@tilmon_sales_db_2025]
covering the period October 1 - December 31, 2024.
```

**Query**:
```markdown
Regional aggregation followed the methodology documented in
[@q4_revenue_query_2025], which groups transactions by geographic
region and calculates summary statistics.
```

**Multiple Data Sources**:
```markdown
Analysis combined data from three sources: production database
[@tilmon_sales_db_2025], customer demographics [@customer_data_2024],
and external market data [@competitor_pricing_2025].
```

### Citations for Tools

**Software**:
```markdown
Analysis was performed using DataPeeker v2.1.0 [@datapeeker_2025],
with data manipulation in pandas [@pandas_2024] and visualization
via plotext [@plotext_2024].
```

**Methodology**:
```markdown
Statistical significance was assessed using the Wilcoxon rank-sum
test [@wilcoxon1945] with α = 0.05.
```

---

## Complete Reference File Example

**`references.bib`**:
```bibtex
% ===================================================================
% DATA SOURCES
% ===================================================================

@misc{tilmon_sales_db_2025,
  author = {Tilmon Engineering},
  title = {Production Sales Metrics Database},
  year = {2025},
  howpublished = {analytics\_prod.sales\_metrics},
  note = {Query timestamp: 2025-11-25 14:30:00 UTC. Records: 50,000}
}

@misc{customer_data_2024,
  author = {Customer Analytics Team},
  title = {Customer Demographics and Profile Data},
  year = {2024},
  howpublished = {customer\_db.demographics},
  note = {Snapshot date: 2024-12-31}
}

% ===================================================================
% SQL QUERIES
% ===================================================================

@misc{q4_revenue_query_2025,
  author = {Analytics Team},
  title = {Q4 Regional Revenue Analysis Query},
  year = {2025},
  howpublished = {SQL query},
  note = {File: queries/q4\_revenue.sql. Execution: 2.3s. Repo: github.com/tilmon/analysis}
}

% ===================================================================
% SOFTWARE AND TOOLS
% ===================================================================

@software{datapeeker_2025,
  author = {Tilmon Engineering},
  title = {DataPeeker: SQL Analysis Tool},
  year = {2025},
  version = {2.1.0},
  url = {https://github.com/tilmon/datapeeker}
}

@software{pandas_2024,
  author = {{pandas development team}},
  title = {pandas: Powerful data structures for data analysis},
  year = {2024},
  version = {2.1.0},
  url = {https://pandas.pydata.org/},
  doi = {10.5281/zenodo.3509134}
}

@software{plotext_2024,
  author = {Piccolo, Savino},
  title = {plotext: Terminal plotting library for Python},
  year = {2024},
  version = {5.2.8},
  url = {https://github.com/piccolomo/plotext}
}

% ===================================================================
% PUBLISHED RESEARCH
% ===================================================================

@article{jones2024,
  author = {Jones, Michael and Williams, Sarah},
  title = {Geographic Market Penetration Strategies for B2B SaaS},
  journal = {Journal of Sales Research},
  year = {2024},
  volume = {15},
  number = {3},
  pages = {234--256},
  doi = {10.1234/jsr.2024.15.3}
}

@article{smith2023,
  author = {Smith, Jane},
  title = {Reproducibility Standards for Business Analytics},
  journal = {Data Science Quarterly},
  year = {2023},
  volume = {8},
  number = {2},
  pages = {112--128},
  doi = {10.5678/dsq.2023.8.2}
}

% ===================================================================
% STATISTICAL METHODS
% ===================================================================

@article{wilcoxon1945,
  author = {Wilcoxon, Frank},
  title = {Individual Comparisons by Ranking Methods},
  journal = {Biometrics Bulletin},
  year = {1945},
  volume = {1},
  number = {6},
  pages = {80--83},
  doi = {10.2307/3001968}
}

% ===================================================================
% INTERNAL REPORTS
% ===================================================================

@techreport{tilmon_strategy_2024,
  author = {Strategic Planning Team},
  title = {2024 Geographic Expansion Strategy},
  institution = {Tilmon Engineering},
  year = {2024},
  type = {Internal Report},
  note = {Report ID: SPT-2024-003}
}
```

---

## Citation Style Selection

### Common Styles for Data Analysis

**IEEE** (numbered citations):
```
[1] M. Jones and S. Williams, "Geographic Market Penetration..."
```

**Chicago Author-Date**:
```
(Jones and Williams 2024)
```

**APA 7th**:
```
Jones, M., & Williams, S. (2024). Geographic market penetration...
```

**Harvard**:
```
Jones, M. and Williams, S. (2024) 'Geographic Market Penetration...'
```

### Style Files

Download CSL styles from:
- [Zotero Style Repository](https://www.zotero.org/styles) - 10,000+ styles
- [CSL GitHub](https://github.com/citation-style-language/styles)

**Common styles for technical documents**:
- `ieee.csl` - IEEE (recommended for technical reports)
- `chicago-author-date.csl` - Chicago (default for pandoc)
- `apa.csl` - APA 7th edition
- `acm-sig-proceedings.csl` - ACM conference format

**Use with pandoc**:
```bash
pandoc whitepaper.md \
  --citeproc \
  --bibliography references.bib \
  --csl ieee.csl \
  -s -o whitepaper.pdf
```

---

## Best Practices

### DO:

✅ **Cite all data sources**
```markdown
Data extracted from [@tilmon_sales_db_2025] covering Q4 2024.
```

✅ **Include query timestamps**
```bibtex
note = {Query timestamp: 2025-11-25 14:30:00 UTC}
```

✅ **Document tool versions**
```bibtex
version = {2.1.0}
```

✅ **Link to repositories**
```bibtex
url = {https://github.com/tilmon/analysis}
```

✅ **Use consistent citation keys**
```
Pattern: lastname_year or tool_year
Examples: jones2024, datapeeker_2025
```

✅ **Cite statistical methods**
```markdown
Significance tested using Wilcoxon rank-sum [@wilcoxon1945].
```

✅ **Credit prior research**
```markdown
Our approach builds on [@jones2024; @smith2023].
```

### DON'T:

❌ **Skip data source citations**
- Every database, file, API must be cited

❌ **Omit timestamps**
- Data changes over time, timestamps enable reproducibility

❌ **Forget tool versions**
- Analysis results can vary across software versions

❌ **Use vague citations**
- "Internal database" → Cite specific database.table

❌ **Ignore SQL query provenance**
- Document query file locations and execution details

---

## Special Cases

### Proprietary Data

**Limited access data**:
```bibtex
@misc{proprietary_data_2025,
  author = {Company Name},
  title = {Proprietary Customer Database},
  year = {2025},
  note = {Confidential. Access restricted. Contact: data-team@company.com}
}
```

**Cite in text with caveats**:
```markdown
Analysis used proprietary customer data [@proprietary_data_2025].
Raw data cannot be shared due to confidentiality restrictions, but
aggregated results and methodology are fully documented in Appendix A.
```

### Synthetic or Generated Data

**Machine-generated data**:
```bibtex
@misc{synthetic_data_2025,
  author = {Analytics Team},
  title = {Synthetic Customer Transaction Data},
  year = {2025},
  note = {Generated using Python Faker library v20.1.0. Seed: 42.
         Records: 10,000. Generation script: scripts/generate\_data.py}
}
```

### Real-time Dashboards

**Live data sources**:
```bibtex
@misc{realtime_dashboard_2025,
  author = {Company Name},
  title = {Real-Time Sales Dashboard},
  year = {2025},
  url = {https://analytics.company.com/sales-dashboard},
  note = {Live dashboard. Data as of: 2025-11-25 14:30 UTC.
         Screenshot archived in analysis/dashboards/}
}
```

---

## Integration with Pandoc

### Basic Citation Workflow

**1. Create bibliography file** (`references.bib`)

**2. Add citations to markdown**:
```markdown
Data from production database [@tilmon_sales_db_2025] shows...
```

**3. Convert with --citeproc**:
```bash
pandoc whitepaper.md \
  --citeproc \
  --bibliography references.bib \
  --csl ieee.csl \
  -s -o whitepaper.pdf
```

### In-Document Bibliography Specification

**Alternative: Specify bibliography in YAML**:
```yaml
---
title: "My Analysis"
bibliography: references.bib
csl: ieee.csl
link-citations: true
---
```

**Then convert without flags**:
```bash
pandoc whitepaper.md -s -o whitepaper.pdf
```

---

## Citation Management Tools

### Zotero

**Export from Zotero**:
1. Select references in Zotero
2. Right-click → Export Items
3. Format: BibTeX
4. Save as `references.bib`

**Zotero Better BibTeX** plugin provides enhanced BibTeX export.

### Mendeley

**Export from Mendeley**:
1. Select references
2. File → Export
3. Format: BibTeX
4. Save

### EndNote

**Export from EndNote**:
1. Select references
2. File → Export
3. Format: BibTeX
4. Save

---

## Troubleshooting

### Issue: Citations showing as [@key] instead of numbers

**Solution**: Use `--citeproc` flag
```bash
pandoc input.md --citeproc --bibliography refs.bib -s -o output.pdf
```

### Issue: Bibliography not appearing

**Solution**: Ensure bibliography file path is correct
```bash
# Correct
--bibliography references.bib

# Wrong (if file doesn't exist at path)
--bibliography ../other/refs.bib
```

### Issue: Citation key not found

**Solution**: Check citation key matches BibTeX entry
```bibtex
% BibTeX entry
@misc{tilmon_data_2025,
  ...
}

% Correct citation in markdown
[@tilmon_data_2025]

% Wrong
[@tilmon_data]  # Missing _2025
```

### Issue: Special characters in BibTeX

**Solution**: Escape underscores and special characters
```bibtex
% Wrong
howpublished = {analytics_prod.sales_metrics}

% Correct
howpublished = {analytics\_prod.sales\_metrics}
```

---

## References

**Citation Standards**:
- [BibTeX Documentation](http://www.bibtex.org/)
- [CSL Specification](https://citationstyles.org/)
- [Zotero Style Repository](https://www.zotero.org/styles)

**Related DataPeeker Skills**:
- `tools/pandoc.md` - Using pandoc with citations
- `formats/reproducibility.md` - Documenting reproducibility
- `frameworks/3-paragraph-essay.md` - Bibliography in essay structure
- `SKILL.md` - Phase 4: Add Citations & Reproducibility
