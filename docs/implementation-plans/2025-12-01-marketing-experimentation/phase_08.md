# Marketing Experimentation System Implementation Plan - Phase 8

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

## Phase 8: Documentation, Common Rationalizations, and Summary

### Task 1: Write Common Rationalizations Section

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Phase 6)

**Step 1: Add Common Rationalizations section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

---

## Common Rationalizations

These are rationalizations that lead to failure. When you catch yourself thinking any of these, STOP and follow the skill process instead.

### "I'll skip discovery and just start testing - the concept is obvious"

**Why this fails:** Discovery surfaces assumptions, constraints, and existing assets that dramatically affect experiment design. "Obvious" concepts often hide critical assumptions that need validation.

**Reality:** Market-researcher agent provides current, data-driven validation signals. Asset inventory reveals resources that reduce experiment cost and time. Success criteria definition prevents ambiguous results. Always start with discovery.

**What to do instead:** Complete Phase 1 (Discovery & Asset Inventory) before generating hypotheses. Invoke market-researcher agent. Document all findings.

---

### "I'll design the experiment myself instead of using hypothesis-testing"

**Why this fails:** hypothesis-testing skill provides rigorous experimental design, statistical analysis, and signal detection. Skipping it produces weak experiments with ambiguous results.

**Reality:** Marketing-experimentation is a meta-orchestrator that coordinates multiple hypothesis-testing sessions. It does NOT design experiments itself. Delegation ensures statistical rigor.

**What to do instead:** Invoke hypothesis-testing skill for each experiment in Phase 4. Let hypothesis-testing handle all experimental design, execution, and analysis.

---

### "One experiment is enough to draw conclusions"

**Why this fails:** Single experiments miss cross-experiment patterns. Some tactics work, others don't. Single-experiment campaigns can't identify which channels/tactics are most effective.

**Reality:** Marketing-experimentation tests 2-4 hypotheses to reveal strategic insights. Synthesis (Phase 5) identifies patterns across experiments - which tactics work, which don't, and why.

**What to do instead:** Follow Phase 3 prioritization to select 2-4 hypotheses. Complete all experiments before synthesis. Use Phase 5 to identify patterns.

---

### "I'll wait until all experiments complete before updating the tracker"

**Why this fails:** Batch updates create opportunity for lost data. Multi-day campaigns lose context between conversations. Incomplete tracker leads to missed experiments and confusion.

**Reality:** The experiment tracker (04-experiment-tracker.md) is the ONLY source of truth that persists across sessions. Update it IMMEDIATELY after status changes.

**What to do instead:** Update tracker after every status change (Planned → In Progress, In Progress → Complete). Commit tracker updates to git. Read tracker FIRST in every new conversation.

---

### "Results are obvious, I don't need to document synthesis"

**Why this fails:** Individual experiment signals don't reveal cross-experiment patterns. "Obvious" interpretations miss confounding factors and alternative explanations.

**Reality:** Documented synthesis with presenting-data skill ensures intellectual honesty. Visualization reveals patterns. Statistical assessment identifies robust vs uncertain findings.

**What to do instead:** Always complete Phase 5 (Cross-Experiment Synthesis). Invoke presenting-data skill. Document patterns, visualizations, and signal classification. Get user confirmation.

---

### "I'll form hypotheses in Phase 6 for efficiency"

**Why this fails:** Phase 6 generates IDEAS, not hypotheses. Ideas need discovery (Phase 1) and hypothesis generation (Phase 2) in new sessions. Skipping these steps leads to untested assumptions and vague experiments.

**Reality:** Feed-forward cycle: Phase 6 ideas → new marketing-experimentation session → Phase 1 discovery → Phase 2 hypothesis generation → Phase 3-6 complete cycle.

**What to do instead:** Generate IDEAS in Phase 6. Start NEW marketing-experimentation session with selected idea. Complete Phase 1 and Phase 2 to formalize idea into testable hypotheses.

---

### "I'll estimate ICE/RICE scores mentally instead of running the script"

**Why this fails:** Manual estimation introduces calculation errors and inconsistency. Mental math is unreliable for multiplication and division.

**Reality:** Python scripts ensure exact, reproducible results that can be audited and verified. Computational methods eliminate human error.

**What to do instead:** Use Python scripts (ICE or RICE calculator) from Phase 3 instructions. Update hypothesis data in script. Run script and document exact scores. Copy output table to prioritization document.

---

### "I'll synthesize results mentally - no need to use presenting-data"

**Why this fails:** Mental synthesis loses details and creates false confidence. Cross-experiment patterns require systematic analysis.

**Reality:** presenting-data skill handles pattern identification (via interpreting-results), visualization creation (via creating-visualizations), and synthesis documentation. It ensures intellectual honesty and reproducibility.

