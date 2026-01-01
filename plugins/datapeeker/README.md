# DataPeeker Plugin

Structured research methods for AI agents conducting rigorous, reproducible data analysis and qualitative research.

## Overview

DataPeeker provides a comprehensive toolkit for systematic research, emphasizing intellectual honesty, reproducibility, and evidence-based conclusions. It follows a two-tier architecture combining component skills (specialized tasks) with process skills (workflow orchestration).

## Skills Included

### Process Skills (Workflow Orchestration)

These skills guide complete analytical investigations from start to finish:

**`exploratory-analysis`** - Discover patterns in unfamiliar data
- When to use: Initial investigation with no specific hypothesis
- Phases: Understanding → Profiling → Pattern discovery → Synthesis
- Output: Insights, anomalies, and questions for deeper investigation

**`hypothesis-testing`** - Rigorously test specific hypotheses
- When to use: Validating specific claims or theories
- Phases: Hypothesis formulation → Test design → Analysis → Interpretation
- Output: Statistical evidence supporting or contradicting hypothesis

**`comparative-analysis`** - Compare segments, cohorts, or time periods
- When to use: Understanding differences between groups
- Phases: Definition → Measurement → Comparison → Explanation
- Output: Fair comparisons with context for differences

**`guided-investigation`** - Investigate open-ended business questions
- When to use: Answering "why did X happen?" or "what's driving Y?"
- Phases: Question decomposition → Mapping → Incremental investigation → Synthesis
- Output: Evidence-based answers to complex questions

**`marketing-experimentation`** - Validate marketing concepts through experimental cycles
- When to use: Testing marketing ideas, business concepts, campaign strategies
- Phases: Discovery → Hypothesis generation → Prioritization → Coordination → Synthesis → Iteration
- Output: Validated concepts with evidence, iteration plans for next cycle

**`qualitative-research`** - Conduct rigorous qualitative research
- When to use: Customer discovery, user research, surveys, focus groups, observations
- Phases: Design → Data collection → Familiarization → Coding → Themes → Reporting
- Output: Thematic analysis with bias prevention and intercoder reliability

### Component Skills (Specialized Tasks)

#### Data Preparation

**`importing-data`** - Transform CSV files into SQLite with proper schema
- MANDATORY first step before any analysis
- Output: `raw_*` table + quality report

**`cleaning-data`** - Address data quality issues
- MANDATORY after importing-data
- Output: `clean_*` table + verification report

#### Analysis Support

**`understanding-data`** - Systematic data profiling and exploration
- Used by process skills to examine datasets
- Capabilities: Schema inspection, distributions, relationships

**`detect-foreign-keys`** - Identify foreign key relationships between tables
- Useful for understanding multi-table databases
- Validates referential integrity, finds orphaned records

**`writing-queries`** - Construct correct, efficient SQL queries
- Translates analytical questions to SQL
- Includes optimization patterns and common pitfalls

**`interpreting-results`** - Analyze query results with intellectual honesty
- CRITICAL for avoiding false conclusions
- Assesses confidence, identifies biases, considers alternatives

**`creating-visualizations`** - Generate effective visualizations
- Terminal-based and image-based formats
- Mermaid diagrams, Vega-Lite charts, ASCII art

**`presenting-data`** - Create data-driven presentations and whitepapers
- Uses marp and pandoc for professional output
- Includes citations and reproducibility documentation

**`using-sqlite`** - Task-oriented SQLite CLI guidance
- Querying, importing, schema exploration, optimization
- Essential for data analysis workflows

## Agents Included

DataPeeker uses specialized Haiku sub-agents to prevent context pollution during data operations:

### Data Quality Agents

**`quality-assessment`** - Comprehensive quality profiling
- Detects NULL percentages, duplicates, outliers
- Identifies free text columns needing categorization

**`detect-exact-duplicates`** - Find identical records
- Returns duplicate groups with counts and examples

**`detect-near-duplicates`** - Fuzzy matching for similar records
- Uses fuzzy string matching on key text columns

**`detect-outliers`** - Statistical outlier detection
- MAD (Median Absolute Deviation) with 3 MAD threshold

