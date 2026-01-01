# Schema Design: [dataset_name]

## Objective
Design SQLite schema for importing [CSV_filename] based on data profiling from Phase 1.

## Column Type Analysis

### [Column 1 Name]
- **Sample values:** [examples from 01-csv-profile.md]
- **Proposed type:** [INTEGER|REAL|TEXT]
- **Rationale:** [Why this type - reference inference rules above]
- **NULL handling:** [How NULL values will be handled]

### [Column 2 Name]
- **Sample values:** [examples]
- **Proposed type:** [INTEGER|REAL|TEXT]
- **Rationale:** [Explanation]
- **NULL handling:** [Approach]

[Continue for all columns...]

## NULL Representation Mapping

| CSV Representation | SQLite Value | Count in Sample |
|--------------------|--------------|-----------------|
| (empty cell)       | NULL         | [count]         |
| "N/A"              | NULL         | [count]         |
| [others]           | NULL         | [count]         |

## Proposed Schema

```sql
CREATE TABLE raw_[table_name] (
  [column_1] [TYPE],  -- [Rationale]
  [column_2] [TYPE],  -- [Rationale]
  ...
);
```

## User Confirmation

- **Proposed table name:** `raw_[name]`
- **Total columns:** [count]
- **User approval:** [Date/time of approval]
- **Modifications requested:** [None / List of changes made]

## Next Steps
Proceed to Phase 3: Basic Standardization
