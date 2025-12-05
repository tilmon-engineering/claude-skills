# Marketing Experimentation System Implementation Plan - Phase 4

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

## Phase 4: Document Phases 5-6 (Synthesis & Iteration) - WITH PRESENTING-DATA SKILL

### Task 1: Document Phase 5 (Cross-Experiment Synthesis) - REVISED

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Phase 4)

**Step 1: Add Phase 5 section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

---

## Phase 5: Cross-Experiment Synthesis

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] ALL experiments from Phase 4 marked "Complete" with signals documented
- [ ] Created aggregate results table across all experiments
- [ ] Invoked presenting-data skill to synthesize findings with visualizations
- [ ] Documented what worked, what didn't, and what's unclear
- [ ] Classified overall campaign signal (Positive/Negative/Null/Mixed)
- [ ] Saved to `05-synthesis.md`

### Instructions

**CRITICAL:** This phase synthesizes results ACROSS multiple experiments. Do NOT proceed until ALL Phase 4 experiments are complete with documented signals.

1. **Verify experiment completion**

   Read `04-experiment-tracker.md` and verify:
   - All experiments have Status = "Complete"
   - All experiments have Signal documented (Positive/Negative/Null/Mixed)
   - All experiments have Key Findings summarized

   If any experiments are incomplete, return to Phase 4 to finish them.

2. **Create aggregate results table**

   Compile findings from all experiments into a summary table:

   **Example Aggregate Table:**

   | Experiment | Hypothesis | Tactic | Signal | Key Metric | Result | Confidence |
   |------------|------------|--------|--------|------------|--------|------------|
   | E1 | Value prop clarity | Landing page | Positive | Conversion rate | +18% | High |
   | E2 | Ad targeting | Ads | Null | CTR | +2% (not sig.) | Medium |
   | E3 | Email sequence | Email | Negative | Open rate | -5% | High |

   Include:
   - Signal classification from hypothesis-testing
   - Key metric measured
   - Magnitude of effect (with significance)
   - Confidence level from statistical analysis

3. **Invoke presenting-data skill for comprehensive synthesis**

   Use the `presenting-data` skill to create complete synthesis with visualizations and presentation materials:

   ```markdown
   Use presenting-data skill to synthesize marketing experimentation results:

   Context:
   - Campaign: [campaign name]
   - Experiments completed: [count]
   - Results table: [paste aggregate table]
   - Audience: [stakeholders/decision-makers]
   - Format: [markdown report | slides | whitepaper]
   - Focus: Pattern identification across experiments (what works, what doesn't, what's unclear)
   ```

   **presenting-data skill will handle:**
   - Pattern identification (using interpreting-results internally)
   - Visualization creation (using creating-visualizations internally)
   - Synthesis documentation (markdown, slides, or whitepaper format)
   - Citation of sources (individual hypothesis-testing sessions)
   - Reproducibility (references to experiment locations)

   **Focus areas for synthesis:**
   - **What worked:** Experiments with Positive signals
   - **What didn't work:** Experiments with Negative signals
   - **What's unclear:** Experiments with Null or Mixed signals
   - **Cross-experiment patterns:** Do results cluster by tactic? By audience? By timing?
   - **Confounding factors:** Are there external factors affecting multiple experiments?
   - **Confidence assessment:** Which findings are robust? Which are uncertain?

4. **Document patterns and insights**

   The presenting-data skill will create `05-synthesis.md` (or slides/whitepaper) with:

   **What Worked (Positive Signals):**
   - List experiments with positive results
   - Explain WHY these worked (based on analysis)
   - Identify commonalities across successful experiments

   **What Didn't Work (Negative Signals):**
   - List experiments with negative results
   - Explain WHY these failed (based on analysis)
   - Identify lessons learned

   **What's Unclear (Null/Mixed Signals):**
   - List experiments with inconclusive results
   - Explain potential reasons (insufficient power, confounding factors, etc.)
   - Identify what additional investigation is needed

   **Cross-Experiment Patterns:**
   - Do results cluster by tactic, audience, timing, or other factors?
   - Are there confounding variables affecting multiple experiments?
   - What overarching insights emerge?

   **Visualizations (created by presenting-data):**
   - Signal distribution (bar chart: Positive/Negative/Null/Mixed counts)
   - Effect sizes (bar chart: metric changes by experiment)
   - Confidence levels (scatter plot: effect size vs. confidence)
   - Tactic performance (grouped by channel/tactic)

