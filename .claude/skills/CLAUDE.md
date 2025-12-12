# DataPeeker Skills Overview

This document describes the skills available in DataPeeker for conducting rigorous, reproducible data analysis.

## Skill Architecture

DataPeeker uses a **two-tier skill architecture**:

1. **Component Skills**: Specialized skills that handle specific analytical tasks
2. **Process Skills**: Workflow orchestrators that guide complete analytical investigations

## Data Preparation Pipeline

**IMPORTANT**: Before using any process skill, data MUST flow through this pipeline:

```
Raw CSV Files → [importing-data] → raw_* tables → [cleaning-data] → clean_* tables → Process Skills
```

### Why This Matters

- **Quality first**: Process skills assume clean, validated data
- **Traceability**: Every transformation is documented in numbered markdown files
- **Reproducibility**: Cleaning decisions are preserved for audit and replication
- **Context efficiency**: Sub-agents handle data profiling to keep analysis sessions focused

## Component Skills

### Data Preparation

**`importing-data`** - Transform CSV files into SQLite with proper schema and types
- **When to use**: Starting analysis with new data sources
- **Input**: CSV file path
- **Output**: `raw_*` table + quality report + documentation
- **Phases**: CSV profiling → schema design → standardization → import → quality assessment
- **Location**: `.claude/skills/importing-data/SKILL.md`

**`cleaning-data`** - Address data quality issues and prepare analysis-ready tables
- **When to use**: After importing-data completes (MANDATORY before analysis)
- **Input**: `raw_*` table + quality report
- **Output**: `clean_*` table + verification report + documentation
- **Phases**: Quality review → issue detection → strategy design → execution → verification
- **Location**: `.claude/skills/cleaning-data/SKILL.md`

### Analysis Support

**`understanding-data`** - Systematic data profiling and exploration
- **When to use**: Beginning investigation of any dataset
- **Capabilities**: Schema inspection, distributions, relationships, quality checks
- **Location**: `.claude/skills/understanding-data/SKILL.md`

**`detect-foreign-keys`** - Identify and validate foreign key relationships between tables
- **When to use**: Multiple tables with undocumented relationships, validating referential integrity
- **Capabilities**: FK candidate identification, value overlap analysis, cardinality assessment, orphaned record detection
- **Location**: `.claude/skills/detect-foreign-keys/SKILL.md`

**`writing-queries`** - Construct correct, efficient SQL queries
- **When to use**: Translating analytical questions to SQL
- **Capabilities**: Query patterns, optimization, common pitfalls
- **Location**: `.claude/skills/writing-queries/SKILL.md`

**`interpreting-results`** - Analyze query results with intellectual honesty
- **When to use**: After executing queries, before drawing conclusions
- **Capabilities**: Statistical interpretation, bias detection, confidence assessment
- **Location**: `.claude/skills/interpreting-results/SKILL.md`

**`creating-visualizations`** - Generate effective text-based visualizations
- **When to use**: Communicating findings from analysis
- **Capabilities**: Chart selection, ASCII art, markdown tables
- **Location**: `.claude/skills/creating-visualizations/SKILL.md`

## Process Skills

**`exploratory-analysis`** - Discover patterns in unfamiliar data
- **When to use**: Initial investigation, no specific hypothesis
- **Phases**: Understanding → profiling → pattern discovery → synthesis
- **Prerequisites**: Data imported and cleaned
- **Location**: `.claude/skills/exploratory-analysis/SKILL.md`

**`guided-investigation`** - Investigate open-ended business questions
- **When to use**: Answering "why did X happen?" or "what's driving Y?"
- **Phases**: Question decomposition → mapping → incremental investigation → synthesis
- **Prerequisites**: Data imported and cleaned
- **Location**: `.claude/skills/guided-investigation/SKILL.md`

**`hypothesis-testing`** - Rigorously test specific hypotheses
- **When to use**: Validating specific claims or theories
- **Phases**: Hypothesis formulation → test design → analysis → interpretation
- **Prerequisites**: Data imported and cleaned
- **Location**: `.claude/skills/hypothesis-testing/SKILL.md`

**`comparative-analysis`** - Compare segments, cohorts, or time periods
- **When to use**: Understanding differences between groups
- **Phases**: Definition → measurement → comparison → explanation
- **Prerequisites**: Data imported and cleaned
- **Location**: `.claude/skills/comparative-analysis/SKILL.md`

**`marketing-experimentation`** - Validate marketing concepts through rigorous experimental cycles
- **When to use**: Testing marketing ideas, business concepts, or campaign strategies
- **Phases**: Discovery → Hypothesis Generation → Prioritization → Experiment Coordination → Synthesis → Iteration Planning
- **Prerequisites**: None initially (qualitative market research), data needs emerge from experiments
- **Location**: `.claude/skills/marketing-experimentation/SKILL.md`

## Workflow Patterns

### Starting a New Analysis

```
1. Use `importing-data` skill
   ├─ Input: CSV file path
   ├─ Output: raw_* table + 05-quality-report.md
   └─ Documents: 01-csv-profile.md through 05-quality-report.md

2. Use `cleaning-data` skill (MANDATORY)
   ├─ Input: raw_* table + quality report
   ├─ Output: clean_* table + verification report
   └─ Documents: 01-cleaning-scope.md through 05-verification-report.md

3. Choose appropriate process skill
   ├─ Exploratory: No specific question, discover patterns
   ├─ Guided Investigation: Answer open-ended "why" questions
   ├─ Hypothesis Testing: Validate specific claims
   └─ Comparative Analysis: Understand group differences
```

