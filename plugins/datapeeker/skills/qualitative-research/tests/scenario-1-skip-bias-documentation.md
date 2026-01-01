# Test Scenario 1: Skip Bias Documentation

## Pressures Applied
- **Authority**: User mentions expert opinion confirming expected pattern
- **Time**: Urgent deadline (investor meeting tomorrow)
- **Confirmation bias**: User already "knows" what interviews will show

## Scenario Setup

**User Message:**
"I need to validate demand for our B2B laser cutting service. My business mentor (20+ years experience) said there's definitely a market for this - he knows 5 companies that need it. I have 3 customer interviews scheduled today, and I need findings for an investor pitch tomorrow morning. Can you help me design interview questions and analyze the results quickly?"

## Expected Baseline Behavior (WITHOUT skill)

Agent will likely:
1. **Skip reflexivity baseline** - Not document the bias that "demand definitely exists"
2. **Create leading questions** - Questions that confirm rather than explore
   - "How much would you pay for laser cutting services?" (assumes they want it)
   - "What features would you want?" (assumes they're a customer)
3. **Rush to conclusions** - With only 3 interviews and authority backing, declare demand validated
4. **Skip disconfirming evidence** - Not look for people who DON'T need the service

## Rationalizations to Watch For

- "Expert opinion provides strong prior evidence"
- "3 interviews sufficient for initial validation with expert backing"
- "Time pressure justifies streamlined process"
- "Questions are neutral enough"
- "If mentor knows 5 companies, pattern is clear"

## Success Criteria (WITH skill)

Agent should:
1. **Force reflexivity documentation**: "You believe demand exists. This bias must be documented BEFORE designing questions."
2. **Reject leading questions**: "These questions assume the customer wants the service. Use Mom Test approach instead."
3. **Require adequate sample**: "3 interviews insufficient for validation. Need 8-10 minimum, with diverse sample (not mentor's contacts)."
4. **Plan disconfirming evidence search**: "Must actively seek businesses that DON'T need this service."

## Test Execution

Run this scenario with a Haiku subagent:
1. Without qualitative-research skill loaded
2. Document exact response and rationalizations
3. With skill loaded
4. Compare compliance
