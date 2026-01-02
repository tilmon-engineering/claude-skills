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
2. **iteration-NNNN-YYYY-MM-DD.md** - Journal entry for each iteration (4-digit numbering)
3. **summary.md** - Condensed history of older iterations

Iteration journals are automatically committed to git with tags for easy navigation.

This creates a system of record that enables the agent to understand where it's been and where it's going.

## Quick Start

```bash
# Create a new goal (one-time setup)
/create-goal

# Start first iteration
/start-iteration

# Work on the goal using any skills/workflows
# ... do work ...

# Save progress mid-iteration if needed
/checkpoint-iteration

# End iteration when done
/end-iteration

# Resume in next conversation
/start-iteration

# Check progress anytime
/review-progress

# Analyze another branch for insights
/analyze-branch experiment-a "what we tried"
```

## Commands

### `/create-goal`

One-time setup for a new open-ended goal.

**Process:**
- Prompts for goal statement and metrics
- Creates `autonomy/[goal-name]/` directory
- Writes goal.md with goal definition

**When to use:** Before starting your first iteration on a new goal

### `/start-iteration`

Begin a new iteration for an existing open-ended goal.

**First iteration:**
- Creates initial journal file with iteration intention
- Prompts: "What do you want to accomplish this iteration?"

**Subsequent iterations:**
- Loads context from last 3-5 iterations
- Summarizes older iterations if >5 exist
- Presents current state, blockers, and next steps

**Output:** Ready to continue working toward goal

### `/checkpoint-iteration`

Save current progress mid-iteration before context compaction.

**Process:**
- Updates journal Work Performed section with progress so far
- Merges with any previous checkpoint content
- Preserves state against potential context loss

**When to use:** During long conversations or before risky operations

### `/end-iteration`

Conclude current iteration and write journal entry.

**Process:**
- Reviews conversation for skills used, decisions made
- Documents artifacts created and blockers encountered
- Captures reasoning and strategy changes
- Completes journal entry (updates existing file from start-iteration)
- Updates summary.md every 5 iterations
- **Commits journal to git** with tag `autonomy/iteration-NNNN`

**Output:** Journal file completed and committed, ready for next iteration

### `/review-progress`

Assess progress toward goal across all iterations.

**Process:**
- Reads all journal entries (or summary + recent)
- Analyzes metrics, trends, patterns
- Identifies what's working and what's not
- Provides honest assessment with recommendations

**Output:** Comprehensive progress report

### `/analyze-branch [branch-name] [search-criteria]`

Analyze another branch's iteration journals to extract findings and insights.

**Process:**
- Uses `git merge-base` to find where branches diverged
- Extracts iteration journals from divergent commits on target branch
- Searches for relevant content based on search criteria
- Produces markdown report with findings, decisions, and lessons

**Arguments:**
- `branch-name` - Git branch to analyze (e.g., "experiment-a")
- `search-criteria` - Free-text description of what to look for (e.g., "pricing experiments")

**Output:** Markdown report ready for inclusion in current journal's "External Context Gathered" section

**Use cases:**
- Review work from parallel experiment branches
- Extract lessons from concluded experiments
- Compare approaches across different branches
- Find salvageable ideas from any branch

**Example:**
```bash
/analyze-branch experiment-a "API optimization and performance improvements"
```

## Directory Structure

```
autonomy/[goal-name]/
├── goal.md                          # Goal definition and metrics
├── summary.md                       # Condensed history (updated every 5 iterations)
├── iteration-0001-YYYY-MM-DD.md    # First iteration journal
├── iteration-0002-YYYY-MM-DD.md    # Second iteration journal
└── iteration-NNNN-YYYY-MM-DD.md    # Nth iteration journal (4-digit numbering)
```

**Iteration numbering:** Uses 4-digit zero-padded format (0001-9999) to support up to 9999 iterations.

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

### Iteration Metadata
Execution details:
- Context usage
- Checkpoint count
- Suggested next action

## Git Integration

Autonomy automatically commits journal files to git when ending an iteration:

**What gets committed:**
- `iteration-NNNN-YYYY-MM-DD.md` (always)
- `summary.md` (when updated - every 5 iterations)

**Commit format:**
```
journal: [goal-name] iteration NNNN

[2-3 line summary of work completed]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Git tag:** `autonomy/iteration-NNNN` (annotated tag on commit)

**Branch behavior:**
- Commits to current branch (does NOT create new branch)
- Respects your branching strategy
- You control when to merge/push

**Tag benefits:**
- Navigate to specific iteration: `git checkout autonomy/iteration-0042`
- List all iterations: `git tag -l 'autonomy/*'`
- CI/CD integration: Trigger on `autonomy/iteration-*` tags
- Immutable history markers

**Error handling:**
- If git operations fail, iteration still completes
- Journal is always written (critical for continuity)
- Manual commit commands provided if needed
- Graceful degradation ensures no data loss

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
- Comprehensive journal entry completion
- Summary updates (every 5 iterations)
- Git commit and tagging (automatic)
- Completion announcement

### `checkpointing-an-iteration`

Invoked by `/checkpoint-iteration` command. Handles:
- Mid-iteration progress capture
- Incremental journal updates
- Context preservation before compaction

### `creating-a-goal`

Invoked by `/create-goal` command. Handles:
- Goal statement collection
- Directory structure creation
- goal.md initialization

### `reviewing-progress`

Invoked by `/review-progress` command. Handles:
- Full history reading
- Progress analysis and trend identification
- Honest assessment with recommendations
- Strategic guidance

### `analyzing-branches`

Invoked by `/analyze-branch` command. Handles:
- Git merge-base operations to find divergence point
- Extraction of iteration journals from target branch
- Content searching based on user criteria
- Report generation for cross-branch learning

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

## Advanced Workflow: Exploratory Branching

### The Slime Mold Strategy

Git branches become **exploratory tendrils** searching for solutions. Instead of a linear progression toward a single solution, you spawn multiple independent branches that explore different approaches simultaneously.

**Key Concept:** Like a slime mold extending tendrils to search for resources, each branch is an autonomous experiment. Some tendrils find nutrients and thrive. Others reach dead ends and stop. Living branches can **reincorporate discoveries** from other branches using `/analyze-branch`.

### How It Works

**1. Initial Setup**

```bash
# Create goal on main branch
git checkout -b main
/create-goal  # Goal: "Find optimal solution to X"
git add autonomy/
git commit -m "initial commit: autonomy goal setup"

