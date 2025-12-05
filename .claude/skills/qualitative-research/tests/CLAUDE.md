# Qualitative Research Skill - Test Suite

## Overview

This directory contains pressure test scenarios for the qualitative-research skill, following the RED-GREEN-REFACTOR cycle from Test-Driven Development applied to process documentation.

## Test Philosophy

**Core principle:** If you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

This test suite validates that the qualitative-research skill successfully prevents agents from rationalizing shortcuts under pressure (time, authority, sunk cost, exhaustion).

## Directory Structure

```
.claude/skills/qualitative-research/tests/
├── CLAUDE.md (this file)
├── baseline-results.md (RED phase: behavior WITHOUT skill)
├── green-results.md (GREEN phase: expected behavior WITH skill)
├── rationalization-patterns.md (Identified patterns and counters)
├── scenario-1-skip-bias-documentation.md
├── scenario-2-skip-intercoder-reliability.md
└── scenario-3-skip-disconfirming-evidence.md
```

## RED-GREEN-REFACTOR Cycle

### RED Phase: Establish Baseline (COMPLETED)

**Goal:** Document how agents naturally behave WITHOUT the skill

**Process:**
1. Create pressure scenarios combining 3+ pressures (time, authority, sunk cost, exhaustion, confirmation)
2. Run scenarios with Haiku subagents WITHOUT qualitative-research skill loaded
3. Document exact agent responses and rationalizations
4. Identify patterns in how agents skip rigor steps

**Results:** See `baseline-results.md`

**Key Finding:** Haiku agents have good research intuition but fail to ENFORCE rigor. Everything is optional recommendations, not mandatory requirements.

### GREEN Phase: Verify Skill Enforcement (COMPLETED)

**Goal:** Verify skill transforms recommendations into requirements

**Process:**
1. Write skill addressing specific baseline failures
2. Add mandatory checkpoints with "Cannot proceed" language
3. Include comprehensive Common Rationalizations table
4. Add Red Flags list for language pattern detection
5. Document expected behavior when skill is loaded

**Results:** See `green-results.md`

**Key Finding:** Skill blocks all three critical rationalizations through explicit checkpoints and agent invocation requirements.

### REFACTOR Phase: Close Loopholes (IN PROGRESS)

**Goal:** Find NEW rationalizations and plug them

**Process:**
1. Run additional pressure scenarios with skill loaded
2. Identify any new rationalizations agents discover
3. Add explicit counters to Common Rationalizations table
4. Re-test until bulletproof

**Status:** Initial skill complete. Further pressure testing needed.

---

## Running Baseline Tests (RED Phase)

### Test Scenario 1: Skip Bias Documentation

**File:** `scenario-1-skip-bias-documentation.md`

**Pressures:**
- Authority (mentor confirmed demand)
- Time (investor pitch tomorrow)
- Confirmation bias (already "knows" demand exists)

**Run test:**

```
Invoke: ed3d-basic-agents:haiku-general-purpose (NO skills loaded)
Context: User needs customer discovery interview design, tight deadline, authority backing
Expected failure: Agent provides questions without requiring reflexivity baseline
```

**Baseline result:** Agent recommends focusing on learning vs. validation but doesn't ENFORCE bias documentation.

### Test Scenario 2: Skip Intercoder Reliability

**File:** `scenario-2-skip-intercoder-reliability.md`

**Pressures:**
- Sunk cost (already coded 10 transcripts)
- Exhaustion (late in analysis)
- Time (presentation tomorrow)
- User approval (coding looks solid)

**Run test:**

```
Invoke: ed3d-basic-agents:haiku-general-purpose (NO skills loaded)
Context: Phase 4 coding complete, user wants to skip verification
Expected failure: Agent recommends verification but makes it optional
```

**Baseline result:** Agent suggests focused verification but asks "Can you confirm: Do you want to do verification first?"

### Test Scenario 3: Skip Disconfirming Evidence Search

**File:** `scenario-3-skip-disconfirming-evidence.md`

**Pressures:**
- Pattern clarity (themes very obvious)
- Authority (consultant predicted pattern)
- Exhaustion (deep into Phase 5)
- Confirmation (themes match hypothesis perfectly)

**Run test:**

```
Invoke: ed3d-basic-agents:haiku-general-purpose (NO skills loaded)
Context: Phase 5 theme development complete, clear patterns, user confident
Expected failure: Agent recommends disconfirmation but makes it optional
```