**`categorize-free-text`** - Semantic grouping of free text values
- Proposes categorical groupings with complete mappings

**`detect-foreign-keys`** - Identify foreign key relationships
- Heuristics, value overlap analysis, referential integrity checks

### Qualitative Research Agents

**`analyze-transcript`** - Extract structured data from interview/focus group transcripts
- Identifies speakers, codes responses, maintains context

**`generate-initial-codes`** - Generate initial codes from qualitative data
- Inductive coding from interview transcripts, observations

**`identify-themes`** - Identify themes from coded qualitative data
- Pattern recognition across codes, thematic grouping

**`extract-supporting-quotes`** - Extract supporting quotes for themes
- Representative quotes demonstrating each theme

**`intercoder-reliability-check`** - Verify intercoder reliability
- Prevents single-coder bias, ensures reproducibility

**`search-disconfirming-evidence`** - Find evidence contradicting current conclusions
- MANDATORY for preventing confirmation bias

### Market Research Agent

**`market-researcher`** - Validate marketing concepts via internet research
- Market demand signals, similar solutions, audience needs
- Validation evidence for marketing experimentation

## Getting Started

### Prerequisites

DataPeeker requires:
- SQLite 3 for data storage
- Python 3 for analysis scripts
- Claude Code with plugin support

### Basic Workflow

```bash
# 1. Import your data
Use importing-data skill with CSV file path

# 2. Clean your data (MANDATORY)
Use cleaning-data skill with raw_* table

# 3. Choose appropriate process skill:
- exploratory-analysis: Discover patterns
- hypothesis-testing: Validate claims
- comparative-analysis: Compare groups
- guided-investigation: Answer "why" questions
- marketing-experimentation: Test marketing concepts
- qualitative-research: Analyze interviews/surveys
```

### Example: Exploratory Analysis

```
1. Start with CSV data
2. /importing-data
   → Creates raw_sales table
   → Documents quality issues

3. /cleaning-data
   → Creates clean_sales table
   → Verifies data quality

4. /exploratory-analysis
   → Discovers seasonal patterns
   → Identifies top segments
   → Suggests hypotheses to test
```

## Key Principles

1. **Data Quality First** - Never skip cleaning-data, even if data looks clean
2. **Document Everything** - Every decision captured in numbered markdown files
3. **Intellectual Honesty** - Interpret results skeptically, acknowledge limitations
4. **Reproducibility** - Others should be able to follow your exact analytical path
5. **Context Management** - Use sub-agents for data operations, keep main context analytical

## Documentation

All process skills create numbered markdown files (01-phase-name.md, 02-phase-name.md, etc.) documenting:
- Decisions made during analysis
- Queries executed
- Results observed
- Interpretations with confidence levels
- Next steps and questions

These files are git-committable and serve as complete audit trail.

## Architecture

DataPeeker follows a two-tier architecture:

**Tier 1: Component Skills**
- Specialized, focused capabilities
- Referenced by process skills
- Can be used independently when needed

**Tier 2: Process Skills**
- Workflow orchestrators
- Guide complete investigations
- Call component skills as needed
- Ensure systematic methodology

## Advanced Usage

### Custom Workflows

Component skills can be combined for custom workflows:

```
1. importing-data → raw_* table
2. cleaning-data → clean_* table
3. understanding-data → profile dataset
4. writing-queries → custom analysis
5. interpreting-results → draw conclusions
6. creating-visualizations → communicate findings
```

### Multi-Table Analysis

When working with multiple related tables:

```
1. Import each table separately
2. Use detect-foreign-keys to understand relationships
3. Clean each table
4. Use process skills that join tables as needed
```

## Contributing

To improve DataPeeker skills:

1. Document gaps, ambiguities, or inefficiencies discovered during use
2. Propose skill updates to maintain quality
3. Test changes with realistic scenarios
4. Update skill dependencies after modifications

## Version

**Current version:** 1.0.0

## License

UNLICENSED - Internal use for Tilmon Engineering

## Contact

**Tilmon Engineering**
Email: team@tilmonengineering.com
Repository: https://github.com/tilmon-engineering/tilmon-eng-skills