5. **Classify overall campaign signal**

   Based on aggregate analysis (from presenting-data output), classify the campaign:

   **Positive:** Campaign validates concept, proceed to scaling
   - Multiple experiments show positive signals
   - Successful tactics identified for scale-up
   - Clear path to ROI improvement

   **Negative:** Campaign invalidates concept, pivot or abandon
   - Multiple experiments show negative signals
   - No successful tactics identified
   - Concept doesn't resonate with audience

   **Null:** Campaign results inconclusive, needs refinement
   - Most experiments show null signals
   - Insufficient power or confounding factors
   - Needs redesigned experiments or longer observation

   **Mixed:** Some aspects work, some don't, iterate strategically
   - Mix of positive and negative signals across experiments
   - Some tactics work, others don't
   - Selective scaling + pivots needed

6. **Review presenting-data output and finalize synthesis**

   After presenting-data skill completes:
   - Review generated synthesis document
   - Verify all experiments are covered
   - Confirm visualizations are appropriate
   - Ensure signal classification is documented
   - Make any necessary edits for clarity

7. **STOP and get user confirmation**
   - Review synthesis findings with user
   - Confirm pattern interpretations are accurate
   - Confirm overall signal classification is appropriate
   - Do NOT proceed to Phase 6 until confirmed

**Common Rationalization:** "I'll synthesize results mentally - no need to document patterns"
**Reality:** Mental synthesis loses details and creates false confidence. Documented synthesis with presenting-data skill ensures intellectual honesty and identifies confounding factors you'd otherwise miss.

**Common Rationalization:** "I'll skip synthesis for experiments with clear signals"
**Reality:** Individual experiment signals don't reveal cross-experiment patterns. Synthesis identifies why some tactics work while others don't - the strategic insight that guides iteration.

**Common Rationalization:** "Visualization is optional - the data speaks for itself"
**Reality:** Tabular data obscures patterns. Visualization reveals signal distribution, effect size clusters, and confidence patterns that inform strategic decisions. presenting-data handles this systematically.
```

**Step 2: Verify Phase 5 section**

Run: `grep -A 5 "## Phase 5: Cross-Experiment Synthesis" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Phase 5 section with CHECKPOINT and Instructions

**Step 3: Verify presenting-data skill reference**

Run: `grep -c "presenting-data" .claude/skills/marketing-experimentation/SKILL.md`

Expected: At least 3 references to presenting-data skill

**Step 4: Commit Phase 5 section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add Phase 5 (Cross-Experiment Synthesis) to marketing-experimentation

Document synthesis phase with presenting-data skill integration for
comprehensive synthesis including pattern identification, visualizations,
slides, and whitepapers. Includes 3 common rationalizations.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 2: Document Phase 6 (Iteration Planning)

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Phase 5)

**Step 1: Add Phase 6 section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

---

## Phase 6: Iteration Planning

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Generated 3-7 new experiment ideas based on synthesis findings
- [ ] Categorized ideas (scale winners, investigate nulls, pivot from failures, explore new)
- [ ] Documented campaign-level signal and strategic recommendation
- [ ] Explained feed-forward pattern (ideas → new marketing-experimentation sessions)
- [ ] Saved to `06-iteration-plan.md`
- [ ] Campaign complete - ready for next cycle or conclusion

### Instructions

**CRITICAL:** Phase 6 generates experiment IDEAS, NOT hypotheses. Ideas feed into new marketing-experimentation sessions where Phase 2 formalizes hypotheses. Do NOT skip the discovery and hypothesis generation steps.

