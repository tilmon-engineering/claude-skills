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

**Not for:** Closed goals with clear completion criteria (use [ed3d-plugins](https://github.com/ed3dai/ed3d-plugins) plan-and-execute workflow instead)

## Core Concept: Iteration Journals

Each conversation is one **iteration**. The plugin maintains state across iterations through:

1. **goal.md** - Stable goal definition and current metrics
2. **iteration-NNNN-YYYY-MM-DD.md** - Journal entry for each iteration (4-digit numbering)
3. **summary.md** - Condensed history of older iterations

Iteration journals are automatically committed to git with tags for easy navigation.

This creates a system of record that enables the agent to understand where it's been and where it's going.

## Quick Start

**Standard workflow:**
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

**Slime mold strategy workflow (parallel exploration):**
```bash
# One-command setup for parallel exploration
/slime

# Start first real iteration
/start-iteration

# Work on the goal
# ... do work ...

# End iteration
/end-iteration

# Fork new exploration branch to try different approach
/fork-iteration alternative-approach

# Work on alternative branch
/start-iteration
# ... do work ...
/end-iteration

# Compare branches to see different outcomes
/compare-branches [goal-name] alternative-approach

# Extract insights from other branch
/analyze-branch alternative-approach "optimization techniques"

# List all exploration branches
/list-branches recent
```

**Parallel agent workflow (with worktrees):**
```bash
# Terminal 1: Create first experiment with isolated worktree
/fork-worktree experiment-pricing-a
cd .worktrees/autonomy/experiment-pricing-a
/start-iteration
# Agent 1 works on usage-based pricing approach
# ... do work ...
/end-iteration

# Terminal 2: Create second experiment (while agent 1 is still working)
/fork-worktree experiment-pricing-b
cd .worktrees/autonomy/experiment-pricing-b
/start-iteration
# Agent 2 works on flat enterprise pricing approach
# ... do work ...
/end-iteration

# Terminal 3: Create third experiment
/fork-worktree experiment-hybrid
cd .worktrees/autonomy/experiment-hybrid
/start-iteration
# Agent 3 explores hybrid approach
# ... do work ...
/end-iteration

# From any location: analyze and compare
/list-worktrees                                    # See active worktrees
/list-branches                                     # See all branches
/compare-branches experiment-pricing-a experiment-pricing-b
/analyze-branch experiment-pricing-a "successful strategies"

# Clean up worktrees when done (branches persist)
/remove-worktree experiment-pricing-a
/remove-worktree experiment-pricing-b
# experiment-hybrid continues in its worktree
```

**When to use worktrees:**
- Running multiple Claude agents in parallel on different autonomy branches
- Each agent needs isolated working directory
- Testing multiple approaches simultaneously

**When NOT to use worktrees:**
- Single agent workflow (use `/fork-iteration` instead)
- Working sequentially on different branches (just git checkout)

## Commands

### `/create-goal`

One-time setup for a new open-ended goal.

**Process:**
- Prompts for goal statement and metrics
- Creates `autonomy/[goal-name]/` directory
- Writes goal.md with goal definition

**When to use:** Before starting your first iteration on a new goal

### `/slime`

One-command setup for the "slime mold strategy" - parallel exploration using autonomy branches as a genetic algorithm.

**If no goal exists yet (full setup):**
- Invokes `/create-goal` to define goal and create `autonomy/[goal-name]/` directory
- Creates/updates `autonomy/CLAUDE.md` with slime mold strategy documentation
- Invokes `/fork-iteration` to create initial branch `autonomy/[goal-name]`
- Creates `iteration-0000-YYYY-MM-DD.md` as baseline setup journal
- Makes git commit with tag `autonomy/[goal-name]/iteration-0000`

**If goal already exists (idempotent):**
- Updates `autonomy/CLAUDE.md` to ensure slime mold strategy description is current
- Skips goal creation, branching, and iteration 0000

**What is the slime mold strategy?**

Like a slime mold organism extending multiple tendrils to find optimal paths, this strategy maintains parallel autonomy branches exploring different approaches to the same goal. Branches are NOT competing—they cooperate as part of the same organism. Use `/analyze-branch` to extract insights from other branches and incorporate them into your current work. Use `/compare-branches` to understand how different approaches diverged. The goal is to explore the solution space thoroughly and cross-pollinate insights across branches.

**After running `/slime`:**
- Run `/start-iteration` to begin iteration 0001 (first real work iteration)
- Use `/fork-iteration <strategy-name>` to create additional exploration branches
- Use `/analyze-branch <branch> <search>` to cross-pollinate learnings
- Use `/compare-branches <branch-a> <branch-b>` to compare approaches

**When to use:** When adopting parallel exploration strategy with multiple autonomy branches

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

## Branch Management Commands

The autonomy plugin includes commands for managing exploration branches in the "slime mold strategy" workflow. These commands only operate on `autonomy/*` branches.

### `/list-branches [optional-query]`

Inventory all autonomy branches with flexible sorting, grouping, and filtering.

**Arguments:**
- `optional-query` - Free-text description of how to sort, group, and what information to display
- If no query provided, defaults to: sort by most recent update, show all branches

**Process:**
- Finds all `autonomy/*` branches via git
- Reads latest journal commit from each branch (commit messages, not files)
- Dispatches branch-analyzer agent to generate Python script for computational analysis
- Produces formatted markdown table with requested information

**Examples:**
```bash
/list-branches
/list-branches sort by most recent, show only active
/list-branches group by status, show metrics
/list-branches show branches updated in last 30 days
```

**Output:** Markdown table showing branch name, latest iteration, last update, status, metrics, and next steps

### `/fork-iteration [iteration] <strategy-name>`

Create new autonomy branch forked from current commit or specific past iteration.

**Arguments:**
- `iteration` (optional) - Iteration number (NNNN format) to fork from. If provided, searches current branch history for matching iteration tag. If omitted, forks from current HEAD.
- `strategy-name` (required) - Name for new branch (kebab-case). Will become `autonomy/<strategy-name>`.

**Process:**
- Resolves fork point (iteration tag or current HEAD)
- Validates fork point exists
- Checks out fork point
- Creates new branch `autonomy/<strategy-name>`
- Reports success with next steps

**Examples:**
```bash
# Fork from current commit
/fork-iteration experiment-b

# Fork from specific iteration in current branch history
/fork-iteration 0015 experiment-b

# Bootstrap autonomy workflow from non-autonomy branch
git checkout main
/fork-iteration initial-strategy
```

**Output:** Branch created message with next steps (`/start-iteration` to begin work)

**Note:** This creates the branch but does NOT start an iteration. Iteration numbering is handled by `/start-iteration`.

### `/branch-status <branch-name>`

Detailed status report for single autonomy branch.

**Arguments:**
- `branch-name` (required) - Branch name to analyze. `autonomy/` prefix optional (added automatically if missing).

**Process:**
- Normalizes branch name (adds `autonomy/` prefix if missing)
- Validates branch exists
- Dispatches branch-analyzer agent to read all journal commits on branch
- Agent generates Python script to analyze iteration timeline, metrics progression, status changes
- Produces comprehensive report

**Example:**
```bash
/branch-status experiment-a
/branch-status autonomy/experiment-b
```

**Output:**
- Complete iteration timeline with dates and status
- Metrics progression over time (if applicable)
- Blocker history
- Current state assessment
- Recommended next actions

### `/compare-branches <branch-a> <branch-b>`

Compare two autonomy branches to show different approaches and outcomes.

**Arguments:**
- `branch-a` (required) - First branch name. `autonomy/` prefix optional.
- `branch-b` (required) - Second branch name. `autonomy/` prefix optional.

**Process:**
- Normalizes both branch names
- Validates both branches exist
- Uses `git merge-base` to find where branches diverged
- Dispatches branch-analyzer agent for comparative analysis
- Agent generates Python script for comparison
- Produces report showing differences

**Example:**
```bash
/compare-branches experiment-a experiment-b
/compare-branches autonomy/usage-pricing autonomy/flat-enterprise
```

**Output:**
- Where branches diverged (common ancestor)
- Iteration timeline comparison
- Metrics trajectories (if applicable)
- Status comparison
- Different decisions made
- Outcomes on each branch
- Cross-branch learning insights

### `/fork-worktree [iteration] <strategy-name>`

Create new autonomy branch with dedicated worktree for parallel agent workflows.

**Arguments:**
- `iteration` (optional) - Iteration number to fork from (same as `/fork-iteration`)
- `strategy-name` (required) - Name for branch and worktree (kebab-case)

**Process:**
- Detects repository root (works from main repo or within other worktrees)
- Resolves fork point (iteration tag or current HEAD)
- Creates branch `autonomy/<strategy-name>` with worktree at `.worktrees/autonomy/<strategy-name>/`
- All worktrees created at repository root level (no nested worktrees)

**Example:**
```bash
# Fork from current commit
/fork-worktree experiment-b

# Fork from specific iteration
/fork-worktree 0015 experiment-c

# Fork from within another worktree (creates sibling, not nested)
cd .worktrees/autonomy/experiment-a
/fork-worktree experiment-d  # Creates .worktrees/autonomy/experiment-d/ at root
```

**Next steps:**
```bash
cd .worktrees/autonomy/<strategy-name>
/start-iteration
```

**Difference from `/fork-iteration`:**
- `/fork-iteration`: Creates branch in current working directory
- `/fork-worktree`: Creates branch + isolated worktree for parallel work
- Use worktrees for running multiple agents simultaneously

### `/remove-worktree [--force] <strategy-name>`

Safely remove autonomy worktree while preserving branch and history.

**Arguments:**
- `--force` (optional) - Skip uncommitted changes check and force removal
- `strategy-name` (required) - Worktree to remove (without `autonomy/` prefix)

**Process:**
- Detects repository root
- Validates worktree exists
- Checks for uncommitted changes (unless `--force`)
- Removes worktree directory
- Prunes git metadata

**Example:**
```bash
# Safe removal (fails if uncommitted changes)
/remove-worktree experiment-b

# Force removal (discards uncommitted changes)
/remove-worktree --force experiment-b
```

**What gets removed:**
- Worktree directory `.worktrees/autonomy/<strategy-name>/`
- Git worktree metadata

**What persists:**
- Branch `autonomy/<strategy-name>` and all commits
- All iteration tags
- Git history (can checkout branch later or create new worktree)

### `/list-worktrees`

List all autonomy worktrees with status and location.

**Process:**
- Finds all git worktrees
- Filters to autonomy worktrees (`.worktrees/autonomy/`)
- Displays formatted table

**Example output:**
```
Autonomy Worktrees:

Branch                    Path                                      HEAD       Locked
autonomy/experiment-a     .worktrees/autonomy/experiment-a          a1b2c3d
autonomy/experiment-b     .worktrees/autonomy/experiment-b          d4e5f6g    🔒

Total: 2 autonomy worktrees
```

**Note:** This lists worktrees only, not all branches. Use `/list-branches` to see all autonomy branches (including those without worktrees).

## Directory Structure

**Main repository structure:**
```
autonomy/[goal-name]/
├── goal.md                          # Goal definition and metrics
├── summary.md                       # Condensed history (updated every 5 iterations)
├── iteration-0001-YYYY-MM-DD.md    # First iteration journal
├── iteration-0002-YYYY-MM-DD.md    # Second iteration journal
└── iteration-NNNN-YYYY-MM-DD.md    # Nth iteration journal (4-digit numbering)
```

**With worktrees (for parallel agent workflows):**
```
project-root/
├── .git/                            # Git repository metadata
├── .worktrees/                      # Worktree container (gitignored)
│   └── autonomy/                    # Autonomy-specific worktrees
│       ├── experiment-a/            # Worktree for autonomy/experiment-a
│       │   ├── autonomy/
│       │   │   └── goal-name/
│       │   │       ├── goal.md
│       │   │       └── iteration-0001-YYYY-MM-DD.md
│       │   └── [other project files]
│       └── experiment-b/            # Worktree for autonomy/experiment-b
│           └── autonomy/
│               └── goal-name/
│                   └── iteration-0001-YYYY-MM-DD.md
└── autonomy/                        # Main repo autonomy work (optional)
    └── goal-name/
```

**Notes:**
- Iteration numbering: 4-digit zero-padded format (0001-9999) supports up to 9999 iterations
- Each worktree is a complete working copy with own `autonomy/` directory
- All worktrees share same `.git` directory (commits visible across all worktrees)
- Add `.worktrees/` to `.gitignore` to prevent committing worktree directories

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

**Commit format (enhanced for branch management):**
```
journal: [goal-name] iteration NNNN

[2-3 line summary of work completed]

## Journal Summary

[4-6 sentence summary of iteration - what happened, what was learned, what changed]

## Iteration Metadata

Status: [active|blocked|concluded|dead-end]
Metrics: [quantitative metrics or "None"]
Blockers: [critical blockers or "None"]
Next: [next iteration intention]

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>
```

**Enhanced commit metadata:**
- **Status** - Determined from Ending State: active (default), blocked (waiting on dependency), concluded (goal achieved), dead-end (approach invalidated)
- **Metrics** - Quantitative progress indicators extracted from Ending State (e.g., "MRR: $62k (+12%)")
- **Blockers** - Summary of current blockers from journal
- **Next** - Next iteration intention/recommended action

This metadata enables branch management commands to summarize branches without reading journal files.

**Git tag (branch-aware):**
- On autonomy branches: `autonomy/<branch-name>/iteration-NNNN` (e.g., `autonomy/experiment-a/iteration-0015`)
- On non-autonomy branches: `autonomy/<goal-name>/iteration-NNNN` (backward compatibility)
- Each branch has its own iteration namespace
- No tag collisions when multiple branches have same iteration number

**Branch behavior:**
- Commits to current branch (does NOT create new branch)
- Respects your branching strategy
- You control when to merge/push

**Tag benefits:**
- Navigate to iteration on specific branch: `git checkout autonomy/experiment-a/iteration-0042`
- List all iterations on a branch: `git tag -l 'autonomy/experiment-a/*'`
- List all autonomy iterations: `git tag -l 'autonomy/*/*'`
- CI/CD integration: Trigger on `autonomy/*/iteration-*` tags
- Immutable history markers
- Enables branch management queries without reading journal files

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

### `slime-strategy`

Invoked by `/slime` command. Handles:
- Checking if autonomy workflow already exists
- Orchestrating creating-a-goal skill for new goals
- Creating/updating autonomy/CLAUDE.md with slime mold strategy documentation
- Orchestrating forking-iteration skill to create initial branch
- Creating iteration-0000 baseline journal
- Git commit and branch-aware tagging
- Idempotent behavior (only updates CLAUDE.md if goal exists)

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

### `listing-branches`

Invoked by `/list-branches` command. Handles:
- Parsing user's query for sorting/grouping/filtering requirements
- Dispatching branch-analyzer agent with query
- Presenting formatted markdown table of all autonomy branches

### `forking-iteration`

Invoked by `/fork-iteration` command. Handles:
- Parsing and validating strategy name
- Resolving fork point (iteration tag or HEAD)
- Checking out fork point and creating new autonomy branch
- Direct git operations (no agent needed)

### `analyzing-branch-status`

Invoked by `/branch-status` command. Handles:
- Normalizing and validating branch name
- Dispatching branch-analyzer agent for comprehensive analysis
- Presenting detailed status report for single branch

### `comparing-branches`

Invoked by `/compare-branches` command. Handles:
- Normalizing and validating both branch names
- Using git merge-base to find divergence point
- Dispatching branch-analyzer agent for comparative analysis
- Presenting comparison report

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

### `branch-analyzer` (Haiku)

Analyzes autonomy branches via git operations and computational methods. Used by list-branches, branch-status, and compare-branches commands. Handles:
- Reading git log data from autonomy branches
- Parsing enhanced commit message metadata (status, metrics, blockers, next steps)
- Generating Python scripts for computational analysis (sorting, filtering, grouping, comparison)
- Executing Python scripts for precise results (never "eyeball it")
- Formatting output as markdown tables and reports
- Read-only operations (never checks out branches or modifies files)

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
# Start first exploration path using branch management
/fork-iteration experiment-pricing-model-a
/start-iteration
# Intention: "Explore usage-based pricing with tiered caps"
# ... work on this approach ...
/end-iteration

# Start parallel exploration path
/fork-iteration experiment-pricing-model-b
/start-iteration
# Intention: "Explore flat enterprise pricing with seat limits"
# ... work on this approach ...
/end-iteration

# List all branches to see status
/list-branches
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
# Compare approaches to inform new direction
/compare-branches experiment-pricing-model-a experiment-pricing-model-b

# Fork new branch from iteration 0015 (divergence point)
/fork-iteration 0015 experiment-simple-per-unit
/start-iteration
# Intention: "Pure per-unit pricing. Incorporating usage tracking
#             from experiment-a and simplicity from experiment-b."

# Extract specific learnings from each branch
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
# List all autonomy branches with status
/list-branches

# See detailed status of specific branch
/branch-status experiment-a

# Compare two branches
/compare-branches experiment-a experiment-b

# List all iteration tags across all branches
git tag -l 'autonomy/*/*'

# List iterations on specific branch
git tag -l 'autonomy/experiment-a/*'

# View branch divergence points
git log --graph --oneline --all

# Jump to any iteration on any branch
git checkout autonomy/experiment-a/iteration-0042
```

The repository preserves the **entire exploration**, not just the final answer. Future work can mine this history for insights using branch management commands.

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

See the [ed3d-plugins](https://github.com/ed3dai/ed3d-plugins) creating-a-plugin skill for plugin development guidance.

**Testing locally:**
```bash
/plugin install file:///absolute/path/to/autonomy
/plugin reload
/start-iteration
```

## License

MIT - See [LICENSE](../../LICENSE) for details.
