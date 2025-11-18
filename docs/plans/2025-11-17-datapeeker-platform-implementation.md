# DataPeeker Platform Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Build complete DataPeeker analytics platform with process-driven skills, testing infrastructure, and documentation

**Architecture:** Hybrid Workspace Architecture - analysis sessions create dated directories with numbered markdown files documenting the analytical journey

**Tech Stack:**
- Python 3.8+ for CSV import and utilities
- SQLite for data storage
- Just for command orchestration
- Claude Code Agent Skills for process guidance
- Git for version control and reproducibility

**Scope:** 8 phases from original design (complete platform)

**Codebase verified:** 2025-11-17 (blank repository with design document only)

---

## Phase 1: Foundation Setup

### Task 1: Create Directory Structure

**Files:**
- Create: `data/.gitkeep`
- Create: `analysis/.gitkeep`
- Create: `analysis/_template/.gitkeep`

**Step 1: Create directories with placeholder files**

```bash
mkdir -p data analysis/_template
touch data/.gitkeep analysis/.gitkeep analysis/_template/.gitkeep
```

**Step 2: Verify directory structure**

Run: `tree -L 2 -a`
Expected: Shows data/, analysis/, analysis/_template/ directories

**Step 3: Commit**

```bash
git add data/.gitkeep analysis/.gitkeep analysis/_template/.gitkeep
git commit -m "chore: create initial directory structure

- Add data/ for CSV files and SQLite database
- Add analysis/ for analysis session outputs
- Add analysis/_template/ for analysis templates"
```

### Task 2: Create Justfile with import-csvs Command

**Files:**
- Create: `Justfile`
- Create: `scripts/import_csvs.py`
- Create: `tests/test_import.py`

**Step 1: Write test script for import functionality**

Create: `tests/test_import.py`

```python
import sqlite3
import os
import pytest
from pathlib import Path

def test_import_creates_database():
    """Test that import creates analytics.db"""
    # Setup: ensure clean state
    db_path = Path("data/analytics.db")
    if db_path.exists():
        db_path.unlink()

    # Execute import (assuming we have a test CSV)
    import subprocess
    result = subprocess.run(["just", "import-csvs"], capture_output=True)

    # Verify database was created
    assert db_path.exists()

def test_import_creates_table_from_csv():
    """Test that CSV becomes a table"""
    # Setup: create test CSV
    test_csv = Path("data/test_sales.csv")
    test_csv.write_text("date,product,amount\n2025-01-01,Widget,100\n2025-01-02,Gadget,200")

    # Execute import
    import subprocess
    subprocess.run(["just", "import-csvs"])

    # Verify table exists with correct data
    conn = sqlite3.connect("data/analytics.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_sales'")
    assert cursor.fetchone() is not None

    cursor.execute("SELECT COUNT(*) FROM test_sales")
    assert cursor.fetchone()[0] == 2

    conn.close()
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_import.py -v`
Expected: FAIL - "just" command not found or import-csvs recipe doesn't exist

**Step 3: Write Justfile**

Create: `Justfile`

```makefile
# Import CSV files from data/ directory into SQLite database
import-csvs:
    python scripts/import_csvs.py

# Start a new analysis session
start-analysis PROCESS NAME:
    python scripts/start_analysis.py {{PROCESS}} {{NAME}}

# Test a skill with a specific scenario
test-skill PROCESS SCENARIO:
    python scripts/test_skill.py {{PROCESS}} {{SCENARIO}}
```

**Step 4: Write minimal import script**

Create: `scripts/import_csvs.py`

