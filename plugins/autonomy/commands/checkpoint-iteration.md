---
description: Save current iteration progress before conversation compaction or as interim checkpoint
allowed-tools: Skill, Read, Write, Edit
model: sonnet
---

# Checkpoint Iteration

You must invoke the `checkpointing-an-iteration` skill to save current progress.

Use the Skill tool:
```
skill: "autonomy:checkpointing-an-iteration"
```

The skill will:
1. Review conversation since iteration started
2. Update journal entry with current work performed
3. Capture decisions, artifacts, blockers so far
4. Preserve state before potential context compaction

Use this when:
- Conversation getting long, compaction imminent
- Reached natural pause point mid-iteration
- Want to preserve important context discovered so far
