---
name: marketing-experimentation
description: Systematic marketing experimentation process - discover concepts, generate hypotheses, coordinate multiple experiments, synthesize results, generate next-iteration ideas through rigorous validation cycles
---

# Marketing Experimentation

## Overview

Use this skill when you need to validate marketing concepts or business ideas through rigorous experimental cycles. This skill orchestrates the complete Build-Measure-Learn cycle from concept to data-driven signal.

**When to use this skill:**
- You have a marketing concept or business idea that needs validation
- You want to test multiple related hypotheses systematically
- You need to integrate results across multiple experiments
- You're designing the next iteration based on experimental evidence
- You're conducting qualitative market research combined with quantitative testing

**What this skill does:**
- Validates concepts through market research before experimentation
- Generates multiple testable hypotheses from marketing ideas
- Coordinates multiple hypothesis-testing sessions (delegates to hypothesis-testing skill)
- Synthesizes results across experiments using interpreting-results and creating-visualizations
- Produces clear signals (positive/negative/null/mixed) for each campaign
- Generates actionable next-iteration ideas based on experimental evidence

**What this skill does NOT do:**
- Design individual experiments (delegates to hypothesis-testing skill)
- Execute statistical analysis directly (uses hypothesis-testing for rigor)
- Operationalize successful ideas (focuses on validation, not scaling)
- Platform-specific implementation (tool-agnostic techniques only)

**Integration with existing skills:**
- **Delegates to `hypothesis-testing`** for individual experiment design and execution
- **Uses `interpreting-results`** to synthesize findings across multiple experiments
- **Uses `creating-visualizations`** to communicate aggregate results
- **Invokes `market-researcher` agent** for concept validation via internet research

**Multi-conversation persistence:**
This skill is designed for campaigns spanning days or weeks. Each phase documents completely enough that new conversations can resume after extended breaks. The experiment tracker (04-experiment-tracker.md) serves as the living coordination hub.

## Prerequisites

**Required skills:**
- `hypothesis-testing` - Individual experiment design and execution (invoked once per hypothesis)
- `interpreting-results` - Result synthesis and pattern identification (invoked in Phase 5)
- `creating-visualizations` - Aggregate result visualization (invoked in Phase 5)

**Required agents:**
- `market-researcher` - Concept validation via internet research (invoked in Phase 1)

**Required knowledge:**
- Understanding of Lean Startup Build-Measure-Learn cycle
- Familiarity with marketing tactics (landing pages, ads, email, content)
- Basic experimental design principles (control/treatment, signals, metrics)

**Data requirements:**
- None initially (market research is qualitative)
- Data requirements emerge from experiment design in Phase 4
- Each hypothesis-testing session will specify its own data needs

## Mandatory Process Structure

**CRITICAL:** This is a 6-phase process skill. You MUST complete all phases in order. Use TodoWrite to track progress through each phase.

**TodoWrite template:**

When starting a marketing-experimentation session, create these todos:

```markdown
- [ ] Phase 1: Discovery & Asset Inventory
- [ ] Phase 2: Hypothesis Generation
- [ ] Phase 3: Prioritization
- [ ] Phase 4: Experiment Coordination
- [ ] Phase 5: Cross-Experiment Synthesis
- [ ] Phase 6: Iteration Planning
```

**Workspace structure:**

All work for a marketing-experimentation session is saved to:
```
analysis/marketing-experimentation/[campaign-name]/
├── 01-discovery.md
├── 02-hypothesis-generation.md
├── 03-prioritization.md
├── 04-experiment-tracker.md
├── 05-synthesis.md
├── 06-iteration-plan.md
└── experiments/
    ├── [experiment-1]/               # hypothesis-testing session
    ├── [experiment-2]/               # hypothesis-testing session
    └── [experiment-3]/               # hypothesis-testing session
```

