---
description: Start a new iteration for an open-ended goal, loading context from previous iterations
allowed-tools: Skill, Read, Write, Glob, Bash, Task, TodoWrite
model: sonnet
---

# Start Iteration

You must invoke the `starting-an-iteration` skill to begin a new iteration for an open-ended goal.

Use the Skill tool:
```
skill: "autonomy:starting-an-iteration"
```

The skill will:
1. Detect if a goal already exists or prompt to create a new one
2. Load context from recent iterations
3. Present the current state and open questions
4. Prepare you to continue working toward the goal
