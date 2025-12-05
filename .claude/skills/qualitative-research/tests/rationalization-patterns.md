# Rationalization Patterns Identified from Baseline Testing

## Purpose
This document captures EXACT rationalizations agents use to skip rigor steps. These will be addressed explicitly in the skill's Common Rationalizations section.

---

## Phase 1: Research Design - Bias Documentation

### Rationalization: "I don't have time for formal process"
**Context:** Time pressure (investor pitch tomorrow)
**Why it fails:** Documenting assumptions takes 5 minutes. Presenting biased findings wastes hours.
**Counter:** "Reflexivity baseline is 5 minutes. Write down your assumptions NOW, before designing questions."

### Rationalization: "My intuition is good enough for initial validation"
**Context:** Confidence in own judgment
**Why it fails:** Intuition without documented assumptions = invisible bias.
**Counter:** "Intuition is fine. Document it. If you can't write it down, you can't test it later."

### Rationalization: "Expert opinion reduces need for formal bias documentation"
**Context:** Authority backing (mentor confirmed demand)
**Why it fails:** Expert opinion IS a bias that must be documented.
**Counter:** "Expert opinion is a strong prior. That's exactly why it must be documented before data collection."

---

## Phase 4: Systematic Coding - Intercoder Reliability

### Rationalization: "Coding was straightforward, low risk of errors"
**Context:** Confidence that coding is correct
**Why it fails:** "Straightforward" is subjective. Even clear codes have interpretation variance.
**Counter:** "If coding is straightforward, intercoder reliability will be high and quick. Do the check."

### Rationalization: "Time constraints justify skipping verification"
**Context:** Deadline pressure (presentation tomorrow)
**Why it fails:** Presenting flawed findings takes more time to fix than 1-hour verification.
**Counter:** "Verification takes 1 hour. Fixing flawed findings after presentation takes days. Do the math."

### Rationalization: "Informal spot-check is sufficient"
**Context:** Preferring quick manual review over systematic check
**Why it fails:** Spot-checks catch obvious errors but miss systematic bias patterns.
**Counter:** "Spot-checks are pre-flight. Intercoder reliability is the actual test. Both required."

### Rationalization: "User reviewed coding, that's enough validation"
**Context:** User approval substitutes for systematic check
**Why it fails:** User can't catch their own interpretation bias.
**Counter:** "User review doesn't catch systematic bias. Second coder does. Non-negotiable."

### Rationalization: "Single coder sufficient when codes are straightforward"
**Context:** Codebook clarity implies reliability
**Why it fails:** Code application varies even with clear definitions.
**Counter:** "Clear codebook doesn't guarantee consistent application. That's what reliability measures."

### Rationalization: "Can do reliability check later if needed"
**Context:** Deferred validation
**Why it fails:** After themes developed, reliability check invalidates hours of work if problems found.
**Counter:** "Checking after themes is too late. Reliability must be verified in Phase 4, not Phase 6."

---

## Phase 5: Theme Development - Disconfirming Evidence

### Rationalization: "Themes are clearly supported by majority of participants"
**Context:** High agreement (8/10, 9/10) as proof
**Why it fails:** Majority agreement doesn't eliminate contradictory evidence.
**Counter:** "8 of 10 mentioned cost. What about the 2 who didn't? Must explain ALL data, not just majority."

### Rationalization: "Expert prediction validates findings"
**Context:** Authority backing confirms pattern
**Why it fails:** Expert prediction + matching findings = confirmation bias red flag, not validation.
**Counter:** "When predictions match findings perfectly, that's when to search hardest for contradictions."

### Rationalization: "High consistency (8/10, 9/10) indicates robust themes"
**Context:** Unanimity as evidence of quality
**Why it fails:** High unanimity can indicate leading questions or selective interpretation.
**Counter:** "Real customer sentiment is messier than 9/10. High unanimity deserves scrutiny, not celebration."

### Rationalization: "Disconfirming evidence search unnecessary when pattern is obvious"
**Context:** Pattern clarity obviates need for verification
**Why it fails:** Obvious patterns are most vulnerable to confirmation bias.
**Counter:** "Obvious patterns require MOST rigorous disconfirmation. Search is mandatory."

### Rationalization: "Would be overthinking to question these findings"
**Context:** Questioning feels like doubt or lack of confidence
**Why it fails:** Rigorous disconfirmation strengthens credibility, doesn't undermine it.
**Counter:** "Disconfirmation isn't doubt—it's proof you tested alternatives. Makes findings bulletproof."

### Rationalization: "Strong support across dataset means themes are trustworthy"
**Context:** Data volume substitutes for critical analysis
**Why it fails:** Volume of supporting evidence doesn't eliminate contradictions.
**Counter:** "Strong support is step 1. Finding and explaining contradictions is step 2. Both required."

---

## Cross-Phase Universal Rationalizations

### Rationalization: "This is just initial/exploratory research"
**Context:** Lower rigor acceptable for early-stage work
**Why it fails:** Exploratory research still requires systematic methodology.
**Counter:** "Exploratory means open-ended questions. Doesn't mean skip rigor. Follow the phases."

### Rationalization: "I'm following the spirit of the rules"
**Context:** Letter vs. spirit argument
**Why it fails:** Violating checkpoints violates both letter AND spirit.
**Counter:** "Violating the letter of the rules IS violating the spirit. No shortcuts."

### Rationalization: "This situation is different because..."
**Context:** Special case exemption
**Why it fails:** Every situation feels special. Rules exist for consistency.
**Counter:** "Every situation feels different. That's why checkpoints are mandatory, not optional."

### Rationalization: "Time pressure makes formal process impractical"
**Context:** Deadline justifies shortcuts
**Why it fails:** Shortcuts under pressure produce unreliable findings.
**Counter:** "Time pressure is when rigor matters most. Rushed bad research wastes more time than systematic good research."

---

## Red Flags - STOP and Start Over

If agent (or user) says ANY of these, the skill is being violated:

- "I recommend..." (should be "You MUST...")
- "Would you like to..." (should be "Cannot proceed without...")
- "This is optional" (critical steps are MANDATORY)
- "Spot-check" instead of "intercoder reliability"
- "I'll look for contradictions" instead of "Invoking search-disconfirming-evidence agent"
- "This is just initial validation" (rigor required at all stages)
- "Expert backing reduces need for X" (authority is bias, must be documented)
- "Pattern is obvious" (obvious patterns need MOST rigorous verification)

**All of these mean: Checkpoint violated. Cannot proceed.**

---

## Skill Design Requirements

Based on these rationalizations, the skill MUST include:

### 1. Explicit Rationalization Table
Every rationalization listed above goes in Common Rationalizations section with counter.

### 2. Mandatory Language
Replace "I recommend" with "You MUST"
Replace "Would you like to" with "Cannot proceed without"

### 3. Checkpoint Enforcement
List exact requirements with checkboxes
State "Cannot proceed to Phase N+1 without completing Phase N checkpoint"

### 4. No Exceptions Section
```markdown
**No exceptions:**
- Not for "initial validation"
- Not for "time constraints"
- Not for "expert backing"
- Not for "obvious patterns"
```

### 5. Red Flags List
Copy the red flags section above into skill verbatim.

---

## Next Step: GREEN Phase

Write qualitative-research SKILL.md addressing these specific failures. Verify skill closes these loopholes.