**Phase progression rules:**
1. Each phase has a CHECKPOINT with verification requirements
2. You MUST satisfy all checkpoint requirements before proceeding to the next phase
3. Document every decision with rationale in the numbered markdown files
4. Commit markdown files after each phase completes
5. The experiment tracker (04-experiment-tracker.md) is a LIVING DOCUMENT - update it throughout Phase 4

**Multi-conversation resumption:**
- At the start of any conversation, check if an experiment tracker exists for this campaign
- If it exists, read it first to understand current experiment status
- Update the tracker as experiments progress
- All phases should be complete enough to resume after days or weeks

---

## Phase 1: Discovery & Asset Inventory

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Gathered business concept description from user
- [ ] Invoked market-researcher agent and documented findings
- [ ] Completed asset inventory (content, campaigns, audiences, data)
- [ ] Defined success criteria and validation signals
- [ ] Documented known constraints
- [ ] Saved to `01-discovery.md`

### Instructions

1. **Gather the business concept**
   - Ask user to describe the marketing concept or business idea to validate
   - What problem does it solve? Who is the target audience?
   - What's the desired outcome? (awareness, leads, conversions, etc.)
   - What stage is this idea at? (new concept, existing campaign, iteration)

2. **Invoke market-researcher agent for concept validation**

   Dispatch the `market-researcher` agent with the concept description:
   - Agent will research market demand signals
   - Agent will identify similar solutions and competitors
   - Agent will analyze audience needs and pain points
   - Agent will find validation evidence (case studies, reviews, testimonials)

   Document agent findings in `01-discovery.md` under "Market Research Findings"

3. **Conduct asset inventory**

   Work with user to inventory existing assets that could be leveraged:

   **Content Assets:**
   - Blog posts, case studies, whitepapers
   - Video content, webinars, tutorials
   - Social media presence and following
   - Email lists and subscriber segments

   **Campaign Assets:**
   - Existing ad campaigns and performance data
   - Landing pages and conversion rates
   - Email campaigns and open/click rates
   - SEO performance and keyword rankings

   **Audience Assets:**
   - Customer segments and personas
   - Audience data (demographics, behaviors, preferences)
   - Customer feedback and reviews
   - Support tickets and common questions

   **Data Assets:**
   - Analytics platforms (Google Analytics, Mixpanel, etc.)
   - CRM data (Salesforce, HubSpot, etc.)
   - Ad platform data (Google Ads, Facebook Ads, etc.)
   - Email platform data (Mailchimp, SendGrid, etc.)

4. **Define success criteria and validation signals**

   Work with user to define:
   - What metrics indicate success? (CTR, conversion rate, CAC, LTV, etc.)
   - What magnitude of change is meaningful? (practical significance thresholds)
   - What signal types are acceptable?
     - Positive: Validates concept, proceed to scale
     - Negative: Invalidates concept, pivot or abandon
     - Null: Inconclusive, needs refinement or more data
     - Mixed: Some aspects work, some don't, iterate strategically

5. **Document known constraints**

   Capture any constraints that will affect experimentation:
   - Budget constraints (ad spend limits, tool costs)
   - Time constraints (launch deadlines, seasonal factors)
   - Resource constraints (team capacity, content production)
   - Technical constraints (platform limitations, integration issues)
   - Regulatory constraints (GDPR, CCPA, industry regulations)

6. **Create `01-discovery.md`** with: `./templates/01-discovery.md`

7. **STOP and get user confirmation**
   - Review discovery findings with user
   - Confirm asset inventory is complete
   - Confirm success criteria are appropriate
   - Do NOT proceed to Phase 2 until confirmed

**Common Rationalization:** "I'll skip discovery and go straight to testing - the concept is obvious"
**Reality:** Discovery surfaces assumptions, constraints, and existing assets that dramatically affect experiment design. Always start with discovery.

**Common Rationalization:** "I don't need market research - I already know this market"
**Reality:** The market-researcher agent provides current, data-driven validation signals that prevent building experiments around false assumptions. Always validate.

