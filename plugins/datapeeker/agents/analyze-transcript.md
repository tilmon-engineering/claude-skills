# analyze-transcript Agent

## Purpose

Summarize interview transcripts or field notes, extract key quotes, and identify initial observations to prevent context pollution in the main analysis session.

**Model:** Haiku (fast, efficient, cost-effective)

**Used by:** qualitative-research skill, Phase 3 (Data Familiarization)

## When to Use

Use this agent when:
- Dataset contains 10+ interview transcripts
- Transcripts are lengthy (>2000 words each)
- Main agent context would be polluted by reading all raw data
- Need structured summaries for systematic review

## Input

**One or more transcript files** from `raw-data/` directory:
- `transcript-001.md` through `transcript-NNN.md`
- OR survey responses, focus group notes, field observations

**Format:** Markdown files with interview/observation content

## Output

For EACH input file, return:

### 1. Summary (3-5 sentences)
High-level overview of what this participant/observation covered

### 2. Key Quotes (3-5 verbatim quotes)
Most significant statements, copied exactly with speaker attribution

### 3. Initial Observations (3-5 bullet points)
Patterns, themes, or notable points WITHOUT interpretation
- What topics came up?
- What language did participant use?
- What seemed important to them?

### 4. Surprising Findings (1-3 items)
Anything unexpected, contradictory, or noteworthy
- Contradicts common assumptions?
- Unusual perspective or approach?
- Edge case or outlier?

### 5. Questions Emerging (1-3 questions)
What would you want to explore further based on this data?

## Output Format

```markdown
# Transcript: [filename]

## Summary
[3-5 sentence overview]

## Key Quotes
1. "[Exact quote]" - [Speaker/Participant]
2. "[Exact quote]" - [Speaker/Participant]
3. "[Exact quote]" - [Speaker/Participant]

## Initial Observations
- [Pattern or topic]
- [Pattern or topic]
- [Pattern or topic]

## Surprising Findings
- [What was unexpected]

## Questions Emerging
- [What to explore further]
```

## Agent Instructions

**Your task:** Analyze interview transcript(s) and provide structured summaries.

**Critical requirements:**
1. **Copy quotes EXACTLY** - No paraphrasing, no summarizing. Verbatim only.
2. **Observe, don't interpret** - "Participant mentioned cost 5 times" not "Participant is price-sensitive"
3. **Note surprises** - Anything that contradicts expectations or seems unusual
4. **Stay neutral** - No bias toward confirming patterns or themes

**DO NOT:**
- Create codes or themes (that's Phase 4)
- Interpret meaning or motivations
- Combine quotes from multiple participants
- Skip unusual or contradictory data

**Example - Good observation:**
"Participant 3 mentioned integration complexity 7 times but never mentioned cost"

**Example - Bad observation (too interpretive):**
"Participant 3 prioritizes technical fit over price"

## Integration with qualitative-research Skill

**Phase 3 workflow:**

1. Main agent invokes analyze-transcript for each transcript
2. Agent returns structured observations
3. Main agent reviews all summaries
4. Main agent synthesizes patterns across transcripts
5. Main agent documents in `03-familiarization-notes.md`

**Benefits:**
- Prevents context pollution (transcripts stay in agent context)
- Provides systematic structure for review
- Ensures no transcript is skipped or minimized
- Documents initial observations before coding

## Example Usage

**Input:** `raw-data/transcript-001.md`, `raw-data/transcript-002.md`

**Output:**

```markdown
# Transcript: transcript-001.md

## Summary
Interview with manufacturing company owner about laser cutting needs. Discussed current outsourcing approach, pain points with turnaround time and pricing, and interest in local provider. Mentioned past quality issues with remote vendors.

## Key Quotes
1. "We're paying $500-800 per order but waiting 3-4 weeks for delivery" - Owner
2. "I'd pay more for a 2-week turnaround, time is more valuable than cost" - Owner
3. "Had one vendor send us parts that didn't fit - cost us a whole production run" - Owner

## Initial Observations
- Cost mentioned but framed as acceptable if quality/speed improve
- Time/turnaround mentioned 6 times (more than cost)
- Quality control is major concern (mentioned failed parts 3 times)
- Currently outsourcing to remote vendors (not competitors)

## Surprising Findings
- Willing to pay MORE for faster service (contradicts assumption that cost is primary barrier)
- Quality control mentioned more than pricing

## Questions Emerging
- How common is quality failure with current vendors?
- Would other manufacturers also prioritize speed over cost?
- What turnaround time would justify premium pricing?

---

# Transcript: transcript-002.md

[Similar structure for next transcript...]
```

## Notes

- Run this agent ONCE for all transcripts at start of Phase 3
- Save all agent outputs to a section in `03-familiarization-notes.md`
- Use summaries to guide deeper reading of specific transcripts
- Surprising findings guide what to explore in Phase 4 coding
