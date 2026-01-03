---
description: Safely remove an autonomy worktree while preserving the branch and its history
allowed-tools: Skill, AskUserQuestion, Bash
model: sonnet
argument-hint: "[--force] <strategy-name>"
---

# Remove Worktree

Safely remove an autonomy worktree directory while preserving the autonomy branch, commits, and iteration tags.

You must invoke the `removing-worktree` skill to perform the removal.

Use the Skill tool:
```
skill: "autonomy:removing-worktree"
args: "[--force] <strategy-name>"
```

**Arguments:**
- `--force` (optional) - Skip uncommitted changes check and force removal
- `strategy-name` (required) - Name of worktree to remove (without `autonomy/` prefix)

**The skill will:**
1. Detect repository root (works from anywhere)
2. Validate worktree exists at `.worktrees/autonomy/<strategy-name>/`
3. Check for uncommitted changes (unless `--force`)
4. Remove worktree directory
5. Prune git worktree metadata
6. Report success

**Example usage:**
```
# Safe removal (fails if uncommitted changes)
/remove-worktree experiment-b

# Force removal (discards uncommitted changes)
/remove-worktree --force experiment-b

# Remove from within another worktree
cd .worktrees/autonomy/experiment-a
/remove-worktree experiment-b  # Removes sibling worktree
```

**What gets removed:**
- Worktree directory: `.worktrees/autonomy/<strategy-name>/`
- Git worktree metadata

**What persists:**
- Branch `autonomy/<strategy-name>` and all commits
- All iteration tags (`autonomy/<strategy-name>/iteration-NNNN`)
- Git history and journal commits
- Can checkout branch later or create new worktree for it

**Manual removal:**
If automated removal fails:
```bash
git worktree remove --force .worktrees/autonomy/<strategy-name>
git worktree prune
```