**Common Rationalization:** "Asset inventory is busywork - I'll figure out what's available as I go"
**Reality:** Existing assets can dramatically reduce experiment cost and time. Inventorying first prevents reinventing wheels and enables building on proven foundations.

---

## Phase 2: Hypothesis Generation

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Generated 5-10 testable hypotheses from the concept
- [ ] Each hypothesis maps to a specific tactic/channel
- [ ] Each hypothesis has expected outcome and rationale
- [ ] Hypotheses cover multiple tactics (not all ads or all email)
- [ ] Referenced relevant frameworks (Lean Startup, AARRR, ICE/RICE)
- [ ] Saved to `02-hypothesis-generation.md`

### Instructions

1. **Generate 5-10 testable hypotheses**

   For each hypothesis, use this format:

   **Hypothesis [N]: [Brief statement]**
   - **Tactic/Channel:** [landing page | ad campaign | email sequence | content marketing | social media | SEO | etc.]
   - **Expected Outcome:** [Specific, measurable result]
   - **Rationale:** [Why we believe this will work based on discovery findings]
   - **Variables to Test:** [What will we manipulate/measure]

   **Example hypothesis:**

   **Hypothesis 1: Value proposition clarity drives conversion**
   - **Tactic/Channel:** Landing page A/B test
   - **Expected Outcome:** 15%+ increase in conversion rate from landing page variant with simplified value proposition
   - **Rationale:** Market research showed audience confusion about product benefits. Discovery found existing landing page has 8 different value propositions competing for attention.
   - **Variables to Test:** Headline clarity, benefit hierarchy, CTA prominence

2. **Ensure tactic coverage**

   Verify hypotheses cover multiple marketing tactics:

   **Acquisition Tactics:**
   - Landing pages (conversion optimization, value prop testing, layout)
   - Ad campaigns (targeting, creative, messaging, platforms)
   - Content marketing (blog posts, videos, webinars, lead magnets)
   - SEO (keyword targeting, content optimization, technical SEO)

   **Activation Tactics:**
   - Email sequences (onboarding, nurture, activation)
   - Product tours (in-app guidance, feature discovery)
   - Social proof (testimonials, case studies, reviews)

   **Retention Tactics:**
   - Email campaigns (engagement, re-activation, upsell)
   - Content (newsletters, educational content, community)

   Don't generate 10 ad hypotheses. Aim for diversity across tactics.

3. **Reference experimentation frameworks**

   **Lean Startup Build-Measure-Learn:**
   - Build: What's the minimum viable test? (landing page, ad, email, etc.)
   - Measure: What metrics indicate success/failure?
   - Learn: What will we learn regardless of outcome?

   **AARRR Pirate Metrics:**
   - Acquisition: How do users find us?
   - Activation: Do they have a great first experience?
   - Retention: Do they come back?
   - Referral: Do they tell others?
   - Revenue: Do they pay?

   Map each hypothesis to one or more AARRR stages.

   **ICE/RICE Prioritization (used in Phase 3):**
   - Impact: How much will this move the metric?
   - Confidence: How sure are we this will work?
   - Ease: How easy is this to implement?
   - Reach: How many users will this affect? (RICE only)

4. **Create `02-hypothesis-generation.md`** with: `./templates/02-hypothesis-generation.md`

5. **STOP and get user confirmation**
   - Review all hypotheses with user
   - Confirm hypotheses are testable and meaningful
   - Confirm tactic coverage is appropriate
   - Do NOT proceed to Phase 3 until confirmed

**Common Rationalization:** "I'll generate hypotheses as I build experiments - more efficient"
**Reality:** Generating hypotheses before prioritization enables strategic selection of highest-impact tests. Generating ad-hoc leads to testing whatever's easiest, not what matters most.

**Common Rationalization:** "I'll focus all hypotheses on one tactic (ads) since that's what we know"
**Reality:** Tactic diversity reveals which channels work for this concept. Single-tactic testing creates blind spots and missed opportunities.