```python
#!/usr/bin/env python3
import sqlite3
import csv
import sys
from pathlib import Path
from typing import List, Dict

def infer_type(value: str) -> str:
    """Infer SQLite type from string value"""
    try:
        int(value)
        return "INTEGER"
    except ValueError:
        pass

    try:
        float(value)
        return "REAL"
    except ValueError:
        pass

    return "TEXT"

def create_table_from_csv(csv_path: Path, conn: sqlite3.Connection) -> None:
    """Create SQLite table from CSV file"""
    table_name = csv_path.stem

    with open(csv_path, 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        if not rows:
            print(f"Skipping empty file: {csv_path}")
            return

        # Infer column types from first few rows
        headers = list(rows[0].keys())
        sample_size = min(10, len(rows))
        column_types = {}

        for header in headers:
            types_seen = set()
            for row in rows[:sample_size]:
                if row[header]:  # Skip empty values
                    types_seen.add(infer_type(row[header]))

            # Use most specific type, default to TEXT
            if "TEXT" in types_seen:
                column_types[header] = "TEXT"
            elif "REAL" in types_seen:
                column_types[header] = "REAL"
            elif "INTEGER" in types_seen:
                column_types[header] = "INTEGER"
            else:
                column_types[header] = "TEXT"

        # Create table
        cursor = conn.cursor()

        # Drop existing table if it exists
        cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

        columns_def = ", ".join([f"{col} {column_types[col]}" for col in headers])
        cursor.execute(f"CREATE TABLE {table_name} ({columns_def})")

        # Insert data
        placeholders = ", ".join(["?" for _ in headers])
        insert_sql = f"INSERT INTO {table_name} VALUES ({placeholders})"

        for row in rows:
            values = [row[header] for header in headers]
            cursor.execute(insert_sql, values)

        conn.commit()
        print(f"✓ Imported {csv_path.name} → {table_name} ({len(rows)} rows)")

def main():
    data_dir = Path("data")
    db_path = data_dir / "analytics.db"

    # Find all CSV files
    csv_files = list(data_dir.glob("*.csv"))

    if not csv_files:
        print("No CSV files found in data/ directory")
        return

    # Create/connect to database
    conn = sqlite3.connect(db_path)

    try:
        for csv_file in csv_files:
            try:
                create_table_from_csv(csv_file, conn)
            except Exception as e:
                print(f"✗ Error importing {csv_file.name}: {e}", file=sys.stderr)
                with open(data_dir / "import.log", "a") as log:
                    log.write(f"{csv_file.name}: {e}\n")

        print(f"\nDatabase created at: {db_path}")
        print(f"Tables: {len(csv_files)}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
```

**Step 5: Run test to verify it passes**

Run: `pytest tests/test_import.py -v`
Expected: PASS - both tests pass

**Step 6: Commit**

```bash
git add Justfile scripts/import_csvs.py tests/test_import.py
git commit -m "feat: add CSV to SQLite import functionality

- Add Justfile with import-csvs command
- Implement CSV importer with type inference
- Add tests for import functionality
- Log errors to data/import.log"
```

### Task 3: Create start-analysis Command

**Files:**
- Create: `scripts/start_analysis.py`
- Create: `tests/test_start_analysis.py`

**Step 1: Write test for start-analysis**

Create: `tests/test_start_analysis.py`

```python
import subprocess
from pathlib import Path
from datetime import datetime
import shutil

def test_start_analysis_creates_directory():
    """Test that start-analysis creates correct directory structure"""
    # Setup: clean any existing test analysis
    test_dir = Path("analysis/hypothesis-testing")
    if test_dir.exists():
        shutil.rmtree(test_dir)

    # Execute
    result = subprocess.run(
        ["just", "start-analysis", "hypothesis-testing", "test-analysis"],
        capture_output=True,
        text=True
    )

    # Verify directory created with date
    today = datetime.now().strftime("%Y-%m-%d")
    expected_dir = Path(f"analysis/hypothesis-testing/{today}-test-analysis")
    assert expected_dir.exists()

    # Verify template was copied
    assert (expected_dir / ".gitkeep").exists()  # Will be replaced with actual template files later

def test_start_analysis_prevents_duplicates():
    """Test that start-analysis handles existing directories"""
    # Create an existing analysis directory
    today = datetime.now().strftime("%Y-%m-%d")
    existing_dir = Path(f"analysis/hypothesis-testing/{today}-duplicate-test")
    existing_dir.mkdir(parents=True, exist_ok=True)

    # Execute - should prompt or error
    result = subprocess.run(
        ["just", "start-analysis", "hypothesis-testing", "duplicate-test"],
        capture_output=True,
        text=True,
        input="n\n"  # Answer 'no' to overwrite prompt
    )

    # Verify it didn't silently overwrite
    assert "already exists" in result.stdout or result.returncode != 0
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_start_analysis.py -v`
Expected: FAIL - script doesn't exist

**Step 3: Write start-analysis script**

Create: `scripts/start_analysis.py`

