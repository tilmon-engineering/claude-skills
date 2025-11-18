# DataPeeker Analytics Platform Design

## Overview

DataPeeker is an AI-driven data analytics platform that enables teams to perform rigorous, reproducible business analytics using process-driven workflows. Users clone the repository, import CSV files, and leverage Claude Code Agent Skills to guide structured analytical processes based on the scientific method.

**Goals:**
- Enable business teams to analyze data through disciplined, process-driven workflows
- Support multiple analytical methodologies (hypothesis testing, guided investigation, exploratory analysis, comparative analysis)
- Ensure analyses are rigorous (following systematic processes), actionable (producing business-relevant insights), and reproducible (git-committable, shareable)

**Success Criteria:**
- Claude follows disciplined analytical processes without jumping to conclusions
- Analysis produces clear, actionable business insights
- Complete analysis sessions are version-controlled and reproducible

## Architecture

**Hybrid Workspace Architecture**: The platform uses a workspace-directory model where each analysis session creates a structured directory containing incrementally numbered markdown files that document the analytical journey.

### Core Components

**1. Data Layer**
- CSV files in `data/` directory
- `just import-csvs` command converts CSVs to SQLite tables in `data/analytics.db`
- Automatic schema inference with type detection

**2. Analysis Orchestration**
- `just start-analysis <process> <name>` creates dated analysis directory
- Copies `analysis/_template/` to `analysis/<process>/YYYY-MM-DD-<name>/`
- Template provides common infrastructure for all analysis types

**3. Process Skills** (`.claude/skills/datapeeker/processes/`)
Claude Code Agent Skills that guide complete analytical workflows:
- `hypothesis-testing.md` - Scientific method workflow
- `guided-investigation.md` - Structured question decomposition
- `exploratory-analysis.md` - Open-ended pattern discovery
- `comparative-analysis.md` - Segment comparison framework

Each process skill instructs Claude to create numbered markdown files documenting each stage of analysis.

**4. Component Skills** (`.claude/skills/datapeeker/components/`)
Reusable skills that process skills invoke:
- `understanding-data.md` - Data profiling and exploration
- `writing-queries.md` - SQL query construction
- `interpreting-results.md` - Result analysis and insight generation
- `creating-visualizations.md` - Text-based charts and tables

### Data Flow

1. **Setup**: User drops CSVs in `data/`, runs `just import-csvs` to create SQLite database
2. **Initiation**: User runs `just start-analysis <process> <name>` to create workspace directory
3. **Execution**: User invokes process skill with analytical goal (e.g., "Use the hypothesis-testing skill on the following hypothesis: Weekend sales are 20% higher than weekday sales")
4. **Iteration**: Claude creates numbered files (`00 - hypothesis.md`, `01 - preliminary findings.md`, etc.), each building on previous findings
5. **Conclusion**: Final file synthesizes insights, complete directory committed to git

### Error Handling Philosophy

- **Import Errors**: Log to `data/import.log`, continue with valid files
- **Query Errors**: Fix syntax errors without documentation; only document analytical dead ends
- **Workflow Errors**: Prompt for conflicts, maintain file numbering
- **Skill Execution**: Include checkpoints to prevent process deviation

## Existing Patterns

N/A - New repository with no existing codebase patterns.

## Implementation Phases

### Phase 1: Foundation Setup
**Goal**: Establish basic infrastructure for data import and analysis workspace creation

**Components**:
- `Justfile` with commands:
  - `import-csvs`: Convert CSVs in `data/` to SQLite tables
  - `start-analysis <process> <name>`: Create dated analysis directory from template
- Directory structure: `data/`, `analysis/`, `analysis/_template/`
- Basic CSV to SQLite conversion with schema inference

**Dependencies**: None

**Testing**: Manually verify CSV import creates correct tables; verify start-analysis creates proper directory structure

### Phase 2: Template Infrastructure
**Goal**: Define reusable template structure for all analysis types

**Components**:
- `analysis/_template/` directory with common infrastructure
- Template markdown files with standard sections
- Metadata and organizational structure

**Dependencies**: Phase 1 (directory structure must exist)

**Testing**: Verify template copies correctly and contains necessary sections

### Phase 3: First Process Skill (Hypothesis Testing)
**Goal**: Create fully functional hypothesis-testing process skill

**Components**:
- `.claude/skills/datapeeker/processes/hypothesis-testing.md`
- Skill defines complete workflow: state hypothesis → design test → analyze → conclude
- Instructions for creating numbered files at each stage
- Checkpoints to ensure rigor

**Dependencies**: Phase 2 (template must exist)

**Testing**: Use `testing-skills-with-subagents` with retail-seasonality scenario

### Phase 4: Component Skills
**Goal**: Build reusable component skills that process skills can reference

**Components**:
- `.claude/skills/datapeeker/components/understanding-data.md`
- `.claude/skills/datapeeker/components/writing-queries.md`
- `.claude/skills/datapeeker/components/interpreting-results.md`
- `.claude/skills/datapeeker/components/creating-visualizations.md`

**Dependencies**: Phase 3 (need reference process skill to validate components)

**Testing**: Verify each component provides clear, actionable guidance in isolation

### Phase 5: Additional Process Skills
**Goal**: Implement remaining analytical methodologies

**Components**:
- `.claude/skills/datapeeker/processes/guided-investigation.md`
- `.claude/skills/datapeeker/processes/exploratory-analysis.md`
- `.claude/skills/datapeeker/processes/comparative-analysis.md`

**Dependencies**: Phase 4 (component skills must exist)

**Testing**: Use `testing-skills-with-subagents` with process-specific scenarios

### Phase 6: Testing Infrastructure
**Goal**: Establish systematic validation framework

**Components**:
- `tests/test-cases/<process>/<scenario>/` directory structure
- Test data CSVs for each scenario
- `prompt.md`, `expected-behavior.md`, `known-failures.md` for each test case
- `just test-skill <process> <scenario>` command
- Initial test cases:
  - `hypothesis-testing/retail-seasonality`
  - `guided-investigation/customer-churn`
  - `exploratory-analysis/new-dataset`
  - `comparative-analysis/segment-performance`

**Dependencies**: Phase 5 (all process skills must exist)

**Testing**: Run test suite and verify failures are caught correctly

### Phase 7: Documentation & Examples
**Goal**: Provide clear guidance for users and contributors

**Components**:
- `README.md` with quickstart guide
- `examples/<process>-example/` reference implementations with real analysis outputs
- `docs/writing-new-skills.md` guide for creating custom process skills

**Dependencies**: Phase 6 (need validated skills to document)

**Testing**: Follow README from scratch to verify setup works; verify examples run successfully

### Phase 8: Validation & Refinement
**Goal**: Ensure all skills are bulletproof against rationalization

**Components**:
- Run complete test suite with `testing-skills-with-subagents`
- Iterate on skills based on observed failures
- Document known limitations and edge cases
- Polish error messages and user guidance

**Dependencies**: Phase 7 (complete system must exist)

**Testing**: All test cases pass with rigorous process adherence

## Additional Considerations

### Extensibility
- Platform designed for users to create custom process skills for domain-specific workflows
- Component skills provide building blocks for new processes
- Test case structure allows validation of custom skills

### Git Workflow
- Each analysis directory is a self-contained unit
- Numbered files create clear narrative progression
- Commits at each stage enable collaboration and review
- Analysis results are text-based (markdown, SQL) for diffing

### Future Enhancements
- Data visualization beyond text-based charts (SVG generation)
- Cross-analysis insights (compare multiple analysis sessions)
- Collaborative analysis (multiple users contributing to same investigation)
- Analysis templates for common business questions
