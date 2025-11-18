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

def test_import_preserves_data_values():
    """Test that numeric and text data values are preserved correctly"""
    # Setup: create CSV with various data types
    test_csv = Path("data/test_data_types.csv")
    test_csv.write_text("product,price,quantity,description\nWidget,99.99,5,Premium widget\nGadget,149.50,3,Deluxe gadget")

    # Execute import
    subprocess.run(["just", "import-csvs"])

    # Verify data values are preserved correctly
    conn = sqlite3.connect("data/analytics.db")
    cursor = conn.cursor()

    cursor.execute("SELECT product, price, quantity, description FROM test_data_types WHERE product='Widget'")
    row = cursor.fetchone()
    assert row is not None, "Widget row should exist"
    assert row[0] == "Widget", "Product name should be preserved"
    assert row[1] == "99.99", "Price should be preserved as 99.99"
    assert row[2] == "5", "Quantity should be preserved"
    assert row[3] == "Premium widget", "Description should be preserved"

    conn.close()

    # Cleanup
    if test_csv.exists():
        test_csv.unlink()

def test_import_with_no_csvs():
    """Test that import handles empty CSV directory gracefully"""
    # Setup: ensure no test CSV files exist
    data_dir = Path("data")
    test_csvs = list(data_dir.glob("test_*.csv"))
    for csv in test_csvs:
        csv.unlink()

    # Execute import (should complete without error even with no CSVs)
    result = subprocess.run(["just", "import-csvs"], capture_output=True, text=True)

    # Verify it completes successfully
    assert result.returncode == 0, "Import should succeed even with no CSV files"
