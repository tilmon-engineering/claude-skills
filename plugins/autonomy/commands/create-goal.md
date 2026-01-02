---
description: Create a new open-ended goal for autonomy tracking
allowed-tools: Skill, Read, Write, Glob, Bash
model: sonnet
---

# Create Goal

You must invoke the `creating-a-goal` skill to set up a new open-ended goal.

Use the Skill tool:
```
skill: "autonomy:creating-a-goal"
```

The skill will:
1. Prompt for goal statement and success criteria
2. Generate goal directory name
3. Create autonomy/[goal-name]/ directory structure
4. Write goal.md with goal definition
5. Prepare for first iteration

After creating the goal, use `/start-iteration` to begin work.
