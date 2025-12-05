# Marketing Experimentation System Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Build marketing experimentation skill system for validating business ideas through rigorous experimental cycles

**Architecture:** Meta-orchestrator skill that coordinates multiple hypothesis-testing sessions and synthesizes results across experiments. Delegates to hypothesis-testing for individual experiments, uses interpreting-results and creating-visualizations for synthesis.

**Tech Stack:**
- DataPeeker skill architecture (SKILL.md + templates/)
- YAML frontmatter for metadata
- Markdown for documentation
- Git for version control
- Sub-agent delegation (market-researcher agent with Haiku model)

**Scope:** 8 phases from original design (complete implementation)

**Codebase verified:** 2025-12-01

---

## Phase 1: Create Skill Structure and Core Documentation

### Task 1: Create Directory Structure

**Files:**
- Create: `.claude/skills/marketing-experimentation/` directory
- Create: `.claude/skills/marketing-experimentation/templates/` directory

**Step 1: Create skill directory**

```bash
mkdir -p .claude/skills/marketing-experimentation/templates
```

**Step 2: Verify directory creation**

Run: `ls -la .claude/skills/marketing-experimentation/`

Expected output:
```
total 0
drwxr-xr-x  3 user  staff   96 Dec  1 10:00 .
drwxr-xr-x  N user  staff  NNN Dec  1 10:00 ..
drwxr-xr-x  2 user  staff   64 Dec  1 10:00 templates
```

**Step 3: Commit directory structure**

```bash
git add .claude/skills/marketing-experimentation/
git commit -m "feat: create marketing-experimentation skill directory structure

Create base directory structure for marketing-experimentation skill
following DataPeeker skill architecture patterns.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 2: Create Skill File with Frontmatter

**Files:**
- Create: `.claude/skills/marketing-experimentation/SKILL.md`

**Step 1: Create SKILL.md with frontmatter**

Create `.claude/skills/marketing-experimentation/SKILL.md` with the following content:

```markdown
---
name: marketing-experimentation
description: Systematic marketing experimentation process - discover concepts, generate hypotheses, coordinate multiple experiments, synthesize results, generate next-iteration ideas through rigorous validation cycles
---
```

**Step 2: Verify file creation and frontmatter format**

Run: `head -n 5 .claude/skills/marketing-experimentation/SKILL.md`

Expected output:
```markdown
---
name: marketing-experimentation
description: Systematic marketing experimentation process - discover concepts, generate hypotheses, coordinate multiple experiments, synthesize results, generate next-iteration ideas through rigorous validation cycles
---
```

**Step 3: Commit skill file with frontmatter**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "feat: add marketing-experimentation skill frontmatter

Add YAML frontmatter following DataPeeker skill pattern with name
and description fields.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 3: Write Overview Section

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after frontmatter)

**Step 1: Add Overview section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

# Marketing Experimentation

## Overview

Use this skill when you need to validate marketing concepts or business ideas through rigorous experimental cycles. This skill orchestrates the complete Build-Measure-Learn cycle from concept to data-driven signal.

**When to use this skill:**
- You have a marketing concept or business idea that needs validation
- You want to test multiple related hypotheses systematically
- You need to integrate results across multiple experiments
- You're designing the next iteration based on experimental evidence
- You're conducting qualitative market research combined with quantitative testing

**What this skill does:**
- Validates concepts through market research before experimentation
- Generates multiple testable hypotheses from marketing ideas
- Coordinates multiple hypothesis-testing sessions (delegates to hypothesis-testing skill)
- Synthesizes results across experiments using interpreting-results and creating-visualizations
- Produces clear signals (positive/negative/null/mixed) for each campaign
- Generates actionable next-iteration ideas based on experimental evidence

**What this skill does NOT do:**
- Design individual experiments (delegates to hypothesis-testing skill)
- Execute statistical analysis directly (uses hypothesis-testing for rigor)
- Operationalize successful ideas (focuses on validation, not scaling)
- Platform-specific implementation (tool-agnostic techniques only)

**Integration with existing skills:**
- **Delegates to `hypothesis-testing`** for individual experiment design and execution
- **Uses `interpreting-results`** to synthesize findings across multiple experiments
- **Uses `creating-visualizations`** to communicate aggregate results
- **Invokes `market-researcher` agent** for concept validation via internet research

**Multi-conversation persistence:**
This skill is designed for campaigns spanning days or weeks. Each phase documents completely enough that new conversations can resume after extended breaks. The experiment tracker (04-experiment-tracker.md) serves as the living coordination hub.
```

**Step 2: Verify Overview section**

