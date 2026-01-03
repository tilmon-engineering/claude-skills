---
description: Create new autonomy branch with dedicated worktree for parallel agent workflows
allowed-tools: Skill, AskUserQuestion, Bash
model: sonnet
argument-hint: "[iteration] <strategy-name>"
---

# Fork Worktree

Create a new autonomy branch with a dedicated worktree for running parallel Claude agents on different branches simultaneously.

You must invoke the `forking-worktree` skill to perform the fork.

Use the Skill tool:
```
skill: "autonomy:forking-worktree"
args: "[iteration] <strategy-name>"
```

**Arguments:**
- `iteration` (optional) - Iteration number (NNNN format) to fork from. If provided, searches backward in current branch history for matching iteration tag. If omitted, forks from current HEAD.
- `strategy-name` (required) - Name for new branch and worktree (kebab-case). Will become `autonomy/<strategy-name>` branch and `.worktrees/autonomy/<strategy-name>/` directory.

**The skill will:**
1. Detect repository root (works from main repo or within worktrees)
2. Resolve fork point (iteration tag or current HEAD)
3. Validate fork point exists and worktree path is available
4. Create new branch `autonomy/<strategy-name>` with worktree at `.worktrees/autonomy/<strategy-name>/`
5. Report success with navigation instructions

**Example usage:**
```
# Fork from current commit (works from anywhere)
/fork-worktree experiment-b

# Fork from specific iteration in current branch history
/fork-worktree 0015 experiment-b

# Fork from within another worktree (creates sibling worktree, not nested)
cd .worktrees/autonomy/experiment-a
/fork-worktree experiment-c  # Creates .worktrees/autonomy/experiment-c/ at root level
```

**Note:** This creates the branch AND worktree but does NOT start an iteration. After forking, navigate to the worktree directory and run `/start-iteration` to begin work:
```bash
cd .worktrees/autonomy/<strategy-name>
/start-iteration
```

**Difference from `/fork-iteration`:**
- `/fork-iteration` creates branch in current working directory (main repo)
- `/fork-worktree` creates branch + isolated worktree directory for parallel work
- Use worktrees when running multiple agents in parallel on different branches
