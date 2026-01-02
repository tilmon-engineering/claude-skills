# Autonomy Plugin

Enable AI agents to iteratively self-direct in pursuit of open-ended goals with state continuity across conversations through iteration journals.

## Overview

**Autonomy** is for goals that never truly end - ongoing optimization, continuous improvement, and iterative exploration. Unlike closed goals with a definition of done, autonomy goals are about making incremental progress toward an ever-evolving target.

**Example open-ended goals:**
- Maximize monthly recurring revenue
- Improve developer productivity
- Reduce customer churn
- Optimize application performance
- Grow monthly active users

**Not for:** Closed goals with clear completion criteria (use ed3d-superpowers workflow instead)

## Core Concept: Iteration Journals

Each conversation is one **iteration**. The plugin maintains state across iterations through:

1. **goal.md** - Stable goal definition and current metrics
2. **iteration-NNN-YYYY-MM-DD.md** - Journal entry for each iteration
3. **summary.md** - Condensed history of older iterations

This creates a system of record that enables the agent to understand where it's been and where it's going.

## Quick Start

```bash
# Start first iteration for a new goal
/start-iteration

# Work on the goal using any skills/workflows
# ... do work ...

# End iteration when done
/end-iteration

# Resume in next conversation
/start-iteration

# Check progress anytime
/review-progress
```

## Commands

### `/start-iteration`

Begin a new iteration for an open-ended goal.

**First time:**
- Prompts for goal statement
- Creates `autonomy/[goal-name]/` directory
- Sets up goal.md with success criteria

**Subsequent times:**
- Loads context from last 3-5 iterations
- Summarizes older iterations if >5 exist
- Presents current state, blockers, and next steps

**Output:** Ready to continue working toward goal

### `/end-iteration`

Conclude current iteration and write journal entry.

**Process:**
- Reviews conversation for skills used, decisions made
- Documents artifacts created and blockers encountered
- Captures reasoning and strategy changes
- Writes comprehensive journal entry
- Updates summary.md every 5 iterations

**Output:** Journal file written, ready for next iteration

### `/review-progress`

Assess progress toward goal across all iterations.

**Process:**
- Reads all journal entries (or summary + recent)
- Analyzes metrics, trends, patterns
- Identifies what's working and what's not
- Provides honest assessment with recommendations

**Output:** Comprehensive progress report

## Directory Structure

```
autonomy/[goal-name]/
├── goal.md                          # Goal definition and metrics
├── summary.md                       # Condensed history (updated every 5 iterations)
├── iteration-001-YYYY-MM-DD.md     # First iteration journal
├── iteration-002-YYYY-MM-DD.md     # Second iteration journal
└── iteration-NNN-YYYY-MM-DD.md     # Nth iteration journal
```

## Iteration Journal Format

Each iteration journal documents:

### Beginning State
What was the state when iteration started?
- Current progress
- Known blockers
- Open questions

### Work Performed
What happened during this iteration?
- **Skills & Workflows Used** - Which methodologies were applied
- **Key Decisions Made** - Major choices with rationale
- **Artifacts Created/Modified** - Files, commits, PRs
- **External Context Gathered** - Research, feedback, docs
- **Reasoning & Strategy Changes** - Why approach evolved
- **Blockers Encountered** - What's preventing progress
- **Open Questions** - What needs resolution

### Ending State
What is the state now?
- Progress made
- Updated metrics
- Recommended next steps

## Skills

### `starting-an-iteration`

Invoked by `/start-iteration` command. Handles:
- Goal detection and setup
- Context loading from previous iterations
- Agent delegation for journal reading and summarization
- State presentation to user

### `ending-an-iteration`

Invoked by `/end-iteration` command. Handles:
- Conversation review for key information
- Comprehensive journal entry writing
- Summary updates (every 5 iterations)
- Completion announcement

### `reviewing-progress`

Invoked by `/review-progress` command. Handles:
- Full history reading
- Progress analysis and trend identification
- Honest assessment with recommendations
- Strategic guidance

