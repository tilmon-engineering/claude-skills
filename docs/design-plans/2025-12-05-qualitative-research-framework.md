# Qualitative Research Framework Design

## Overview

General-purpose qualitative research framework for conducting and analyzing interviews, surveys, focus groups, and observational research. Provides systematic, reproducible workflow from research design through data collection to rigorous analysis with mandatory bias prevention.

Peer skill to `hypothesis-testing` (quantitative data analysis). Both can be invoked by `marketing-experimentation` for validation experiments, or used independently for any research need.

**Goals:**
- Systematic, reproducible analysis through codebook rigor and complete audit trails
- Prevent confirmation bias through mandatory disconfirming evidence search and intercoder reliability
- Method-agnostic core supporting multiple qualitative data collection approaches
- Full cycle coverage (planning → collection → analysis)

**Success Criteria:**
- Complete audit trail in numbered markdown files (git-committable artifacts)
- Mandatory checkpoints prevent skipping critical rigor steps
- Haiku sub-agents handle data-intensive operations (prevent context pollution)
- Framework accessible to non-researchers while maintaining academic rigor

## Architecture

**Core Workflow:** 6-phase Thematic Analysis framework following proven qualitative methodology.

**Phases:**
1. **Research Design** - Define question, select method, create instrument, plan sampling, document biases
2. **Data Collection** - Execute method-specific protocol, track saturation, maintain reflexive journal
3. **Data Familiarization** - Immerse in data without coding, document observations and surprises
4. **Systematic Coding** - Develop codebook, code systematically, verify with intercoder reliability
5. **Theme Development & Refinement** - Build themes from codes, search for disconfirming evidence
6. **Synthesis & Reporting** - Document findings with limitations, confidence assessment, follow-ups

**Method-Agnostic Design:**
- Core workflow universal (Phases 1-6 apply to all methods)
- Method-specific templates for Phases 1-2 (interviews, surveys, focus groups, observations)
- Phases 3-6 templates universal regardless of collection method

**File Structure:**
```
analysis/qualitative-research/[session-name]/
├── 00-overview.md (living document)
├── 01-research-design.md (Phase 1)
├── 02-data-collection-log.md (Phase 2)
├── raw-data/ (Phase 2 - transcripts/responses)
├── 03-familiarization-notes.md (Phase 3)
├── 04-coding-analysis.md (Phase 4 - codebook + coding + reliability)
├── 05-theme-development.md (Phase 5)
└── 06-findings-report.md (Phase 6)
```

One file per phase (numbered to match: Phase N → `0N-*.md`).

**Sub-Agent Architecture:**

Six Haiku agents handle data-intensive operations:

1. **`analyze-transcript`** - Summarize transcripts, extract key quotes, initial observations (Phase 3)
2. **`generate-initial-codes`** - Suggest codes from data segments, accelerate codebook development (Phase 4)
3. **`intercoder-reliability-check`** - Independent coding of 10-20% sample, agreement analysis (Phase 4)
4. **`identify-themes`** - Group codes into themes, extract supporting data (Phase 5)
5. **`search-disconfirming-evidence`** - Find contradictions to proposed themes (Phase 5 - MANDATORY)
6. **`extract-supporting-quotes`** - Find best verbatim quotes for each theme (Phase 6)

Agents return structured findings to main skill. Main skill orchestrates workflow and maintains rigor. All agent outputs documented in phase files for audit trail.

**Bias Prevention:**

Built into every phase:
- **Phase 1**: Document biases BEFORE data collection, neutral question design
- **Phase 2**: Consistency protocols, separate observation from interpretation
- **Phase 3**: No premature coding, document surprises that contradict expectations
- **Phase 4**: Codebook transparency, mandatory intercoder reliability check
- **Phase 5**: MANDATORY disconfirming evidence search via agent (cannot skip)
- **Phase 6**: Explicit limitations, verbatim quotes (not paraphrases), honest confidence assessment

**Integration with Marketing-Experimentation:**

Marketing-experimentation Phase 4 (Experiment Coordination) can invoke:
- `hypothesis-testing` for quantitative experiments
- `qualitative-research` for qualitative experiments (NEW)
- Both sequentially for mixed-methods experiments

