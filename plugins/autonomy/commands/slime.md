---
description: Set up slime mold strategy for parallel exploration with autonomy branches
allowed-tools: Skill
model: sonnet
---

# Slime Mold Strategy Setup

You must invoke the `slime-strategy` skill to set up the complete slime mold exploration workflow.

Use the Skill tool:
```
skill: "autonomy:slime-strategy"
```

**What this command does:**

If no autonomy goal exists yet:
1. Uses `creating-a-goal` skill to define goal and set up `autonomy/[goal-name]/` directory
2. Creates/updates `autonomy/CLAUDE.md` with slime mold strategy documentation
3. Uses `forking-iteration` skill to create initial `autonomy/[goal-name]` branch
4. Creates `iteration-0000-YYYY-MM-DD.md` as baseline setup journal
5. Makes git commit with tag `autonomy/[goal-name]/iteration-0000`

If autonomy goal already exists:
- Updates `autonomy/CLAUDE.md` to ensure slime mold strategy documentation is current
- Skips goal creation, branching, and iteration 0000 (idempotent behavior)

**After running `/slime`:**
- Use `/start-iteration` to begin iteration 0001 (first real work iteration)
- Use `/fork-iteration <strategy-name>` to create additional exploration branches
- Use `/analyze-branch <branch> <search>` to cross-pollinate learnings between branches
- Use `/compare-branches <branch-a> <branch-b>` to understand divergent approaches
