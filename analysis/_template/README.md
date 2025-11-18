# Analysis Session

This directory contains a complete analytical investigation session using DataPeeker.

## Directory Structure

```
<analysis-name>/
├── README.md                    # This file - session overview
├── 00 - overview.md            # Analytical goal and metadata
├── 01 - query.md               # First query and results
├── 02 - query.md               # Second query and results
└── ...                         # Additional queries as needed
```

## Numbered File Workflow

Each analysis query is documented in a numbered markdown file (01, 02, 03, etc.) that includes:

1. **Rationale** - Why are we running this query?
2. **Query** - The SQL code (formatted in code blocks)
3. **Results** - Output from the query (tables, counts, values)
4. **Interpretation** - What do these results mean?

This creates a **linear, reproducible narrative** of your analytical journey.

## Data Sources

All queries run against the SQLite database at `data/analytics.db`.

To see available tables and schemas:

```sql
-- List all tables
SELECT name FROM sqlite_master WHERE type='table';

-- Show schema for a table
PRAGMA table_info(table_name);
```

## Session Metadata

See `00 - overview.md` for:
- Analytical goal
- Business context
- Data sources used
- Timeline
- Key findings summary

## Best Practices

1. **One file per query** - Keep each investigation step separate
2. **Sequential numbering** - Follow the chronological order (01, 02, 03...)
3. **Document reasoning** - Always explain WHY before running a query
4. **Include context** - Raw numbers need interpretation
5. **Update overview** - Keep the overview file current as analysis progresses

## Process Skills

DataPeeker provides Claude Code Agent Skills for different analytical processes:

- **hypothesis-testing** - Test specific claims with statistical rigor
- **guided-investigation** - Answer complex questions systematically
- **exploratory-analysis** - Discover patterns in new datasets
- **comparative-analysis** - Compare segments or time periods

Each skill provides a structured workflow with checkpoints and guidance.
