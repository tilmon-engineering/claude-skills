# Data Import and Cleaning Skills Design

## Overview

This design creates two complementary **component skills** for the DataPeeker analytics platform: `importing-data` and `cleaning-data`. These skills establish a rigorous, documented workflow for transforming raw CSV files into analysis-ready SQLite tables.

### Goals

1. **Replace "just import-csvs" command** with comprehensive, documented import workflow
2. **Ensure data quality** through systematic issue detection and cleaning
3. **Maintain audit trail** from raw CSV → clean tables via numbered markdown files
4. **Leverage sub-agents** to prevent context pollution during data analysis
5. **Integrate seamlessly** with existing process skills (exploratory-analysis, guided-investigation, etc.)

### Success Criteria

**For importing-data:**
- CSV successfully imported to `raw_*` table with basic standardization
- Schema proposed with rationale and user-confirmed
- Quality issues detected and documented in handoff report
- All decisions captured in numbered markdown files

**For cleaning-data:**
- Advanced issues addressed (duplicates, business rules, free text categorization)
- Clean tables created with consistent types and formats
- All exclusions/transformations documented with impact analysis
- Data validated against domain rules and passes verification queries

### Context

These skills sit at the beginning of the DataPeeker pipeline:

```
Raw CSV Files → [importing-data] → raw_* tables → [cleaning-data] → clean tables → Process Skills
```

They replace the current ad-hoc "just import-csvs" approach with a structured, documented workflow that creates traceability and ensures data quality before analysis begins.

## Architecture

### Approach: Import with Embedded Basic Cleaning

The design splits data preparation into **technical transformation** (importing-data) and **semantic cleaning** (cleaning-data):

**importing-data** handles:
- CSV structure discovery and profiling
- Schema inference and type mapping
- **Basic standardization** (date formats, number formats, whitespace, NULL representations)
- Import to `raw_*` tables with standardized data
- Quality issue detection (delegated to sub-agent)

**cleaning-data** handles:
- Advanced issue detection (duplicates, outliers, pattern analysis)
- **Free text grouping and categorization** (agent-assisted)
- Business rule validation framework
- Exclusion/transformation decisions with full documentation
- Creation of `clean_*` or final tables

### Key Components

**Component 1: importing-data skill**
- Location: `/Users/edwards/Work/TilmonEngineering/datapeeker/.claude/skills/importing-data/SKILL.md`
- Type: Component skill (supports data setup)
- Phases: 5 (CSV profiling → schema design → standardization → import → quality assessment)
- Outputs: `raw_*` table + numbered markdown files + quality report

**Component 2: cleaning-data skill**
- Location: `/Users/edwards/Work/TilmonEngineering/datapeeker/.claude/skills/cleaning-data/SKILL.md`
- Type: Component skill (supports data quality)
- Phases: 5 (scope → detection → strategy → execution → verification)
- Outputs: `clean_*` or final tables + numbered markdown files + verification report

**Integration Point: Quality Report**
- File: `05-quality-report.md` (from importing-data)
- Contains: Completeness stats, duplicate counts, outlier flags, free text candidates
- Purpose: Bridges the two skills, primes cleaning-data with known issues

### Data Flow

```
1. User invokes importing-data skill
   ├─ Phase 1: Profile CSV structure
   ├─ Phase 2: Design schema (propose & confirm)
   ├─ Phase 3: Define standardization rules
   ├─ Phase 4: Import to raw_* table
   └─ Phase 5: Detect quality issues (SUB-AGENT)
       └─ Output: 05-quality-report.md

2. User invokes cleaning-data skill
   ├─ Phase 1: Read quality report, define scope
   ├─ Phase 2: Deep-dive issue detection (SUB-AGENT)
   ├─ Phase 3: Design cleaning strategy (propose & confirm)
   ├─ Phase 4: Execute cleaning (SUB-AGENT for free text)
   └─ Phase 5: Verify and document results
       └─ Output: clean_* tables ready for analysis

3. User invokes process skill (e.g., exploratory-analysis)
   └─ References clean tables with full traceability
```

### Sub-Agent Delegation Strategy

**Critical Design Principle:** Never analyze data in main agent context. Always delegate to `ed3d-basic-agents:haiku-general-purpose`.