**Common Rationalization:** "I'll write vague hypotheses and refine them during experiment design"
**Reality:** Vague hypotheses lead to vague experiments that produce vague results. Specific hypotheses with expected outcomes enable clear signal detection.

**Common Rationalization:** "More hypotheses = better coverage, I'll generate 20+"
**Reality:** Too many hypotheses dilute focus and create analysis paralysis in prioritization. 5-10 high-quality hypotheses enable strategic selection of 2-4 tests.

---

## Phase 3: Prioritization

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Scored all hypotheses using ICE or RICE framework with computational method
- [ ] Created prioritized backlog (highest to lowest score) using Python script
- [ ] Selected 2-4 highest-priority hypotheses for testing
- [ ] Documented prioritization rationale
- [ ] Identified any dependencies or sequencing requirements
- [ ] Saved to `03-prioritization.md`

### Instructions

**CRITICAL:** You MUST use computational methods (Python scripts) to calculate scores. Do NOT estimate or manually calculate scores.

1. **Choose prioritization framework**

   **ICE Framework** (simpler, faster):
   - **Impact:** How much will this move the success metric? (1-10 scale)
   - **Confidence:** How confident are we this will work? (1-10 scale)
   - **Ease:** How easy is this to implement? (1-10 scale)
   - **Score:** (Impact × Confidence) / Ease

   **RICE Framework** (more comprehensive):
   - **Reach:** How many users will this affect? (absolute number or percentage)
   - **Impact:** How much will this move the metric per user? (1-10 scale: 0.25=minimal, 3=massive)
   - **Confidence:** How confident are we in our estimates? (percentage: 50%, 80%, 100%)
   - **Effort:** Person-weeks to implement (absolute number)
   - **Score:** (Reach × Impact × Confidence) / Effort

   Choose ICE for speed, RICE for precision when reach varies significantly.

