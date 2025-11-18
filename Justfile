# Import CSV files from data/ directory into SQLite database
import-csvs:
    python scripts/import_csvs.py

# Start a new analysis session
start-analysis PROCESS NAME:
    python scripts/start_analysis.py {{PROCESS}} {{NAME}}

# Test a skill with a specific scenario
test-skill PROCESS SCENARIO:
    python scripts/test_skill.py {{PROCESS}} {{SCENARIO}}