## Agents

### `journal-reader` (Haiku)

Reads and structures recent journal entries (last 3-5) for context loading. Extracts:
- Current state
- Open blockers and questions
- Recent progress
- Key metrics
- Recommended next steps

### `journal-summarizer` (Haiku)

Condenses older iterations into summary.md. Preserves:
- Major milestones
- Persistent blockers
- Strategic pivots
- Key learnings
- Metric trends

## Integration with Other Plugins

Autonomy automatically detects and logs skills from any plugin:
- Scans conversation for `Skill` tool invocations
- Records skill name and observed purpose
- No hardcoded plugin list - works with current and future plugins

## Context Loading Strategy

**Iterations 1-5:**
- Load all iterations in detail via journal-reader

**Iterations 6+:**
- Load last 3-5 iterations in detail
- Sub-agent reads and summarizes older iterations
- Balance between context and performance

**Summary updates:**
- Automatically triggered every 5 iterations (5, 10, 15, etc.)
- Keeps summary.md current without manual updates

## Goal Lifecycle

Goals are **append-only** - you can always add new iterations:
- No "complete" state (goals are open-ended)
- Can pause by not starting new iterations
- Can resume anytime, even after long gaps
- Mark as "Paused" in goal.md if desired

## Best Practices

### When to Start Iteration
- Beginning of new conversation session
- After long break from goal
- When context from previous work is needed

### When to End Iteration
- Natural stopping point (subtask complete)
- Blocked on external dependency
- Context limit approaching
- Good handoff point for future iteration

### Review Frequency
- Every 5 iterations (automatic checkpoint)
- Before major strategic decisions
- When feeling uncertain about direction
- If progress seems stalled

### Journal Quality
- Be comprehensive - future iterations depend on it
- Document rationale, not just actions
- Capture all blockers, even minor ones
- Specific next steps, not vague "continue working"

## Examples

### Example: Maximize MRR Goal

**Directory:** `autonomy/maximize-monthly-recurring-revenue/`

**Iteration 1:** Research competitor pricing, analyze current metrics
**Iteration 2:** Design new pricing tiers based on research
**Iteration 3:** Implement usage-based billing
**Iteration 4:** Run A/B test on pricing page
**Iteration 5:** Analyze results, update summary.md

**Progress:** MRR increased from $45k to $62k (+37.8%) over 5 iterations

### Example: Reduce Customer Churn Goal

**Directory:** `autonomy/reduce-customer-churn/`

**Iteration 1:** Analyze churn data, identify patterns
**Iteration 2:** Interview churned customers
**Iteration 3:** Implement email engagement campaign
**Iteration 4:** Build onboarding improvements
**Iteration 5:** Measure impact, update summary.md

**Progress:** Churn reduced from 13% to 8% over 5 iterations

## Troubleshooting

### "No goal found" when starting iteration
- First time: Normal, will prompt for goal creation
- Expected goal: Check if `autonomy/[goal-name]/goal.md` exists
- Wrong directory: Navigate to project root

### Journal files out of order
- Plugin expects sequential numbering (001, 002, 003...)
- Missing numbers are okay (will skip gaps)
- Duplicate numbers: Rename manually to fix

### Summary not updating
- Check if iteration count % 5 == 0 (5, 10, 15...)
- Verify journal-summarizer agent ran successfully
- Manually trigger: Can run `/review-progress` to regenerate

### Context loading too slow
- Normal for many iterations (>20)
- Summary.md reduces load time
- Can manually review fewer iterations by editing skill

## Development

See [creating-a-plugin](../../ed3d-extending-claude/skills/creating-a-plugin/) skill for plugin development guidance.

**Testing locally:**
```bash
/plugin install file:///absolute/path/to/autonomy
/plugin reload
/start-iteration
```

## License

UNLICENSED - Internal use only

## Author

Tilmon Engineering
- Email: team@tilmonengineering.com
- Repository: https://github.com/tilmon-engineering/tilmon-eng-skills