```python
#!/usr/bin/env python3
import sys
import shutil
from pathlib import Path
from datetime import datetime

def main():
    if len(sys.argv) != 3:
        print("Usage: start-analysis <process> <name>")
        sys.exit(1)

    process = sys.argv[1]
    name = sys.argv[2]

    # Create dated directory name
    today = datetime.now().strftime("%Y-%m-%d")
    analysis_dir = Path(f"analysis/{process}/{today}-{name}")

    # Check if directory already exists
    if analysis_dir.exists():
        response = input(f"Directory {analysis_dir} already exists. Overwrite? (y/n): ")
        if response.lower() != 'y':
            print("Cancelled.")
            sys.exit(0)
        shutil.rmtree(analysis_dir)

    # Create directory
    analysis_dir.mkdir(parents=True, exist_ok=True)

    # Copy template
    template_dir = Path("analysis/_template")
    if template_dir.exists():
        for item in template_dir.iterdir():
            if item.is_file():
                shutil.copy(item, analysis_dir)
            elif item.is_dir():
                shutil.copytree(item, analysis_dir / item.name)

    print(f"✓ Analysis workspace created at: {analysis_dir}")
    print(f"\nNext steps:")
    print(f"1. Invoke the {process} skill with your analytical goal")
    print(f"2. Claude will guide you through the analysis process")

if __name__ == "__main__":
    main()
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/test_start_analysis.py -v`
Expected: PASS

**Step 5: Commit**

```bash
git add scripts/start_analysis.py tests/test_start_analysis.py
git commit -m "feat: add start-analysis command

- Create dated analysis directories
- Copy template to new analysis workspace
- Prevent accidental overwrites with confirmation prompt"
```

---


## Phase 2: Template Infrastructure

### Task 1: Create Analysis Template README

**Files:**
- Create: `analysis/_template/README.md`
- Create: `analysis/_template/00 - overview.md`
- Create: `tests/test_template.py`

**Step 1: Write test for template structure**

Create: `tests/test_template.py`

```python
from pathlib import Path

def test_template_has_readme():
    """Test that template contains README"""
    readme = Path("analysis/_template/README.md")
    assert readme.exists()
    
    content = readme.read_text()
    assert "Analysis Session" in content
    assert "Data Sources" in content

def test_template_has_metadata():
    """Test that template includes metadata file"""
    metadata = Path("analysis/_template/00 - overview.md")
    assert metadata.exists()
    
    content = metadata.read_text()
    assert "# Analysis Overview" in content
    assert "## Analytical Goal" in content
```

**Step 2: Run test to verify it fails**

Run: `pytest tests/test_template.py -v`

**Step 3: Create template files**

Create: `analysis/_template/README.md` with structure explanation
Create: `analysis/_template/00 - overview.md` with standard sections

**Step 4: Run test to verify it passes**

**Step 5: Commit**

```bash
git add analysis/_template/*.md tests/test_template.py
git commit -m "feat: add analysis template infrastructure"
```

### Task 2: Create Query Template Helper

**Files:**
- Create: `analysis/_template/.query-template.md`

**Steps:**
1. Write test for query template existence
2. Create query template with sections: Rationale, Query, Results, Interpretation
3. Verify test passes
4. Commit

### Task 3: Update start-analysis Tests

**Files:**
- Modify: `tests/test_start_analysis.py`

**Steps:**
1. Update test to verify template files are copied (README, overview, query-template)
2. Run test to verify it passes
3. Commit

---

## Phase 3: First Process Skill (Hypothesis Testing)

### Task 1: Create Skill Directory Structure

**Files:**
- Create: `.claude/skills/datapeeker/processes/.gitkeep`
- Create: `.claude/skills/datapeeker/components/.gitkeep`

**Steps:**
1. Create directory structure
2. Verify with tree command
3. Commit

### Task 2: Write Hypothesis Testing Skill

**Files:**
- Create: `.claude/skills/datapeeker/processes/hypothesis-testing.md`

**Key Sections:**
- YAML frontmatter with name/description
- Overview and prerequisites
- 5-phase process with TodoWrite tracking:
  - Phase 1: Hypothesis Formulation (H0/H1)
  - Phase 2: Test Design (before looking at data)
  - Phase 3: Data Analysis (execute queries)
  - Phase 4: Result Interpretation (consider confounds)
  - Phase 5: Conclusion and Follow-up
- Checkpoints at each phase
- SQL examples for day-of-week analysis
- Common Rationalizations section

**Steps:**
1. Write complete skill file following approved structure
2. Verify skill file exists and has proper format
3. Commit with descriptive message

---

## Phase 4: Component Skills

### Task 1: Create Understanding-Data Component Skill

**Files:**
- Create: `.claude/skills/datapeeker/components/understanding-data.md`

**Key Content:**
- 4-phase data profiling checklist with TodoWrite
- Schema exploration queries
- Data quality assessment patterns
- Distribution analysis SQL
- Relationship identification

**Steps:**
1. Write skill file
2. Commit

