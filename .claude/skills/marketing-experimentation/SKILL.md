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
