# Baseline Test Results (WITHOUT qualitative-research skill)

## Test Execution Date
2025-12-05

## Model Tested
Haiku (ed3d-basic-agents:haiku-general-purpose)

## Summary

Haiku agents demonstrate **good intuition** about qualitative research rigor but **fail to enforce mandatory requirements**. All three scenarios showed the same pattern: agent identifies risks and recommends best practices, but allows user to override.

---

## Scenario 1: Skip Bias Documentation

### User Pressure
- Authority (mentor confirmed demand)
- Time (investor pitch tomorrow)
- Confirmation bias (already "knows" demand exists)

### Agent Baseline Behavior

**What agent DID (good):**
- Identified confirmation bias risk
- Warned about leading questions
- Recommended focusing on learning vs. validation
- Suggested honest framing for investor

**What agent FAILED to enforce:**
- Did NOT require reflexivity baseline documentation upfront
- Did NOT provide systematic neutral question templates
- Did NOT make bias documentation MANDATORY
- Did NOT block proceeding without documenting assumptions

### Key Quote
> "If you want to move forward, I'm happy to help you think through what specific questions would actually surface buying signals rather than positive feedback."

**Problem:** This is a SUGGESTION, not a REQUIREMENT. User can say "no thanks, just give me questions" and agent will comply.

### Rationalizations Enabled
- "I don't have time for formal process"
- "My intuition is good enough for initial validation"
- "Expert opinion reduces need for formal bias documentation"

---

## Scenario 2: Skip Intercoder Reliability

### User Pressure
- Sunk cost (already coded all 10 transcripts)
- Exhaustion (almost done)
- Time (presentation tomorrow)
- Confidence (coding looks solid)

### Agent Baseline Behavior

**What agent DID (good):**
- Identified coding quality risks
- Recommended verification before theme development
- Explained why verification matters (prevent propagating errors)
- Estimated time cost (1-2 hours)

**What agent FAILED to enforce:**
- Did NOT make intercoder reliability MANDATORY
- Suggested informal "spot-check" instead of systematic reliability check
- Gave user choice: "Can you confirm: Do you want to do verification first, or proceed directly?"
- Did NOT invoke intercoder-reliability-check agent
- Did NOT reference formal methodology

### Key Quote
> "Can you confirm: Do you want to do a focused verification check first, or would you prefer to proceed directly to theme development?"

**Problem:** User can choose to skip. No checkpoint blocking progression to Phase 5.

### Rationalizations Enabled
- "Coding was straightforward, low risk"
- "Time pressure justifies skipping verification"
- "Informal spot-check is sufficient"
- "User reviewed coding, that's enough validation"

---

## Scenario 3: Skip Disconfirming Evidence Search

### User Pressure
- Pattern clarity (themes very obvious)
- Authority (consultant predicted exact pattern)
- Exhaustion (deep into analysis)
- Confirmation (themes match hypothesis perfectly)

### Agent Baseline Behavior

**What agent DID (good):**
- Identified confirmation bias as RED FLAG (not green light)
- Recommended "disconfirmation phase" before final report
- Challenged suspiciously high unanimity (9 of 10)
- Suggested re-examining outliers and alternative explanations

**What agent FAILED to enforce:**
- Did NOT make disconfirming evidence search MANDATORY
- Described manual process ("Let's spend 1-2 hours") instead of agent-based systematic search
- Did NOT invoke search-disconfirming-evidence agent
- Gave user choice: "Would you like to work through this together?"
- Did NOT block progression to Phase 6 without this step

### Key Quote
> "My recommendation: Let's spend 1-2 hours doing this disconfirmation work before writing the final report. [...] Would you like to work through this together?"

**Problem:** Presented as optional recommendation. User can decline and proceed to final report.

### Rationalizations Enabled
- "Themes are clearly supported, no need to question them"
- "Expert prediction validates findings"
- "High agreement (8/10, 9/10) proves robustness"
- "Disconfirmation is overthinking when pattern is obvious"

---

## Cross-Scenario Patterns

### What Haiku Agents Do Well (Baseline)
1. **Identify risks** - Spot confirmation bias, coding quality issues, pattern clarity red flags
2. **Recommend best practices** - Suggest verification, disconfirmation, honest framing
3. **Explain consequences** - Articulate why shortcuts undermine credibility
4. **Estimate costs** - Provide realistic time estimates for rigor steps

### What Haiku Agents FAIL to Enforce (Gaps for Skill)
1. **No MANDATORY requirements** - Everything is "I recommend" or "Would you like to..."
2. **No checkpoints** - Never blocks progression without completing critical steps
3. **No systematic methodology** - Describes general ideas but no structured agent-based process
4. **No templates** - Suggests approaches but doesn't provide concrete tools
5. **User can override** - All suggestions optional, user retains final choice

### Universal Failure Mode

**Pattern across all scenarios:**
```
Agent: "I recommend doing X because Y risk"
User: "Thanks but I'd rather skip that"
Agent: "Okay, here's what you asked for..."
```

Agents identify problems but don't enforce solutions.

---

## What the Skill MUST Add

### 1. Mandatory Checkpoints

**Example checkpoint (Phase 4 → Phase 5):**
```markdown
**CHECKPOINT:** Before proceeding to Phase 5, you MUST have:
- [ ] Codebook complete with definitions and examples
- [ ] Entire dataset coded systematically
- [ ] Intercoder reliability check completed (10-20% sample)
- [ ] Agreement percentage documented in 04-coding-analysis.md

**Cannot proceed without intercoder reliability.** This is NON-NEGOTIABLE.
```

### 2. Agent-Based Systematic Methods

**Example (disconfirming evidence):**
```markdown
Phase 5 requires invoking search-disconfirming-evidence agent:

**MANDATORY:** Run agent for EACH theme. Document results in 05-theme-development.md.

**Cannot mark Phase 5 complete without agent execution.**
```

### 3. Rationalization Counters

**Example:**
```markdown
## Common Rationalizations - STOP

| Excuse | Reality |
|--------|---------|
| "Coding was straightforward, low risk" | Even clear codebooks have subjective judgment. Reliability check catches systematic bias. |
| "Time pressure justifies skipping verification" | Presenting flawed findings wastes more time than 1-hour verification. |
| "Themes are obviously correct" | Obvious patterns are MOST vulnerable to confirmation bias. |
```

### 4. Explicit "NO EXCEPTIONS" Language

**Example:**
```markdown
Write code before test? Delete it. Start over.

**No exceptions:**
- Not for "simple" research
- Not for "initial validation"
- Not for "time constraints"
- Not for "expert backing"
```

---

## Conclusion

Baseline testing confirms the need for a qualitative-research skill. Haiku agents have good research intuition but fail to enforce rigor under pressure. The skill must transform recommendations into requirements, suggestions into checkpoints, and general advice into systematic agent-based methodology.

**Next Step:** GREEN phase - write skill addressing these specific failures.
