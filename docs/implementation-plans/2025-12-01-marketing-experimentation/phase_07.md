# Marketing Experimentation System Implementation Plan - Phase 7

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

## Phase 7: Create Phase Templates (04-06)

### Task 1: Create Template 04-experiment-tracker.md

**Files:**
- Create: `.claude/skills/marketing-experimentation/templates/04-experiment-tracker.md`

**Step 1: Create 04-experiment-tracker.md template**

Create `.claude/skills/marketing-experimentation/templates/04-experiment-tracker.md`:

```markdown
# Experiment Tracker

**Campaign:** [Campaign name]

**Created:** [YYYY-MM-DD]

**Last Updated:** [YYYY-MM-DD]

---

## Overview

This is a LIVING DOCUMENT that tracks all experiments in this marketing-experimentation campaign. Update this file as experiments progress through their lifecycle.

**Status Types:**
- **Planned:** Experiment selected, not yet started
- **In Progress:** hypothesis-testing skill currently executing
- **Complete:** All phases done, signal documented

**Multi-Conversation Resumption:**
At the start of any conversation, READ THIS FILE FIRST to understand current experiment status.

---

## Experiment 1: [Hypothesis Brief Name]

**Status:** Planned

**Hypothesis:** [Full hypothesis statement from Phase 2]

**Tactic/Channel:** [landing page | ads | email | content | social | SEO | other]

**Priority Score:** [ICE/RICE score from Phase 3]

**Start Date:** Not started

**Completion Date:** N/A

**Location:** `analysis/marketing-experimentation/[campaign-name]/experiments/[experiment-1-name]/`

**Signal:** Not analyzed

**Key Findings:**
- TBD

**Notes:**
- [Any relevant notes about dependencies, prerequisites, blockers]

---

## Experiment 2: [Hypothesis Brief Name]

**Status:** Planned

**Hypothesis:** [Full hypothesis statement from Phase 2]

**Tactic/Channel:** [tactic/channel]

**Priority Score:** [ICE/RICE score]

**Start Date:** Not started

**Completion Date:** N/A

**Location:** `analysis/marketing-experimentation/[campaign-name]/experiments/[experiment-2-name]/`

**Signal:** Not analyzed

**Key Findings:**
- TBD

**Notes:**
- [Notes]

---

## Experiment 3: [Hypothesis Brief Name]

**Status:** Planned

**Hypothesis:** [Full hypothesis statement from Phase 2]

**Tactic/Channel:** [tactic/channel]

**Priority Score:** [ICE/RICE score]

**Start Date:** Not started

**Completion Date:** N/A

**Location:** `analysis/marketing-experimentation/[campaign-name]/experiments/[experiment-3-name]/`

**Signal:** Not analyzed

**Key Findings:**
- TBD

**Notes:**
- [Notes]

---

## Experiment 4: [Hypothesis Brief Name] (if applicable)

[Same structure as above]

---

## Completion Summary

**Experiments Planned:** [count]

**Experiments In Progress:** [count]

**Experiments Complete:** [count]

**Ready for Synthesis:** [Yes when all complete | No - [count] remaining]
```

**Step 2: Verify template creation**

Run: `ls .claude/skills/marketing-experimentation/templates/04-experiment-tracker.md`

Expected: File exists

**Step 3: Verify experiment entry structure**

Run: `grep -c "**Status:**" .claude/skills/marketing-experimentation/templates/04-experiment-tracker.md`

Expected: 3+ entries (one per experiment example)

**Step 4: Verify living document instructions**

Run: `grep "LIVING DOCUMENT" .claude/skills/marketing-experimentation/templates/04-experiment-tracker.md`

Expected: Living document instructions present

**Step 5: Commit template**

```bash
git add .claude/skills/marketing-experimentation/templates/04-experiment-tracker.md
git commit -m "feat: add 04-experiment-tracker.md template for marketing-experimentation

Create Phase 4 template with experiment entry structure (status, dates,
location, signal, findings), status types, living document instructions,
and multi-conversation resumption guidance.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 2: Create Template 05-synthesis.md

**Files:**
- Create: `.claude/skills/marketing-experimentation/templates/05-synthesis.md`

**Step 1: Create 05-synthesis.md template**

Create `.claude/skills/marketing-experimentation/templates/05-synthesis.md`:

```markdown
# Cross-Experiment Synthesis

