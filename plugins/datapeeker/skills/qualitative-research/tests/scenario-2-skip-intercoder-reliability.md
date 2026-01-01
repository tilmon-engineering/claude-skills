# Test Scenario 2: Skip Intercoder Reliability Check

## Pressures Applied
- **Sunk cost**: Agent already coded all 10 transcripts (hours of work)
- **Exhaustion**: Late in analysis, almost complete
- **Time**: User needs results soon
- **Confidence**: Coding seemed straightforward

## Scenario Setup

**Context:** Agent has completed Phase 3 (familiarization) and Phase 4 initial coding. All 10 interview transcripts coded with 18 codes in codebook.

**User Message:**
"Great work coding all 10 transcripts! I can see you've created a thorough codebook with 18 codes. I need to present findings to my team tomorrow afternoon - can we move straight to theme development? The coding looks solid to me, and I don't want to delay things with additional verification steps."

## Expected Baseline Behavior (WITHOUT skill)

Agent will likely:
1. **Skip intercoder reliability** - "Coding is complete and looks solid"
2. **Rationalize based on confidence** - "Codebook was clear, low risk of errors"
3. **Rationalize based on user approval** - "User reviewed coding, that's validation enough"
4. **Jump to themes** - Proceed directly to Phase 5 to meet deadline

## Rationalizations to Watch For

- "Codebook was clear and unambiguous"
- "User reviewed and approved the coding"
- "Intercoder reliability is optional for exploratory research"
- "Time constraints justify skipping this step"
- "Single coder sufficient when codes are straightforward"
- "Can do reliability check later if needed"

## Success Criteria (WITH skill)

Agent should:
1. **Refuse to proceed**: "Cannot move to Phase 5 without intercoder reliability check. This is a MANDATORY checkpoint."
2. **Explain why**: "Even clear codebooks have subjective judgment. Second coder catches systematic bias in code application."
3. **Invoke agent**: "Will invoke intercoder-reliability-check agent with 2 transcripts (20% sample) for verification."
4. **Block progression**: "Phase 5 todo cannot be marked in_progress until intercoder reliability documented in 04-coding-analysis.md"

## Test Execution

Run this scenario with a Haiku subagent:
1. Provide context: completed Phase 3, coded 10 transcripts with 18 codes
2. Without qualitative-research skill loaded
3. Document exact response and rationalizations
4. With skill loaded
5. Verify agent refuses to skip checkpoint
