# Reproducibility Documentation

Reproducible research enables others to validate findings, replicate analysis, and build upon your work. This guide provides a comprehensive checklist for documenting reproducible data analysis.

---

## Why Reproducibility Matters

**Validation**: Others can verify your findings are correct.

**Transparency**: Full methodology enables critical evaluation.

**Efficiency**: Future analysts can build on your work instead of starting from scratch.

**Trust**: Reproducible research demonstrates rigor and integrity.

**Compliance**: Many organizations and journals require reproducibility documentation.

---

## The Five Pillars of Reproducibility

### 1. Data Provenance
Document where data came from and how to access it.

### 2. Environment Specification
Record exact software versions and configuration.

### 3. Process Documentation
Step-by-step instructions for running analysis.

### 4. Validation Evidence
Demonstrate data quality and result verification.

### 5. Accessibility
Make materials available to those who need to reproduce.

---

## Complete Reproducibility Checklist

Use this checklist to ensure comprehensive reproducibility documentation:

### Data Sources

- [ ] **Database connection details** documented (host, database, schema, table)
- [ ] **Query timestamp** recorded (YYYY-MM-DD HH:MM:SS UTC)
- [ ] **Data period** specified (date range for temporal data)
- [ ] **Record counts** documented (rows examined, rows returned)
- [ ] **Schema information** included (column names, types, constraints)
- [ ] **Access instructions** provided (how to access the database)
- [ ] **Data freshness** noted (real-time, daily snapshot, archival)
- [ ] **File locations** specified for file-based data (full paths)
- [ ] **File checksums** computed (MD5/SHA256 for validation)
- [ ] **API versions** documented (for web service data)

### SQL Queries and Scripts

- [ ] **Full query text** included (in appendix or repository)
- [ ] **Execution time** recorded
- [ ] **Indexes used** documented
- [ ] **Query optimization** notes (if applicable)
- [ ] **Query file location** specified (repository path)
- [ ] **Explain plan** included (for complex queries)
- [ ] **Parameter values** documented (for parameterized queries)
- [ ] **Query purpose** explained (what each query does)
- [ ] **Data transformations** documented (aggregations, joins, filters)
- [ ] **Error handling** specified (how errors were managed)

### Analysis Environment

- [ ] **Tool name and version** (DataPeeker v2.1.0)
- [ ] **Programming language version** (Python 3.11.5, R 4.3.1)
- [ ] **Library versions** (pandas 2.1.0, plotext 5.2.8, etc.)
- [ ] **Operating system** (macOS 14.6.0, Ubuntu 22.04, etc.)
- [ ] **Hardware specifications** (if relevant for performance-sensitive code)
- [ ] **Environment variables** (configuration settings)
- [ ] **Virtual environment** (requirements.txt, conda environment.yml)
- [ ] **Docker image** (if containerized)
- [ ] **Package manager** (pip, conda, npm versions)
- [ ] **System dependencies** (database drivers, system libraries)

### Process Documentation

- [ ] **Step-by-step instructions** provided
- [ ] **Installation steps** documented
- [ ] **Configuration steps** explained
- [ ] **Execution commands** listed
- [ ] **Expected output** described
- [ ] **Execution time estimates** provided
- [ ] **Common errors** and solutions documented
- [ ] **Prerequisites** listed (required access, credentials)
- [ ] **Directory structure** explained
- [ ] **Input file locations** specified

### Data Quality

- [ ] **NULL value counts** and handling documented
- [ ] **Duplicate detection** methods and results
- [ ] **Outlier detection** methods and thresholds
- [ ] **Data validation** checks performed
- [ ] **Missing data** handling approach
- [ ] **Data cleaning** steps documented
- [ ] **Quality metrics** computed and reported
- [ ] **Assumptions** about data documented
- [ ] **Known limitations** acknowledged
- [ ] **Cross-validation** results (if performed)

### Artifacts and Outputs

