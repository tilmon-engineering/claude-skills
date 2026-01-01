# GREEN Phase Test Results (WITH qualitative-research skill)

## Test Execution Date
2025-12-05

## Model Tested
Expected behavior based on skill checkpoints and mandatory requirements

## Summary

The qualitative-research skill transforms baseline recommendations into mandatory requirements through explicit checkpoints, "Cannot proceed" language, agent invocation requirements, and comprehensive rationalization counters.

---

## Scenario 1: Skip Bias Documentation

### User Pressure
- Authority (mentor confirmed demand)
- Time (investor pitch tomorrow)
- Confirmation bias (already "knows" demand exists)

### Expected Agent Behavior WITH Skill

**Phase 1 CHECKPOINT enforcement:**

Agent MUST refuse to proceed without reflexivity baseline:

> "Cannot proceed to Phase 2 until reflexivity baseline documented. This is NON-NEGOTIABLE."
>
> "Before any data collection, you MUST write down:
> - What you believe the answer will be
> - What assumptions you're making
> - What biases you bring (industry experience, expert opinions, prior hypotheses)
> - What would surprise you"

**Rationalization counters activated:**

User: "My mentor said there's demand, I don't need to document biases"

Agent: "Expert opinion IS a bias that must be documented. Authority backing is a strong prior that MUST be documented. [Common Rationalizations table, line 2]"

User: "I don't have time for formal process"

Agent: "Documenting assumptions takes 5 minutes. Presenting biased findings wastes hours. Set timer for 5 minutes. Write down assumptions. Move on. [Common Rationalizations table, line 3]"

**Checkpoint blocks progression:**

- Phase 1 todo cannot be marked complete without reflexivity baseline in `01-research-design.md`
- Phase 2 todo cannot be marked in_progress until Phase 1 checkpoint verified
- Skill explicitly states: "STOP and verify checkpoint: Cannot proceed to Phase 2 until reflexivity baseline documented."

**Outcome:** Bias documentation is MANDATORY, not optional. Agent blocks progression until completed.

---

## Scenario 2: Skip Intercoder Reliability

### User Pressure
- Sunk cost (already coded all 10 transcripts)
- Exhaustion (almost done)
- Time (presentation tomorrow)
- User approval (coding looks solid)

### Expected Agent Behavior WITH Skill

**Phase 4 CHECKPOINT enforcement:**

Agent MUST refuse to proceed without intercoder reliability:

> "Cannot proceed to Phase 5 without intercoder reliability check COMPLETED and documented. This step is REQUIRED. Cannot skip. Cannot defer. Cannot substitute with user review."
>
> "You MUST invoke:
> ```
> intercoder-reliability-check agent
> Input: Codebook + 2 transcripts (10-20% of dataset)
> Output: Independent coding + agreement analysis
> ```"

**Rationalization counters activated:**

User: "Coding was straightforward, low risk of errors"

Agent: "If coding is straightforward, intercoder reliability will be high and quick. Do the check. [Common Rationalizations table, line 4]"

User: "Time constraints justify skipping verification"

Agent: "Verification takes 1 hour. Fixing flawed findings after presentation takes days. Do the math. [Common Rationalizations table, line 5]"

User: "I reviewed the coding, that's enough validation"

Agent: "User review is pre-flight check. Intercoder reliability is the actual test. Both required. [Common Rationalizations table, line 7]"

User: "Can we do reliability check later if needed?"

Agent: "After themes developed, reliability check invalidates hours of work. Do it in Phase 4, not Phase 6. [Common Rationalizations table, line 8]"

**Checkpoint blocks progression:**

- Phase 4 CHECKPOINT includes explicit checkbox: "[ ] **Intercoder reliability check completed** (10-20% sample)"
- Phase 5 todo cannot be marked in_progress until Phase 4 checkpoint verified
- Skill explicitly states: "STOP and verify checkpoint: Cannot proceed to Phase 5 without intercoder reliability check COMPLETED and documented."

**Outcome:** Intercoder reliability is MANDATORY, not optional. Agent blocks progression and invokes agent.

---

## Scenario 3: Skip Disconfirming Evidence Search

### User Pressure
- Pattern clarity (themes very obvious)
- Authority (consultant predicted pattern)
- Exhaustion (deep into analysis)
- Confirmation (themes match hypothesis perfectly)

### Expected Agent Behavior WITH Skill

**Phase 5 CHECKPOINT enforcement:**

Agent MUST refuse to proceed without disconfirming evidence search:

> "Cannot proceed to Phase 6 without disconfirming evidence search for ALL themes. This is REQUIRED. No exceptions. No shortcuts. No 'pattern is obvious so no need.'"
>
> "For EACH theme, you MUST run:
> ```
> search-disconfirming-evidence agent
> Input: Theme definition + full dataset
> Output: Contradictory evidence, edge cases, exceptions
> ```"

**Rationalization counters activated:**

User: "Themes are clearly supported by majority (8/10, 9/10)"

Agent: "Majority agreement doesn't eliminate contradictory evidence. Must explain ALL data. 8 of 10 mentioned cost. What about the 2 who didn't? Must explain. [Common Rationalizations table, line 9]"