### Task 2: Create Writing-Queries Component Skill

**Files:**
- Create: `.claude/skills/datapeeker/components/writing-queries.md`

**Key Content:**
- Query development process (clarify → design → write → verify → document)
- SQL best practices and anti-patterns
- Common query patterns (segmentation, time series, comparison, ranking)
- Documentation requirements

**Steps:**
1. Write skill file
2. Commit

### Task 3: Create Interpreting-Results Component Skill

**Files:**
- Create: `.claude/skills/datapeeker/components/interpreting-results.md`

**Key Content:**
- 6-step interpretation framework
- Context consideration
- Pattern identification
- Alternative explanations
- Significance assessment
- Conclusions with caveats

**Steps:**
1. Write skill file
2. Commit

### Task 4: Create Creating-Visualizations Component Skill

**Files:**
- Create: `.claude/skills/datapeeker/components/creating-visualizations.md`

**Key Content:**
- Text-based visualization formats (markdown tables, ASCII bars, sparklines, histograms)
- Decision tree for visualization selection
- Best practices for annotation and context

**Steps:**
1. Write skill file
2. Commit

---

## Phase 5: Additional Process Skills

### Task 1: Create Guided-Investigation Process Skill

**Files:**
- Create: `.claude/skills/datapeeker/processes/guided-investigation.md`

**Key Sections:**
- 5-phase process with TodoWrite:
  - Phase 1: Question Decomposition
  - Phase 2: Data Discovery
  - Phase 3: Systematic Investigation (one file per sub-question)
  - Phase 4: Synthesis
  - Phase 5: Conclusions and Recommendations
- Sub-question mapping to data
- Incremental investigation pattern

**Steps:**
1. Write skill file
2. Commit

### Task 2: Create Exploratory-Analysis Process Skill

**Files:**
- Create: `.claude/skills/datapeeker/processes/exploratory-analysis.md`

**Key Sections:**
- 5-phase process:
  - Phase 1: Data Familiarization
  - Phase 2: Pattern Discovery (time, segmentation, relationships)
  - Phase 3: Anomaly Investigation
  - Phase 4: Insight Generation
  - Phase 5: Question Formulation
- Exploration vectors and SQL patterns
- Insight criteria (actionable, surprising, meaningful)

**Steps:**
1. Write skill file
2. Commit

### Task 3: Create Comparative-Analysis Process Skill

**Files:**
- Create: `.claude/skills/datapeeker/processes/comparative-analysis.md`

**Key Sections:**
- 5-phase process:
  - Phase 1: Define Comparison
  - Phase 2: Segment Definition
  - Phase 3: Metric Comparison
  - Phase 4: Difference Explanation
  - Phase 5: Conclusions and Recommendations
- Fair comparison principles
- Multi-metric analysis patterns
- Confound analysis

**Steps:**
1. Write skill file
2. Commit

---

## Phase 6: Testing Infrastructure

### Task 1: Create Test Case Directory Structure

**Files:**
- Create test directories for each process/scenario combination

**Steps:**
1. Create directory structure: `tests/test-cases/<process>/<scenario>/data/`
2. Verify structure with tree
3. Commit

### Task 2: Create First Test Case (Hypothesis Testing / Retail Seasonality)

**Files:**
- Create: `tests/test-cases/hypothesis-testing/retail-seasonality/prompt.md`
- Create: `tests/test-cases/hypothesis-testing/retail-seasonality/expected-behavior.md`
- Create: `tests/test-cases/hypothesis-testing/retail-seasonality/known-failures.md`
- Add: `tests/test-cases/hypothesis-testing/retail-seasonality/data/*.csv` (from Maven Analytics)

**Content:**
- `prompt.md`: Setup instructions and user prompt
- `expected-behavior.md`: What correct execution looks like for each phase
- `known-failures.md`: Common failure modes to watch for

**Steps:**
1. Create test case files
2. Document Maven Analytics dataset to use
3. Commit

### Task 3: Create Remaining Test Cases (Stub Files)

**Files:**
- Create stub test cases for:
  - `guided-investigation/customer-churn`
  - `exploratory-analysis/new-dataset`
  - `comparative-analysis/segment-performance`

**Steps:**
1. Create directory structures
2. Add stub prompt/expected/failures files
3. Commit with note that full implementation happens in Phase 8

### Task 4: Create test-skill Command

**Files:**
- Create: `scripts/test_skill.py`

**Functionality:**
- List available test cases
- Copy test data to data/
- Run import-csvs
- Display prompt, expected behavior, known failures
- Guide user through testing process