- [ ] **Analysis scripts** version controlled
- [ ] **Generated visualizations** archived
- [ ] **Intermediate results** saved
- [ ] **Final reports** stored
- [ ] **Presentation materials** archived
- [ ] **Commit hash** recorded (git SHA)
- [ ] **Repository tag** created (version)
- [ ] **File organization** documented
- [ ] **Naming conventions** explained
- [ ] **Backup locations** specified

### Accessibility

- [ ] **Repository URL** provided
- [ ] **Clone instructions** documented
- [ ] **Access permissions** specified
- [ ] **Contact information** for questions
- [ ] **License** specified (MIT, Apache, proprietary)
- [ ] **Data sharing policy** clarified
- [ ] **Embargo period** noted (if applicable)
- [ ] **Citation format** suggested
- [ ] **DOI** obtained (if published)
- [ ] **Archive location** for long-term preservation

---

## Reproducibility Section Template

Include this section in your whitepaper or technical report:

```markdown
# Reproducibility Information

## Data Sources

### Primary Data: Production Sales Database

**Database Details**:
- **Host**: analytics-prod-db.example.com
- **Database**: analytics_prod
- **Schema**: public
- **Table**: sales_metrics
- **Access**: Read-only credentials required (contact: data-team@company.com)

**Data Characteristics**:
- **Query Timestamp**: 2025-11-25 14:30:00 UTC
- **Data Period**: 2024-10-01 to 2024-12-31
- **Records Examined**: 50,000 transactions
- **Data Freshness**: Real-time (replication lag <5 minutes)

**Schema**:
| Column            | Type      | Constraints      | Description                    |
|-------------------|-----------|------------------|--------------------------------|
| transaction_id    | INTEGER   | PRIMARY KEY      | Unique transaction identifier  |
| customer_id       | INTEGER   | NOT NULL, FK     | Customer identifier            |
| region            | VARCHAR   | NOT NULL         | Geographic region              |
| amount            | DECIMAL   | NOT NULL, >0     | Transaction amount (USD)       |
| transaction_date  | DATE      | NOT NULL         | Date of transaction            |

### Secondary Data: Customer Demographics

**File Details**:
- **Location**: `data/customer_demographics.csv`
- **Format**: CSV, UTF-8 encoding
- **Records**: 5,000 customers
- **Checksum**: SHA256: abc123...def456
- **Source**: Customer database snapshot (2024-12-31)

## SQL Queries

### Query 1: Regional Revenue Analysis

**Purpose**: Aggregate transaction data by region and month for Q4 2024.

**File**: `queries/q4_regional_revenue.sql`

**Execution Details**:
- **Runtime**: 2.3 seconds
- **Rows Examined**: 50,000
- **Rows Returned**: 18 (3 regions × 6 months)
- **Indexes Used**: date_region_idx, customer_id_idx

**Full Query**:
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

### Query 2: Customer Acquisition

**Purpose**: Identify new customers acquired during Q2-Q4 2024.

**File**: `queries/customer_acquisition.sql`

**Execution Details**:
- **Runtime**: 1.8 seconds
- **Rows Examined**: 50,000
- **Rows Returned**: 342 (new customers)

[Full query in Appendix B]

## Analysis Environment

### Software Versions

**Primary Tools**:
- **DataPeeker**: v2.1.0
- **Python**: 3.11.5
- **pandas**: 2.1.0
- **plotext**: 5.2.8
- **SQLAlchemy**: 2.0.20
- **psycopg2**: 2.9.7 (PostgreSQL driver)

**Operating System**:
- **OS**: macOS 14.6.0
- **Hardware**: Apple M2, 16GB RAM

**Development Environment**:
- **IDE**: VS Code v1.85.0
- **Shell**: zsh 5.9
- **Python Virtual Environment**: venv (Python 3.11.5)

### Installation Instructions

**1. Install Python and dependencies**:
\```bash
# Ensure Python 3.11+ is installed
python3 --version

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# OR: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
\```

**2. Install DataPeeker**:
\```bash
git clone https://github.com/example-org/datapeeker.git
cd datapeeker
pip install -e .
\```

**3. Configure database connection**:
\```bash
# Set environment variable
export DB_CONN="postgresql://user:password@analytics-prod-db.example.com/analytics_prod"

# Or create .env file
echo "DB_CONN=postgresql://user:password@host/database" > .env
\```

### Dependencies File (requirements.txt)

\```
pandas==2.1.0
plotext==5.2.8
sqlalchemy==2.0.20
psycopg2-binary==2.9.7
python-dotenv==1.0.0
\```

## Data Quality Assessment

### Completeness

**NULL Value Analysis**:
- **transaction_id**: 0 NULL values (0%)
- **customer_id**: 0 NULL values (0%)
- **region**: 0 NULL values (0%)
- **amount**: 0 NULL values (0%)
- **transaction_date**: 0 NULL values (0%)

**Conclusion**: All critical fields 100% complete.

### Consistency

**Duplicate Detection**:
- **Method**: Check for duplicate transaction_id
- **Query**: `SELECT transaction_id, COUNT(*) FROM sales_metrics GROUP BY transaction_id HAVING COUNT(*) > 1`
- **Result**: 0 duplicates found

**Date Validation**:
- **Expected Range**: 2024-10-01 to 2024-12-31
- **Actual Range**: 2024-10-01 to 2024-12-31
- **Out-of-range Records**: 0

**Amount Validation**:
- **Expected**: Positive decimal values
- **Actual Range**: $5.00 to $5,000.00
- **Invalid Values**: 0

### Outliers

**Method**: 3 MAD (Median Absolute Deviation)

**Formula**:
\```
outlier_score = |x - median(X)| / (MAD(X) * 1.4826)
Threshold: outlier_score > 3
\```

**Results**:
- **Outliers Detected**: 12 transactions (0.024%)
- **Outlier Values**: $4,500 - $5,000
- **Review**: All validated as legitimate high-value enterprise transactions

### Known Limitations

1. **Time Period**: Analysis covers Q4 2024 only. Full-year patterns not captured.
2. **Data Gaps**: Transactions from offline channels not included in database.
3. **Attribution**: Customer acquisition source not tracked in this dataset.
4. **Currency**: All amounts in USD. Multi-currency transactions converted at transaction date.

## Reproducibility Instructions

### Step 1: Clone Repository

\```bash
git clone https://github.com/example-org/q4-analysis.git
cd q4-analysis
\```

### Step 2: Check Out Analysis Version

\```bash
# Use specific commit for exact reproducibility
git checkout abc123def456

# Or use tagged version
git checkout v1.0.0
\```

### Step 3: Set Up Environment

\```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
\```

### Step 4: Configure Database Access

\```bash
# Request database credentials from data-team@company.com
# Add credentials to .env file
echo "DB_CONN=postgresql://user:password@host/database" > .env
\```

### Step 5: Run Analysis

\```bash
# Run main analysis script
python scripts/q4_regional_analysis.py

# Expected output: Analysis results in analysis/q4-2024/
\```

### Step 6: Generate Visualizations

\```bash
# Create charts
python scripts/create_visualizations.py

# Expected output: PNG files in analysis/q4-2024/visualizations/
\```

### Step 7: Generate Reports

\```bash
# Build presentation
cd analysis/q4-2024
marp presentation.md -o presentation.pdf

# Build whitepaper
pandoc whitepaper.md \
  --citeproc \
  --bibliography references.bib \
  --csl ieee.csl \
  -F pandoc-crossref \
  -s --toc --number-sections \
  -V geometry:margin=1in \
  -o whitepaper.pdf
\```

### Expected Runtime

- **Data Extraction**: ~5 seconds
- **Analysis Computation**: ~10 seconds
- **Visualization Generation**: ~15 seconds
- **Report Generation**: ~30 seconds
- **Total**: ~60 seconds

### Validation

**Verify outputs match expected results**:
\```bash
# Check output files exist
ls -l analysis/q4-2024/
# Expected: 01-findings.md, presentation.pdf, whitepaper.pdf

# Compare checksums (if provided)
sha256sum analysis/q4-2024/01-findings.md
# Expected: [checksum value]
\```

## Repository Information

**Repository URL**: https://github.com/example-org/q4-analysis

**Commit Hash**: abc123def456 (main branch)

**Tag**: v1.0.0 (Q4 2024 Analysis - Final)

**License**: MIT License

**Contact**: data-team@example.com for questions or access requests

## Data Archival

**Long-term Preservation**:
- **Primary**: GitHub repository (github.com/example-org/q4-analysis)
- **Secondary**: Company internal backup (backup.example.com/analysis/q4-2024/)
- **Tertiary**: Zenodo DOI (10.5281/zenodo.XXXXXX) for public data

**Retention Policy**: Maintained for 7 years per company policy

## Citation

If referencing this analysis, please cite as:

\```
Analytics Team (2025). West Coast Expansion Analysis: Q4 2024
Performance Evaluation. Tilmon Engineering.
https://github.com/example-org/q4-analysis
\```

**BibTeX**:
\```bibtex
@techreport{example_q4_analysis_2025,
  author = {{Analytics Team}},
  title = {West Coast Expansion Analysis: Q4 2024 Performance Evaluation},
  institution = {Tilmon Engineering},
  year = {2025},
  url = {https://github.com/example-org/q4-analysis},
  note = {Version 1.0.0. Commit: abc123def456}
}
\```
```