Run: `grep -A 5 "## Overview" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Overview section with "When to use this skill" and integration explanations

**Step 3: Commit Overview section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add marketing-experimentation skill overview

Document skill purpose, when to use it, what it does/doesn't do,
and integration patterns with hypothesis-testing and other skills.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 4: Write Prerequisites Section

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Overview)

**Step 1: Add Prerequisites section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

## Prerequisites

**Required skills:**
- `hypothesis-testing` - Individual experiment design and execution (invoked once per hypothesis)
- `interpreting-results` - Result synthesis and pattern identification (invoked in Phase 5)
- `creating-visualizations` - Aggregate result visualization (invoked in Phase 5)

**Required agents:**
- `market-researcher` - Concept validation via internet research (invoked in Phase 1)

**Required knowledge:**
- Understanding of Lean Startup Build-Measure-Learn cycle
- Familiarity with marketing tactics (landing pages, ads, email, content)
- Basic experimental design principles (control/treatment, signals, metrics)

**Data requirements:**
- None initially (market research is qualitative)
- Data requirements emerge from experiment design in Phase 4
- Each hypothesis-testing session will specify its own data needs
```

**Step 2: Verify Prerequisites section**

Run: `grep -A 15 "## Prerequisites" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Prerequisites section listing hypothesis-testing, interpreting-results, creating-visualizations, and market-researcher

**Step 3: Commit Prerequisites section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add marketing-experimentation prerequisites

List required skills (hypothesis-testing, interpreting-results,
creating-visualizations), required agents (market-researcher),
and data requirements.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 5: Write Mandatory Process Structure Section

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Prerequisites)

**Step 1: Add Mandatory Process Structure section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

## Mandatory Process Structure

**CRITICAL:** This is a 6-phase process skill. You MUST complete all phases in order. Use TodoWrite to track progress through each phase.

**TodoWrite template:**

When starting a marketing-experimentation session, create these todos:

```markdown
- [ ] Phase 1: Discovery & Asset Inventory
- [ ] Phase 2: Hypothesis Generation
- [ ] Phase 3: Prioritization
- [ ] Phase 4: Experiment Coordination
- [ ] Phase 5: Cross-Experiment Synthesis
- [ ] Phase 6: Iteration Planning
```

**Workspace structure:**

All work for a marketing-experimentation session is saved to:
```
analysis/marketing-experimentation/[campaign-name]/
├── 01-discovery.md
├── 02-hypothesis-generation.md
├── 03-prioritization.md
├── 04-experiment-tracker.md
├── 05-synthesis.md
├── 06-iteration-plan.md
└── experiments/
    ├── [experiment-1]/               # hypothesis-testing session
    ├── [experiment-2]/               # hypothesis-testing session
    └── [experiment-3]/               # hypothesis-testing session
```

**Phase progression rules:**
1. Each phase has a CHECKPOINT with verification requirements
2. You MUST satisfy all checkpoint requirements before proceeding to the next phase
3. Document every decision with rationale in the numbered markdown files
4. Commit markdown files after each phase completes
5. The experiment tracker (04-experiment-tracker.md) is a LIVING DOCUMENT - update it throughout Phase 4

**Multi-conversation resumption:**
- At the start of any conversation, check if an experiment tracker exists for this campaign
- If it exists, read it first to understand current experiment status
- Update the tracker as experiments progress
- All phases should be complete enough to resume after days or weeks
```

**Step 2: Verify Mandatory Process Structure section**

Run: `grep -A 10 "## Mandatory Process Structure" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Mandatory Process Structure section with TodoWrite template and 6 phases listed

**Step 3: Commit Mandatory Process Structure section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add marketing-experimentation mandatory process structure

Document 6-phase workflow, TodoWrite template, workspace structure,
phase progression rules, and multi-conversation resumption strategy.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 6: Verify Phase 1 Completion

**Step 1: Verify all Phase 1 components exist**

Run the following verification commands:

```bash
# Check directory structure
ls -la .claude/skills/marketing-experimentation/
ls -la .claude/skills/marketing-experimentation/templates/

# Check SKILL.md sections
grep "^---$" .claude/skills/marketing-experimentation/SKILL.md
grep "^# Marketing Experimentation$" .claude/skills/marketing-experimentation/SKILL.md
grep "^## Overview$" .claude/skills/marketing-experimentation/SKILL.md
grep "^## Prerequisites$" .claude/skills/marketing-experimentation/SKILL.md
grep "^## Mandatory Process Structure$" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: All grep commands return matches (exit code 0)

**Step 2: Verify frontmatter format**

Run: `python3 -c "import yaml; yaml.safe_load(open('.claude/skills/marketing-experimentation/SKILL.md').read().split('---')[1])"`

Expected: No YAML parsing errors (command exits successfully)

**Step 3: Count lines in SKILL.md**

Run: `wc -l .claude/skills/marketing-experimentation/SKILL.md`

Expected: Approximately 80-100 lines (frontmatter + Overview + Prerequisites + Mandatory Process Structure)

**Phase 1 Checkpoint Requirements:**
- ✓ Skill file exists with valid YAML frontmatter
- ✓ Overview section explains purpose and integration with hypothesis-testing
- ✓ Prerequisites list all required skills (hypothesis-testing, interpreting-results, creating-visualizations)
- ✓ Prerequisites list market-researcher agent
- ✓ TodoWrite template matches 6-phase structure
- ✓ Workspace structure documented
- ✓ Phase progression rules documented