### During Analysis

All process skills follow this pattern:

1. **Phase-based workflow**: Each process has 4-5 phases with clear deliverables
2. **Numbered markdown files**: Every phase produces a documented artifact
3. **Checkpoints**: Mandatory validation before proceeding to next phase
4. **Component skill integration**: Reference understanding-data, writing-queries, etc. as needed

### After Analysis

- Numbered markdown files create complete audit trail
- Git-committable artifacts enable reproducibility
- Quality reports document data lineage and transformations

## Sub-Agents

DataPeeker uses specialized sub-agents to prevent context pollution during data operations:

**Data Quality Agents** (used by importing-data and cleaning-data):
- `quality-assessment` - Comprehensive quality profiling
- `detect-exact-duplicates` - Find identical records
- `detect-near-duplicates` - Fuzzy matching for similar records
- `detect-outliers` - MAD-based statistical outlier detection
- `categorize-free-text` - Semantic grouping of free text values
- `detect-foreign-keys` - Identify foreign key relationships and validate referential integrity

**Location**: `.claude/agents/[agent-name].md`

## Key Principles

1. **Data Quality First**: Never skip cleaning-data, even if data looks clean
2. **Document Everything**: Every decision captured in numbered markdown files
3. **Intellectual Honesty**: Interpret results skeptically, acknowledge limitations
4. **Reproducibility**: Others should be able to follow your exact analytical path
5. **Context Management**: Use sub-agents for data operations, keep main context analytical

## Skill Development Guidelines

### Template Organization

**CRITICAL**: Never embed full markdown templates inline within skill files.

**Why this matters:**
- Nested markdown templates create unreadable skill documentation
- Inline templates make skills difficult to maintain and update
- Large embedded templates obscure the skill's actual workflow logic
- Template changes require editing massive skill files instead of focused template files

**Best Practice:**

✅ **DO**: Create separate template files in a `templates/` directory
```markdown
Create `analysis/[session-name]/01-filename.md` with: ./templates/phase-1.md
```

**Directory structure:**
```
.claude/skills/[skill-name]/
├── SKILL.md
└── templates/
    ├── phase-1.md
    ├── phase-2.md
    └── phase-3.md
```

❌ **DON'T**: Embed full file templates inline
```markdown
Create `analysis/[session-name]/01-filename.md`:

```markdown
# Long Template Content
[50+ lines of template markdown]
```
```

**When inline snippets are acceptable:**
- Very short examples (< 5 lines)
- Code snippets demonstrating syntax
- Brief format examples

**When separate template files are required:**
- Any template describing the full contents of a file to be written
- Templates with > 10 lines of content
- Templates that will be referenced by multiple skills
- Templates that define documentation structure

**Example from DataPeeker:**
- All component skills (importing-data, cleaning-data) use separate template files
- All process skills (exploratory-analysis, guided-investigation, hypothesis-testing, comparative-analysis) use separate template files
- This pattern reduced some skill files by up to 71%, making them dramatically more readable

## Common Anti-Patterns

❌ **Skipping cleaning-data**: "The data looks clean enough"
- **Why it fails**: Quality issues emerge during analysis, invalidating conclusions
- **Correct approach**: Always run cleaning-data, even if it finds no issues

❌ **Analyzing data in main context**: Directly querying tables during skill execution
- **Why it fails**: Pollutes context with irrelevant records, reduces analysis effectiveness
- **Correct approach**: Delegate all data retrieval to sub-agents

❌ **Jumping to conclusions**: Seeing pattern and immediately explaining it
- **Why it fails**: Misses confounding factors, produces false insights
- **Correct approach**: Use interpreting-results skill to assess confidence and alternatives

❌ **Skipping documentation**: "I'll remember the decisions"
- **Why it fails**: Decisions are forgotten, analysis becomes irreproducible
- **Correct approach**: Write numbered markdown files for every phase

## Getting Started

**New to DataPeeker?** Start here:

1. Read `importing-data` skill to understand data ingestion
2. Read `cleaning-data` skill to understand quality workflow
3. Read `exploratory-analysis` to understand process skill structure
4. Try a simple analysis end-to-end: import → clean → explore

**Have existing analysis?** Ensure:
- ✅ Data was imported via `importing-data` (or equivalent documented process)
- ✅ Data was cleaned via `cleaning-data` (or equivalent quality validation)
- ✅ All transformations are documented in numbered markdown files

## Skill Evolution

Skills are continuously improved based on usage. When you discover:
- **Gaps**: Missing guidance for specific scenarios
- **Ambiguities**: Instructions that are unclear
- **Inefficiencies**: Redundant or unnecessary steps

Document findings and propose skill updates to maintain quality.

## Skill Dependencies

Review @skill-dependencies.mermaid

**CRITICAL: Maintaining Skill Dependencies**

⚠️ **MANDATORY STEP AFTER ANY SKILL MODIFICATION** ⚠️

Whenever you create, update, or modify ANY skill in this directory, you **MUST**:

1. Run the analysis script:
   ```bash
   python3 ./.claude/skills/analyze-skill-dependencies.py
   ```

2. Review the generated `.claude/skills/skill-dependencies.mermaid` file

3. Copy the contents and update the Mermaid diagram below with the new findings

**NEVER skip this step.** The dependency diagram is critical for understanding skill relationships and must remain accurate. An outdated diagram leads to:
- Missing prerequisite skills during analysis
- Incorrect workflow planning
- Broken skill orchestration
- Wasted time debugging circular dependencies

If you update a skill and do not run this script, you have failed to complete the task.