---

## Reproducibility Levels

### Level 1: Reviewable (Minimum)
- Full methodology documented
- SQL queries included in appendix
- Data sources cited
- Software versions listed

### Level 2: Repeatable (Standard)
- Code available in repository
- Dependencies specified
- Step-by-step instructions provided
- Expected outputs documented

### Level 3: Reproducible (Target)
- One-command execution
- Environment automated (Docker, conda)
- Validation checks included
- Outputs checksummed for verification

### Level 4: Replicable (Gold Standard)
- Data publicly accessible (or synthetic data provided)
- Automated testing pipeline
- DOI assigned for citation
- Long-term archival (Zenodo, institutional repository)

**Aim for Level 3 (Reproducible)** for internal analysis.
**Aim for Level 4 (Replicable)** for published research.

---

## Common Challenges and Solutions

### Challenge: Proprietary Data

**Solution**: Provide synthetic data with same structure
```python
# generate_synthetic_data.py
import pandas as pd
import numpy as np

np.random.seed(42)  # Reproducible randomness

# Generate synthetic transactions matching real schema
synthetic_data = pd.DataFrame({
    'transaction_id': range(1, 50001),
    'customer_id': np.random.randint(1, 5001, 50000),
    'region': np.random.choice(['West Coast', 'East Coast', 'Central'], 50000),
    'amount': np.random.lognormal(5, 1, 50000),
    'transaction_date': pd.date_range('2024-10-01', '2024-12-31', periods=50000)
})

synthetic_data.to_csv('data/synthetic_transactions.csv', index=False)
```

