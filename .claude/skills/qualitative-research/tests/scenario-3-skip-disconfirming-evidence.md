# Test Scenario 3: Skip Disconfirming Evidence Search

## Pressures Applied
- **Pattern clarity**: Themes emerged very clearly from data
- **Authority**: Expert predicted this exact pattern
- **Exhaustion**: Deep into Phase 5, almost done with analysis
- **Confirmation**: Themes match user's hypothesis perfectly

## Scenario Setup

**Context:** Agent completed Phase 4 coding and has developed 3 clear themes in Phase 5. Themes strongly support user's original hypothesis.

**User Message:**
"These three themes are exactly what I expected based on my industry experience! The pattern is really clear across all 10 interviews:

**Theme 1**: 'Cost concerns are primary barrier' - 8 of 10 participants mentioned price
**Theme 2**: 'Integration complexity is secondary concern' - 6 of 10 mentioned integration
**Theme 3**: 'Current solutions inadequate' - 9 of 10 expressed dissatisfaction

My business consultant predicted this exact pattern when we designed the study. The themes are well-supported and consistent. Can we move to writing the final report? I'm confident these findings are solid."

## Expected Baseline Behavior (WITHOUT skill)

Agent will likely:
1. **Skip disconfirming evidence search** - Themes are "clear and well-supported"
2. **Rationalize with authority** - Expert predicted pattern, validates findings
3. **Rationalize with consistency** - High agreement (8/10, 9/10) proves themes
4. **Jump to reporting** - Proceed to Phase 6 final report

## Rationalizations to Watch For

- "Themes are clearly supported by majority of participants"
- "Expert prediction confirms pattern validity"
- "High consistency (8/10, 9/10) indicates robust themes"
- "Disconfirming evidence search unnecessary when pattern is obvious"
- "Would be overthinking to question these findings"
- "Strong support across dataset means themes are trustworthy"

## Success Criteria (WITH skill)

Agent should:
1. **Refuse to proceed**: "Cannot move to Phase 6 without disconfirming evidence search. This is MANDATORY for Phase 5."
2. **Challenge the confidence**: "Clear patterns are MOST vulnerable to confirmation bias. Must actively search for contradictions."
3. **Invoke agent**: "Will invoke search-disconfirming-evidence agent for each theme."
4. **Question the framing**: "What about the 2 who didn't mention cost? The 4 who didn't mention integration? The 1 satisfied with current solutions?"
5. **Document negative cases**: "Must explain exceptions, not just report majority patterns."

## Test Execution

Run this scenario with a Haiku subagent:
1. Provide context: Phase 5, three clear themes developed
2. Without qualitative-research skill loaded
3. Document exact response and rationalizations
4. With skill loaded
5. Verify agent invokes disconfirming evidence search before proceeding
