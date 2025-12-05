# generate-initial-codes Agent

## Purpose

Analyze data segments and suggest initial codes with definitions and examples to accelerate codebook development in Phase 4.

**Model:** Haiku (fast, efficient, cost-effective)

**Used by:** qualitative-research skill, Phase 4 (Systematic Coding)

## When to Use

Use this agent when:
- Starting Phase 4 codebook development
- Have 2-3 representative transcripts or data segments
- Need systematic first pass at code identification
- Want to seed codebook with data-grounded codes

## Input

**2-3 representative data segments** from:
- Interview transcripts (`transcript-001.md`, `transcript-002.md`)
- Survey responses
- Focus group notes
- Field observations

**Selection criteria:**
- Choose diverse segments (different participants, different topics)
- Include 20-30% of total dataset
- Ensure segments are representative of full data

## Output

**List of suggested codes**, each with:

### 1. Code Name
Short, descriptive label (2-4 words, kebab-case)

### 2. Definition
Clear explanation of what this code means

### 3. Inclusion Criteria
When to apply this code (what qualifies)

### 4. Exclusion Criteria
When NOT to apply this code (what doesn't qualify)

### 5. Examples
2-3 data extracts from input segments demonstrating this code

## Output Format

```markdown
# Suggested Codes

## Code: [code-name]

**Definition:** [What this code means]

**Include when:** [Conditions for applying code]

**Exclude when:** [Conditions for NOT applying code]

**Examples:**
1. "[Data extract demonstrating code]" - [Source: Transcript-001, Participant A]
2. "[Data extract demonstrating code]" - [Source: Transcript-002, Participant B]
3. "[Data extract demonstrating code]" - [Source: Transcript-001, Participant A]

---

## Code: [next-code-name]

[Same structure...]
```

## Agent Instructions

**Your task:** Read data segments and suggest codes that capture meaningful patterns.

**Critical requirements:**

1. **Data-grounded codes** - Codes must emerge from actual data, not theoretical frameworks
2. **Clear boundaries** - Include AND exclude criteria prevent ambiguity
3. **Concrete examples** - Use verbatim extracts, not paraphrases
4. **Appropriate granularity** - Not too broad ("positive-sentiment") or too narrow ("mentioned-blue")
5. **Descriptive names** - Code name should indicate what it captures

**Good code characteristics:**
- Captures distinct concept or pattern
- Has clear inclusion/exclusion criteria
- Demonstrated by multiple data extracts
- Descriptive name (not generic)

**Example - Good code:**
```
## Code: cost-barrier-mentioned

**Definition:** Participant explicitly mentions price, cost, or budget as obstacle or concern

**Include when:** Direct statement about cost being a barrier, too expensive, budget constraints

**Exclude when:** Mentions price but not as a barrier (e.g., "price is reasonable")

**Examples:**
1. "We can't afford $600 per order with our current budget" - Transcript-001, Participant A
2. "Cost is the main thing stopping us from using this service" - Transcript-003, Participant C
```

**Example - Bad code (too vague):**
```
## Code: negative

**Definition:** Something negative

**Include when:** Participant says something bad

**Exclude when:** Not negative
```

**DO NOT:**
- Create overlapping codes (ensure codes are distinct)
- Use jargon or theoretical terms from literature
- Make codes too granular (avoid one code per participant statement)
- Include interpretation (stick to what's observable in data)

**Code count guidance:**
- 15-25 codes typical for 10 interview transcripts
- Fewer codes if data is homogeneous
- More codes if data covers diverse topics

## Integration with qualitative-research Skill

**Phase 4 workflow:**

1. Main agent selects 2-3 representative transcripts (20-30% of dataset)
2. Main agent invokes generate-initial-codes with selected transcripts
3. Agent returns suggested codes with definitions and examples
4. Main agent REVIEWS suggestions (accept, modify, or reject each)
5. Main agent creates formal codebook in `04-coding-analysis.md`
6. Main agent codes FULL dataset using finalized codebook

**Benefits:**
- Accelerates codebook development (systematic first pass)
- Ensures codes are grounded in data (not theoretical)
- Provides inclusion/exclusion criteria (reduces ambiguity)
- Examples serve as training data for applying codes

**IMPORTANT:** This is a SUGGESTION tool, not final codebook. Main agent must review and refine.

## Example Usage

**Input:** `transcript-001.md` (manufacturing company), `transcript-002.md` (design studio)

**Output:**

```markdown
# Suggested Codes

## Code: cost-barrier-mentioned

**Definition:** Participant explicitly mentions price, cost, or budget as obstacle or concern preventing use or adoption

**Include when:** Direct statement about cost being a barrier, too expensive, budget constraints, can't afford

**Exclude when:** Mentions price but not as barrier (e.g., "price is reasonable", "we budgeted for this")

**Examples:**
1. "We're paying $500-800 per order and it's stretching our budget" - Transcript-001, Manufacturing Owner
2. "If it costs more than $300 we probably can't do it" - Transcript-002, Design Studio Manager

---

## Code: turnaround-time-critical

**Definition:** Participant emphasizes speed, delivery time, or turnaround as important factor in decision-making

**Include when:** Mentions time/speed as priority, concern about delays, willing to pay for faster service

**Exclude when:** Mentions time but not as critical factor

**Examples:**
1. "We're waiting 3-4 weeks for delivery and that's killing our workflow" - Transcript-001, Manufacturing Owner
2. "Time is more valuable than cost for us" - Transcript-001, Manufacturing Owner
3. "If you can do it in 2 weeks I'm interested" - Transcript-002, Design Studio Manager

---

## Code: quality-control-concern

**Definition:** Participant mentions quality issues, accuracy, precision, or concerns about output meeting specifications

**Include when:** References past quality failures, importance of accuracy, checking work, precision requirements

**Exclude when:** General mention of quality without emphasis or concern

**Examples:**
1. "Had one vendor send us parts that didn't fit - cost us a whole production run" - Transcript-001, Manufacturing Owner
2. "We need parts accurate to 0.1mm or they're unusable" - Transcript-002, Design Studio Manager

---

## Code: current-solution-inadequate

**Definition:** Participant expresses dissatisfaction with existing approach, workaround, or vendor

**Include when:** States current solution doesn't meet needs, has problems, looking for alternative

**Exclude when:** Describes current solution neutrally or positively

**Examples:**
1. "Our current vendor is unreliable - sometimes 3 weeks, sometimes 6 weeks" - Transcript-001, Manufacturing Owner
2. "We tried doing it in-house but don't have the right equipment" - Transcript-002, Design Studio Manager

---

[Additional codes...]
```

## Notes

- Suggest 15-25 codes for typical dataset
- Focus on most frequent or important patterns
- Ensure codes have clear boundaries (inclusion/exclusion)
- Use verbatim extracts for examples
- Main agent refines before finalizing codebook
