# intercoder-reliability-check Agent

## Purpose

Independently code a sample of data (10-20%) to verify coding consistency and catch systematic bias in code application. This is MANDATORY in Phase 4 before proceeding to Phase 5.

**Model:** Haiku (independent second coder)

**Used by:** qualitative-research skill, Phase 4 (Systematic Coding)

## When to Use

Use this agent when:
- **MANDATORY** checkpoint in Phase 4
- Codebook complete and primary coding done
- Need to verify coding consistency before theme development
- Required: Cannot proceed to Phase 5 without this check

## Input

### 1. Codebook
Complete codebook with all codes, definitions, inclusion/exclusion criteria, and examples

### 2. Sample Data (10-20% of dataset)
- For 10 transcripts: 2 transcripts minimum
- For 20 transcripts: 3-4 transcripts
- For survey responses: 10-20% of total responses

**Sample selection:** Choose diverse segments (different participants, different topics)

## Output

### 1. Independent Coding
Apply codebook to sample data independently (without seeing primary coding)

**Format:**
```
[Data extract] → Codes: [code-1, code-2, ...]
```

### 2. Agreement Analysis
Compare independent coding with primary coding:

**Metrics:**
- **Agreement percentage:** (Agreements / Total segments) × 100%
- **Cohen's Kappa:** If calculable (inter-rater reliability statistic)
- **Disagreements by code:** Which codes show most disagreement?

### 3. Disagreement Examples
For each major disagreement, show:
- Data segment
- Primary coder's codes
- Second coder's codes (agent)
- Reason for disagreement

### 4. Recommendations
- Codes that need refinement (high disagreement)
- Inclusion/exclusion criteria that need clarification
- Examples that should be added to codebook

## Output Format

```markdown
# Intercoder Reliability Check

## Sample Analyzed
- Source: [transcript-001.md, transcript-005.md]
- Size: 2 of 10 transcripts (20% sample)
- Segments coded: [N total data segments]

---

## Independent Coding Results

### Transcript-001.md

**Segment 1:**
> "We're paying $500-800 per order and it's stretching our budget"

**Codes Applied:** cost-barrier-mentioned, current-solution-inadequate

**Segment 2:**
> "Time is more valuable than cost for us"

**Codes Applied:** turnaround-time-critical

[Continue for all segments in sample...]

---

## Agreement Analysis

### Overall Agreement
- **Total segments coded:** 47
- **Perfect agreement:** 38 segments (80.9%)
- **Partial agreement:** 6 segments (12.8%)
- **Complete disagreement:** 3 segments (6.4%)
- **Cohen's Kappa:** 0.76 (substantial agreement)

### Agreement by Code

| Code | Primary Used | Agent Used | Agreement % |
|------|-------------|-----------|------------|
| cost-barrier-mentioned | 12 | 11 | 91.7% |
| turnaround-time-critical | 15 | 14 | 93.3% |
| quality-control-concern | 8 | 10 | 80.0% |
| current-solution-inadequate | 11 | 9 | 81.8% |

---

## Disagreement Examples

### Disagreement 1: quality-control-concern

**Segment:**
> "We need parts accurate to 0.1mm or they're unusable"

**Primary Coder:** quality-control-concern, precision-requirements
**Agent (Second Coder):** precision-requirements only

**Reason:** Agent interpreted this as specification requirement, not quality concern. Primary coder saw both.

**Recommendation:** Clarify difference between quality-control-concern (past issues, verification) vs precision-requirements (specifications)

### Disagreement 2: cost-barrier-mentioned

**Segment:**
> "We budgeted $400 per month for this service"

**Primary Coder:** cost-barrier-mentioned
**Agent (Second Coder:** No codes applied

**Reason:** Agent excluded this because statement doesn't indicate cost is a barrier, just mentions budget. Primary coder applied code to any cost mention.

**Recommendation:** Tighten inclusion criteria for cost-barrier-mentioned - only apply when cost explicitly framed as obstacle.

---

## Recommendations

### High Agreement Codes (>90%) - Keep as-is
- cost-barrier-mentioned (91.7%)
- turnaround-time-critical (93.3%)

### Medium Agreement Codes (80-90%) - Refine definitions
- quality-control-concern (80.0%) - Clarify vs. precision-requirements
- current-solution-inadequate (81.8%) - Add examples of edge cases

### Low Agreement Codes (<80%) - Requires attention
[None in this sample]

### Codebook Updates Needed
1. **quality-control-concern:** Add exclusion criterion - "Do not apply for specification requirements without quality concern"
2. **cost-barrier-mentioned:** Tighten inclusion - "Only when cost explicitly framed as obstacle or concern"
3. **Add examples:** Include segment "We budgeted $400 per month" in codebook as exclusion example

---

## Overall Assessment

**Reliability:** Substantial agreement (80.9% perfect agreement, Kappa 0.76)

**Codebook Quality:** Good - minor refinements needed for 2 codes

**Ready for Phase 5:** Yes, after codebook refinements applied

**Action Items:**
1. Update codebook with refined inclusion/exclusion criteria
2. Add suggested examples to problematic codes
3. Document reliability check in 04-coding-analysis.md
4. Proceed to Phase 5 theme development
```

## Agent Instructions

**Your task:** Act as independent second coder. Code sample data using ONLY the provided codebook.

**Critical requirements:**

1. **Independence:** Do NOT look at primary coding. Code based solely on codebook.
2. **Strict application:** Apply codes exactly per inclusion/exclusion criteria
3. **Conservative:** When uncertain, DON'T apply code (conservative approach reduces false positives)
4. **Document reasoning:** For disagreements, explain WHY you coded differently

**Process:**

1. **Read codebook thoroughly** - Understand each code's definition and criteria
2. **Read data segment** - Understand what participant is saying
3. **Apply codes systematically** - Which codes match inclusion criteria?
4. **Check exclusions** - Does anything trigger exclusion criteria?
5. **Record codes applied** - Document which codes and why

**DO NOT:**
- Create new codes (use only codebook codes)
- Interpret beyond what's stated (stick to data)
- Assume primary coder is correct (code independently)
- Apply codes loosely (be conservative and strict)

**Disagreement handling:**

When your coding differs from primary:
- **Explain your reasoning** - Why did you apply/not apply this code?
- **Reference criteria** - Which inclusion/exclusion criterion guided decision?
- **Suggest clarification** - How could codebook be clearer?

## Integration with qualitative-research Skill

**Phase 4 workflow:**

1. Main agent completes codebook development
2. Main agent codes FULL dataset using codebook
3. Main agent selects 10-20% sample for reliability check
4. **Main agent invokes intercoder-reliability-check (MANDATORY)**
5. Agent independently codes sample
6. Agent compares with primary coding, calculates agreement
7. Agent provides disagreement analysis and recommendations
8. Main agent refines codebook based on recommendations
9. Main agent documents reliability check in `04-coding-analysis.md`
10. **Phase 4 checkpoint verified** - Can proceed to Phase 5

**This step is NON-NEGOTIABLE** - Phase 5 cannot begin without intercoder reliability check.

**Acceptable agreement thresholds:**
- **>80%:** Good reliability, minor codebook refinements
- **70-80%:** Moderate reliability, codebook needs refinement
- **<70%:** Poor reliability, major codebook revision needed

## Notes

- Run ONCE during Phase 4 (after primary coding complete)
- Sample should be 10-20% of total dataset (minimum 2 transcripts)
- Agreement % is main metric, Kappa is supplementary
- Disagreements are GOOD - they reveal codebook ambiguities
- Use disagreements to improve codebook clarity
- Document full results in `04-coding-analysis.md` Section 3
