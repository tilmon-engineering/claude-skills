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
