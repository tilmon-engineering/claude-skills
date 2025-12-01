# Marketing Experimentation System Design

## Overview

Marketing experimentation system for DataPeeker that enables validation of business ideas through rigorous experimental cycles. Takes arbitrary marketing concepts, designs experiments, analyzes results, and produces data-driven signals (positive/negative/null/mixed) to guide iteration.

**Goals:**
- Generate clear signals from marketing ideas through experimental validation
- Coordinate multiple hypothesis tests and synthesize findings
- Support multi-conversation workflows spanning days/weeks
- Integrate qualitative market research with quantitative data analysis
- Produce actionable next-iteration ideas based on experimental evidence

**Success Criteria:**
- Campaign produces clear signal (not ambiguous)
- Next iteration ideas are specific and testable
- All experiment outcomes documented (including failures)
- Future conversations can seamlessly resume from any phase

## Architecture

Single meta-orchestrator skill (`marketing-experimentation`) that coordinates multiple hypothesis tests without duplicating experiment design functionality. Follows Lean Startup Build-Measure-Learn cycle.

**Core Components:**

**marketing-experimentation skill** (`.claude/skills/marketing-experimentation/`)
- 6-phase process skill following DataPeeker patterns
- Orchestrates multiple hypothesis-testing sessions
- Does NOT design experiments (delegates to hypothesis-testing)
- Does NOT execute queries (hypothesis-testing handles)
- DOES synthesize results across multiple experiments
- DOES generate next-iteration ideas

**market-researcher agent** (`.claude/agents/market-researcher.md`)
- Concept validation via internet research
- Invoked during Phase 1 (Discovery)
- Researches: market demand, similar solutions, audience needs, validation signals
- Returns structured findings (not raw data)
- Uses Haiku model for efficiency

**Integration Pattern:**
```
marketing-experimentation
  ├─ Phase 1: Invokes market-researcher agent
  ├─ Phase 4: Invokes hypothesis-testing skill (once per hypothesis)
  │            └─ Each test creates: analysis/hypothesis-testing/[name]/01-08 files
  └─ Phase 5: Uses interpreting-results, creating-visualizations for synthesis
```

**Workspace Structure:**
```
analysis/marketing-experimentation/[campaign-name]/
├── 01-discovery.md
├── 02-hypothesis-generation.md
├── 03-prioritization.md
├── 04-experiment-tracker.md         # Living document
├── 05-synthesis.md
├── 06-iteration-plan.md
└── experiments/
    ├── [experiment-1]/               # hypothesis-testing session
    ├── [experiment-2]/
    └── [experiment-3]/
```

**Key Design Decisions:**
- Single comprehensive skill (not modular components) for unified workflow
- Delegates to hypothesis-testing rather than duplicating experimental rigor
- Multi-conversation persistence via complete documentation at every phase
- Tool-agnostic (techniques, not platforms)
- Cycle-based (ideas feed back into new marketing-experimentation sessions)

## Existing Patterns

Investigation revealed DataPeeker's established process skill architecture. This design follows those patterns:

**Process Skill Structure:**
- 5-6 phase mandatory workflow with TodoWrite tracking
- Separate template files in `templates/` directory (not inline)
- Produces numbered markdown files in `analysis/[skill-name]/[session-name]/`
- Explicit checkpoints before phase transitions
- Common rationalizations documented with refutations
- Git-committable artifacts throughout

**Component Skill References:**
Existing skills: `understanding-data`, `writing-queries`, `interpreting-results`, `creating-visualizations`
- Process skills invoke component skills as needed
- marketing-experimentation follows this pattern by invoking hypothesis-testing

**Agent Pattern:**
Existing agents in `.claude/agents/` for data-heavy operations (quality-assessment, detect-duplicates, etc.)
- Agents use Haiku model for efficiency
- Return structured findings, not raw data
- Prevent context pollution
- market-researcher agent follows this pattern

**No Divergence:**
This design fully aligns with established DataPeeker patterns. No new architectural patterns introduced.

## Implementation Phases

### Phase 1: Create Skill Structure and Core Documentation
**Goal:** Establish skill file structure with frontmatter, overview, prerequisites, and mandatory process structure

**Components:**
- Create: `.claude/skills/marketing-experimentation/SKILL.md`
- Create: `.claude/skills/marketing-experimentation/templates/` directory
- Write: Skill frontmatter (name, description)
- Write: Overview section (purpose, when to use)
- Write: Prerequisites section (reference hypothesis-testing, interpreting-results, creating-visualizations)
- Write: Mandatory Process Structure section (TodoWrite checklist with 6 phases)

