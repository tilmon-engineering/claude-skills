---
name: slime
description: Use when user wants to set up slime mold exploration strategy with parallel autonomy branches for genetic algorithm approach to problem-solving
user-invocable: true
---

# Slime Mold Strategy Setup

## Overview

Set up the complete "slime mold strategy" workflow for exploring problem spaces through parallel autonomy branches that cooperate like a genetic algorithm.

**Core principle:** Initialize autonomy workflow with slime mold philosophy: multiple parallel branches exploring different approaches, cooperating not competing, cross-pollinating insights.

## When to Use

Use this skill when:
- User runs `/slime` command
- User wants to adopt slime mold strategy for exploration
- Setting up parallel branch exploration with genetic algorithm approach

**DO NOT use for:**
- Adding single goal without branch strategy (use `/create-goal`)
- Creating additional branches in existing workflow (use `/fork-iteration`)
- Analyzing existing branches (use `/branch-status` or `/compare-branches`)

## Quick Reference

| Step | Action | Tool |
|------|--------|------|
| 1. Check state | Look for existing autonomy goal | Glob |
| 2a. Create goal | Invoke create-goal skill if needed | Skill |
| 2b. Update only | Skip to CLAUDE.md if goal exists | - |
| 3. Update CLAUDE.md | Replace slime mold section or create file | Read, Write |
| 4. Create branch | Invoke fork-iteration with goal name | Skill |
| 5. Initialize iteration | Create iteration-0001 journal file | Write |
| 6. Git commit | Commit with enhanced format and tag | Bash |

## Process

### Step 1: Check Existing State

First, determine if autonomy workflow already exists:

```bash
# Look for any existing goal.md files
existing_goals=$(find autonomy -name "goal.md" 2>/dev/null)

if [ -n "$existing_goals" ]; then
  mode="update-only"
  echo "Autonomy workflow already exists. Will update CLAUDE.md only."

  # Extract goal name from first goal found
  goal_dir=$(dirname "$existing_goals" | head -1)
  goal_name=$(basename "$goal_dir")
else
  mode="full-setup"
  echo "No existing autonomy goal found. Will perform full setup."
fi
```

**Validation:**
- If multiple goals found, use first one alphabetically
- Warn user: "Multiple goals detected, using [goal-name]"

### Step 2: Create Goal (full-setup mode only)

If `mode="full-setup"`, invoke the create-goal skill:

```bash
# Only run if full-setup mode
if [ "$mode" = "full-setup" ]; then
  # Invoke create-goal skill using Skill tool
  skill: "autonomy:create-goal"

  # After skill completes, extract goal name
  goal_dir=$(find autonomy -name "goal.md" -exec dirname {} \; | head -1)
  goal_name=$(basename "$goal_dir")

  echo "Goal created: $goal_name"
fi
```

**Error Handling:**
- If create-goal fails or user cancels
- Abort entire workflow
- Show: "Goal creation cancelled. Slime mold setup aborted."
- Don't proceed to CLAUDE.md or iteration 0001

### Step 3: Create/Update autonomy/CLAUDE.md

Ensure `autonomy/CLAUDE.md` exists and contains current slime mold strategy documentation.

**CLAUDE.md Content (exact text to use):**

```markdown
# Slime Mold Strategy

This project uses the "slime mold strategy" for exploring the problem space. Like a slime mold organism that extends multiple tendrils to find optimal paths, we maintain parallel autonomy branches that explore different approaches to the same goal. These branches represent a genetic algorithm: each branch is an independent experiment testing different hypotheses, strategies, or implementations.

Crucially, these branches are NOT competing—they are cooperating. All branches are part of the same organism pursuing the same goal. When branches encounter each other or when you discover useful insights in one branch, use `/analyze-branch <branch-name> <search-description>` to extract "genetic material" (learnings, patterns, solutions) and incorporate them into your current branch. Use `/compare-branches <branch-a> <branch-b>` to understand how different approaches diverged and what outcomes each achieved. Use `/list-branches` to inventory all active exploration tendrils. When ready to fork a new experimental direction, use `/fork-iteration [iteration] <strategy-name>` to create a new tendril from any point in history.

The goal is not to find the single "best" branch, but to explore the solution space thoroughly and cross-pollinate insights across branches, allowing the organism as a whole to discover optimal solutions through parallel exploration and cooperation.
```

**Implementation:**