Returns signal classification (Positive/Negative/Null/Mixed) + findings to experiment tracker.

## Existing Patterns

Investigation found comprehensive DataPeeker process skill pattern. This design follows existing architecture exactly:

**Process Skill Structure** (from exploratory-analysis, hypothesis-testing, comparative-analysis, marketing-experimentation):
- 5-6 phase mandatory workflow
- TodoWrite tracking at start (one todo per phase)
- Numbered markdown files as output (01-*, 02-*, etc.)
- Explicit checkpoints before phase transitions
- Common Rationalizations section documenting bias traps
- Separate template files in `skills/[skill-name]/templates/` directory
- SKILL.md references templates: `with: ./templates/phase-N.md`

**Agent Pattern** (from detect-outliers, categorize-free-text, market-researcher, quality-assessment):
- Live in `.claude/agents/` directory
- Use Haiku model for efficiency
- Return structured findings, not raw data
- Prevent main agent context pollution
- Invoked during process skill execution

**Component Skill Integration** (from understanding-data, writing-queries, interpreting-results, creating-visualizations):
- Reference component skills where applicable
- `interpreting-results` for Phase 6 synthesis
- `creating-visualizations` for presenting findings
- `using-sqlite` NOT applicable (qualitative data not in SQLite)

**File Structure Conventions:**
- Skills: `.claude/skills/[skill-name]/SKILL.md`
- Templates: `.claude/skills/[skill-name]/templates/phase-N.md`
- Agents: `.claude/agents/[agent-name].md`
- Analysis outputs: `analysis/[skill-name]/[session-name]/`

**No Divergence:** This design introduces no new patterns. Follows DataPeeker architecture precisely.

## Implementation Phases

### Phase 1: Core Skill Structure

**Goal:** Create qualitative-research skill directory, main SKILL.md with complete 6-phase workflow, and universal templates (Phases 3-6)

**Components:**
- Create: `.claude/skills/qualitative-research/SKILL.md`
  - YAML frontmatter (name, description)
  - Overview section (when to use, prerequisites)
  - Mandatory Process Structure (TodoWrite template for 6 phases)
  - Phase 1-6 instructions with checkpoints
  - Common Rationalizations section
  - Example workflow
  - Summary
- Create: `.claude/skills/qualitative-research/templates/phase-3-familiarization.md`
- Create: `.claude/skills/qualitative-research/templates/phase-4-coding.md`
- Create: `.claude/skills/qualitative-research/templates/phase-5-themes.md`
- Create: `.claude/skills/qualitative-research/templates/phase-6-reporting.md`
- Create: `.claude/skills/qualitative-research/templates/overview-summary.md`

**Dependencies:** None (first phase)

**Testing:**
- Skill tool can invoke `qualitative-research`
- SKILL.md loads without errors
- Template references resolve correctly
- Phase 3-6 templates contain proper structure

### Phase 2: Interview Method Templates

**Goal:** Create interview-specific templates for Phases 1-2 with Mom Test principles and neutral question design

**Components:**
- Create: `.claude/skills/qualitative-research/templates/interviews/phase-1-interview-guide.md`
  - Research question definition
  - Interview question design (open-ended, neutral wording)
  - Mom Test principles (ask about past behavior, not hypothetical futures)
  - Probe techniques
  - Sampling strategy
  - Reflexivity baseline
- Create: `.claude/skills/qualitative-research/templates/interviews/phase-2-interview-execution.md`
  - Consent and recording protocol
  - Interview facilitation guide
  - Note-taking structure
  - Saturation monitoring checklist
  - Reflexive journaling prompts

**Dependencies:** Phase 1 (core skill structure must exist)

**Testing:**
- User selects "interview" method in Phase 1
- Interview templates properly referenced
- Templates contain complete guidance for customer discovery interviews
- Example interview guide demonstrates neutral question design

### Phase 3: Survey Method Templates

**Goal:** Create survey-specific templates for Phases 1-2 with question design best practices and bias prevention