**Dependencies:** None (first phase)

**Testing:**
- Skill file exists and has valid frontmatter
- Overview clearly explains purpose and integration with hypothesis-testing
- Prerequisites list all required skills
- TodoWrite template matches 6-phase structure

### Phase 2: Document Phases 1-2 (Discovery & Hypothesis Generation)
**Goal:** Write detailed instructions for discovery and hypothesis generation phases

**Components:**
- Write: Phase 1 section in `SKILL.md` (Discovery & Asset Inventory)
  - Instructions for gathering business concept
  - market-researcher agent invocation pattern
  - Asset inventory checklist (content, campaigns, audiences, data)
  - Success criteria definition
- Write: Phase 2 section in `SKILL.md` (Hypothesis Generation)
  - Instructions for generating 5-10 testable hypotheses
  - Hypothesis format and structure
  - Tactic coverage (landing pages, ads, email, content)
  - Framework references (Lean Startup, AARRR, ICE/RICE)
- Add: Checkpoints for each phase
- Add: Common rationalizations with refutations

**Dependencies:** Phase 1 complete (skill structure exists)

**Testing:**
- Phase 1 instructions clearly explain market-researcher invocation
- Phase 2 instructions explain hypothesis format with examples
- Checkpoints are actionable and verifiable
- At least 3 common rationalizations documented per phase

### Phase 3: Document Phases 3-4 (Prioritization & Experiment Coordination)
**Goal:** Write instructions for prioritizing hypotheses and coordinating multiple experiments

**Components:**
- Write: Phase 3 section in `SKILL.md` (Prioritization)
  - ICE framework (Impact × Confidence ÷ Ease)
  - RICE framework (Impact × Reach × Confidence ÷ Effort)
  - Scoring methodology and examples
  - Selection criteria (2-4 highest-priority hypotheses)
- Write: Phase 4 section in `SKILL.md` (Experiment Coordination)
  - hypothesis-testing skill invocation pattern (one per hypothesis)
  - Experiment tracker management (living document)
  - Status tracking (Planned, In Progress, Complete)
  - Multi-conversation resumption strategy
- Add: Checkpoints and rationalizations

**Dependencies:** Phase 2 complete (Phases 1-2 documented)

**Testing:**
- Prioritization instructions include concrete ICE/RICE scoring examples
- Experiment coordination clearly explains hypothesis-testing delegation
- Experiment tracker format is complete and actionable
- Resumption strategy enables picking up after days/weeks

### Phase 4: Document Phases 5-6 (Synthesis & Iteration)
**Goal:** Write instructions for synthesizing results and generating next-iteration ideas

**Components:**
- Write: Phase 5 section in `SKILL.md` (Cross-Experiment Synthesis)
  - Aggregating findings across experiments
  - interpreting-results skill integration
  - creating-visualizations skill integration
  - Pattern identification (what works, what doesn't, what's unclear)
  - Overall signal classification (positive/negative/null/mixed)
- Write: Phase 6 section in `SKILL.md` (Iteration Planning)
  - Generating new experiment ideas (not hypotheses)
  - Idea categorization (scale winners, investigate nulls, pivot from failures)
  - Campaign-level signal documentation
  - Feed-forward pattern (ideas → new marketing-experimentation sessions)
- Add: Checkpoints and rationalizations

**Dependencies:** Phase 3 complete (Phases 1-4 documented)

**Testing:**
- Synthesis instructions clearly explain integration with interpreting-results and creating-visualizations
- Iteration planning distinguishes ideas from hypotheses
- Feed-forward cycle is clear (ideas go through Phase 1-2 in new session)
- At least 5 common rationalizations documented across both phases

### Phase 5: Create market-researcher Agent
**Goal:** Implement concept validation agent for market research

**Components:**
- Create: `.claude/agents/market-researcher.md`
- Write: Agent frontmatter (name: market-researcher, model: haiku, description)
- Write: Agent purpose (concept validation via internet research)
- Write: Research focus areas:
  - Market demand signals (search volume, forums, social mentions)
  - Similar solutions (competitors, alternatives, positioning)
  - Audience needs (pain points, jobs-to-be-done)
  - Validation evidence (case studies, reviews, testimonials)
- Write: Output format (structured findings document, not raw search results)
- Write: Integration pattern (invoked from marketing-experimentation Phase 1)

**Dependencies:** Phase 2 complete (Phase 1 documented, shows where agent is invoked)

**Testing:**
- Agent file exists with valid frontmatter
- Research focus areas are comprehensive
- Output format is structured and actionable
- Agent specifies Haiku model for efficiency