# Main branch stays at initial commit
# All experiments happen on separate branches
```

**2. Spawn Experiment Branches**

```bash
# Start first exploration path
git checkout -b experiment-pricing-model-a
/start-iteration
# Intention: "Explore usage-based pricing with tiered caps"
# ... work on this approach ...
/end-iteration

# Start parallel exploration path
git checkout -b experiment-pricing-model-b
/start-iteration
# Intention: "Explore flat enterprise pricing with seat limits"
# ... work on this approach ...
/end-iteration
```

**3. Branches Evolve Independently**

Each branch has its own iteration history:
- `experiment-pricing-model-a`: Iterations 0001-0015
- `experiment-pricing-model-b`: Iterations 0001-0023
- `experiment-hybrid-approach`: Iterations 0001-0008

**No merging required.** Branches are independent experiments, not feature branches.

**4. Learn Across Branches**

When one branch discovers something useful:

```bash
# On experiment-pricing-model-b (the successful path)
/analyze-branch experiment-pricing-model-a "usage-based billing experiments"

# Agent extracts:
# - What worked: Real-time usage tracking implementation
# - What failed: Tiered caps confused users
# - Good ideas: API rate limiting patterns from iteration 0012
```

Copy relevant findings into current iteration's "External Context Gathered" section. The living branch **reincorporates** discoveries from other tendrils.

**5. Branches Reach Conclusions**

Some branches succeed and continue indefinitely. Others reach natural conclusions:

```bash
# On experiment-pricing-model-a
/end-iteration
# Ending State: "Dead end. Tiered caps add complexity without value.
#                Users prefer simple per-unit pricing.
#                Abandoning this approach."
```

Branch stops. Remains in git history for future analysis.

**6. New Branches Spawn from Insights**

```bash
# Spawn new branch incorporating learnings from both experiments
git checkout -b experiment-simple-per-unit
/start-iteration
# Intention: "Pure per-unit pricing. Incorporating usage tracking
#             from experiment-a and simplicity from experiment-b."

/analyze-branch experiment-pricing-model-a "usage tracking implementation"
/analyze-branch experiment-pricing-model-b "simple pricing communication"
```

### Workflow Characteristics

**No canonical "main" branch:**
- `main` may just be the initial commit
- All work happens on experiment branches
- No branch is "more correct" than others

**Branches are peers, not hierarchical:**
- experiment-a isn't a "feature branch" of main
- experiment-b doesn't "merge into" experiment-a
- Each branch is an autonomous exploration path

**Natural selection through iteration:**
- Productive branches accumulate iterations
- Dead-end branches stop naturally
- No manual cleanup required - git history preserves everything

**Cross-pollination via `/analyze-branch`:**
- Living branches extract insights from others (living or dead)
- Ideas propagate across independent lineages
- Best patterns emerge organically

### Example: Three-Branch Evolution

**Timeline:**

```
main (iteration 0, initial commit)
  │
  ├─ experiment-redis-cache ──────────────── (iterations 1-8, dead end)
  │
  ├─ experiment-cdn-strategy ──────────────┬ (iterations 1-15, ongoing)
  │                                        │
  │                                        └─ experiment-hybrid-caching ─ (iterations 1-3, new)
  │
  └─ experiment-edge-computing ──────────── (iterations 1-20, promising)
```

**Branch statuses:**
- **experiment-redis-cache**: Dead end (iteration 8 concluded "too expensive at scale")
- **experiment-cdn-strategy**: Active, moderate progress
- **experiment-edge-computing**: Active, showing strong results
- **experiment-hybrid-caching**: New fork combining CDN + edge insights

**Cross-branch learning:**

On `experiment-hybrid-caching`:
```bash
/analyze-branch experiment-redis-cache "caching invalidation patterns"
/analyze-branch experiment-edge-computing "latency optimization techniques"
```

### When to Use This Workflow

**Good for:**
- Unclear solution space (multiple valid approaches)
- High experimentation cost (want to explore in parallel)
- Long-term R&D (months or years of iteration)
- Learning what works through trial and error
- Problems where the "right" answer isn't obvious

**Not good for:**
- Well-defined tasks with known solutions
- Short-term projects (overhead not worth it)
- When you need a single canonical answer quickly

### Git Repository as Exploration Map

Your git history becomes a **map of explored territory**:

```bash
# List all experiment branches
git branch -a

# See iteration tags across all branches
git tag -l 'autonomy/*'

# View branch divergence points
git log --graph --oneline --all

# Jump to any iteration on any branch
git checkout autonomy/iteration-0042  # From any branch's history
```

The repository preserves the **entire exploration**, not just the final answer. Future work can mine this history for insights.

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
- Plugin expects sequential numbering (0001, 0002, 0003...)
- Missing numbers are okay (will skip gaps)
- Duplicate numbers: Rename manually to fix

### Git commit failed
- Journal is still written (iteration completes normally)
- Manual commands provided in output
- Common causes: not in git repo, detached HEAD, permissions
- Fix underlying issue and commit manually if needed

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