**Components:**
- Create: `.claude/skills/qualitative-research/templates/surveys/phase-1-survey-design.md`
  - Research question definition
  - Open-ended question design
  - Scale selection guidance (Likert, semantic differential, etc.)
  - Question ordering and flow
  - Pilot testing checklist
  - Sampling strategy
- Create: `.claude/skills/qualitative-research/templates/surveys/phase-2-survey-distribution.md`
  - Distribution protocol
  - Response tracking
  - Sample monitoring (response rates, demographics)
  - Data collection consistency

**Dependencies:** Phase 1 (core skill structure must exist)

**Testing:**
- User selects "survey" method in Phase 1
- Survey templates properly referenced
- Templates guide both closed and open-ended survey design
- Bias prevention guidance included

### Phase 4: Focus Group & Observation Templates

**Goal:** Complete method coverage with focus group and observational research templates

**Components:**
- Create: `.claude/skills/qualitative-research/templates/focus-groups/phase-1-facilitator-guide.md`
  - Discussion topic structure
  - Group dynamics management techniques
  - Timing and flow guidance
  - Participant recruitment and composition
- Create: `.claude/skills/qualitative-research/templates/focus-groups/phase-2-session-execution.md`
  - Session facilitation protocol
  - Observer role guidance
  - Capturing group dynamics and dissent
  - Recording and transcription
- Create: `.claude/skills/qualitative-research/templates/observations/phase-1-observation-protocol.md`
  - What to observe (behavior, context, interactions)
  - Field note structure (observation vs. interpretation separation)
  - Duration and frequency planning
- Create: `.claude/skills/qualitative-research/templates/observations/phase-2-field-work.md`
  - Field work execution guidance
  - Thick description techniques
  - Context documentation
  - Reflexivity in observational research

**Dependencies:** Phase 1 (core skill structure must exist)

**Testing:**
- All four methods (interview, survey, focus group, observation) have complete templates
- User can select any method and receive appropriate guidance
- Templates maintain consistent structure across methods

### Phase 5: Transcript Analysis Agent

**Goal:** Create analyze-transcript Haiku agent for Phase 3 support (summarize transcripts, extract key quotes, identify initial observations)

**Components:**
- Create: `.claude/agents/analyze-transcript.md`
  - Agent documentation (purpose, inputs, outputs)
  - Haiku model specification
  - Input: Raw transcript or field notes
  - Output: Summary, key quotes, initial observations, surprising findings
  - Integration with Phase 3 workflow
- Modify: `.claude/skills/qualitative-research/SKILL.md` Phase 3 section
  - Add guidance for invoking analyze-transcript agent
  - Explain when to use (long transcripts, multiple interviews)
  - Document agent output in 03-familiarization-notes.md

**Dependencies:** Phase 1 (core skill must exist to integrate with)

**Testing:**
- Agent invokable via Task tool with subagent_type
- Agent correctly summarizes sample transcript
- Agent extracts relevant quotes
- Agent identifies surprising findings
- Output integrates cleanly into Phase 3 file

### Phase 6: Coding Agents (Initial + Intercoder)

**Goal:** Create generate-initial-codes and intercoder-reliability-check agents for Phase 4 systematic coding support

**Components:**
- Create: `.claude/agents/generate-initial-codes.md`
  - Input: Data segment (transcript section, survey responses)
  - Output: Suggested codes with definitions and example segments
  - Accelerates codebook development with systematic first pass
- Create: `.claude/agents/intercoder-reliability-check.md`
  - Input: Codebook + 10-20% data sample
  - Output: Independent coding + agreement analysis with primary coding
  - Provides systematic reliability verification
- Modify: `.claude/skills/qualitative-research/SKILL.md` Phase 4 section
  - Add guidance for invoking both agents
  - Make intercoder-reliability-check MANDATORY (checkpoint requirement)
  - Document outputs in 04-coding-analysis.md

**Dependencies:** Phase 1 (core skill must exist to integrate with)