### Phase 6: Create Phase Templates (01-03)
**Goal:** Write template files for Phases 1-3

**Components:**
- Create: `.claude/skills/marketing-experimentation/templates/01-discovery.md`
  - Business concept description
  - Market research findings placeholder
  - Existing asset inventory structure
  - Success criteria and validation signals
  - Known constraints
- Create: `.claude/skills/marketing-experimentation/templates/02-hypothesis-generation.md`
  - Hypothesis list structure (5-10 entries)
  - Per-hypothesis format: statement, tactic/channel, expected outcome, rationale
  - Framework reference sections
  - Tactic mapping table
- Create: `.claude/skills/marketing-experimentation/templates/03-prioritization.md`
  - ICE/RICE scoring table
  - Prioritized backlog (high to low)
  - Experiment sequence plan
  - Dependencies and prerequisites section

**Dependencies:** Phase 4 complete (all phases documented, templates can reference instructions)

**Testing:**
- Each template exists in templates/ directory
- Templates include clear structure with placeholders
- Templates match instructions in corresponding phase sections
- Templates include examples where helpful

### Phase 7: Create Phase Templates (04-06)
**Goal:** Write template files for Phases 4-6

**Components:**
- Create: `.claude/skills/marketing-experimentation/templates/04-experiment-tracker.md`
  - Experiment entry structure (status, hypothesis, dates, location, signal, findings)
  - Status types: Planned, In Progress, Complete
  - Living document instructions
- Create: `.claude/skills/marketing-experimentation/templates/05-synthesis.md`
  - Aggregate results table across experiments
  - Pattern analysis structure
  - Statistical assessment section
  - Visualization placeholders
  - Overall signal classification
- Create: `.claude/skills/marketing-experimentation/templates/06-iteration-plan.md`
  - New experiment ideas list (3-7 ideas)
  - Idea categorization (scale winners, investigate nulls, pivot, explore new)
  - Campaign-level signal
  - Recommended next steps

**Dependencies:** Phase 6 complete (templates 01-03 exist)

**Testing:**
- All 6 template files exist in templates/ directory
- Experiment tracker format supports multi-conversation tracking
- Synthesis template integrates with interpreting-results patterns
- Iteration plan template emphasizes ideas (not hypotheses)

### Phase 8: Documentation, Common Rationalizations, and Summary
**Goal:** Complete skill documentation and integrate with DataPeeker docs

**Components:**
- Write: Common Rationalizations section in `SKILL.md`
  - "I'll skip discovery and just start testing"
  - "I'll design the experiment myself instead of using hypothesis-testing"
  - "One experiment is enough to draw conclusions"
  - "I'll wait until all experiments complete before synthesis"
  - "Results are obvious, I don't need to document"
  - "I'll form hypotheses in Phase 6 for efficiency"
  - At least 6 total rationalizations with refutations
- Write: Summary section in `SKILL.md` (overview of what skill ensures)
- Update: `.claude/skills/CLAUDE.md` to add marketing-experimentation to process skills table
- Create: Example scenario walkthrough (optional but recommended)

**Dependencies:** Phase 7 complete (all templates exist, all phases documented)

**Testing:**
- Common Rationalizations section has at least 6 entries
- Summary section captures key principles
- CLAUDE.md references marketing-experimentation in appropriate section
- Skill is complete and ready for use
- Test invocation with simple scenario validates multi-conversation resumption

## Additional Considerations

**Tactic coverage:** Marketing tactics (landing pages, ads, email, content) are referenced within Phase 2 (hypothesis generation) rather than implemented as separate skills. Each hypothesis maps to a tactic/channel with guidance on variables to test and measurements. This keeps the skill tool-agnostic (techniques, not platforms).

**Multi-conversation persistence:** Critical design requirement. Each phase must document completely enough that new conversations can resume after days/weeks. Experiment tracker (04-experiment-tracker.md) serves as living coordination hub. All hypothesis-testing sessions are referenced with locations and status.

**Phase 6 outputs ideas, not hypotheses:** Iteration planning generates experiment ideas that feed back into new marketing-experimentation sessions. Those ideas go through Phase 1 (discovery) and Phase 2 (hypothesis generation) in new sessions. This prevents skipping validation and maintains rigor.

**Statistical rigor delegation:** marketing-experimentation does NOT duplicate statistical analysis. hypothesis-testing handles p-values, confidence intervals, and signal detection. marketing-experimentation uses interpreting-results to synthesize across multiple experiments.

**Implementation scoping:** Design has exactly 8 phases, matching writing-plans skill limit. No additional scoping required.