```bash
# Check if autonomy/CLAUDE.md exists
if [ -f "autonomy/CLAUDE.md" ]; then
  # Read existing content
  existing_content=$(cat autonomy/CLAUDE.md)

  # Check if slime mold section exists
  if echo "$existing_content" | grep -q "# Slime Mold Strategy"; then
    echo "Updating existing slime mold section in CLAUDE.md"

    # Strategy: Replace section from "# Slime Mold Strategy" to next "# " heading or EOF
    # Use Read tool to get current content
    # Use Edit tool to replace the section

    # Read current file
    # Find start of "# Slime Mold Strategy" section
    # Find end (next # heading or EOF)
    # Replace that section with new content
  else
    echo "Appending slime mold section to existing CLAUDE.md"

    # Append new section to end of file
    # Use Edit tool to add content at end
  fi
else
  echo "Creating new autonomy/CLAUDE.md with slime mold section"

  # Create new file with slime mold section
  # Use Write tool to create file
fi
```

**Write/Edit the slime mold section:**

Use Write tool if creating new file, or Edit tool if updating existing file.

The section content is the markdown block shown above under "CLAUDE.md Content".

### Step 4: Create Initial Branch (full-setup mode only)

If `mode="full-setup"`, create the initial autonomy branch:

```bash
# Only run if full-setup mode
if [ "$mode" = "full-setup" ]; then
  # Invoke fork-iteration skill with goal-name as strategy-name
  # No iteration number specified = fork from current HEAD

  skill: "autonomy:fork-iteration"
  args: "$goal_name"

  # This creates branch: autonomy/[goal-name]
  # And checks out that branch

  echo "Created and switched to branch: autonomy/$goal_name"
fi
```

**Error Handling:**
- If fork-iteration fails (e.g., branch already exists)
- Show error from skill
- Don't create iteration 0001
- Suggest: "Use /fork-iteration <different-name> to create branch with different name"

### Step 5: Create Iteration 0001 (full-setup mode only)

If `mode="full-setup"`, create the baseline setup iteration:

```bash
# Only run if full-setup mode
if [ "$mode" = "full-setup" ]; then
  # Get current date in YYYY-MM-DD format
  current_date=$(date +%Y-%m-%d)

  # Create iteration-0001 file
  iteration_file="autonomy/$goal_name/iteration-0001-$current_date.md"

  # Use Write tool to create file with this content:
fi
```

**Iteration 0001 Content:**

```markdown
# Iteration 0001 - YYYY-MM-DD

## Beginning State

No previous iterations. This is the initial setup for the slime mold exploration strategy.

**Baseline Metrics:**
[Extract from goal.md metrics section, or "None established yet" if no metrics defined]

## Iteration Intention

Establish the foundation for slime mold strategy exploration:
- Define goal and success criteria
- Create initial autonomy branch
- Document exploration approach
- Prepare for iteration 0002 (first real work iteration) to be started via `/start-iteration`

## Work Performed

### Setup Completed
- Created goal: [Extract goal statement from goal.md]
- Established autonomy/CLAUDE.md with slime mold strategy documentation
- Created initial branch: autonomy/[goal-name]
- Initialized iteration tracking system

### Slime Mold Strategy Adopted
- Multiple parallel branches will explore different approaches
- Branches cooperate via /analyze-branch for cross-pollination
- Use /fork-iteration to create new exploration tendrils
- Use /compare-branches to understand divergent paths

## Ending State

Autonomy workflow initialized. Iteration 0001 created as baseline setup. Ready to begin iteration 0002 with actual exploration work. Use `/start-iteration` to begin.

**Recommended next action:** Run `/start-iteration` to begin first real iteration of exploration.
```

**Implementation:**

Read `autonomy/[goal-name]/goal.md` to extract:
- Goal statement (from first paragraph or "## Goal" section)
- Metrics (from "## Metrics" or "Success Criteria" section)

Use Write tool to create `iteration-0001-YYYY-MM-DD.md` with content above, substituting:
- `YYYY-MM-DD` with current date
- `[goal-name]` with actual goal name
- Goal statement and metrics from goal.md

### Step 6: Git Commit and Tag (full-setup mode only)

If `mode="full-setup"`, commit iteration 0001 with enhanced format:

