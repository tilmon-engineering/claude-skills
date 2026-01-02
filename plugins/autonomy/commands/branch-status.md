---
description: Detailed status report for single autonomy branch
allowed-tools: Skill
model: sonnet
argument-hint: "<branch-name>"
---

# Branch Status

Provide comprehensive status report for a single autonomy branch showing complete iteration history, metrics progression, and current state.

You must invoke the `analyzing-branch-status` skill to perform the analysis.

Use the Skill tool:
```
skill: "autonomy:analyzing-branch-status"
args: "<branch-name>"
```

**Arguments:**
- `branch-name` (required) - Branch name to analyze. `autonomy/` prefix optional (will be added automatically if missing).

**The skill will:**
1. Normalize branch name (add `autonomy/` prefix if missing)
2. Validate branch exists
3. Dispatch branch-analyzer agent to read all commits on branch
4. Agent generates Python script to analyze iteration timeline, metrics progression, status changes
5. Produce comprehensive report with:
   - Complete iteration list with dates and status
   - Metrics over time (if applicable)
   - Blocker history
   - Current state and recommendations

**Example usage:**
```
/branch-status experiment-a
/branch-status autonomy/experiment-b
```

**Output includes:**
- Iteration timeline (all iterations from first to latest)
- Status changes over time
- Metrics progression
- Blocker history
- Current state assessment
- Recommended next actions

**Note:** This command only operates on `autonomy/*` branches. For general iteration review on current branch, use `/review-progress`.