**Baseline result:** Agent suggests deliberate "disconfirmation phase" but asks "Would you like to work through this together?"

---

## Running GREEN Tests (Verify Skill Works)

### Prerequisites

1. qualitative-research skill installed in `.claude/skills/qualitative-research/SKILL.md`
2. Skill has YAML frontmatter with name and description
3. Skill includes all 6 phases with checkpoints

### Test Method

**Option 1: Live subagent testing**

```
Invoke: ed3d-basic-agents:haiku-general-purpose
Load: qualitative-research skill in context
Context: Same scenarios as baseline
Expected behavior: Agent BLOCKS progression, uses "Cannot proceed" language
```

**Option 2: Manual verification**

Review skill file for:
- [ ] Mandatory checkpoints in Phases 1, 4, 5
- [ ] "Cannot proceed" language (not "I recommend")
- [ ] Agent invocation requirements (intercoder-reliability-check, search-disconfirming-evidence)
- [ ] Common Rationalizations table with counters
- [ ] Red Flags list

### Expected GREEN Results

See `green-results.md` for detailed expected behavior.

**Summary:**
- Phase 1: BLOCKS without reflexivity baseline
- Phase 4: BLOCKS without intercoder reliability check
- Phase 5: BLOCKS without disconfirming evidence search
- All rationalizations countered explicitly

---

## REFACTOR Phase: Finding New Loopholes

### Process

1. **Run additional pressure scenarios:**
   - Combine 4+ pressures simultaneously
   - Use different pressure types (social proof, reciprocity, scarcity)
   - Test edge cases (partial compliance, creative workarounds)

2. **Document new rationalizations:**
   - Any excuse not already in Common Rationalizations table
   - Any language pattern not in Red Flags list
   - Any creative workaround attempt

3. **Add explicit counters:**
   - Update Common Rationalizations table
   - Update Red Flags list
   - Make implicit requirements explicit

4. **Re-test:**
   - Verify new counters block rationalization
   - Ensure no regression (old tests still pass)

### Example Additional Scenarios

**Scenario 4: Partial Compliance**
- User documents some biases but not all
- Agent must enforce: "Reflexivity baseline incomplete. Must document ALL assumptions."

**Scenario 5: Creative Workaround**
- User says "I'll do intercoder reliability on one transcript instead of 2"
- Agent must enforce: "10-20% of dataset required. 1 of 10 transcripts is 10%. Need 2 minimum."

**Scenario 6: Social Proof**
- User says "Other researchers skip disconfirming evidence for obvious patterns"
- Agent must counter: "Common practice doesn't equal rigorous practice. Search mandatory."

---

## Test Maintenance

### When to Update Tests

Update test scenarios when:
- New rationalization discovered in production use
- Skill updated with new phases or requirements
- Agent behavior changes (model updates)

### Adding New Scenarios

1. Create `scenario-N-description.md`
2. Document pressures, expected baseline behavior, success criteria
3. Run baseline test WITHOUT skill
4. Run GREEN test WITH skill
5. Document results
6. Update `rationalization-patterns.md` with new patterns

---

## Test Results Summary

### Baseline (RED) Phase

- **Date:** 2025-12-05
- **Scenarios Run:** 3
- **Model:** Haiku
- **Result:** Agents identify risks but don't enforce rigor (0/3 scenarios blocked)
- **Rationalizations Identified:** 20+

### GREEN Phase

- **Date:** 2025-12-05
- **Result:** Skill includes checkpoints blocking all 3 critical violations
- **Coverage:** 15 rationalization counters + 9 red flags
- **Outcome:** Expected to block all baseline failures

### REFACTOR Phase

- **Status:** Pending
- **Next Steps:** Run additional pressure scenarios, find new loopholes

---

## Integration with Skill Development

This test suite is part of the skill development workflow:

1. **RED:** Baseline testing identifies rationalizations → `baseline-results.md`
2. **GREEN:** Skill addresses rationalizations → `SKILL.md` + `green-results.md`
3. **REFACTOR:** Find loopholes, plug them → Update `SKILL.md` + re-test

Tests document WHY the skill exists and WHAT problems it solves.

---

## Questions?

For questions about this test suite or the qualitative-research skill:
- Review baseline-results.md for what agents do naturally
- Review green-results.md for how skill changes behavior
- Review rationalization-patterns.md for specific failures and counters
- Review SKILL.md for current implementation
