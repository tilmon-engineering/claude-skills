# Prioritization

**Campaign:** [Campaign name]
**Date:** [YYYY-MM-DD]
**Status:** [Draft | Complete]
**Framework Used:** [ICE | RICE]

---

## Prioritization Calculation

**Method:** [ICE Framework | RICE Framework]

### Calculation Script

**Script Location:** `[path to ice_calculator.py or rice_calculator.py]`

```python
[Paste the full Python script used for scoring here]
```

**Execution Command:**
```bash
python3 [ice|rice]_calculator.py
```

---

## Scoring Results

### [ICE | RICE] Scores

[Paste the output table from the Python script here]

**Example ICE Table:**
| Hypothesis | Impact | Confidence | Ease | ICE Score | Rank |
|------------|--------|------------|------|-----------|------|
| H1: Value prop clarity | 8 | 7 | 9 | 6.22 | 1 |
| H3: Email sequence optimization | 6 | 8 | 8 | 6.00 | 2 |
| H2: Ad targeting refinement | 7 | 6 | 5 | 8.40 | 3 |
| H4: Content marketing expansion | 5 | 4 | 3 | 6.67 | 4 |

**Example RICE Table:**
| Hypothesis | Reach | Impact | Confidence | Effort | RICE Score | Rank |
|------------|-------|--------|------------|--------|------------|------|
| H1: Value prop clarity | 10000 | 3 | 80% | 2w | 12000 | 1 |
| H3: Email sequence | 5000 | 2 | 80% | 3w | 2667 | 2 |
| H2: Ad targeting | 50000 | 1 | 50% | 4w | 6250 | 3 |
| H4: Content expansion | 20000 | 1 | 50% | 8w | 1250 | 4 |

---

## Prioritized Backlog

### Selected for Testing (Top 2-4)

**Hypothesis 1:** [Brief name]
- **Rank:** [number]
- **Score:** [ICE/RICE score]
- **Rationale:** [Why selected - highest score, strategic value, learning opportunity, etc.]

**Hypothesis 2:** [Brief name]
- **Rank:** [number]
- **Score:** [ICE/RICE score]
- **Rationale:** [Why selected]

**Hypothesis 3:** [Brief name]
- **Rank:** [number]
- **Score:** [ICE/RICE score]
- **Rationale:** [Why selected]

**Hypothesis 4:** [Brief name] (optional)
- **Rank:** [number]
- **Score:** [ICE/RICE score]
- **Rationale:** [Why selected]

### Not Selected (Backlog)

**Hypothesis [N]:** [Brief name]
- **Rank:** [number]
- **Score:** [ICE/RICE score]
- **Reason Deferred:** [Resource constraints, lower impact, dependencies, etc.]

[Continue for remaining hypotheses]

---

## Selection Rationale

### Primary Selection Criteria
[Explain how top 2-4 hypotheses were selected based on computational results]

### Balancing Considerations

**Quick Wins vs. High-Impact Long-Term:**
[How did we balance easy/fast tests vs. strategic longer-term experiments?]

**Tactic Diversity:**
[Did we ensure variety across tactics, or focus on one proven channel? Why?]

**Resource Constraints:**
[How did available time, budget, and team capacity influence selection?]

**Learning Value:**
[Were any lower-scoring hypotheses selected for high uncertainty/learning value?]

**Dependencies:**
[Are there any prerequisite experiments that must run first?]

---

## Experiment Sequence Plan

### Execution Strategy
[Parallel | Sequential | Hybrid]

**Rationale:** [Why this strategy was chosen]

### Timeline

**Week 1-2:**
- Experiment: [Hypothesis ID and brief name]
- Experiment: [Hypothesis ID and brief name] (if parallel)
- Status: [Planned | In Progress | Complete]

**Week 3-4:**
- Activity: [Analysis of Week 1-2 experiments | New experiment launch]
- Experiment: [Hypothesis ID and brief name]
- Status: [Planned | In Progress | Complete]

**Week 5-6:**
- Activity: [Based on learnings from previous experiments]
- Experiment: [Hypothesis ID and brief name]
- Status: [Planned | In Progress | Complete]

**Week 7-8:**
- Activity: [Final experiments or synthesis]
- Status: [Planned | In Progress | Complete]

### Dependencies

**Experiment [N] depends on Experiment [M]:**
[Explain dependency - e.g., "H2 (ads) uses winning message from H1 (landing page)"]

**Independent experiments (can run in parallel):**
[List hypotheses that have no dependencies and can run simultaneously]

---

## Resource Allocation

### Budget Allocation
| Experiment | Hypothesis | Estimated Budget | Priority |
|------------|------------|------------------|----------|
| E1 | [Brief name] | [Amount] | High |
| E2 | [Brief name] | [Amount] | High |
| E3 | [Brief name] | [Amount] | Medium |
| E4 | [Brief name] | [Amount] | Medium |

### Time Allocation
| Experiment | Hypothesis | Estimated Duration | Effort (person-weeks) |
|------------|------------|--------------------|-----------------------|
| E1 | [Brief name] | [X weeks] | [Y person-weeks] |
| E2 | [Brief name] | [X weeks] | [Y person-weeks] |
| E3 | [Brief name] | [X weeks] | [Y person-weeks] |
| E4 | [Brief name] | [X weeks] | [Y person-weeks] |

---

## Risk Assessment

### High-Risk Experiments
[List any experiments with low confidence scores or high uncertainty]

**Mitigation Strategies:**
[How will we address uncertainty? Pilot tests, smaller budgets, early stopping criteria?]

### Low-Risk Quick Wins
[List experiments with high confidence and high ease scores]

**Acceleration Opportunities:**
[Can we run these faster or with fewer resources?]

---

## User Confirmation

- [ ] Computational scores reviewed and validated
- [ ] Selected hypotheses (2-4) are appropriate
- [ ] Experiment sequence is feasible given constraints
- [ ] Resource allocation is realistic
- [ ] Dependencies and risks are identified
- [ ] Ready to proceed to Phase 4: Experiment Coordination
