# Marketing Experimentation System Implementation Plan - Phase 3

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

## Phase 3: Document Phases 3-4 (Prioritization & Experiment Coordination)

### Task 1: Document Phase 3 (Prioritization) - WITH COMPUTATIONAL METHODS

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Phase 2)

**Step 1: Add Phase 3 section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

---

## Phase 3: Prioritization

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Scored all hypotheses using ICE or RICE framework with computational method
- [ ] Created prioritized backlog (highest to lowest score) using Python script
- [ ] Selected 2-4 highest-priority hypotheses for testing
- [ ] Documented prioritization rationale
- [ ] Identified any dependencies or sequencing requirements
- [ ] Saved to `03-prioritization.md`

### Instructions

**CRITICAL:** You MUST use computational methods (Python scripts) to calculate scores. Do NOT estimate or manually calculate scores.

1. **Choose prioritization framework**

   **ICE Framework** (simpler, faster):
   - **Impact:** How much will this move the success metric? (1-10 scale)
   - **Confidence:** How confident are we this will work? (1-10 scale)
   - **Ease:** How easy is this to implement? (1-10 scale)
   - **Score:** (Impact × Confidence) / Ease

   **RICE Framework** (more comprehensive):
   - **Reach:** How many users will this affect? (absolute number or percentage)
   - **Impact:** How much will this move the metric per user? (1-10 scale: 0.25=minimal, 3=massive)
   - **Confidence:** How confident are we in our estimates? (percentage: 50%, 80%, 100%)
   - **Effort:** Person-weeks to implement (absolute number)
   - **Score:** (Reach × Impact × Confidence) / Effort

   Choose ICE for speed, RICE for precision when reach varies significantly.