**What to do instead:** Always invoke presenting-data skill in Phase 5. Provide aggregate results table. Request pattern analysis and visualizations. Document all findings from presenting-data output.

---
```

**Step 2: Verify Common Rationalizations section**

Run: `grep -c "### \"" .claude/skills/marketing-experimentation/SKILL.md`

Expected: 8 rationalizations (exceeds requirement of 6)

**Step 3: Verify each rationalization has structure**

Run:
```bash
grep -c "**Why this fails:**" .claude/skills/marketing-experimentation/SKILL.md
grep -c "**Reality:**" .claude/skills/marketing-experimentation/SKILL.md
grep -c "**What to do instead:**" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: 8 of each (one per rationalization)

**Step 4: Commit Common Rationalizations section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add Common Rationalizations section to marketing-experimentation

Document 8 common rationalizations with structured refutations
(Why this fails, Reality, What to do instead). Covers discovery,
hypothesis-testing delegation, multi-experiment testing, tracker
updates, synthesis, ideas vs hypotheses, computational scoring,
and presenting-data usage.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 2: Write Summary Section

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Common Rationalizations)

**Step 1: Add Summary section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

## Summary

The marketing-experimentation skill ensures rigorous, evidence-based validation of marketing concepts through structured experimental cycles. This skill orchestrates the complete Build-Measure-Learn loop from concept to data-driven signal.

**What this skill ensures:**

1. **Validated concepts through market research** - market-researcher agent provides current demand signals, competitive landscape analysis, and audience insights before experimentation begins.

2. **Strategic hypothesis generation** - 5-10 testable hypotheses spanning multiple tactics (landing pages, ads, email, content) grounded in discovery findings and mapped to experimentation frameworks (Lean Startup, AARRR).

3. **Data-driven prioritization** - Computational methods (ICE/RICE Python scripts) ensure exact, reproducible scoring. Selection of 2-4 highest-value hypotheses optimizes resource allocation.

4. **Multi-experiment coordination** - Experiment tracker (living document) enables multi-conversation workflows spanning days or weeks. Status tracking (Planned, In Progress, Complete) maintains visibility across all experiments.

5. **Statistical rigor through delegation** - hypothesis-testing skill handles individual experiment design, execution, and analysis. Marketing-experimentation coordinates multiple tests without duplicating statistical methodology.

6. **Cross-experiment synthesis** - presenting-data skill identifies patterns across experiments (what works, what doesn't, what's unclear). Aggregate analysis reveals strategic insights invisible in single experiments.

7. **Clear signal generation** - Campaign-level classification (Positive/Negative/Null/Mixed) with strategic recommendations (Scale/Pivot/Refine/Pause) provides actionable guidance for stakeholders.

8. **Systematic iteration** - Phase 6 generates experiment IDEAS (not hypotheses) that feed into new marketing-experimentation sessions. Feed-forward cycle maintains rigor through repeated discovery and hypothesis generation.

9. **Multi-conversation persistence** - Complete documentation at every phase enables resumption after days or weeks. Experiment tracker serves as coordination hub. All artifacts are git-committable.

10. **Tool-agnostic approach** - Focuses on techniques (value proposition testing, targeting strategies, sequence optimization) rather than specific platforms. Applicable across marketing tools and channels.

**Key principles:**
- Discovery before experimentation (Phase 1 always first)
- Hypothesis generation separate from idea generation (Phase 2 vs Phase 6)
- Multiple experiments for pattern identification (2-4 minimum)
- Computational scoring for objectivity (Python scripts)
- Delegation for statistical rigor (hypothesis-testing skill)
- Synthesis for strategic insight (presenting-data skill)
- Documentation for reproducibility (numbered markdown files, git commits)
- Iteration through validated cycles (ideas → new sessions → discovery → hypotheses)
```

**Step 2: Verify Summary section**

Run: `grep "## Summary" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Summary section present

**Step 3: Count key principles**

Run: `sed -n '/## Summary/,/^##/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "^[0-9]\. \*\*"`

Expected: 10 "What this skill ensures" items

**Step 4: Commit Summary section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add Summary section to marketing-experimentation

Document 10 key capabilities and 8 core principles of the skill.
Summarizes validated concepts, hypothesis generation, prioritization,
coordination, delegation, synthesis, signal generation, iteration,
persistence, and tool-agnostic approach.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 3: Update CLAUDE.md to Reference marketing-experimentation

**Files:**
- Modify: `.claude/skills/CLAUDE.md`

**Step 1: Read CLAUDE.md to find Process Skills section**

Run: `grep -n "## Process Skills" .claude/skills/CLAUDE.md`

Expected: Shows line number of Process Skills section

**Step 2: Add marketing-experimentation to Process Skills section**