**Delegation points:**
1. **importing-data Phase 5:** Quality assessment (NULL %, duplicates, outliers, free text detection)
2. **cleaning-data Phase 2:** Deep-dive issue investigation (duplicate groups, outlier examples, free text values)
3. **cleaning-data Phase 4:** Free text categorization (analyze unique values, propose categories, create mapping)

**Pattern:** Each delegation includes:
- Complete `sqlite3` command(s) for data retrieval
- Specific instructions for analysis
- Expected return format (structured findings)
- No raw data returned to main agent (summaries only)

## Existing Patterns

### DataPeeker Skill Structure

The codebase investigation revealed a clear two-tier skill organization:

**Process Skills (4):** exploratory-analysis, guided-investigation, hypothesis-testing, comparative-analysis
- Orchestrate complete analytical workflows
- Reference component skills as prerequisites
- 4-5 phases with detailed templates

**Component Skills (4):** understanding-data, writing-queries, interpreting-results, creating-visualizations
- Support specific analytical tasks
- Self-contained, focused responsibilities
- Invoked during process skill execution

**Our new skills follow the component skill pattern:**
- Self-contained (can be used independently or referenced by process skills)
- 4-5 phase structure
- Detailed markdown templates for each phase
- TodoWrite integration for progress tracking
- "Common Rationalizations" sections to prevent shortcuts

### Documentation Patterns

All existing skills create numbered markdown files following this template:

```markdown
# [Phase Purpose]

## Objective
[What this phase accomplishes]

## Analysis/Findings
[Results from queries or investigations]

## Queries Used
```sql
[SQL commands executed]
```

## Decisions Made
[User-approved choices with rationale]

## Next Steps
[What follows in next phase]
```

**Our skills follow this exactly**, producing files like:
- `01-csv-profile.md`, `02-schema-design.md`, etc. (importing-data)
- `01-cleaning-scope.md`, `02-detected-issues.md`, etc. (cleaning-data)

### Integration with Process Skills

Existing process skills reference component skills in their prerequisites:

```markdown
## Prerequisites
Be familiar with the component skills:
- `understanding-data` - for data profiling
- `writing-queries` - for SQL query construction
...
```

**Process skills will be updated** to add:

```markdown
## Prerequisites
Before starting analysis, you MUST:
1. Have data imported using `importing-data` skill
2. Have run data quality checks using `cleaning-data` skill
3. Have created analysis workspace
```

### Verification Checkpoints

All DataPeeker skills use mandatory checkpoints between phases:

```markdown
**CHECKPOINT:** Before proceeding to Phase N, you MUST have:
- [ ] Deliverable 1
- [ ] Deliverable 2
```

**Our skills adopt this pattern** with specific verifications:
- importing-data: CSV structure verified, schema confirmed, standardization defined, import successful, quality assessed
- cleaning-data: Scope defined, issues detected, strategy approved, cleaning executed, results verified

## Implementation Phases

This design requires creating two skills, each with 5 internal phases. Implementation is broken into 8 discrete phases:

### Phase 1: Create importing-data Skill Structure

**Goal:** Establish skill file and Phase 1 (CSV Discovery & Profiling) content

**Components:**
- Create `/Users/edwards/Work/TilmonEngineering/datapeeker/.claude/skills/importing-data/SKILL.md`
- Write YAML frontmatter (name, description, allowed-tools if needed)
- Write skill overview and prerequisites section
- Write Phase 1: CSV Discovery & Profiling
  - Instructions for reading CSV, detecting encoding/delimiter
  - Template for `01-csv-profile.md`
  - Checkpoint requirements

**Dependencies:**
- None (new file creation)

**Testing:**
- Verify SKILL.md is valid markdown
- Confirm file matches existing component skill structure (reference understanding-data.md)
- Check Phase 1 template is complete and actionable

---

### Phase 2: Complete importing-data Phases 2-4

**Goal:** Write schema design, standardization, and import execution phases

**Components:**
- Write Phase 2: Schema Design & Type Inference
  - Type inference rules (INTEGER, REAL, TEXT detection)
  - Template for `02-schema-design.md` with rationale structure
  - User confirmation pattern
- Write Phase 3: Basic Standardization
  - Date format standardization rules (ISO 8601)
  - Number format normalization (remove commas, symbols)
  - NULL representation standardization
  - Template for `03-standardization-rules.md`
