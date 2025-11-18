import sqlite3
import subprocess
from pathlib import Path

def test_import_creates_database():
    """Test that import creates analytics.db"""
    # Setup: ensure clean state
    db_path = Path("data/analytics.db")
    if db_path.exists():
        db_path.unlink()

    # Create test CSV for this test to be independent
    test_csv = Path("data/test_db_creation.csv")
    test_csv.write_text("id,name\n1,Test\n2,Data")

    # Execute import
    result = subprocess.run(["just", "import-csvs"], capture_output=True)

    # Verify database was created
    assert db_path.exists(), "Database should be created"

    # Cleanup
    if test_csv.exists():
        test_csv.unlink()

def test_import_creates_table_from_csv():
    """Test that CSV becomes a table"""
    # Setup: create test CSV
    test_csv = Path("data/test_sales.csv")
    test_csv.write_text("date,product,amount\n2025-01-01,Widget,100\n2025-01-02,Gadget,200")

    # Execute import
    subprocess.run(["just", "import-csvs"])

    # Verify table exists with correct data
    conn = sqlite3.connect("data/analytics.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_sales'")
    assert cursor.fetchone() is not None, "Table test_sales should exist"

    cursor.execute("SELECT COUNT(*) FROM test_sales")
    assert cursor.fetchone()[0] == 2, "Table should have 2 rows"

    conn.close()

    # Cleanup
    if test_csv.exists():
        test_csv.unlink()

def test_import_handles_multiple_csvs():
    """Test that multiple CSV files are all imported"""
    # Setup: create multiple test CSVs
    test_csv1 = Path("data/test_products.csv")
    test_csv1.write_text("id,name\n1,Widget\n2,Gadget")

    test_csv2 = Path("data/test_orders.csv")
    test_csv2.write_text("order_id,total\n100,250\n101,150")

    # Execute import
    subprocess.run(["just", "import-csvs"])

    # Verify both tables exist
    conn = sqlite3.connect("data/analytics.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_products'")
    assert cursor.fetchone() is not None, "Table test_products should exist"

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_orders'")
    assert cursor.fetchone() is not None, "Table test_orders should exist"

    conn.close()

    # Cleanup
    if test_csv1.exists():
        test_csv1.unlink()
    if test_csv2.exists():
        test_csv2.unlink()