**Steps:**
1. Write test_skill.py script
2. Verify Justfile has test-skill command
3. Test the command
4. Commit

---

## Phase 7: Documentation & Examples

### Task 1: Create Comprehensive README

**Files:**
- Create: `README.md`

**Sections:**
- What is DataPeeker?
- Quick Start (prerequisites, installation, first analysis)
- Available Processes (descriptions of each)
- Directory Structure
- Commands reference
- Example Analyses
- Best Practices
- Creating Custom Skills
- Testing Skills
- Philosophy
- License

**Steps:**
1. Write complete README
2. Commit

### Task 2: Create Writing Custom Skills Guide

**Files:**
- Create: `docs/writing-new-skills.md`

**Sections:**
- When to create a custom skill
- Skill anatomy
- Design principles (explicit phases, TodoWrite, numbered files, checkpoints, SQL guidance)
- Complete example: funnel-analysis skill
- Testing your skill
- Best practices
- Skill lifecycle
- Contributing skills

**Steps:**
1. Write complete guide
2. Commit

### Task 3: Create Example Analyses (Stub Directories)

**Files:**
- Create: `examples/hypothesis-testing-example/README.md`
- Create: `examples/guided-investigation-example/README.md`
- Create: `examples/exploratory-analysis-example/README.md`
- Create: `examples/comparative-analysis-example/README.md`

**Content:**
- Stub READMEs noting that full examples will be created in Phase 8

**Steps:**
1. Create example directories
2. Add stub READMEs
3. Commit

---

## Phase 8: Validation & Refinement

### Task 1: Complete Test Case Data

**Files:**
- Add: `tests/test-cases/DATA_SOURCES.md`
- Add: CSV files from Maven Analytics to all test cases
- Complete: All `expected-behavior.md` and `known-failures.md` files

**Steps:**
1. Document which Maven Analytics datasets to use for each test case
2. Download and add datasets
3. Complete expected-behavior.md for all scenarios
4. Complete known-failures.md for all scenarios
5. Commit

### Task 2: Test Hypothesis-Testing Skill

**Files:**
- May modify: `.claude/skills/datapeeker/processes/hypothesis-testing.md`
- Create: `tests/test-cases/hypothesis-testing/retail-seasonality/test-results.md`

**Process:**
1. Run `just test-skill hypothesis-testing retail-seasonality`
2. Use `testing-skills-with-subagents` skill to validate with subagent
3. Document test results (passes/failures)
4. Update skill based on observed failures
5. Re-test until test passes
6. Commit skill updates

### Task 3: Test Remaining Process Skills

**For each skill:**
- guided-investigation
- exploratory-analysis
- comparative-analysis

**Process:**
1. Run test case with subagent
2. Document failures
3. Update skill to address failures
4. Re-test until pass
5. Commit each skill after validation

### Task 4: Create Example Analyses from Test Runs

**Files:**
- Copy successful analysis outputs to examples directories
- Add explanatory READMEs for each example

**Process:**
1. After successful test run, copy analysis directory to examples/
2. Add README explaining what the example demonstrates
3. Highlight key learnings
4. Commit examples

### Task 5: Document Known Limitations

**Files:**
- Create: `docs/limitations.md`

**Sections:**
- Platform limitations (data size, types, joins)
- Skill limitations (statistical tests, visualizations)
- Testing limitations
- Process limitations
- How to report issues

**Steps:**
1. Write limitations document
2. Commit

### Task 6: Final Validation

**Process:**
1. End-to-end test following README from scratch
2. Document and fix any README issues
3. Final README polish
4. Commit

### Task 7: Final Git Housekeeping

**Files:**
- Create: `.gitignore`
- Create: `LICENSE`

**Content:**
- `.gitignore`: Ignore generated databases, caches, work-in-progress analyses
- `LICENSE`: Your chosen license

**Steps:**
1. Create .gitignore
2. Add license
3. Commit

---

## Execution Notes

**Test-Driven Development:**
- Every phase follows RED-GREEN-REFACTOR
- Write tests first, see them fail, then implement

**Skills Quality:**
- Phase 8 validation is critical
- Use `testing-skills-with-subagents` to find loopholes
- Iterate until skills are bulletproof

**Maven Analytics Data:**
- Phase 6 note updated: Test cases use real datasets from Maven Analytics Data Playground
- Document exact datasets and download URLs in DATA_SOURCES.md

**Git Workflow:**
- Commit after each task
- Clear, descriptive commit messages
- Analysis directories are git-committable artifacts