- Write Phase 4: Import Execution
  - CREATE TABLE generation instructions
  - Import verification (row count check)
  - Template for `04-import-log.md`

**Dependencies:**
- Phase 1 complete

**Testing:**
- Verify each phase has clear checkpoint
- Confirm templates are detailed enough for consistent execution
- Check standardization rules cover common CSV issues

---

### Phase 3: Complete importing-data Phase 5 (Quality Assessment with Sub-Agent)

**Goal:** Write quality assessment phase with complete sub-agent delegation instructions

**Components:**
- Write Phase 5: Quality Assessment & Reporting
  - **Complete sub-agent invocation prompt** with exact sqlite3 commands:
    - Schema and row count query
    - NULL percentage query (per column)
    - Exact duplicate detection query
    - Outlier detection query (3 MAD threshold)
    - Free text uniqueness query
  - Expected return format from sub-agent
  - Template for `05-quality-report.md` with all sections
- Write "Common Rationalizations" section
- Write Summary section

**Dependencies:**
- Phases 1-4 complete

**Testing:**
- Verify sub-agent prompt includes ALL necessary sqlite3 commands
- Confirm commands are parameterized correctly (table/column names as placeholders)
- Test quality report template captures all necessary information for cleaning-data

---

### Phase 4: Create cleaning-data Skill Structure

**Goal:** Establish skill file and Phase 1 (Quality Report Review)

**Components:**
- Create `/Users/edwards/Work/TilmonEngineering/datapeeker/.claude/skills/cleaning-data/SKILL.md`
- Write YAML frontmatter
- Write skill overview and prerequisites (must reference importing-data)
- Write Phase 1: Quality Report Review
  - Instructions for reading `05-quality-report.md`
  - Issue prioritization guidance
  - Template for `01-cleaning-scope.md`
  - Checkpoint requirements

**Dependencies:**
- importing-data skill complete (phases 1-5)

**Testing:**
- Verify Phase 1 correctly references importing-data outputs
- Confirm scope template captures all issue types from quality report
- Check integration point is clear

---

### Phase 5: Complete cleaning-data Phase 2 (Issue Detection with Sub-Agents)

**Goal:** Write deep-dive detection phase with multiple sub-agent delegations

**Components:**
- Write Phase 2: Issue Detection (Agent-Delegated)
  - **Duplicate detection sub-agent prompt** with:
    - Exact duplicate query
    - Near-duplicate (fuzzy match) query
    - Expected return format (groups with counts, examples)
  - **Outlier detection sub-agent prompt** with:
    - MAD-based outlier query per numeric column
    - Outlier record retrieval query
    - Expected return format (stats + examples)
  - Guidance for reviewing agent findings
  - Template for `02-detected-issues.md`

**Dependencies:**
- Phase 4 complete (Phase 1 written)

**Testing:**
- Verify each sub-agent prompt has complete sqlite3 commands
- Confirm detection covers all issue types from quality report
- Test template captures findings in structured format

---

### Phase 6: Complete cleaning-data Phases 3-4 (Strategy & Execution)

**Goal:** Write strategy design and cleaning execution phases

**Components:**
- Write Phase 3: Cleaning Strategy Design
  - Decision frameworks for each issue type:
    - Duplicates: keep first/most complete/merge
    - Outliers: exclude/cap/flag
    - Free text: categorization approach
    - Business rules: validation constraints
  - User confirmation pattern
  - Template for `03-cleaning-strategy.md`
- Write Phase 4: Cleaning Execution
  - **Free text categorization sub-agent prompt** with:
    - Unique value retrieval query
    - Categorization instructions
    - Mapping return format
  - SQL transformation patterns
  - Exclusion tracking requirements
  - Template for `04-cleaning-execution.md`

**Dependencies:**
- Phase 5 complete (Phase 2 written)

**Testing:**
- Verify strategy template covers all issue types
- Confirm free text sub-agent prompt is complete
- Check execution template tracks all transformations and exclusions

---

### Phase 7: Complete cleaning-data Phase 5 (Verification)

**Goal:** Write verification and documentation phase