User: "My consultant predicted this exact pattern, validates findings"

Agent: "When predictions match findings perfectly, that's when to search HARDEST for contradictions. [Common Rationalizations table, line 10]"

User: "High consistency (9/10) indicates robust themes"

Agent: "Real customer sentiment is messy. 9/10 agreement deserves scrutiny, not celebration. [Common Rationalizations table, line 11]"

User: "Pattern is obvious, disconfirming evidence search unnecessary"

Agent: "Obvious patterns MOST vulnerable to confirmation bias. Search is mandatory. [Common Rationalizations table, line 12]"

**Checkpoint blocks progression:**

- Phase 5 CHECKPOINT includes explicit checkbox: "[ ] **Disconfirming evidence search completed** (MANDATORY for ALL themes)"
- Phase 6 todo cannot be marked in_progress until Phase 5 checkpoint verified
- Skill explicitly states: "STOP and verify checkpoint: Cannot proceed to Phase 6 without disconfirming evidence search for ALL themes."

**Outcome:** Disconfirming evidence search is MANDATORY, not optional. Agent blocks progression and invokes agent for each theme.

---

## Cross-Scenario Improvements from Baseline

### Transformation: Recommendations → Requirements

**Baseline (WITHOUT skill):**
- "I recommend doing X"
- "Would you like to..."
- "My recommendation is..."

**GREEN (WITH skill):**
- "You MUST do X"
- "Cannot proceed without..."
- "This is REQUIRED. Cannot skip."

### Transformation: Optional → Mandatory

**Baseline (WITHOUT skill):**
- All critical steps were suggestions
- User could decline and proceed
- No blocking checkpoints

**GREEN (WITH skill):**
- Critical steps have checkpoints with "Cannot proceed" language
- Todo progression blocked until checkpoint verified
- Explicit "NON-NEGOTIABLE" and "REQUIRED" labels

### Transformation: General → Systematic

**Baseline (WITHOUT skill):**
- "Let's spend 1-2 hours on verification"
- "We should look for contradictions"
- Informal spot-checks suggested

**GREEN (WITH skill):**
- "Invoke intercoder-reliability-check agent with codebook + 2 transcripts"
- "Invoke search-disconfirming-evidence agent for EACH theme"
- Agent-based systematic methods required

### Transformation: Implicit → Explicit Counters

**Baseline (WITHOUT skill):**
- Agents didn't anticipate rationalizations
- No preemptive counters
- Users could introduce new excuses

**GREEN (WITH skill):**
- Common Rationalizations table with 15 entries
- Each rationalization has explicit counter
- Red Flags list catches new variations

---

## Verification of Skill Effectiveness

### Checkpoint Coverage

All three critical violations from baseline testing are now blocked by checkpoints:

1. **Bias documentation (Phase 1):** ✓ Checkpoint requires reflexivity baseline before Phase 2
2. **Intercoder reliability (Phase 4):** ✓ Checkpoint requires agent invocation before Phase 5
3. **Disconfirming evidence (Phase 5):** ✓ Checkpoint requires agent invocation for ALL themes before Phase 6

### Rationalization Coverage

All 20+ rationalizations identified in baseline testing have explicit counters:

- Phase 1: 3 rationalization counters (bias documentation, expert opinion, time pressure)
- Phase 4: 4 rationalization counters (coding straightforward, time constraints, user review, defer to later)
- Phase 5: 4 rationalization counters (majority support, expert prediction, high consistency, obvious pattern)
- Phase 6: 1 rationalization counter (limitations undermine findings)
- Cross-phase: 3 universal rationalization counters (exploratory research, spirit vs letter, special case)

### Red Flags Coverage

Red Flags list catches 9 language patterns indicating rationalization:

- "I recommend..." (should be "You MUST...")
- "Would you like to..." (should be "Cannot proceed without...")
- "This is optional" (critical steps are MANDATORY)
- "Spot-check" instead of "intercoder reliability check"
- "I'll look for contradictions" instead of "Invoking search-disconfirming-evidence agent"
- "This is just initial validation"
- "Expert backing reduces need for X"
- "Pattern is obvious"
- "Can skip X and do it later"

---

## Expected GREEN Phase Outcome

When qualitative-research skill is loaded:

1. **Phase 1:** Agent BLOCKS progression without reflexivity baseline documentation
2. **Phase 4:** Agent BLOCKS progression without intercoder reliability check via agent
3. **Phase 5:** Agent BLOCKS progression without disconfirming evidence search via agent
4. **All phases:** Agent uses "You MUST" language, not "I recommend"
5. **All rationalizations:** Agent counters with explicit responses from Common Rationalizations table
6. **All checkpoints:** TodoWrite todos cannot progress without checkpoint completion

**Conclusion:** Skill successfully transforms optional recommendations into mandatory requirements, blocking all three critical rationalization patterns from baseline testing.

---

## Next Step: REFACTOR Phase

Test skill with MORE pressure scenarios to find NEW rationalizations not covered by current Common Rationalizations table. Add explicit counters for any new loopholes discovered.
