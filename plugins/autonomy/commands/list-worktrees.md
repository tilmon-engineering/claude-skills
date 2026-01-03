---
description: List all autonomy worktrees with their status and location
allowed-tools: Skill, Bash
model: sonnet
argument-hint: ""
---

# List Worktrees

List all autonomy worktrees showing their branch, location, and current HEAD commit.

You must invoke the `listing-worktrees` skill to perform the listing.

Use the Skill tool:
```
skill: "autonomy:listing-worktrees"
args: ""
```

**The skill will:**
1. Find all git worktrees in the repository
2. Filter to autonomy worktrees (in `.worktrees/autonomy/`)
3. Display formatted table with branch, path, HEAD commit, and lock status
4. Provide navigation hints

**Example output:**
```
Autonomy Worktrees:

Branch                    Path                                      HEAD       Locked
autonomy/experiment-a     .worktrees/autonomy/experiment-a          a1b2c3d
autonomy/experiment-b     .worktrees/autonomy/experiment-b          d4e5f6g    🔒
autonomy/cdn-optimize     .worktrees/autonomy/cdn-optimize          h7i8j9k

Total: 3 autonomy worktrees

To navigate to a worktree:
  cd .worktrees/autonomy/<strategy-name>

To remove a worktree:
  /remove-worktree <strategy-name>
```

**Note:** This only lists worktrees, not branches. To see all autonomy branches (including those without worktrees), use `/list-branches`.