**Components:**
- Write Phase 5: Verification & Documentation
  - Before/after comparison queries (row counts, key metrics)
  - Business rule validation queries
  - Exclusion accounting requirements
  - Template for `05-verification-report.md` with:
    - Summary statistics (raw vs clean)
    - All exclusions documented
    - Quality improvements quantified
- Write "Common Rationalizations" section
- Write Summary section

**Dependencies:**
- Phase 6 complete (Phases 3-4 written)

**Testing:**
- Verify verification queries are comprehensive
- Confirm report template creates complete audit trail
- Check success criteria are measurable

---

### Phase 8: Update Supporting Documentation and Integration

**Goal:** Update CLAUDE.md and ensure integration with process skills

**Components:**
- Update `/Users/edwards/Work/TilmonEngineering/datapeeker/.claude/skills/CLAUDE.md`:
  - Add importing-data and cleaning-data to component skills list
  - Update workflow diagram to show import → clean → analyze pipeline
  - Add note about mandatory cleaning before analysis
- Update process skills to reference new prerequisites:
  - exploratory-analysis/SKILL.md
  - guided-investigation/SKILL.md
  - hypothesis-testing/SKILL.md
  - comparative-analysis/SKILL.md
  - Add prerequisite note: "Data must be imported via importing-data and cleaned via cleaning-data"

**Dependencies:**
- Phases 1-7 complete (both skills written)

**Testing:**
- Verify CLAUDE.md accurately reflects new workflow
- Confirm all process skills reference new prerequisites
- Test that documentation creates clear pipeline understanding

---

## Additional Considerations

### Encoding and Delimiter Detection

**Challenge:** CSVs may have non-UTF-8 encoding or unusual delimiters.

**Approach:**
- Phase 1 of importing-data uses `file` command to detect encoding
- If non-UTF-8, document and convert during import
- Auto-detect delimiter (comma, tab, pipe, semicolon) by analyzing first few lines

### Large CSV Files

**Challenge:** Very large CSVs (>100K rows) may be slow to analyze.

**Approach:**
- Profile using samples (head/tail + random rows) rather than full scans
- Sub-agents work with query results, not full table scans where possible
- Document sampling approach in quality report

### Schema Evolution

**Challenge:** User may need to re-import same CSV with updated schema.

**Approach:**
- Keep schema design in `02-schema-design.md` as template
- Support "re-import" workflow that reads previous schema and asks what changed
- Version raw tables if needed: `raw_table_v1`, `raw_table_v2`

### Business Rule Framework

**Challenge:** Business rules are domain-specific and can't be pre-defined.

**Approach:**
- Phase 3 of cleaning-data provides template for defining rules:
  ```markdown
  ## Business Rules

  ### Rule 1: [Name]
  - **Field:** [column_name]
  - **Constraint:** [e.g., "must be between 0 and 100"]
  - **Validation Query:** `SELECT ... WHERE NOT (...)`
  - **Action if violated:** [exclude/flag/cap]
  ```
- Not every field needs rules - framework is optional but structured

### Free Text Edge Cases

**Challenge:** Some free text may be too messy for categorization.

**Approach:**
- Sub-agent flags "uncategorizable" values
- User can choose to: (a) exclude them, (b) keep in "Other" category, (c) refine categories
- Document ambiguous cases in cleaning execution phase

### Future Extensibility

**Potential enhancements not in initial scope:**
- Support for multiple CSV files → single table (concatenation)
- Support for CSV files → multiple related tables (normalization)
- Support for non-CSV formats (TSV, Excel) - would extend Phase 1 profiling
- Automated business rule suggestion (ML-based anomaly detection)
- Integration with external data quality tools

These would be added as separate phases or skills if needed.

---

## Summary

This design creates a comprehensive, documented data import and cleaning workflow for DataPeeker that:

1. **Follows existing patterns:** Component skill structure, 5 phases each, numbered markdown files, TodoWrite integration
2. **Ensures quality:** Systematic issue detection via sub-agents, mandatory cleaning before analysis
3. **Maintains audit trail:** Every decision documented, raw → clean traceability
4. **Prevents context pollution:** All data analysis delegated to Haiku sub-agents
5. **Integrates seamlessly:** Prerequisite for all process skills, replaces ad-hoc import command

The 8 implementation phases provide a clear path from design → working skills with proper testing at each step.
