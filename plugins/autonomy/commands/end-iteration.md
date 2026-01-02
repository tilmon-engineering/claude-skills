---
description: End the current iteration, writing journal entry and summarizing work completed
allowed-tools: Skill, Read, Write, Glob, Bash, Task, TodoWrite
model: sonnet
---

# End Iteration

You must invoke the `ending-an-iteration` skill to finalize the current iteration.

Use the Skill tool:
```
skill: "autonomy:ending-an-iteration"
```

The skill will:
1. Review the conversation to identify skills used, decisions made, and artifacts created
2. Write a comprehensive journal entry documenting this iteration
3. Update summary if needed (every 5 iterations)
4. Prepare the state for the next iteration