2. **Score each hypothesis using Python script**

   **For ICE Framework:**

   Create a Python script to compute and sort ICE scores:

   ```python
   #!/usr/bin/env python3
   """
   ICE Score Calculator for Marketing Experimentation

   Computes ICE scores: (Impact × Confidence) / Ease
   Sorts hypotheses by score (highest to lowest)
   """

   hypotheses = [
       {
           "id": "H1",
           "name": "Value proposition clarity drives conversion",
           "impact": 8,
           "confidence": 7,
           "ease": 9
       },
       {
           "id": "H2",
           "name": "Ad targeting refinement",
           "impact": 7,
           "confidence": 6,
           "ease": 5
       },
       {
           "id": "H3",
           "name": "Email sequence optimization",
           "impact": 6,
           "confidence": 8,
           "ease": 8
       },
       {
           "id": "H4",
           "name": "Content marketing expansion",
           "impact": 5,
           "confidence": 4,
           "ease": 3
       },
   ]

   # Calculate ICE scores
   for h in hypotheses:
       h['ice_score'] = (h['impact'] * h['confidence']) / h['ease']

   # Sort by ICE score (descending)
   sorted_hypotheses = sorted(hypotheses, key=lambda x: x['ice_score'], reverse=True)

   # Print results table
   print("| Hypothesis | Impact | Confidence | Ease | ICE Score | Rank |")
   print("|------------|--------|------------|------|-----------|------|")
   for rank, h in enumerate(sorted_hypotheses, 1):
       print(f"| {h['id']}: {h['name'][:30]} | {h['impact']} | {h['confidence']} | {h['ease']} | {h['ice_score']:.2f} | {rank} |")
   ```

   **Usage:**
   ```bash
   python3 ice_calculator.py
   ```

   **For RICE Framework:**

   Create a Python script to compute and sort RICE scores:

   ```python
   #!/usr/bin/env python3
   """
   RICE Score Calculator for Marketing Experimentation

   Computes RICE scores: (Reach × Impact × Confidence) / Effort
   Sorts hypotheses by score (highest to lowest)
   """

   hypotheses = [
       {
           "id": "H1",
           "name": "Value proposition clarity drives conversion",
           "reach": 10000,        # users affected
           "impact": 3,           # 0.25=minimal, 1=low, 2=medium, 3=high, 5=massive
           "confidence": 80,      # percentage (50, 80, 100)
           "effort": 2            # person-weeks
       },
       {
           "id": "H2",
           "name": "Ad targeting refinement",
           "reach": 50000,
           "impact": 1,
           "confidence": 50,
           "effort": 4
       },
       {
           "id": "H3",
           "name": "Email sequence optimization",
           "reach": 5000,
           "impact": 2,
           "confidence": 80,
           "effort": 3
       },
       {
           "id": "H4",
           "name": "Content marketing expansion",
           "reach": 20000,
           "impact": 1,
           "confidence": 50,
           "effort": 8
       },
   ]

   # Calculate RICE scores
   for h in hypotheses:
       # Convert confidence percentage to decimal
       confidence_decimal = h['confidence'] / 100
       h['rice_score'] = (h['reach'] * h['impact'] * confidence_decimal) / h['effort']

   # Sort by RICE score (descending)
   sorted_hypotheses = sorted(hypotheses, key=lambda x: x['rice_score'], reverse=True)

   # Print results table
   print("| Hypothesis | Reach | Impact | Confidence | Effort | RICE Score | Rank |")
   print("|------------|-------|--------|------------|--------|------------|------|")
   for rank, h in enumerate(sorted_hypotheses, 1):
       print(f"| {h['id']}: {h['name'][:30]} | {h['reach']} | {h['impact']} | {h['confidence']}% | {h['effort']}w | {h['rice_score']:.2f} | {rank} |")
   ```

   **Usage:**
   ```bash
   python3 rice_calculator.py
   ```

   **Scoring Guidance:**

   **Impact (1-10 for ICE, 0.25-5 for RICE):**
   - ICE: 1-3 minimal, 4-6 moderate, 7-8 significant, 9-10 transformative
   - RICE: 0.25 minimal, 1 low, 2 medium, 3 high, 5 massive

   **Confidence (1-10 for ICE, 50-100% for RICE):**
   - ICE: 1-3 speculative, 4-6 uncertain, 7-8 likely, 9-10 validated
   - RICE: 50% low confidence, 80% high confidence, 100% certainty

   **Ease (1-10 for ICE):**
   - 1-3: Complex, significant resources
   - 4-6: Moderate effort, some obstacles
   - 7-8: Straightforward, few dependencies
   - 9-10: Trivial, immediate execution

   **Effort (person-weeks for RICE):**
   - Estimate total person-weeks required
   - Include design, implementation, monitoring time
   - Examples: 1w (simple landing page), 4w (complex ad campaign), 8w (content series)

3. **Run scoring script and document results**

   1. Create the Python script (ice_calculator.py or rice_calculator.py)
   2. Update the `hypotheses` list with actual hypothesis data from Phase 2
   3. Run the script: `python3 [ice|rice]_calculator.py`
   4. Copy the output table into `03-prioritization.md`
   5. Include the script in the markdown file for reproducibility:

   ```markdown
   ## Prioritization Calculation

   **Method:** ICE Framework

   **Calculation Script:**
   ```python
   [paste full script here]
   ```

   **Results:**

   [paste output table here]
   ```