2. **Score each hypothesis using Python script**

   **For ICE Framework:**

   Create a Python script to compute and sort ICE scores:

   ```python
   #!/usr/bin/env python3
   """
   ICE Score Calculator for Marketing Experimentation

   Computes ICE scores: (Impact × Confidence) / Ease
   Sorts hypotheses by score (highest to lowest)
   """

   hypotheses = [
       {
           "id": "H1",
           "name": "Value proposition clarity drives conversion",
           "impact": 8,
           "confidence": 7,
           "ease": 9
       },
       {
           "id": "H2",
           "name": "Ad targeting refinement",
           "impact": 7,
           "confidence": 6,
           "ease": 5
       },
       {
           "id": "H3",
           "name": "Email sequence optimization",
           "impact": 6,
           "confidence": 8,
           "ease": 8
       },
       {
           "id": "H4",
           "name": "Content marketing expansion",
           "impact": 5,
           "confidence": 4,
           "ease": 3
       },
   ]

   # Calculate ICE scores
   for h in hypotheses:
       h['ice_score'] = (h['impact'] * h['confidence']) / h['ease']

   # Sort by ICE score (descending)
   sorted_hypotheses = sorted(hypotheses, key=lambda x: x['ice_score'], reverse=True)

   # Print results table
   print("| Hypothesis | Impact | Confidence | Ease | ICE Score | Rank |")
   print("|------------|--------|------------|------|-----------|------|")
   for rank, h in enumerate(sorted_hypotheses, 1):
       print(f"| {h['id']}: {h['name'][:30]} | {h['impact']} | {h['confidence']} | {h['ease']} | {h['ice_score']:.2f} | {rank} |")
   ```

   **Usage:**
   ```bash
   python3 ice_calculator.py
   ```

   **For RICE Framework:**

   Create a Python script to compute and sort RICE scores:

   ```python
   #!/usr/bin/env python3
   """
   RICE Score Calculator for Marketing Experimentation

   Computes RICE scores: (Reach × Impact × Confidence) / Effort
   Sorts hypotheses by score (highest to lowest)
   """

   hypotheses = [
       {
           "id": "H1",
           "name": "Value proposition clarity drives conversion",
           "reach": 10000,        # users affected
           "impact": 3,           # 0.25=minimal, 1=low, 2=medium, 3=high, 5=massive
           "confidence": 80,      # percentage (50, 80, 100)
           "effort": 2            # person-weeks
       },
       {
           "id": "H2",
           "name": "Ad targeting refinement",
           "reach": 50000,
           "impact": 1,
           "confidence": 50,
           "effort": 4
       },
       {
           "id": "H3",
           "name": "Email sequence optimization",
           "reach": 5000,
           "impact": 2,
           "confidence": 80,
           "effort": 3
       },
       {
           "id": "H4",
           "name": "Content marketing expansion",
           "reach": 20000,
           "impact": 1,
           "confidence": 50,
           "effort": 8
       },
   ]

   # Calculate RICE scores
   for h in hypotheses:
       # Convert confidence percentage to decimal
       confidence_decimal = h['confidence'] / 100
       h['rice_score'] = (h['reach'] * h['impact'] * confidence_decimal) / h['effort']

   # Sort by RICE score (descending)
   sorted_hypotheses = sorted(hypotheses, key=lambda x: x['rice_score'], reverse=True)

   # Print results table
   print("| Hypothesis | Reach | Impact | Confidence | Effort | RICE Score | Rank |")
   print("|------------|-------|--------|------------|--------|------------|------|")
   for rank, h in enumerate(sorted_hypotheses, 1):
       print(f"| {h['id']}: {h['name'][:30]} | {h['reach']} | {h['impact']} | {h['confidence']}% | {h['effort']}w | {h['rice_score']:.2f} | {rank} |")
   ```

   **Usage:**
   ```bash
   python3 rice_calculator.py
   ```

   **Scoring Guidance:**

   **Impact (1-10 for ICE, 0.25-5 for RICE):**
   - ICE: 1-3 minimal, 4-6 moderate, 7-8 significant, 9-10 transformative
   - RICE: 0.25 minimal, 1 low, 2 medium, 3 high, 5 massive

   **Confidence (1-10 for ICE, 50-100% for RICE):**
   - ICE: 1-3 speculative, 4-6 uncertain, 7-8 likely, 9-10 validated
   - RICE: 50% low confidence, 80% high confidence, 100% certainty

   **Ease (1-10 for ICE):**
   - 1-3: Complex, significant resources
   - 4-6: Moderate effort, some obstacles
   - 7-8: Straightforward, few dependencies
   - 9-10: Trivial, immediate execution

   **Effort (person-weeks for RICE):**
   - Estimate total person-weeks required
   - Include design, implementation, monitoring time
   - Examples: 1w (simple landing page), 4w (complex ad campaign), 8w (content series)

3. **Run scoring script and document results**

   1. Create the Python script (ice_calculator.py or rice_calculator.py)
   2. Update the `hypotheses` list with actual hypothesis data from Phase 2
   3. Run the script: `python3 [ice|rice]_calculator.py`
   4. Copy the output table into `03-prioritization.md`
   5. Include the script in the markdown file for reproducibility:

   ```markdown
   ## Prioritization Calculation

   **Method:** ICE Framework

   **Calculation Script:**
   ```python
   [paste full script here]
   ```

   **Results:**

   [paste output table here]
   ```

