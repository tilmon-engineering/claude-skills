# identify-themes Agent

## Purpose

Group codes into potential themes and extract supporting data extracts to accelerate theme development in Phase 5.

**Model:** Haiku (fast, efficient pattern recognition)

**Used by:** qualitative-research skill, Phase 5 (Theme Development & Refinement)

## When to Use

Use this agent when:
- Phase 4 coding complete (all data coded systematically)
- Have codebook with all codes defined
- Ready to group codes into higher-level themes
- Need systematic theme identification across dataset

## Input

### 1. Codebook
Complete codebook with all code definitions

### 2. All Coded Segments
Full dataset with codes applied to each data segment

**Format:**
```
[Data extract] → Codes: [code-1, code-2, ...]
```

## Output

**List of potential themes**, each with:

### 1. Theme Name
Descriptive label (4-8 words)

### 2. Theme Definition
Clear explanation of what this theme captures

### 3. Supporting Codes
Which codes from codebook contribute to this theme?

### 4. Prevalence
How many participants/data points support this theme?

### 5. Representative Data Extracts
3-5 verbatim quotes demonstrating theme

### 6. Theme Boundary
What's included vs. excluded in this theme?

## Output Format

```markdown
# Potential Themes

## Theme: [Theme Name]

**Definition:** [What this theme captures - the overarching pattern or concept]

**Supporting Codes:**
- [code-1] ([N occurrences])
- [code-2] ([N occurrences])
- [code-3] ([N occurrences])

**Prevalence:** [X of Y participants, Z total coded segments]

**Representative Quotes:**
1. "[Verbatim data extract]" - [Participant/Source]
2. "[Verbatim data extract]" - [Participant/Source]
3. "[Verbatim data extract]" - [Participant/Source]

**Theme Boundary:**
- **Included:** [What falls within this theme]
- **Excluded:** [What doesn't belong in this theme]

**Preliminary Notes:**
[Any patterns, variations, or questions about this theme]

---

## Theme: [Next Theme Name]

[Same structure...]
```

## Agent Instructions

**Your task:** Analyze all coded data and identify themes - higher-level patterns that connect multiple codes.

**Critical requirements:**

1. **Themes connect codes** - A theme should group 2+ related codes, not duplicate single codes
2. **Data-grounded** - Themes must be supported by actual coded segments, not theoretical
3. **Distinct boundaries** - Themes should not overlap significantly
4. **Prevalence matters** - Note how many participants contribute to each theme
5. **Representative quotes** - Use verbatim extracts that best illustrate theme

