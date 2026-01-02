---
description: Compare two autonomy branches to show different approaches and outcomes
allowed-tools: Skill
model: sonnet
argument-hint: "<branch-a> <branch-b>"
---

# Compare Branches

Compare two autonomy branches to show differences in approaches, iterations, metrics, and outcomes.

You must invoke the `comparing-branches` skill to perform the comparison.

Use the Skill tool:
```
skill: "autonomy:comparing-branches"
args: "<branch-a> <branch-b>"
```

**Arguments:**
- `branch-a` (required) - First branch name. `autonomy/` prefix optional.
- `branch-b` (required) - Second branch name. `autonomy/` prefix optional.

**The skill will:**
1. Normalize both branch names (add `autonomy/` prefix if missing)
2. Validate both branches exist
3. Use `git merge-base` to find where branches diverged
4. Dispatch branch-analyzer agent to compare approaches
5. Agent generates Python script for comparative analysis
6. Produce report showing:
   - Where branches diverged
   - Iteration counts on each branch since divergence
   - Comparative metrics (if applicable)
   - Different approaches taken
   - Outcomes on each branch

**Example usage:**
```
/compare-branches experiment-a experiment-b
/compare-branches autonomy/usage-pricing autonomy/flat-enterprise
```

**Output includes:**
- Divergence point (common ancestor)
- Iteration timeline comparison
- Metrics trajectories (if applicable)
- Status comparison
- Different decisions made
- Outcomes on each branch
- Insights and recommendations

**Note:** This command only operates on `autonomy/*` branches.