**Document in reproducibility section**:
```markdown
## Data Access Limitations

Original data is proprietary and cannot be shared. Synthetic dataset
provided (`data/synthetic_transactions.csv`) preserves statistical
properties (distributions, correlations) while protecting sensitive
information. Analysis code runs identically on synthetic data.
```

### Challenge: Large Data Files

**Solution**: Provide sample + instructions for full dataset
```markdown
## Large Dataset Access

**Sample Data**: `data/sample_transactions.csv` (1,000 records)
- Use for testing and development
- Sufficient for validating code

**Full Dataset**: 50,000 records (12MB compressed)
- Available via internal data warehouse
- Contact: data-team@company.com
- Access requires approved project code
```

### Challenge: Credentials and Secrets

**Solution**: Template configuration with instructions
```markdown
## Configuration

**Create `.env` file** (not in version control):
\```
DB_CONN=postgresql://user:password@host/database
API_KEY=your_api_key_here
\```

**Request credentials** from data-team@company.com

**Never commit** `.env` to repository (check `.gitignore`)
```

### Challenge: Complex Environment

**Solution**: Use Docker for containerization
```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "scripts/q4_regional_analysis.py"]
```

**Instructions**:
```bash
# Build container
docker build -t q4-analysis .

# Run analysis
docker run -v $(pwd)/analysis:/app/analysis q4-analysis
```

