---
description: Analyze another branch to extract findings, decisions, and insights
allowed-tools: Skill, Read, Glob, Bash, Task, AskUserQuestion
model: sonnet
argument-hint: "[branch-name] [search-description]"
---

# Analyze Branch

Analyze another branch's iteration journals to extract key findings, decisions, and insights.

You must invoke the `analyzing-branches` skill to perform the analysis.

Use the Skill tool:
```
skill: "autonomy:analyzing-branches"
args: "[branch-name] [search-description]"
```

**Arguments:**
- `branch-name` - The git branch to analyze (e.g., "experiment-a")
- `search-description` - Free-text description of what to look for (e.g., "pricing experiments and revenue optimization")

The skill will:
1. Use `git merge-base` to find where the branches diverged
2. Extract iteration journals from the divergent commits
3. Search for relevant content based on your criteria
4. Produce a markdown report ready for inclusion in your journal

**Use cases:**
- Review work from parallel experiment branch
- Extract lessons learned from concluded experiments
- Compare approaches across different branches
- Salvage good ideas from any branch

**Example:**
```
/analyze-branch experiment-a "API optimization attempts and performance improvements"
```

The resulting report can be copied into your current iteration's "External Context Gathered" section.
