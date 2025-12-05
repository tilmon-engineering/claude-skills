# Marketing Experimentation System Implementation Plan - Phase 2

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development to implement this plan task-by-task.

## Phase 2: Document Phases 1-2 (Discovery & Hypothesis Generation)

### Task 1: Document Phase 1 (Discovery & Asset Inventory)

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Mandatory Process Structure)

**Step 1: Add Phase 1 section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

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
```

**Step 2: Verify Phase 1 section**

Run: `grep -A 5 "## Phase 1: Discovery & Asset Inventory" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Phase 1 section with CHECKPOINT and Instructions

**Step 3: Commit Phase 1 section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add Phase 1 (Discovery & Asset Inventory) to marketing-experimentation

Document discovery phase with market-researcher agent invocation,
asset inventory checklist, success criteria definition, and 3 common
rationalizations with refutations.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 2: Document Phase 2 (Hypothesis Generation)

**Files:**
- Modify: `.claude/skills/marketing-experimentation/SKILL.md` (append after Phase 1)

**Step 1: Add Phase 2 section to SKILL.md**

Append to `.claude/skills/marketing-experimentation/SKILL.md`:

```markdown

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
```

**Step 2: Verify Phase 2 section**

Run: `grep -A 5 "## Phase 2: Hypothesis Generation" .claude/skills/marketing-experimentation/SKILL.md`

Expected: Shows Phase 2 section with CHECKPOINT and Instructions

**Step 3: Commit Phase 2 section**

```bash
git add .claude/skills/marketing-experimentation/SKILL.md
git commit -m "docs: add Phase 2 (Hypothesis Generation) to marketing-experimentation

Document hypothesis generation phase with format, tactic coverage,
framework references (Lean Startup, AARRR, ICE/RICE), and 4 common
rationalizations with refutations.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude <noreply@anthropic.com>"
```

---

### Task 3: Verify Phase 2 Completion

**Step 1: Verify both skill phases documented**

Run:
```bash
grep "## Phase 1: Discovery & Asset Inventory" .claude/skills/marketing-experimentation/SKILL.md
grep "## Phase 2: Hypothesis Generation" .claude/skills/marketing-experimentation/SKILL.md
```

Expected: Both commands return matches

**Step 2: Count checkpoints per phase**

Run:
```bash
echo "Phase 1 checkpoints:"
sed -n '/## Phase 1: Discovery/,/## Phase 2/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "- \[ \]"
echo "Phase 2 checkpoints:"
sed -n '/## Phase 2: Hypothesis/,/## Phase 3/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "- \[ \]"
```

Expected: Phase 1 has 6 checkpoints, Phase 2 has 6 checkpoints

**Step 3: Count common rationalizations**

Run:
```bash
echo "Phase 1 rationalizations:"
sed -n '/## Phase 1: Discovery/,/## Phase 2/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "Common Rationalization:"
echo "Phase 2 rationalizations:"
sed -n '/## Phase 2: Hypothesis/,/## Phase 3/p' .claude/skills/marketing-experimentation/SKILL.md | grep -c "Common Rationalization:"
```

Expected: Phase 1 has 3 rationalizations, Phase 2 has 4 rationalizations (exceeds requirement of 3 per phase)

**Step 4: Verify template references**

Run:
```bash
grep "with: \./templates/" .claude/skills/marketing-experimentation/SKILL.md
```

Expected output:
```
Create `01-discovery.md` with: `./templates/01-discovery.md`
Create `02-hypothesis-generation.md` with: `./templates/02-hypothesis-generation.md`
```

**Phase 2 Checkpoint Requirements:**
- ✓ Phase 1 instructions clearly explain market-researcher invocation
- ✓ Phase 2 instructions explain hypothesis format with examples
- ✓ Checkpoints are actionable and verifiable
- ✓ At least 3 common rationalizations documented per phase (Phase 1: 3, Phase 2: 4)
- ✓ Template references use correct pattern (`with: ./templates/...`)
- ✓ Framework references included (Lean Startup, AARRR, ICE/RICE)
- ✓ Tactic coverage explained (landing pages, ads, email, content)