---

## Best Practices

### DO:

✅ **Use version control** (git) for all code and documentation

✅ **Pin dependency versions** (requirements.txt, environment.yml)

✅ **Document every SQL query** with purpose and execution details

✅ **Record timestamps** for all data queries

✅ **Include checksums** for data files

✅ **Provide step-by-step instructions** that assume no prior knowledge

✅ **Test reproducibility** on a fresh machine/environment

✅ **Archive final outputs** with version tags

✅ **Use random seeds** for any stochastic processes

✅ **Document known limitations** and caveats

### DON'T:

❌ **Hardcode credentials** in scripts

❌ **Rely on undocumented external dependencies**

❌ **Skip data quality checks and documentation**

❌ **Assume others have same system configuration**

❌ **Use relative paths without documentation**

❌ **Forget to document manual steps**

❌ **Skip testing on clean environment**

❌ **Omit error messages and troubleshooting**

---

## Reproducibility Testing

Before publishing, test reproducibility:

### 1. Clean Machine Test

```bash
# Set up new VM or use colleague's machine
# Follow ONLY your documentation
# No other knowledge allowed

# Document any steps missing from instructions
# Update documentation accordingly
```

### 2. Automated Validation

```python
# validate_outputs.py
import hashlib

def validate_output(file_path, expected_checksum):
    """Verify output matches expected result."""
    with open(file_path, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()

    if actual == expected_checksum:
        print(f"✓ {file_path} matches expected output")
        return True
    else:
        print(f"✗ {file_path} differs from expected")
        print(f"  Expected: {expected_checksum}")
        print(f"  Actual:   {actual}")
        return False

# Test key outputs
validate_output('analysis/01-findings.md', 'abc123...')
validate_output('visualizations/revenue-chart.png', 'def456...')
```

### 3. Peer Review

Ask colleague to:
- Clone repository
- Follow reproducibility instructions
- Report any missing steps or unclear instructions
- Verify outputs match

---

## Reproducibility Statement Template

Include in your publication:

```markdown
## Reproducibility Statement

This analysis was conducted following reproducible research principles.
All data sources, SQL queries, analysis code, and visualization scripts
are available in the public repository:

**Repository**: https://github.com/example-org/q4-analysis
**Version**: v1.0.0 (Commit: abc123def456)
**License**: MIT

Detailed reproducibility information is provided in Appendix A,
including:
- Data sources and query timestamps
- Complete SQL query text
- Software environment specification
- Step-by-step execution instructions
- Expected runtime and outputs
- Validation procedures

Original data is proprietary. Synthetic dataset with identical
statistical properties is provided for reproducibility testing.

Analysis was tested for reproducibility on macOS 14.6, Ubuntu 22.04,
and Windows 11 systems. All outputs matched expected checksums within
numerical precision limits (±0.01%).

Questions or issues: data-team@example.com
```

---

## References

**Reproducible Research Standards**:
- [FAIR Principles](https://www.go-fair.org/fair-principles/) - Findable, Accessible, Interoperable, Reusable
- [Reproducibility Guide](https://the-turing-way.netlify.app/reproducible-research/reproducible-research.html) - The Turing Way
- [Best Practices for Scientific Computing](https://doi.org/10.1371/journal.pbio.1001745)

**Related DataPeeker Skills**:
- `formats/citations.md` - Citing data sources
- `tools/pandoc.md` - Creating reproducible documents
- `SKILL.md` - Phase 4: Add Citations & Reproducibility
