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