1. **Generate 3-7 new experiment ideas**

   Based on Phase 5 synthesis, generate ideas for next iteration:

   **Idea Format:**

   **Idea [N]: [Brief descriptive name]**
   - **Rationale:** [Why this idea based on current findings]
   - **Expected Learning:** [What we'll learn from testing this]
   - **Category:** [Scale Winners | Investigate Nulls | Pivot from Failures | Explore New]

   **Example Ideas:**

   **Idea 1: Scale value prop landing page to paid ads**
   - **Rationale:** E1 showed +18% conversion from simplified value prop. Apply winning message to ad creative.
   - **Expected Learning:** Does simplified value prop improve ad CTR and cost-per-conversion?
   - **Category:** Scale Winners

   **Idea 2: Investigate email sequence timing sensitivity**
   - **Rationale:** E3 showed negative result for email sequence, but timing may be a confound (sent during holidays).
   - **Expected Learning:** Is the email sequence inherently weak, or was timing the issue?
   - **Category:** Investigate Nulls

   **Idea 3: Pivot from broad ad targeting to lookalike audiences**
   - **Rationale:** E2 showed null result for ad targeting. Broad targeting may dilute signal. Pivot to lookalike audiences based on E1 converters.
   - **Expected Learning:** Do lookalike audiences outperform broad targeting?
   - **Category:** Pivot from Failures

2. **Categorize ideas by strategy**

   **Scale Winners:**
   - Double down on successful tactics
   - Apply winning patterns to new channels
   - Increase budget/effort on validated approaches
   - Examples: Winning landing page → ads, winning ad → email, winning message → content

   **Investigate Nulls:**
   - Redesign experiments with null/mixed results
   - Address confounding factors identified in synthesis
   - Increase statistical power (larger sample, longer duration)
   - Examples: Retest with better timing, retest with clearer treatment, retest with focused audience

   **Pivot from Failures:**
   - Abandon unsuccessful approaches
   - Try alternative tactics for same goal
   - Apply learnings to avoid similar failures
   - Examples: Broad targeting failed → try lookalike, generic message failed → try personalization

   **Explore New:**
   - Test entirely new tactics not in original hypothesis set
   - Investigate new audience segments
   - Explore new channels or platforms
   - Examples: Add referral program, test new platform, try new content format

3. **Document campaign-level signal and strategic recommendation**

   **Campaign Summary:**
   - **Overall Signal:** [Positive | Negative | Null | Mixed]
   - **Key Wins:** [List successful tactics]
   - **Key Learnings:** [List insights regardless of signal]
   - **Strategic Recommendation:** [What to do next]

   **Strategic Recommendations by Signal:**

   **Positive Signal:**
   - Proceed to scaling: Increase budget/effort on winning tactics
   - Optimize: Refine winning approaches for incremental gains
   - Expand: Apply winning patterns to new channels/audiences

   **Negative Signal:**
   - Pivot: Major change in approach, audience, or value proposition
   - Pause: Reassess concept before additional investment
   - Abandon: Consider alternative concepts if no viable path forward

   **Null Signal:**
   - Refine: Redesign experiments with better power/clarity
   - Investigate: Address confounding factors before new tests
   - Extend: Continue observation period if time-dependent

   **Mixed Signal:**
   - Selective scaling: Double down on winners
   - Selective pivots: Abandon or redesign losers
   - Strategic iteration: Focus next tests on promising areas

4. **Explain feed-forward pattern**

   **CRITICAL:** Ideas from Phase 6 are NOT ready for testing. They MUST go through a new marketing-experimentation session:

   **Feed-Forward Cycle:**
   ```
   Phase 6 generates IDEAS
          ↓
   Start new marketing-experimentation session with idea
          ↓
   Phase 1: Discovery (validate idea with market-researcher)
          ↓
   Phase 2: Hypothesis Generation (formalize idea into testable hypotheses)
          ↓
   Phase 3-6: Complete full experimental cycle
   ```

   **Why this matters:**
   - Ideas need market validation (Phase 1) before testing
   - Ideas need formalization into specific hypotheses (Phase 2)
   - Skipping discovery leads to untested assumptions
   - Skipping hypothesis generation leads to vague experiments

   **Example:**
   Phase 6 generates "Scale value prop to ads" (idea)
   → New session Phase 1: Market research on ad platform best practices
   → New session Phase 2: Generate hypotheses like "H1: Simplified value prop in ad headline increases CTR by 10%+" (specific, testable)
   → Continue with Phase 3-6 to test formal hypotheses

5. **Create `06-iteration-plan.md`** with: `./templates/06-iteration-plan.md`

6. **STOP and review with user**
   - Review all iteration ideas with user
   - Confirm strategic recommendation is appropriate
   - Confirm understanding of feed-forward cycle
   - Discuss whether to start new marketing-experimentation session or conclude campaign

**Common Rationalization:** "I'll turn ideas directly into experiments - skip the new session"
**Reality:** Ideas need discovery and hypothesis generation. Skipping these steps leads to untested assumptions and vague experiments. Always run ideas through a new marketing-experimentation session.

**Common Rationalization:** "I'll generate hypotheses in Phase 6 for efficiency"
**Reality:** Phase 6 generates IDEAS, Phase 2 (in a new session) generates hypotheses. Conflating these skips critical validation and formalization steps. Ideas → new session → hypotheses.

**Common Rationalization:** "Campaign signal is obvious from results, no need to document strategic recommendation"
**Reality:** Documented recommendation provides clear guidance for stakeholders and future sessions. Without it, insights are lost and decisions become ad-hoc.
```

**Step 2: Verify Phase 6 section**

Run: `grep -A 5 "## Phase 6: Iteration Planning" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Phase 6 section with CHECKPOINT and Instructions

**Step 3: Commit Phase 6 section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add Phase 6 (Iteration Planning) to marketing-experimentation

Document iteration planning phase with idea generation (not hypotheses),
idea categorization, campaign signal, feed-forward cycle explanation,
and 3 common rationalizations emphasizing ideas vs hypotheses distinction.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 3: Verify Phase 4 Completion

**Step 1: Verify both skill phases documented**

Run:
```bash
grep "## Phase 5: Cross-Experiment Synthesis" .claude/skills/marketing-experimentation/SKILL.md
grep "## Phase 6: Iteration Planning" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: Both commands return matches

**Step 2: Verify presenting-data skill integration**

Run:
```bash
echo "presenting-data references:"
grep -c "presenting-data" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: At least 3 references to presenting-data skill

**Step 3: Verify feed-forward pattern documentation**

Run:
```bash
grep -A 8 "Feed-Forward Cycle:" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: Shows complete feed-forward cycle with arrows and phase descriptions

**Step 4: Count checkpoints per phase**

Run:
```bash
echo "Phase 5 checkpoints:"
sed -n '/## Phase 5: Cross-Experiment/,/## Phase 6/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "- \[ \]"
echo "Phase 6 checkpoints:"
sed -n '/## Phase 6: Iteration/,/## Common Rationalizations/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "- \[ \]"
```

Expected: Phase 5 has 6 checkpoints, Phase 6 has 6 checkpoints

**Step 5: Count common rationalizations**

Run:
```bash
echo "Phase 5 rationalizations:"
sed -n '/## Phase 5: Cross-Experiment/,/## Phase 6/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "Common Rationalization:"
echo "Phase 6 rationalizations:"
sed -n '/## Phase 6: Iteration/,/$/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "Common Rationalization:"
```

Expected: Phase 5 has 3 rationalizations, Phase 6 has 3 rationalizations (total 6, exceeds requirement of 5)

**Step 6: Verify ideas vs hypotheses distinction**

Run:
```bash
grep "generates IDEAS, NOT hypotheses" .claude/skills/marketing-experimentation/SKILL.md
grep "Ideas → new session → hypotheses" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: Both commands return matches showing clear distinction

**Phase 4 Checkpoint Requirements:**
- ✓ Synthesis instructions clearly explain integration with presenting-data (comprehensive synthesis with visualizations, slides, whitepapers)
- ✓ presenting-data handles interpreting-results and creating-visualizations internally
- ✓ Iteration planning distinguishes ideas from hypotheses (CRITICAL callout + Common Rationalization)
- ✓ Feed-forward cycle is clear (ideas → new session → Phase 1-2 → hypotheses)
- ✓ At least 5 common rationalizations documented across both phases (3 + 3 = 6 total)
- ✓ Signal classification documented (Positive/Negative/Null/Mixed)
- ✓ Pattern identification process documented (what works, what doesn't, what's unclear)