After the existing process skills (exploratory-analysis, guided-investigation, hypothesis-testing, comparative-analysis), add:

```markdown

**`marketing-experimentation`** - Validate marketing concepts through rigorous experimental cycles
- **When to use:** Testing marketing ideas, business concepts, or campaign strategies
- **Phases:** Discovery → Hypothesis Generation → Prioritization → Experiment Coordination → Synthesis → Iteration Planning
- **Prerequisites:** None initially (qualitative market research), data needs emerge from experiments
- **Location:** `.claude/skills/marketing-experimentation/SKILL.md`
```

**Step 3: Verify addition to CLAUDE.md**

Run: `grep "marketing-experimentation" .claude/skills/CLAUDE.md`

Expected: Returns match showing marketing-experimentation entry

**Step 4: Commit CLAUDE.md update**

```bash
git add .claude/skills/CLAUDE.md
git commit -m "docs: add marketing-experimentation to CLAUDE.md process skills

Add marketing-experimentation to process skills table with description,
when to use, phases, prerequisites, and location. Documents skill as
complete and ready for use.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 4: Verify Phase 8 Completion

**Step 1: Verify Common Rationalizations section has at least 6 entries**

Run: `grep -c "### \"" .claude/skills/marketing-experimentation/SKILL.md`

Expected: 8 rationalizations (exceeds requirement)

**Step 2: Verify Summary section captures key principles**

Run: `grep -A 50 "## Summary" .claude/skills/marketing-experimentation/SKILL.md | grep -c "\*\*Key principles:\*\*"`

Expected: 1 (Key principles section present)

**Step 3: Verify CLAUDE.md references marketing-experimentation**

Run: `grep -c "marketing-experimentation" .claude/skills/CLAUDE.md`

Expected: At least 1 reference in Process Skills section

**Step 4: Verify skill is complete**

Run:
```bash
# Check all 6 phases are documented
grep -c "## Phase [1-6]:" .claude/skills/marketing-experimentation/SKILL.md

# Check all 6 templates exist
ls .claude/skills/marketing-experimentation/templates/*.md | wc -l

# Check Common Rationalizations exists
grep "## Common Rationalizations" .claude/skills/marketing-experimentation/SKILL.md

# Check Summary exists
grep "## Summary" .claude/skills/marketing-experimentation/SKILL.md

# Check market-researcher agent exists
ls .claude/agents/market-researcher.md
```

Expected: 6 phases documented, 6 templates exist, both sections present, agent exists

**Step 5: Count total lines in SKILL.md**

Run: `wc -l .claude/skills/marketing-experimentation/SKILL.md`

Expected: Comprehensive skill file (500+ lines estimated)

**Phase 8 Checkpoint Requirements:**
- ✓ Common Rationalizations section has 8 entries (exceeds requirement of 6)
- ✓ Each rationalization has structured refutation (Why fails, Reality, What to do)
- ✓ Summary section captures 10 key capabilities and 8 core principles
- ✓ CLAUDE.md references marketing-experimentation in Process Skills section
- ✓ Skill is complete and ready for use:
  - All 6 phases documented with checkpoints and instructions
  - All 6 templates created in templates/ directory
  - market-researcher agent implemented
  - Common Rationalizations documented
  - Summary completed
  - CLAUDE.md updated

---

## Implementation Complete

All 8 phases of the marketing experimentation system implementation are complete:

1. ✅ Phase 1: Skill structure and core documentation
2. ✅ Phase 2: Phases 1-2 documented (Discovery, Hypothesis Generation)
3. ✅ Phase 3: Phases 3-4 documented (Prioritization, Experiment Coordination)
4. ✅ Phase 4: Phases 5-6 documented (Synthesis, Iteration)
5. ✅ Phase 5: market-researcher agent created
6. ✅ Phase 6: Templates 01-03 created
7. ✅ Phase 7: Templates 04-06 created
8. ✅ Phase 8: Documentation, rationalizations, summary complete

**Files created:**
- `.claude/skills/marketing-experimentation/SKILL.md` - Complete skill documentation
- `.claude/skills/marketing-experimentation/templates/01-discovery.md`
- `.claude/skills/marketing-experimentation/templates/02-hypothesis-generation.md`
- `.claude/skills/marketing-experimentation/templates/03-prioritization.md`
- `.claude/skills/marketing-experimentation/templates/04-experiment-tracker.md`
- `.claude/skills/marketing-experimentation/templates/05-synthesis.md`
- `.claude/skills/marketing-experimentation/templates/06-iteration-plan.md`
- `.claude/agents/market-researcher.md` - Market research agent
- `.claude/skills/CLAUDE.md` - Updated with marketing-experimentation reference

**Ready for execution using:** `superpowers:subagent-driven-development`