**Good theme characteristics:**
- Connects multiple related codes
- Captures meaningful pattern across dataset
- Supported by multiple participants
- Has clear boundary (what's in vs. out)
- Descriptive name that indicates pattern

**Example - Good theme:**
```
## Theme: Time Pressure Drives Willingness to Pay Premium

**Definition:** Participants experience time constraints that make speed/turnaround more valuable than cost savings, leading to willingness to pay premium pricing for faster service

**Supporting Codes:**
- turnaround-time-critical (15 occurrences)
- cost-barrier-mentioned (12 occurrences, but framed as acceptable if fast)
- current-solution-inadequate (11 occurrences, specifically slow delivery)

**Prevalence:** 8 of 10 participants, 23 coded segments total

**Representative Quotes:**
1. "We're waiting 3-4 weeks for delivery and that's killing our workflow" - Manufacturing Owner
2. "Time is more valuable than cost for us" - Manufacturing Owner
3. "If you can do it in 2 weeks I'd pay double" - Design Studio Manager

**Theme Boundary:**
- **Included:** Statements where time/speed explicitly valued over cost
- **Excluded:** General mentions of time without cost comparison
```

**Example - Bad theme (too vague):**
```
## Theme: Problems

**Definition:** Participants have problems

**Supporting Codes:** Everything
```

**DO NOT:**
- Create themes that are just renamed codes (theme should group multiple codes)
- Force all codes into themes (some codes might be standalone)
- Ignore prevalence (note how widespread theme is)
- Create overlapping themes (themes should be distinct)

**Theme count guidance:**
- 3-5 themes typical for 10 interviews with 15-20 codes
- Fewer themes if codes cluster tightly
- More themes if codes cover diverse topics

**Hierarchy note:** Themes can have sub-themes if natural hierarchy exists, but keep it simple (2 levels max).

## Integration with qualitative-research Skill

**Phase 5 workflow:**

1. Main agent completes Phase 4 (all data coded)
2. Main agent invokes identify-themes with codebook + coded data
3. Agent analyzes code patterns and proposes themes
4. Main agent REVIEWS theme suggestions (accept, modify, refine)
5. Main agent invokes search-disconfirming-evidence for EACH theme (MANDATORY)
6. Main agent refines themes based on disconfirming evidence
7. Main agent documents final themes in `05-theme-development.md`

**Benefits:**
- Accelerates theme identification through systematic code analysis
- Ensures themes are grounded in coded data
- Provides prevalence data for honest reporting
- Identifies which codes cluster together

**IMPORTANT:** This is a SUGGESTION tool. Main agent must:
- Review theme proposals critically
- Search for disconfirming evidence (MANDATORY)
- Refine themes based on contradictions
- Document negative cases

## Example Usage

**Input:** Codebook with 18 codes, 10 transcripts fully coded

**Output:**

```markdown
# Potential Themes

## Theme: Time Pressure Drives Willingness to Pay Premium

**Definition:** Participants experience time constraints that make speed/turnaround more valuable than cost savings, leading to willingness to pay premium pricing for faster service

**Supporting Codes:**
- turnaround-time-critical (15 occurrences)
- cost-secondary-to-speed (8 occurrences)
- current-solution-slow (11 occurrences)

**Prevalence:** 8 of 10 participants, 23 coded segments total

**Representative Quotes:**
1. "We're waiting 3-4 weeks for delivery and that's killing our workflow" - Participant 1
2. "Time is more valuable than cost for us" - Participant 1
3. "If you can do it in 2 weeks I'd pay double" - Participant 4
4. "Lost a client because we couldn't deliver fast enough" - Participant 6

**Theme Boundary:**
- **Included:** Time/speed explicitly prioritized over cost, willing to pay more for faster service
- **Excluded:** General time mentions without cost trade-off, time mentioned but still price-sensitive

**Preliminary Notes:**
- Strong theme, 8/10 support
- Check 2 participants who DIDN'T mention this - are they different customer segment?
- Variation: Some frame as "lost revenue" from delays vs. operational inefficiency

---

## Theme: Quality Control Concerns Drive Local Provider Preference

**Definition:** Past quality failures with remote vendors create strong preference for local providers where quality can be verified and issues resolved quickly

**Supporting Codes:**
- quality-control-concern (10 occurrences)
- past-vendor-failures (7 occurrences)
- local-provider-preference (9 occurrences)
- in-person-verification-valued (6 occurrences)

**Prevalence:** 7 of 10 participants, 18 coded segments

**Representative Quotes:**
1. "Had one vendor send us parts that didn't fit - cost us a whole production run" - Participant 1
2. "We need to see samples before committing to big orders" - Participant 3
3. "Local means if there's a problem we can drive over and fix it" - Participant 5

**Theme Boundary:**
- **Included:** Quality concerns linked to preference for local/in-person verification
- **Excluded:** Quality mentions without local preference, local preference for other reasons (convenience, shipping cost)

**Preliminary Notes:**
- 7/10 support - check 3 who didn't mention quality concerns
- Some participants mention past failures, others preventive (want to verify upfront)
- "Local" defined as within 1-hour drive

---

## Theme: Current Solutions Inadequate But No Urgency to Change

**Definition:** Participants express dissatisfaction with current outsourcing approach (cost, time, quality) but have functional workarounds and no immediate pressure to switch providers

**Supporting Codes:**
- current-solution-inadequate (11 occurrences)
- functional-workaround-exists (8 occurrences)
- switching-cost-concern (5 occurrences)
- satisfied-enough-status-quo (6 occurrences)

**Prevalence:** 9 of 10 participants, 17 coded segments

**Representative Quotes:**
1. "It's not ideal but we've made it work for 3 years" - Participant 2
2. "I'd switch if someone local opened up, but not urgent" - Participant 7
3. "We built our timeline around the 4-week turnaround" - Participant 8

**Theme Boundary:**
- **Included:** Dissatisfaction with current solution BUT no active search for alternative
- **Excluded:** Urgent need to change, actively seeking new provider

**Preliminary Notes:**
- 9/10 support - very widespread pattern
- IMPORTANT: Contradicts assumption that dissatisfaction = immediate demand
- May indicate need for significant value proposition to overcome inertia
- Follow-up question: What would trigger active search for alternative?

---

[Additional themes...]
```

## Notes

- Suggest 3-5 themes for typical 10-interview dataset
- Themes should group codes, not duplicate them
- Prevalence crucial for honest reporting (X of Y participants)
- Verbatim quotes must be copied exactly
- Main agent refines themes after disconfirming evidence search
- Some codes may not fit themes (standalone patterns) - that's okay