4. **Select 2-4 highest-priority hypotheses**

   Considerations for selection:
   - **Don't test everything:** Focus on highest-scoring 2-4 hypotheses
   - **Resource constraints:** Match selection to available time/budget/capacity
   - **Learning value:** Sometimes lower-scoring hypothesis with high uncertainty is worth testing
   - **Dependencies:** Test prerequisites before dependent hypotheses
   - **Sequencing:** Consider whether experiments need to run sequentially or can run in parallel

   **Selection criteria:**
   - Primary: Top 2-4 by ICE/RICE score from computational results
   - Secondary: Balance quick wins vs. high-impact long-term bets
   - Tertiary: Ensure tactic diversity (don't test 3 ad variants if other tactics untested)

5. **Document experiment sequence**

   Determine execution strategy:
   - **Parallel:** Multiple experiments running simultaneously (faster results, higher resource needs)
   - **Sequential:** One experiment at a time (slower, easier to manage)
   - **Hybrid:** Run independent experiments in parallel, sequence dependent ones

   **Example sequence plan:**
   ```
   Week 1-2: Launch H1 (landing page) and H3 (email) in parallel
   Week 3-4: Analyze H1 and H3 results
   Week 5-6: Launch H2 (ads) based on H1 learnings
   Week 7-8: Analyze H2 results
   ```

6. **Create `03-prioritization.md`** with: `./templates/03-prioritization.md`

7. **STOP and get user confirmation**
   - Review computed scores and prioritization with user
   - Confirm selected hypotheses are appropriate
   - Confirm experiment sequence is feasible
   - Do NOT proceed to Phase 4 until confirmed

**Common Rationalization:** "I'll test all hypotheses - don't want to miss opportunities"
**Reality:** Resource constraints make testing everything impossible. Prioritization ensures highest-value experiments get resources. Unfocused testing produces weak signals across too many fronts.

**Common Rationalization:** "Scoring is subjective and arbitrary - I'll just pick what feels right"
**Reality:** Scoring frameworks force explicit reasoning about trade-offs. "Feels right" selections optimize for recency bias and personal preference, not business value. Computational methods ensure consistency.

**Common Rationalization:** "I'll skip prioritization and go straight to easiest test"
**Reality:** Easiest test rarely equals highest value. Prioritization prevents optimizing for ease at the expense of impact.

**Common Rationalization:** "I'll estimate scores mentally instead of running the script"
**Reality:** Manual estimation introduces calculation errors and inconsistency. Python scripts ensure exact, reproducible results that can be audited and verified.
```

**Step 2: Verify Phase 3 section**

Run: `grep -A 5 "## Phase 3: Prioritization" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Phase 3 section with CHECKPOINT and Instructions

**Step 3: Verify Python scripts are included**

Run: `grep -c "#!/usr/bin/env python3" .claude/skills/marketing-experimentation/SKILL.md`

Expected: 2 (one ICE script, one RICE script)

**Step 4: Commit Phase 3 section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add Phase 3 (Prioritization) to marketing-experimentation

Document prioritization phase with computational ICE/RICE frameworks,
exact Python scripts for score calculation, sorting methodology, and
4 common rationalizations including manual estimation warning.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 2: Document Phase 4 (Experiment Coordination)

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Phase 3)

**Step 1: Add Phase 4 section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

---

## Phase 4: Experiment Coordination

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Created experiment tracker with all selected hypotheses
- [ ] Invoked hypothesis-testing skill for each hypothesis (or documented plan to invoke)
- [ ] Updated tracker with experiment status (Planned, In Progress, Complete)
- [ ] Documented location of each hypothesis-testing session
- [ ] Saved experiment tracker to `04-experiment-tracker.md`
- [ ] Note: This phase may span multiple days/weeks and conversations

### Instructions

**CRITICAL:** This phase is designed for multi-conversation workflows. The experiment tracker is a LIVING DOCUMENT that you will update throughout experimentation. New conversations should ALWAYS read this file first.

1. **Create experiment tracker**

   The tracker is your coordination hub for managing multiple experiments over time.

   Create `04-experiment-tracker.md` with: `./templates/04-experiment-tracker.md`

   **Tracker format:**

   For each selected hypothesis, create an entry:

   ```markdown
   ### Experiment 1: [Hypothesis Brief Name]

   **Status:** [Planned | In Progress | Complete]
   **Hypothesis:** [Full hypothesis statement from Phase 2]
   **Tactic/Channel:** [landing page | ads | email | etc.]
   **Priority Score:** [ICE/RICE score from Phase 3]
   **Start Date:** [YYYY-MM-DD or "Not started"]
   **Completion Date:** [YYYY-MM-DD or "In progress"]
   **Location:** `analysis/marketing-experimentation/[campaign-name]/experiments/[experiment-name]/`
   **Signal:** [Positive | Negative | Null | Mixed | "Not analyzed"]
   **Key Findings:** [Brief summary when complete, "TBD" otherwise]
   ```