```bash
# Only run if full-setup mode
if [ "$mode" = "full-setup" ]; then
  # Stage the iteration file and CLAUDE.md
  git add "autonomy/$goal_name/iteration-0001-$current_date.md"
  git add "autonomy/CLAUDE.md"

  # Create enhanced commit message
  git commit -m "$(cat <<'EOF'
journal: $goal_name iteration 0001

Established slime mold exploration strategy with initial autonomy branch.

## Journal Summary

Created goal definition for $goal_name, initialized slime mold strategy documentation in CLAUDE.md, created initial autonomy/$goal_name branch, and established iteration 0001 as baseline. Workflow ready for iteration 0002 to begin actual exploration work.

## Iteration Metadata

Status: active
Metrics: None (baseline setup)
Blockers: None
Next: Run /start-iteration to begin iteration 0002

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"

  # Create branch-aware tag
  git tag -a "autonomy/$goal_name/iteration-0001" \
    -m "journal: $goal_name iteration 0001"

  echo "Created git commit and tag: autonomy/$goal_name/iteration-0001"
fi
```

**Commit Message Format:**
- First line: `journal: [goal-name] iteration 0001`
- Blank line
- 2-3 line summary
- `## Journal Summary` section (4-6 sentences)
- `## Iteration Metadata` section (Status, Metrics, Blockers, Next)
- Claude Code attribution

**Tag Format:**
- `autonomy/[goal-name]/iteration-0001`
- Matches branch-aware tagging from end-iteration skill

### Step 7: Final Messages

Display completion message based on mode:

**Full-setup mode:**
```
Slime mold strategy initialized successfully!

✓ Goal created: [goal-name]
✓ CLAUDE.md documented slime mold strategy
✓ Branch created: autonomy/[goal-name]
✓ Iteration 0001 established as baseline
✓ Git commit and tag: autonomy/[goal-name]/iteration-0001

Next steps:
1. Run /start-iteration to begin iteration 0002
2. Use /fork-iteration <strategy-name> to create additional exploration branches
3. Use /analyze-branch to cross-pollinate insights between branches
4. Use /compare-branches to understand divergent approaches
```

**Update-only mode:**
```
Slime mold strategy documentation updated!

✓ CLAUDE.md updated with current slime mold strategy description

Your autonomy workflow is ready. Use these commands:
- /fork-iteration <strategy-name> - Create new exploration branch
- /list-branches - Inventory all autonomy branches
- /compare-branches <a> <b> - Compare two exploration paths
- /analyze-branch <branch> <search> - Extract insights from another branch
```

## Important Notes

### Git Repository Required

This skill requires a git repository:
- Check with `git rev-parse --git-dir` before starting
- If not in git repo, show error: "This command requires a git repository. Run 'git init' first."
- Abort workflow if git not available

### Idempotent Behavior

The skill is designed to be idempotent:
- Safe to run multiple times
- If goal exists: Only updates CLAUDE.md (doesn't recreate goal or iteration 0001)
- CLAUDE.md section replacement ensures documentation stays current
- Use this to update slime mold description as concept evolves

### CLAUDE.md Location

- File created at `autonomy/CLAUDE.md` (working directory, not plugin directory)
- At same level as `autonomy/[goal-name]/` directories
- Provides project-level context for slime mold strategy

### Iteration 0001 is Special

- Iteration 0001 is baseline setup only
- First real work iteration is 0002 (via `/start-iteration`)
- Don't use `start-iteration` skill for iteration 0001
- Manually create the file with setup-specific content

### Branch Name = Goal Name

- Initial branch always named `autonomy/[goal-name]`
- Matches goal directory name for consistency
- Additional branches via `/fork-iteration` can use different strategy names
- Example: goal "improve-performance" → branch "autonomy/improve-performance"

## Common Mistakes

| Mistake | Reality |
|---------|---------|
| "I'll use start-iteration for iteration 0001" | NO. Manually create iteration 0001 with setup-specific content. |
| "I'll skip CLAUDE.md in update-only mode" | NO. Always update CLAUDE.md to keep description current. |
| "I'll append to CLAUDE.md even if section exists" | NO. Replace existing slime mold section to keep it current. |
| "I'll create iteration 0002 after 0001" | NO. User runs /start-iteration for 0002. This skill only creates 0001 (baseline). |
| "I'll use different branch name than goal name" | NO. Initial branch must be autonomy/[goal-name]. Use /fork-iteration for other names. |
| "I'll skip git commit if user doesn't want it" | NO. Git integration is core to autonomy workflow. Always commit. |

## After Setup

Once `/slime` completes:
- User should run `/start-iteration` to begin iteration 0002
- User can run `/fork-iteration <strategy-name>` to create additional branches
- User can use `/analyze-branch` for cross-pollination
- User can use `/compare-branches` to understand divergence

The slime mold strategy is now active and documented in `autonomy/CLAUDE.md`.