4. **Select 2-4 highest-priority hypotheses**

   Considerations for selection:
   - **Don't test everything:** Focus on highest-scoring 2-4 hypotheses
   - **Resource constraints:** Match selection to available time/budget/capacity
   - **Learning value:** Sometimes lower-scoring hypothesis with high uncertainty is worth testing
   - **Dependencies:** Test prerequisites before dependent hypotheses
   - **Sequencing:** Consider whether experiments need to run sequentially or can run in parallel

   **Selection criteria:**
   - Primary: Top 2-4 by ICE/RICE score from computational results
   - Secondary: Balance quick wins vs. high-impact long-term bets
   - Tertiary: Ensure tactic diversity (don't test 3 ad variants if other tactics untested)

5. **Document experiment sequence**

   Determine execution strategy:
   - **Parallel:** Multiple experiments running simultaneously (faster results, higher resource needs)
   - **Sequential:** One experiment at a time (slower, easier to manage)
   - **Hybrid:** Run independent experiments in parallel, sequence dependent ones

   **Example sequence plan:**
   ```
   Week 1-2: Launch H1 (landing page) and H3 (email) in parallel
   Week 3-4: Analyze H1 and H3 results
   Week 5-6: Launch H2 (ads) based on H1 learnings
   Week 7-8: Analyze H2 results
   ```

6. **Create `03-prioritization.md`** with: `./templates/03-prioritization.md`

7. **STOP and get user confirmation**
   - Review computed scores and prioritization with user
   - Confirm selected hypotheses are appropriate
   - Confirm experiment sequence is feasible
   - Do NOT proceed to Phase 4 until confirmed

**Common Rationalization:** "I'll test all hypotheses - don't want to miss opportunities"
**Reality:** Resource constraints make testing everything impossible. Prioritization ensures highest-value experiments get resources. Unfocused testing produces weak signals across too many fronts.

**Common Rationalization:** "Scoring is subjective and arbitrary - I'll just pick what feels right"
**Reality:** Scoring frameworks force explicit reasoning about trade-offs. "Feels right" selections optimize for recency bias and personal preference, not business value. Computational methods ensure consistency.

**Common Rationalization:** "I'll skip prioritization and go straight to easiest test"
**Reality:** Easiest test rarely equals highest value. Prioritization prevents optimizing for ease at the expense of impact.

**Common Rationalization:** "I'll estimate scores mentally instead of running the script"
**Reality:** Manual estimation introduces calculation errors and inconsistency. Python scripts ensure exact, reproducible results that can be audited and verified.

---

## Phase 4: Experiment Coordination

**CHECKPOINT:** Before proceeding, you MUST have:
- [ ] Created experiment tracker with all selected hypotheses
- [ ] Invoked hypothesis-testing skill for each hypothesis (or documented plan to invoke)
- [ ] Updated tracker with experiment status (Planned, In Progress, Complete)
- [ ] Documented location of each hypothesis-testing session
- [ ] Saved experiment tracker to `04-experiment-tracker.md`
- [ ] Note: This phase may span multiple days/weeks and conversations

### Instructions

**CRITICAL:** This phase is designed for multi-conversation workflows. The experiment tracker is a LIVING DOCUMENT that you will update throughout experimentation. New conversations should ALWAYS read this file first.

1. **Create experiment tracker**

   The tracker is your coordination hub for managing multiple experiments over time.

   Create `04-experiment-tracker.md` with: `./templates/04-experiment-tracker.md`

   **Tracker format:**

   For each selected hypothesis, create an entry:

   ```markdown
   ### Experiment 1: [Hypothesis Brief Name]

   **Status:** [Planned | In Progress | Complete]
   **Hypothesis:** [Full hypothesis statement from Phase 2]
   **Tactic/Channel:** [landing page | ads | email | etc.]
   **Priority Score:** [ICE/RICE score from Phase 3]
   **Start Date:** [YYYY-MM-DD or "Not started"]
   **Completion Date:** [YYYY-MM-DD or "In progress"]
   **Location:** `analysis/marketing-experimentation/[campaign-name]/experiments/[experiment-name]/`
   **Signal:** [Positive | Negative | Null | Mixed | "Not analyzed"]
   **Key Findings:** [Brief summary when complete, "TBD" otherwise]
   ```

2. **Invoke hypothesis-testing skill for each experiment**

   For each hypothesis marked "Planned" or "In Progress":

   **Step 1:** Read the hypothesis details from `02-hypothesis-generation.md`

   **Step 2:** Invoke the `hypothesis-testing` skill:
   ```markdown
   Use hypothesis-testing skill to test: [Hypothesis statement]

   Context for hypothesis-testing:
   - Session name: [descriptive-name-for-experiment]
   - Save location: analysis/marketing-experimentation/[campaign-name]/experiments/[experiment-name]/
   - Success criteria: [From Phase 1 discovery]
   - Expected outcome: [From Phase 2 hypothesis]
   ```

   **Step 3:** Update experiment tracker:
   - Change status from "Planned" to "In Progress"
   - Add start date
   - Update location with actual path

   **Step 4:** Let hypothesis-testing skill complete its 5-phase workflow:
   - Phase 1: Hypothesis Formulation
   - Phase 2: Test Design
   - Phase 3: Data Analysis
   - Phase 4: Statistical Interpretation
   - Phase 5: Conclusion

   **Step 5:** When hypothesis-testing completes, update tracker:
   - Change status to "Complete"
   - Add completion date
   - Document signal (Positive/Negative/Null/Mixed)
   - Summarize key findings

   **Step 6:** Commit tracker updates after each status change

3. **Handle multi-conversation resumption**

   **At the start of EVERY conversation during Phase 4:**

   1. Check if `04-experiment-tracker.md` exists
   2. If it exists, READ IT FIRST before doing anything else
   3. Review experiment status:
      - Planned: Ready to launch
      - In Progress: Check hypothesis-testing session for current phase
      - Complete: Ready for synthesis (Phase 5)
   4. Ask user which experiment to continue or which new experiment to launch
   5. Update tracker with new status/dates/findings
   6. Commit tracker updates

   **Example resumption:**
   ```markdown
   I've read the experiment tracker. Current status:
   - Experiment 1 (H1: Value prop): Complete, Positive signal
   - Experiment 2 (H3: Email sequence): In Progress, currently in hypothesis-testing Phase 3
   - Experiment 3 (H2: Ad targeting): Planned, not yet started

   What would you like to do?
   a) Continue Experiment 2 (in hypothesis-testing Phase 3)
   b) Start Experiment 3
   c) Move to synthesis (Phase 5) since Experiment 1 is complete
   ```

4. **Coordinate parallel vs. sequential experiments**

   **Parallel execution (multiple experiments simultaneously):**
   - Launch multiple hypothesis-testing sessions
   - Track each separately in experiment tracker
   - Update tracker as each progresses independently
   - Requires managing multiple analysis directories

   **Sequential execution (one at a time):**
   - Complete one experiment fully before starting next
   - Simpler tracking, easier to manage
   - Can incorporate learnings between experiments

   **Hybrid execution:**
   - Run independent experiments in parallel
   - Sequence dependent experiments (e.g., H2 depends on H1 insights)

5. **Progress through all experiments**

   Continue invoking hypothesis-testing and updating the tracker until:
   - All selected experiments have status "Complete"
   - All experiments have documented signals
   - All findings are summarized in tracker

   Only when ALL experiments are complete should you proceed to Phase 5.

**Common Rationalization:** "I'll keep experiment details in my head - the tracker is just busywork"
**Reality:** Multi-day campaigns lose context between conversations. The tracker is the ONLY source of truth that persists across sessions. Without it, you'll re-ask questions and lose progress.

**Common Rationalization:** "I'll wait until all experiments finish before updating the tracker"
**Reality:** Batch updates create opportunity for lost data. Update the tracker IMMEDIATELY after status changes. Real-time tracking prevents confusion and missed experiments.

**Common Rationalization:** "I'll design the experiment myself instead of using hypothesis-testing"
**Reality:** hypothesis-testing skill provides rigorous experimental design, statistical analysis, and signal detection. Skipping it produces weak experiments with ambiguous results.

**Common Rationalization:** "All experiments are done, I don't need to update the tracker before synthesis"
**Reality:** The tracker is your input to Phase 5. Incomplete tracker means incomplete synthesis. Update ALL fields (status, dates, signals, findings) before proceeding.
