---
description: Inventory autonomy branches with flexible sorting and grouping
allowed-tools: Skill
model: sonnet
argument-hint: "[optional-query]"
---

# List Branches

Display inventory of all autonomy branches with user-specified sorting, grouping, and information display.

You must invoke the `listing-branches` skill to perform the analysis.

Use the Skill tool:
```
skill: "autonomy:listing-branches"
args: "[optional-query]"
```

**Arguments:**
- `optional-query` - Free-text description of how to sort, group, and what information to display (e.g., "sort by most recent, group by status", "show branches updated in last 30 days with metrics")
- If no query provided, defaults to: sort by most recent update, show all branches

**The skill will:**
1. Parse user's query to understand desired sorting/grouping/information
2. Dispatch branch-analyzer agent to read git data
3. Agent generates Python script for computational analysis (never "eyeball it")
4. Produce formatted markdown table with requested information

**Example queries:**
```
/list-branches
/list-branches sort by most recent, show only active
/list-branches group by status, show metrics
/list-branches show branches updated in last 30 days
```

**Note:** This command only operates on `autonomy/*` branches. For general iteration review, use `/review-progress`.