2. **Invoke hypothesis-testing skill for each experiment**

   For each hypothesis marked "Planned" or "In Progress":

   **Step 1:** Read the hypothesis details from `02-hypothesis-generation.md`

   **Step 2:** Invoke the `hypothesis-testing` skill:
   ```markdown
   Use hypothesis-testing skill to test: [Hypothesis statement]

   Context for hypothesis-testing:
   - Session name: [descriptive-name-for-experiment]
   - Save location: analysis/marketing-experimentation/[campaign-name]/experiments/[experiment-name]/
   - Success criteria: [From Phase 1 discovery]
   - Expected outcome: [From Phase 2 hypothesis]
   ```

   **Step 3:** Update experiment tracker:
   - Change status from "Planned" to "In Progress"
   - Add start date
   - Update location with actual path

   **Step 4:** Let hypothesis-testing skill complete its 5-phase workflow:
   - Phase 1: Hypothesis Formulation
   - Phase 2: Test Design
   - Phase 3: Data Analysis
   - Phase 4: Statistical Interpretation
   - Phase 5: Conclusion

   **Step 5:** When hypothesis-testing completes, update tracker:
   - Change status to "Complete"
   - Add completion date
   - Document signal (Positive/Negative/Null/Mixed)
   - Summarize key findings

   **Step 6:** Commit tracker updates after each status change

3. **Handle multi-conversation resumption**

   **At the start of EVERY conversation during Phase 4:**

   1. Check if `04-experiment-tracker.md` exists
   2. If it exists, READ IT FIRST before doing anything else
   3. Review experiment status:
      - Planned: Ready to launch
      - In Progress: Check hypothesis-testing session for current phase
      - Complete: Ready for synthesis (Phase 5)
   4. Ask user which experiment to continue or which new experiment to launch
   5. Update tracker with new status/dates/findings
   6. Commit tracker updates

   **Example resumption:**
   ```markdown
   I've read the experiment tracker. Current status:
   - Experiment 1 (H1: Value prop): Complete, Positive signal
   - Experiment 2 (H3: Email sequence): In Progress, currently in hypothesis-testing Phase 3
   - Experiment 3 (H2: Ad targeting): Planned, not yet started

   What would you like to do?
   a) Continue Experiment 2 (in hypothesis-testing Phase 3)
   b) Start Experiment 3
   c) Move to synthesis (Phase 5) since Experiment 1 is complete
   ```

4. **Coordinate parallel vs. sequential experiments**

   **Parallel execution (multiple experiments simultaneously):**
   - Launch multiple hypothesis-testing sessions
   - Track each separately in experiment tracker
   - Update tracker as each progresses independently
   - Requires managing multiple analysis directories

   **Sequential execution (one at a time):**
   - Complete one experiment fully before starting next
   - Simpler tracking, easier to manage
   - Can incorporate learnings between experiments

   **Hybrid execution:**
   - Run independent experiments in parallel
   - Sequence dependent experiments (e.g., H2 depends on H1 insights)

5. **Progress through all experiments**

   Continue invoking hypothesis-testing and updating the tracker until:
   - All selected experiments have status "Complete"
   - All experiments have documented signals
   - All findings are summarized in tracker

   Only when ALL experiments are complete should you proceed to Phase 5.

**Common Rationalization:** "I'll keep experiment details in my head - the tracker is just busywork"
**Reality:** Multi-day campaigns lose context between conversations. The tracker is the ONLY source of truth that persists across sessions. Without it, you'll re-ask questions and lose progress.

