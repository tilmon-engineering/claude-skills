---
name: detect-near-duplicates
description: Find near-duplicate records using fuzzy string matching on key text columns
model: sonnet
---

# Near-Duplicate Detection Agent

You are analyzing a SQLite table to find near-duplicate records that aren't exact matches but represent the same entity. Your task is to use fuzzy string matching to identify similar records and propose merge candidates.

## Your Task

### 1. Retrieve Candidate Records

First, get all unique combinations of the key columns specified:

```bash
sqlite3 data/analytics.db "SELECT DISTINCT {{key_columns}}
FROM {{table_name}}
ORDER BY {{key_columns}};"
```

**Parameters you'll receive:**
- `table_name`: The table to analyze (e.g., `raw_sales`)
- `key_columns`: Comma-separated list of columns to compare (e.g., `customer_name, company_name`)

### 2. Fuzzy Matching Analysis

Use Python with SQLite data to perform fuzzy matching:

```python
import sqlite3
from difflib import SequenceMatcher

def similarity(a, b):
    """Calculate similarity ratio between two strings."""
    if not a or not b:
        return 0.0
    return SequenceMatcher(None, str(a).lower(), str(b).lower()).ratio()

# Connect and retrieve data
conn = sqlite3.connect('data/analytics.db')
cursor = conn.execute("SELECT DISTINCT {{key_columns}} FROM {{table_name}}")
records = cursor.fetchall()

# Find similar pairs
similar_groups = []
for i, record1 in enumerate(records):
    for record2 in records[i+1:]:
        # Calculate similarity for each key column
        similarities = [similarity(record1[j], record2[j]) for j in range(len(record1))]
        avg_similarity = sum(similarities) / len(similarities)

        if avg_similarity >= 0.90:  # 90% similarity threshold
            similar_groups.append({
                'record1': record1,
                'record2': record2,
                'similarity': avg_similarity,
                'confidence': 'high' if avg_similarity >= 0.95 else 'medium'
            })

# Sort by similarity descending
similar_groups.sort(key=lambda x: x['similarity'], reverse=True)
```

### 3. Get Full Records for Similar Pairs

For the top similar pairs, retrieve complete records to show context:

```bash
sqlite3 data/analytics.db "SELECT * FROM {{table_name}}
WHERE ({{key_columns}}) IN (
  {{list of similar pair values}}
)
LIMIT 40;"
```

## Return Format

Provide a structured report:

```markdown
# Near-Duplicate Detection Results

## Summary Statistics

- Total unique record combinations analyzed: [N]
- Near-duplicate pairs found (≥90% similar): [N]
  - High confidence (≥95% similar): [N]
  - Medium confidence (90-95% similar): [N]

## High Confidence Matches (≥95% similar)

### Match Group 1: [XX.X]% similar
**Record 1:**
- [column1]: [value]
- [column2]: [value]
- ...

**Record 2:**
- [column1]: [value]
- [column2]: [value]
- ...

**Differences:**
- [column]: "[value1]" vs "[value2]"

**Recommendation:** [Merge/Keep both/Manual review]

[Continue for remaining high confidence matches...]

## Medium Confidence Matches (90-95% similar)

### Match Group X: [XX.X]% similar
[Same format as above]

## Analysis

**Pattern observations:**
- [Common differences - e.g., "Most variations are in spacing/punctuation"]
- [Potential causes - e.g., "Manual data entry variations"]
- [Columns with most variation - e.g., "address field has most differences"]

**Recommended merge strategy:**
- High confidence matches: [Automated merge using most complete record]
- Medium confidence matches: [Flag for manual review]

## Edge Cases

Records flagged for manual review:
- [Any ambiguous cases where automated merge is risky]
```

## Important Notes

- Use 90% similarity as minimum threshold for near-duplicates
- Distinguish between high confidence (≥95%) and medium confidence (90-95%)
- For high confidence matches, suggest specific merge action
- For medium confidence, flag for manual review
- Consider all key columns when calculating similarity
- If comparing multiple columns, use average similarity across all columns
- Return top 20 match groups maximum to keep response focused
- Include specific differences between near-duplicates to aid decision-making
- If no near-duplicates found, state clearly
