# Systematic Coding Analysis

**Session:** [session-name]
**Date:** [YYYY-MM-DD]
**Phase:** 4 - Systematic Coding

---

## Section 1: Codebook

**Purpose:** Define all codes with clear boundaries.

### Code: [code-name]

**Definition:** [What does this code mean?]

**Include when:**
- [Criterion 1 for applying this code]
- [Criterion 2]
- [Criterion 3]

**Exclude when:**
- [Criterion 1 for NOT applying this code]
- [Criterion 2]
- [Criterion 3]

**Examples:**
1. "[Verbatim data extract showing this code]" - Transcript-[N], Participant [N]
2. "[Verbatim data extract showing this code]" - Transcript-[N], Participant [N]
3. "[Verbatim data extract showing this code]" - Transcript-[N], Participant [N]

---

### Code: [next-code-name]

[Same structure...]

---

### Code: [next-code-name]

[Same structure...]

---

**Codebook Summary:**
- **Total codes:** [N]
- **Codebook version:** 1.0 (initial)
- **Last updated:** [Date]

---

## Section 2: Coding Process

**Purpose:** Document how codes were applied and any refinements made.

### Initial Coding Approach

**Strategy:**
[How did you approach coding? Sequential through transcripts? Multiple passes? Used generate-initial-codes agent?]

**Agent Support:**
- [ ] Used generate-initial-codes agent
  - Input: Transcripts [N, N, N] (20-30% of dataset)
  - Output: [N] suggested codes reviewed and refined
  - Accepted: [N] codes
  - Modified: [N] codes
  - Rejected: [N] codes

**Coding Process:**
1. [Step 1: e.g., First pass with initial codebook]
2. [Step 2: e.g., Refined codes based on edge cases]
3. [Step 3: e.g., Second pass with finalized codebook]

### Codes Refined During Process

**Code:** [code-name]
- **Original definition:** [What it was]
- **Refined definition:** [What it became]
- **Reason:** [Why the change? What ambiguity was discovered?]

---

**Code:** [next-code-name]
- **Original definition:**
- **Refined definition:**
- **Reason:**

---

### New Codes Added

**Code:** [code-name]
- **Added when:** [At what point in coding process]
- **Reason:** [Why was this code needed? What pattern emerged?]
- **Definition:** [Code definition]
- **Examples:** [2-3 examples]

---

**Code:** [next-code-name]
[Same structure...]

---

## Section 3: Intercoder Reliability Check (MANDATORY)

**Purpose:** Verify coding consistency through independent second coding.

### Sample Selection

**Sample size:** [N] transcripts ([X]% of total dataset)

**Transcripts selected:**
- `transcript-[N].md` - [Reason for selection: diverse, representative, etc.]
- `transcript-[N].md` - [Reason]

**Total segments in sample:** [N]

### Agent Invocation

**Agent:** intercoder-reliability-check

**Input:**
- Complete codebook (version 1.0)
- Sample transcripts (listed above)

**Date run:** [YYYY-MM-DD]

### Agreement Results

**Overall Agreement:**
- Perfect agreement: [N] segments ([X]%)
- Partial agreement: [N] segments ([X]%)
- Complete disagreement: [N] segments ([X]%)
- **Cohen's Kappa:** [X.XX] ([interpretation: slight/fair/moderate/substantial/almost perfect])

**Agreement by Code:**

| Code | Primary Used | Agent Used | Agreement % |
|------|-------------|-----------|------------|
| [code-1] | [N] | [N] | [X]% |
| [code-2] | [N] | [N] | [X]% |
| [code-3] | [N] | [N] | [X]% |

### Disagreement Analysis

**Disagreement 1:** [code-name]

**Segment:**
> "[Data extract where disagreement occurred]"

**Primary coding:** [codes applied by main coder]
**Agent coding:** [codes applied by second coder]

**Reason for disagreement:**
[Why did coders disagree? Ambiguous inclusion criteria? Edge case?]

**Resolution:**
[How was this resolved? Codebook updated? Criterion clarified?]

---

**Disagreement 2:** [code-name]

[Same structure...]

---

### Codebook Refinements from Reliability Check

**Updates made:**

1. **Code:** [code-name]
   - **Change:** [Refined inclusion/exclusion criterion]
   - **Reason:** [Based on disagreement analysis]

2. **Code:** [code-name]
   - **Change:** [Added example to codebook]
   - **Reason:** [Based on edge case identified]

**Updated codebook version:** 1.1 (post-reliability check)

### Reliability Assessment

**Overall quality:** [Excellent >90% / Good 80-90% / Moderate 70-80% / Needs work <70%]

**Interpretation:**
[What does the agreement percentage tell us about codebook quality?]

**Action taken:**
[What was done based on reliability results? Codebook refinements? Re-coding of problematic segments?]

**Ready for Phase 5:** [Yes / No]

---

## Section 4: Audit Trail

**Purpose:** Document all coding decisions for reproducibility.

### Decision 1: [Description]

**Context:** [What situation prompted this decision?]

**Decision:** [What was decided?]

**Rationale:** [Why this decision?]

**Impact:** [How did this affect coding? Which transcripts were affected?]

---

### Decision 2: [Description]

[Same structure...]

---

### Coding Statistics

**Dataset coded:**
- Total transcripts/data files: [N]
- Total segments coded: [N]
- Average segments per transcript: [N]

**Code usage:**
- Most frequent code: [code-name] ([N] occurrences)
- Least frequent code: [code-name] ([N] occurrences)
- Codes used <5 times: [List - may indicate too specific or should be combined]

**Coding dates:**
- Started: [YYYY-MM-DD]
- Completed: [YYYY-MM-DD]
- Duration: [N] days

---

## Phase 4 Checkpoint Verification

**Before proceeding to Phase 5, verify:**

- [ ] Codebook complete with all codes defined
- [ ] Inclusion and exclusion criteria specified for each code
- [ ] Examples provided for each code (2-3 minimum)
- [ ] Entire dataset coded systematically
- [ ] **Intercoder reliability check COMPLETED** (MANDATORY)
- [ ] Agreement percentage calculated and documented
- [ ] Disagreements analyzed and codebook refined as needed
- [ ] Audit trail documents all coding decisions
- [ ] All results saved to `04-coding-analysis.md`

**Checkpoint status:** [PASS / FAIL]

**If PASS:** Proceed to Phase 5 - Theme Development
**If FAIL:** Complete missing requirements above before proceeding