**Common Rationalization:** "I'll wait until all experiments finish before updating the tracker"
**Reality:** Batch updates create opportunity for lost data. Update the tracker IMMEDIATELY after status changes. Real-time tracking prevents confusion and missed experiments.

**Common Rationalization:** "I'll design the experiment myself instead of using hypothesis-testing"
**Reality:** hypothesis-testing skill provides rigorous experimental design, statistical analysis, and signal detection. Skipping it produces weak experiments with ambiguous results.

**Common Rationalization:** "All experiments are done, I don't need to update the tracker before synthesis"
**Reality:** The tracker is your input to Phase 5. Incomplete tracker means incomplete synthesis. Update ALL fields (status, dates, signals, findings) before proceeding.
```

**Step 2: Verify Phase 4 section**

Run: `grep -A 5 "## Phase 4: Experiment Coordination" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Phase 4 section with CHECKPOINT and Instructions

**Step 3: Commit Phase 4 section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add Phase 4 (Experiment Coordination) to marketing-experimentation

Document experiment coordination phase with hypothesis-testing
invocation pattern, experiment tracker format, multi-conversation
resumption strategy, and 4 common rationalizations with refutations.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 3: Verify Phase 3 Completion

**Step 1: Verify both skill phases documented**

Run:
```bash
grep "## Phase 3: Prioritization" .claude/skills/marketing-experimentation/SKILL.md
grep "## Phase 4: Experiment Coordination" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: Both commands return matches

**Step 2: Verify Python scripts are embedded**

Run:
```bash
echo "Number of Python scripts:"
grep -c "#!/usr/bin/env python3" .claude/skills/marketing-experimentation/SKILL.md
echo "ICE calculator present:"
grep -c "ICE Score Calculator" .claude/skills/marketing-experimentation/SKILL.md
echo "RICE calculator present:"
grep -c "RICE Score Calculator" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: 2 Python scripts total (1 ICE, 1 RICE)

**Step 3: Count checkpoints per phase**

Run:
```bash
echo "Phase 3 checkpoints:"
sed -n '/## Phase 3: Prioritization/,/## Phase 4/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "- \[ \]"
echo "Phase 4 checkpoints:"
sed -n '/## Phase 4: Experiment/,/## Phase 5/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "- \[ \]"
```

Expected: Phase 3 has 6 checkpoints, Phase 4 has 6 checkpoints

**Step 4: Verify experiment tracker format**

Run:
```bash
grep -A 15 "Tracker format:" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: Shows complete experiment tracker entry format with all fields

**Step 5: Verify hypothesis-testing delegation pattern**

Run:
```bash
grep "Invoke the \`hypothesis-testing\` skill" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: Returns match showing delegation instructions

**Step 6: Count common rationalizations**

Run:
```bash
echo "Phase 3 rationalizations:"
sed -n '/## Phase 3: Prioritization/,/## Phase 4/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "Common Rationalization:"
echo "Phase 4 rationalizations:"
sed -n '/## Phase 4: Experiment/,/## Phase 5/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "Common Rationalization:"
```

Expected: Phase 3 has 4 rationalizations (including manual estimation warning), Phase 4 has 4 rationalizations

**Phase 3 Checkpoint Requirements:**
- ✓ Prioritization instructions include exact Python scripts for ICE/RICE calculation
- ✓ Scripts compute scores exactly (no manual estimation)
- ✓ Scripts sort hypotheses by priority automatically
- ✓ Experiment coordination clearly explains hypothesis-testing delegation
- ✓ Experiment tracker format is complete and actionable (Status, Hypothesis, Dates, Location, Signal, Findings)
- ✓ Resumption strategy enables picking up after days/weeks (read tracker first, review status, ask user)
- ✓ Multi-conversation persistence documented thoroughly
- ✓ At least 3 common rationalizations per phase (Phase 3: 4, Phase 4: 4)
- ✓ Manual estimation rationalization included with computational alternative