**Campaign:** [Campaign name]

**Experiments Analyzed:** [Count from experiment tracker]

**Analysis Date:** [YYYY-MM-DD]

---

## Executive Summary

[2-3 sentence summary of overall campaign findings]

**Overall Campaign Signal:** [Positive | Negative | Null | Mixed]

**Strategic Recommendation:** [Scale | Pivot | Refine | Pause/Abandon]

---

## Aggregate Results Table

| Experiment | Hypothesis | Tactic | Signal | Key Metric | Result | Confidence |
|------------|------------|--------|--------|------------|--------|------------|
| E1 | [Brief hypothesis] | [tactic] | [Positive/Negative/Null/Mixed] | [metric] | [e.g., +18%] | [High/Medium/Low] |
| E2 | [Brief hypothesis] | [tactic] | [signal] | [metric] | [result] | [confidence] |
| E3 | [Brief hypothesis] | [tactic] | [signal] | [metric] | [result] | [confidence] |
| ... | ... | ... | ... | ... | ... | ... |

**Signal Distribution:**
- Positive: [count] experiments
- Negative: [count] experiments
- Null: [count] experiments
- Mixed: [count] experiments

---

## Pattern Analysis

### What Worked (Positive Signals)

**Experiments:**
- E[#]: [Brief description of experiment and result]
- E[#]: [Brief description of experiment and result]

**Why These Worked:**
[Analysis from presenting-data skill explaining commonalities and reasons for success]

**Common Characteristics:**
- [Characteristic 1 across successful experiments]
- [Characteristic 2]
- [Characteristic 3]

---

### What Didn't Work (Negative Signals)

**Experiments:**
- E[#]: [Brief description of experiment and result]
- E[#]: [Brief description of experiment and result]

**Why These Failed:**
[Analysis from presenting-data skill explaining reasons for failure]

**Lessons Learned:**
- [Lesson 1 from failed experiments]
- [Lesson 2]
- [Lesson 3]

---

### What's Unclear (Null/Mixed Signals)

**Experiments:**
- E[#]: [Brief description of experiment and result]
- E[#]: [Brief description of experiment and result]

**Potential Reasons for Inconclusive Results:**
[Analysis from presenting-data skill]

**Recommendations for Further Investigation:**
- [Investigation recommendation 1]
- [Investigation recommendation 2]

---

## Cross-Experiment Patterns

**Tactic Performance:**
[Do results cluster by tactic? Which tactics performed best/worst?]

**Audience Segments:**
[Do results vary by audience segment? Which segments responded best?]

**Timing/Seasonality:**
[Do results show temporal patterns? Were some experiments affected by timing?]

**Confounding Factors:**
[Were there external factors (market conditions, holidays, competitors) affecting multiple experiments?]

**Confidence Assessment:**
[Which findings are robust? Which are uncertain? Where is more data needed?]

---

## Visualizations

[Output from presenting-data skill]

### Signal Distribution

```
[Visualization or description of signal distribution across experiments]
```

### Effect Sizes by Experiment

```
[Visualization or description of effect magnitudes]
```

### Confidence Levels

```
[Visualization showing effect size vs. confidence for each experiment]
```

### Tactic Performance Comparison

```
[Visualization comparing performance across tactics/channels]
```

---

## Overall Campaign Signal Classification

**Signal:** [Positive | Negative | Null | Mixed]

**Rationale:**

**Positive Campaign:**
[If positive: Multiple experiments validated concept, successful tactics identified, clear path to ROI]

**Negative Campaign:**
[If negative: Multiple experiments invalidated concept, no successful tactics, concept doesn't resonate]

**Null Campaign:**
[If null: Most experiments inconclusive, insufficient power or confounding factors, needs refinement]

**Mixed Campaign:**
[If mixed: Some tactics work, some don't, selective scaling and pivots needed]

---

## Synthesis Sources

[References to individual hypothesis-testing session locations]

- Experiment 1: `[location from tracker]`
- Experiment 2: `[location from tracker]`
- Experiment 3: `[location from tracker]`

**presenting-data Output:** [Reference to any slides, whitepapers, or visualizations created]

---

## Next Steps

Proceed to Phase 6 (Iteration Planning) to generate new experiment ideas based on these findings.
```

**Step 2: Verify template creation**

Run: `ls .claude/skills/marketing-experimentation/templates/05-synthesis.md`

Expected: File exists

**Step 3: Verify aggregate results table structure**

Run: `grep -A 5 "## Aggregate Results Table" .claude/skills/marketing-experimentation/templates/05-synthesis.md`

Expected: Shows table with Experiment, Hypothesis, Tactic, Signal, etc. columns

**Step 4: Verify pattern analysis sections**

Run:
```bash
grep "### What Worked" .claude/skills/marketing-experimentation/templates/05-synthesis.md
grep "### What Didn't Work" .claude/skills/marketing-experimentation/templates/05-synthesis.md
grep "### What's Unclear" .claude/skills/marketing-experimentation/templates/05-synthesis.md
```

Expected: All three pattern sections present

**Step 5: Verify visualization placeholders**

Run: `grep -c "Visualization" .claude/skills/marketing-experimentation/templates/05-synthesis.md`

Expected: Multiple visualization sections (4+)

**Step 6: Verify signal classification section**

Run: `grep "## Overall Campaign Signal Classification" .claude/skills/marketing-experimentation/templates/05-synthesis.md`

Expected: Signal classification section present

**Step 7: Commit template**

```bash
git add .claude/skills/marketing-experimentation/templates/05-synthesis.md
git commit -m "feat: add 05-synthesis.md template for marketing-experimentation

Create Phase 5 template with aggregate results table, pattern analysis
(what worked/didn't/unclear), cross-experiment patterns, visualization
placeholders, signal classification, and presenting-data references.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 3: Create Template 06-iteration-plan.md

**Files:**
- Create: `.claude/skills/marketing-experimentation/templates/06-iteration-plan.md`

**Step 1: Create 06-iteration-plan.md template**

Create `.claude/skills/marketing-experimentation/templates/06-iteration-plan.md`:

```markdown
# Iteration Planning

**Campaign:** [Campaign name]

**Based on Synthesis:** [Reference to 05-synthesis.md]

**Planning Date:** [YYYY-MM-DD]

---

## Campaign Summary

**Overall Signal:** [Positive | Negative | Null | Mixed]

**Key Wins:**
- [Successful tactic 1 with result]
- [Successful tactic 2 with result]

**Key Learnings:**
- [Learning 1 regardless of signal]
- [Learning 2 regardless of signal]
- [Learning 3 regardless of signal]

**Strategic Recommendation:** [What to do next based on signal]

---

## New Experiment Ideas

**IMPORTANT:** These are IDEAS, not hypotheses. Each idea must go through a new marketing-experimentation session (Phase 1: Discovery, Phase 2: Hypothesis Generation) before testing.

---

### Idea 1: [Brief descriptive name]

**Category:** Scale Winners

**Rationale:** [Why this idea based on synthesis findings]

**Expected Learning:** [What we'll learn from testing this idea]

**Based on:** [Which successful experiment(s) this builds on]

**Example:**
Scale value prop landing page to paid ads - E1 showed +18% conversion from simplified value prop. Apply winning message to ad creative to test if it improves ad CTR and cost-per-conversion.

---

### Idea 2: [Brief descriptive name]

**Category:** Investigate Nulls

**Rationale:** [Why this idea]

**Expected Learning:** [What we'll learn]

**Based on:** [Which null/mixed result this investigates]

**Example:**
Investigate email sequence timing sensitivity - E3 showed negative result but timing may be confound (sent during holidays). Retest to determine if sequence is inherently weak or if timing was the issue.

---

### Idea 3: [Brief descriptive name]

**Category:** Pivot from Failures

**Rationale:** [Why this idea]

**Expected Learning:** [What we'll learn]

**Based on:** [Which failed experiment this pivots from]

**Example:**
Pivot from broad ad targeting to lookalike audiences - E2 showed null result for broad targeting. Pivot to lookalike audiences based on E1 converters to test if targeting precision improves results.

---

### Idea 4: [Brief descriptive name]

**Category:** [Scale Winners | Investigate Nulls | Pivot from Failures | Explore New]

**Rationale:** [Why this idea]

**Expected Learning:** [What we'll learn]

**Based on:** [Relevant experiment or new direction]

---

### Idea 5: [Brief descriptive name]

[Same structure as above]

---

[Add Ideas 6-7 if applicable]

---

## Idea Categorization Summary

**Scale Winners:** [count] ideas
- [List idea numbers/names that scale successful tactics]

**Investigate Nulls:** [count] ideas
- [List idea numbers/names that investigate inconclusive results]

**Pivot from Failures:** [count] ideas
- [List idea numbers/names that pivot from negative results]

**Explore New:** [count] ideas
- [List idea numbers/names that test entirely new directions]

---

## Strategic Recommendations by Signal

[Select the appropriate section based on Overall Campaign Signal]

### For Positive Signal Campaigns:

**Recommendation: Proceed to Scaling**

**Actions:**
- Increase budget/effort on winning tactics ([list specific tactics])
- Apply winning patterns to new channels ([suggest channels])
- Optimize successful approaches for incremental gains

**Priority Ideas to Pursue:**
- [Idea # - Scale Winners category]
- [Idea # - Scale Winners category]

---

### For Negative Signal Campaigns:

**Recommendation: Major Pivot or Pause**

**Actions:**
- Pivot: Major change in approach, audience, or value proposition
- Pause: Reassess concept before additional investment
- Consider: Alternative concepts if no viable path forward

**Priority Ideas to Pursue:**
- [Idea # - Pivot from Failures category]
- [Idea # - Explore New category]

---

### For Null Signal Campaigns:

**Recommendation: Refine and Reinvestigate**

**Actions:**
- Redesign experiments with better power/clarity
- Address confounding factors identified in synthesis
- Extend observation periods if time-dependent

**Priority Ideas to Pursue:**
- [Idea # - Investigate Nulls category]
- [Idea # - improved versions of previous experiments]

---

### For Mixed Signal Campaigns:

**Recommendation: Selective Scaling + Strategic Pivots**

**Actions:**
- Double down on winners ([list successful tactics])
- Abandon or redesign losers ([list failed tactics])
- Focus next tests on promising areas

**Priority Ideas to Pursue:**
- [Idea # - Scale Winners for successful tactics]
- [Idea # - Pivot from Failures for unsuccessful tactics]

---

## Feed-Forward Pattern

**CRITICAL:** Ideas from this phase are NOT ready for testing. They MUST go through a new marketing-experimentation session.

### How Ideas Become Experiments:

```
Phase 6 generates IDEAS (this document)
         ↓
Start NEW marketing-experimentation session with selected idea
         ↓
Phase 1: Discovery & Asset Inventory
    - Invoke market-researcher agent to validate idea
    - Inventory assets for implementing idea
    - Define success criteria
         ↓
Phase 2: Hypothesis Generation
    - Formalize idea into 5-10 specific, testable hypotheses
    - Map hypotheses to tactics and expected outcomes
         ↓
Phases 3-6: Complete full experimental cycle
    - Prioritize hypotheses (Phase 3)
    - Coordinate experiments (Phase 4)
    - Synthesize results (Phase 5)
    - Generate next iteration ideas (Phase 6)
```

**Why This Matters:**
- Ideas need market validation before testing (Phase 1)
- Ideas need formalization into specific hypotheses (Phase 2)
- Skipping discovery leads to untested assumptions
- Skipping hypothesis generation leads to vague experiments

**Example Flow:**

1. Phase 6 generates: "Scale value prop to ads" (idea)
2. Start new marketing-experimentation session
3. Phase 1: Research ad platform best practices, inventory ad assets
4. Phase 2: Generate hypotheses:
   - H1: Simplified value prop in ad headline increases CTR by 10%+
   - H2: Value prop in ad body copy increases conversion rate by 15%+
   - H3: Value prop as video script improves engagement by 20%+
5. Continue with Phases 3-6 to test formal hypotheses

---

## Next Steps

**Immediate:**
- Review iteration ideas with stakeholders
- Select 1-2 highest-priority ideas to pursue
- Decide: Start new marketing-experimentation session OR conclude campaign

**If Starting New Session:**
- Choose idea from this list
- Begin with Phase 1: Discovery & Asset Inventory
- Use market-researcher agent to validate selected idea
- Do NOT skip to Phase 2 - always start with Phase 1

**If Concluding Campaign:**
- Archive all analysis files
- Document key learnings in campaign retrospective
- Share synthesis findings with relevant teams
- Update knowledge base with validated tactics
```

**Step 2: Verify template creation**

Run: `ls .claude/skills/marketing-experimentation/templates/06-iteration-plan.md`

Expected: File exists

**Step 3: Verify ideas structure (not hypotheses)**

Run:
```bash
grep "These are IDEAS, not hypotheses" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
grep -c "### Idea [0-9]:" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
```

Expected: Warning present, 5+ idea entries

**Step 4: Verify idea categorization**

Run:
```bash
grep "**Category:** Scale Winners" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
grep "**Category:** Investigate Nulls" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
grep "**Category:** Pivot from Failures" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
```

Expected: All three categories present in examples

**Step 5: Verify feed-forward pattern section**

Run: `grep -A 20 "## Feed-Forward Pattern" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md`

Expected: Shows complete feed-forward cycle with arrows and phase flow

**Step 6: Verify strategic recommendations section**

Run:
```bash
grep "### For Positive Signal" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
grep "### For Negative Signal" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
grep "### For Null Signal" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
grep "### For Mixed Signal" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
```

Expected: All four signal-specific recommendation sections present

**Step 7: Commit template**

```bash
git add .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
git commit -m "feat: add 06-iteration-plan.md template for marketing-experimentation

Create Phase 6 template with experiment IDEAS (not hypotheses), idea
categorization (scale/investigate/pivot/explore), campaign signal,
strategic recommendations by signal type, and feed-forward pattern.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 4: Verify Phase 7 Completion

**Step 1: Verify all six template files exist**

Run:
```bash
ls .claude/skills/marketing-experimentation/templates/01-discovery.md
ls .claude/skills/marketing-experimentation/templates/02-hypothesis-generation.md
ls .claude/skills/marketing-experimentation/templates/03-prioritization.md
ls .claude/skills/marketing-experimentation/templates/04-experiment-tracker.md
ls .claude/skills/marketing-experimentation/templates/05-synthesis.md
ls .claude/skills/marketing-experimentation/templates/06-iteration-plan.md
```

Expected: All six template files exist

**Step 2: Verify experiment tracker supports multi-conversation tracking**

Run: `grep "Multi-Conversation Resumption" .claude/skills/marketing-experimentation/templates/04-experiment-tracker.md`

Expected: Resumption instructions present

**Step 3: Verify synthesis template integrates with presenting-data**

Run: `grep "presenting-data" .claude/skills/marketing-experimentation/templates/05-synthesis.md`

Expected: References to presenting-data skill output

**Step 4: Verify iteration plan emphasizes ideas not hypotheses**

Run: `grep "IDEAS, not hypotheses" .claude/skills/marketing-experimentation/templates/06-iteration-plan.md`

Expected: Clear emphasis on ideas vs hypotheses distinction

**Phase 7 Checkpoint Requirements:**
- ✓ All 6 template files exist in templates/ directory
- ✓ Experiment tracker format supports multi-conversation tracking (living document, resumption instructions)
- ✓ Synthesis template integrates with presenting-data patterns (references to presenting-data output)
- ✓ Iteration plan template emphasizes ideas (not hypotheses) with feed-forward pattern
