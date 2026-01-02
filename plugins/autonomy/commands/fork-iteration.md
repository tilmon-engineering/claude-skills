---
description: Create new autonomy branch forked from current commit or specific iteration
allowed-tools: Skill, AskUserQuestion, Bash
model: sonnet
argument-hint: "[iteration] <strategy-name>"
---

# Fork Iteration

Create a new autonomy branch forked from current commit or any iteration tag in git history.

You must invoke the `forking-iteration` skill to perform the fork.

Use the Skill tool:
```
skill: "autonomy:forking-iteration"
args: "[iteration] <strategy-name>"
```

**Arguments:**
- `iteration` (optional) - Iteration number (NNNN format) to fork from. If provided, searches backward in current branch history for matching iteration tag. If omitted, forks from current HEAD.
- `strategy-name` (required) - Name for new branch (kebab-case). Will become `autonomy/<strategy-name>`.

**The skill will:**
1. Resolve fork point (iteration tag or current HEAD)
2. Validate fork point exists
3. Checkout fork point
4. Create new branch `autonomy/<strategy-name>`
5. Report success with next steps

**Example usage:**
```
# Fork from current commit
/fork-iteration experiment-b

# Fork from specific iteration in current branch history
/fork-iteration 0015 experiment-b

# Bootstrap autonomy workflow from non-autonomy branch
git checkout main
/fork-iteration initial-strategy
```

**Note:** This creates the branch but does NOT start an iteration. After forking, run `/start-iteration` to begin work on the new branch.
