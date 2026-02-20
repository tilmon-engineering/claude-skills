# Import CSV files from data/ directory into SQLite database
import-csvs:
    #!/usr/bin/env bash
    set -euo pipefail
    for csv in data/*.csv; do
        [ -e "$csv" ] || continue
        table=$(basename "$csv" .csv)
        sqlite3 data/analytics.db ".mode csv" ".import \"$csv\" \"$table\""
        echo "✓ Imported $(basename "$csv") → $table"
    done
    echo ""
    echo "Database: data/analytics.db"


