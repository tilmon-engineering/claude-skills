# Result Interpretation

## Summary of Findings

### Primary Metric Results
[Describe what the analysis showed - facts first]

Example: "Sales vary significantly by day of week:
- Sunday: $36.71 avg (lowest)
- Wednesday: $52.30 avg (highest)
- Range: $15.59 (42% difference from Sunday to Wednesday)"

### Statistical Assessment
[Without formal tests, assess practical significance]

- Magnitude: [How big are the differences?]
- Consistency: [Do sample sizes support the pattern?]
- Practical importance: [Do differences matter for decisions?]

## Alternative Explanations

[Consider other factors that might explain the pattern]

1. **[Confound 1]:** [How it might explain results, can we rule it out?]
   - Evidence for/against: [What data suggests this is/isn't the explanation?]

2. **[Confound 2]:** [How it might explain results]
   - Evidence for/against: [...]

Example:
1. **Promotions:** Maybe Wednesday has more promotions
   - Evidence: Would need promotion data to check (not available in current dataset)
   - Impact: Could fully explain the pattern

2. **Store hours:** Maybe stores open later/close earlier on Sundays
   - Evidence: Transaction counts are lower (1,250 vs 2,140), supporting this
   - Impact: Might partially explain lower sales

## Hypothesis Test Result

### Null Hypothesis (H0)
[Restate from Phase 1]

### Decision
**[REJECT H0 / FAIL TO REJECT H0]**

### Rationale
[Why did you make this decision? What evidence was most compelling?]

Example: "REJECT H0. The 42% difference between Sunday and Wednesday average sales is both statistically meaningful (based on large sample sizes) and practically significant. However, this rejection comes with caveats (see limitations)."

## Limitations

[What reduces confidence in conclusions?]

1. [Data limitation]
2. [Methodological limitation]
3. [Confounding factor not addressed]

Example:
1. Cannot separate time-of-day effects from day-of-week effects
2. Did not control for promotions or holidays
3. Sample period may not be representative (need date range check)