**Testing:**
- Both agents invokable via Task tool
- generate-initial-codes produces reasonable code suggestions
- intercoder-reliability-check performs independent coding
- Agreement percentage calculated correctly
- Checkpoint enforces intercoder reliability before Phase 5

### Phase 7: Theme & Quote Agents

**Goal:** Create identify-themes and extract-supporting-quotes agents for Phases 5-6 support

**Components:**
- Create: `.claude/agents/identify-themes.md`
  - Input: Codebook + all coded segments
  - Output: Potential themes with supporting codes and data extracts
  - Handles large-scale pattern recognition across dataset
- Create: `.claude/agents/extract-supporting-quotes.md`
  - Input: Theme definition + coded dataset
  - Output: Best representative verbatim quotes for each theme
  - Finds most illustrative data extracts for reporting
- Modify: `.claude/skills/qualitative-research/SKILL.md`
  - Phase 5 section: Add identify-themes agent guidance
  - Phase 6 section: Add extract-supporting-quotes agent guidance
  - Document outputs in phase files

**Dependencies:** Phase 1 (core skill must exist to integrate with)

**Testing:**
- Both agents invokable via Task tool
- identify-themes groups codes into coherent themes
- extract-supporting-quotes finds relevant verbatim data
- Outputs integrate into Phase 5 and 6 files
- Themes supported by actual data extracts

### Phase 8: Disconfirming Evidence Agent (Critical Bias Prevention)

**Goal:** Create search-disconfirming-evidence agent and make MANDATORY in Phase 5 workflow to prevent confirmation bias

**Components:**
- Create: `.claude/agents/search-disconfirming-evidence.md`
  - Input: Proposed theme + full dataset
  - Output: Contradictory evidence, edge cases, exceptions to pattern
  - Systematically searches for data that contradicts theme
  - Documents strength of disconfirming evidence
- Modify: `.claude/skills/qualitative-research/SKILL.md` Phase 5 section
  - Make search-disconfirming-evidence agent MANDATORY
  - Add checkpoint: "Disconfirming evidence agent run for ALL themes"
  - Cannot proceed to Phase 6 without running this agent
  - Add Common Rationalization: "My themes are obvious, no contradictions exist" → WRONG
- Test with sample data showing clear confirmation bias scenario

**Dependencies:** Phase 1 (core skill must exist to integrate with)

**Testing:**
- Agent invokable via Task tool
- Agent successfully finds contradictory evidence when present
- Agent reports when no contradictions found (with confidence assessment)
- Phase 5 checkpoint BLOCKS progression without agent execution
- Common Rationalizations section documents why this is mandatory
- Test case: Provide biased theme, verify agent finds contradictions

## Additional Considerations

**Multi-conversation resumption:** All phase files complete enough to resume after days/weeks. `00-overview.md` living document tracks current phase and key decisions. Users can return to analysis and pick up where they left off.

**Flexible entry points:** Users with existing qualitative data can skip Phases 1-2 and start at Phase 3 (familiarization). Skill checks for raw data in `raw-data/` directory and adapts workflow accordingly.

**Integration testing with marketing-experimentation:** After core skill complete, test full workflow:
1. Create experiment in marketing-experimentation experiment tracker
2. Invoke qualitative-research skill for experiment
3. Complete all 6 phases
4. Return signal classification to tracker
5. Verify synthesis in marketing-experimentation Phase 5

**Agent efficiency:** All agents use Haiku model. Expected cost: <$0.50 per complete qualitative analysis (10 interviews, ~50,000 words of transcripts). Main agent remains focused on orchestration.

**No database integration:** Unlike quantitative skills (hypothesis-testing, exploratory-analysis), qualitative data lives in markdown files, not SQLite. This is intentional - qualitative data doesn't fit tabular structure. Raw transcripts, coded segments, and themes all remain in human-readable markdown.

**Skill testing strategy:** Since qualitative-research is a skill (not code), use testing-skills-with-subagents to validate the skill resists rationalization under pressure before deployment. RED phase: Run without bias prevention, observe failures. GREEN phase: Add mandatory checkpoints, verify agent enforcement prevents shortcuts. REFACTOR phase: Close loopholes in Common Rationalizations section.
