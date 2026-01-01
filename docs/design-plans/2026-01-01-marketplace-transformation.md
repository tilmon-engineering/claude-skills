# DataPeeker to Tilmon Engineering Skills Marketplace Transformation

## Overview

Transform the datapeeker repository into a Claude Code marketplace named `tilmon-eng-skills` that hosts multiple plugins. DataPeeker becomes the first plugin within this marketplace, preserving all 14 skills, 14 agents, and supporting infrastructure while establishing a structure for future plugins (security analysis, customer service, knowledge management).

**Goals:**
- Create marketplace structure following Claude Code monorepo pattern
- Preserve datapeeker as first plugin with full git history
- Enable future plugin additions (local or external via git URLs)
- Maintain institutional knowledge and established workflows
- Remove user data from distribution while keeping locally

**Success Criteria:**
- Marketplace validates with `claude plugin validate .`
- All 14 skills and 14 agents accessible in new structure
- Git history preserved for all moved files
- Clean separation between plugin code and user data

## Architecture

**Monorepo marketplace with local plugins** - single repository hosting multiple plugins in `plugins/` subdirectories. Follows pattern from Anthropic's official Claude Code repository (not ed3d's external plugin approach).

**Big-bang transformation** - complete restructuring in single operation. Clean result, faster execution, acceptable risk given no production dependencies and strong testing validation.

**Structure:**
```
tilmon-eng-skills/                    # Marketplace root
├── .claude-plugin/
│   └── marketplace.json              # Marketplace manifest
├── plugins/
│   └── datapeeker/                   # First plugin
│       ├── .claude-plugin/
│       │   └── plugin.json           # Plugin metadata
│       ├── skills/                   # 14 skills (moved from .claude/skills/)
│       ├── agents/                   # 14 agents (moved from .claude/agents/)
│       ├── templates/                # Analysis workspace template
│       └── README.md                 # Plugin documentation
├── docs/                             # Design documentation (preserved)
├── testing/                          # QA evidence (preserved)
├── .gitignore                        # Updated to exclude user data
├── Justfile                          # Updated paths
└── README.md                         # Marketplace overview
```

**User data handling:**
- `data/`, `analysis/`, `.obsidian/`, `.serena/` untracked via `.gitignore`
- Files remain locally but not distributed with marketplace
- `analysis/_template/` preserved as plugin template

## Existing Patterns

**Investigation findings:**

**ed3d-claude-marketplace** (external plugin pattern):
- Each plugin is separate git repository referenced via git URL in marketplace.json
- Suitable for public distribution but unnecessary complexity for internal team

**Anthropic's claude-code repository** (local plugin pattern):
- Plugins in `./plugins/` subdirectories with relative paths
- Single repository, coordinated releases
- Chosen pattern: Better for Tilmon Engineering internal team tools

**Plugin structure follows Claude Code requirements:**
- `.claude-plugin/plugin.json` with metadata (name, version, author, description)
- Skills in `skills/` subdirectory
- Agents in `agents/` subdirectory
- Marketplace manifest at `.claude-plugin/marketplace.json` lists all plugins

**Git history preservation:**
- Research recommends `git filter-repo` for large migrations
- For this case: `git mv` sufficient (preserves history, simpler for single-step moves)
- Verified with `git log --follow` post-migration

## Implementation Phases

### Phase 1: Preparation and Backup
**Goal:** Establish safe baseline and enable rollback

**Components:**
- Create backup branch: `git branch backup-pre-marketplace`
- Create feature branch: `git checkout -b transform-to-marketplace`
- Verify clean working directory: `git status`

**Dependencies:** None (first phase)

**Testing:**
- Backup branch exists and matches current main
- Feature branch checked out
- No uncommitted changes in working directory

### Phase 2: Create Marketplace Structure
**Goal:** Add marketplace configuration and root directories

**Components:**
- Create: `.claude-plugin/` directory
- Create: `.claude-plugin/marketplace.json` with marketplace metadata
- Create: `plugins/` directory (will contain all plugins)

**Dependencies:** Phase 1 complete

**Testing:**
- `.claude-plugin/marketplace.json` validates with `claude plugin validate .`
- JSON follows schema from `https://anthropic.com/claude-code/marketplace.schema.json`
- Marketplace metadata includes name, version, owner, plugins array

**marketplace.json content:**
```json
{
  "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
  "name": "tilmon-eng-skills",
  "version": "1.0.0",
  "description": "Tilmon Engineering institutional knowledge marketplace - AI agent skills for analysis, security, customer service, and knowledge management",
  "owner": {
    "name": "Tilmon Engineering",
    "email": "team@tilmonengineering.com"
  },
  "plugins": [
    {
      "name": "datapeeker",
      "description": "Structured research methods for AI agents - hypothesis testing, exploratory analysis, comparative analysis, and qualitative research",
      "version": "1.0.0",
      "source": "./plugins/datapeeker",
      "author": {
        "name": "Tilmon Engineering",
        "email": "team@tilmonengineering.com"
      },
      "keywords": ["data-analysis", "research-methods", "hypothesis-testing", "qualitative-research"]
    }
  ]
}
```

### Phase 3: Create DataPeeker Plugin Structure
**Goal:** Establish plugin directory and metadata

**Components:**
- Create: `plugins/datapeeker/` directory
- Create: `plugins/datapeeker/.claude-plugin/` directory
- Create: `plugins/datapeeker/.claude-plugin/plugin.json` with plugin metadata
- Create: `plugins/datapeeker/skills/` directory
- Create: `plugins/datapeeker/agents/` directory
- Create: `plugins/datapeeker/templates/` directory

**Dependencies:** Phase 2 complete (plugins/ directory exists)

**Testing:**
- Plugin directory structure matches design
- `plugin.json` validates with Claude Code schema
- Directory structure ready to receive moved files

**plugin.json content:**
```json
{
  "name": "datapeeker",
  "description": "Structured research methods for AI agents - hypothesis testing, exploratory analysis, comparative analysis, and qualitative research",
  "version": "1.0.0",
  "author": {
    "name": "Tilmon Engineering",
    "email": "team@tilmonengineering.com"
  },
  "homepage": "https://github.com/tilmon-engineering/tilmon-eng-skills",
  "repository": "https://github.com/tilmon-engineering/tilmon-eng-skills",
  "license": "UNLICENSED",
  "keywords": [
    "data-analysis",
    "research-methods",
    "hypothesis-testing",
    "exploratory-analysis",
    "comparative-analysis",
    "qualitative-research",
    "market-research"
  ]
}
```

### Phase 4: Move Skills and Agents
**Goal:** Relocate all skills and agents preserving git history

**Components:**
- Move: `.claude/skills/*` → `plugins/datapeeker/skills/` using `git mv`
  - All 14 skill directories (exploratory-analysis, hypothesis-testing, etc.)
  - `CLAUDE.md` overview file
  - `analyze-skill-dependencies.py` script
  - `skill-dependencies.mermaid` diagram
- Move: `.claude/agents/*` → `plugins/datapeeker/agents/` using `git mv`
  - All 14 agent files (quality-assessment.md, market-researcher.md, etc.)
- Move: `analysis/_template/` → `plugins/datapeeker/templates/_template/` using `git mv`
- Remove: `.claude/` directory (now empty)

**Dependencies:** Phase 3 complete (target directories exist)

**Testing:**
- Verify all 14 skills present in `plugins/datapeeker/skills/`
- Verify all 14 agents present in `plugins/datapeeker/agents/`
- Verify template present in `plugins/datapeeker/templates/_template/`
- Test git history preservation: `git log --follow plugins/datapeeker/skills/exploratory-analysis/SKILL.md`
- Verify `git blame` works on moved files
- `.claude/` directory removed

### Phase 5: Update References and Configuration
**Goal:** Update all file references to new structure and exclude user data

**Components:**
- Modify: `.gitignore` - Add exclusions:
  ```
  # User data and analysis
  data/
  analysis/
  !analysis/_template/

  # Local configurations
  .serena/
  .obsidian/

  # Database files
  *.db
  *.sqlite
  ```
- Execute: `git rm --cached -r data/ analysis/ .obsidian/ .serena/` (untrack but keep local)
- Modify: `Justfile` - Update paths from `.claude/skills/` to `plugins/datapeeker/skills/`
- Review: `.claude/settings.local.json` - Determine if needs adaptation or can be removed

**Dependencies:** Phase 4 complete (files moved)

**Testing:**
- Git status shows `data/`, `analysis/` as untracked (ignored)
- Justfile commands work with new paths
- No references to old `.claude/skills/` paths remain
- Settings file handled appropriately

### Phase 6: Documentation
**Goal:** Create marketplace and plugin README files

**Components:**
- Create: `README.md` (marketplace root) - Marketplace overview, installation, plugin list
- Create: `plugins/datapeeker/README.md` - Plugin documentation, skills list, getting started

**Dependencies:** Phase 5 complete (structure finalized)

**Testing:**
- Root README explains marketplace purpose and installation
- Plugin README documents all 14 skills and 14 agents
- Documentation references correct paths
- Getting started guide is actionable

**Root README.md structure:**
```markdown
# Tilmon Engineering Skills Marketplace

Institutional knowledge marketplace powering Tilmon Engineering's AI agent team.

## Plugins

### DataPeeker - Structured Research Methods
[Description and link to plugin README]

## Installation
[Installation instructions]

## Future Plugins
- Security Analysis - Coming soon
- Customer Service - Coming soon
- Knowledge Management - Coming soon

## Contributing
[Guidelines for adding new plugins]
```

**Plugin README.md structure:**
```markdown
# DataPeeker Plugin

Structured research methods for AI agents conducting rigorous, reproducible data analysis.

## Skills Included
[List of 14 skills with brief descriptions]

## Agents Included
[List of 14 agents with purposes]

## Getting Started
[Quick start guide referencing key skills]
```

### Phase 7: Validation
**Goal:** Verify transformation success and structural integrity

**Components:**
- Run: `claude plugin validate .` - Marketplace validation
- Execute validation checklist:
  - File counts: 14 skills + 14 agents present
  - Git history: `git log --follow` works on sample files
  - Structure: All directories match design
  - Configuration: JSON files valid
  - Ignored files: User data untracked properly

**Dependencies:** Phase 6 complete (all changes made)

**Testing:**
- `claude plugin validate .` passes without errors
- All 14 skills accessible in new location
- All 14 agents accessible in new location
- Git history intact (spot-check 3-5 files with `git log --follow`)
- No unexpected differences: `git diff --name-status backup-pre-marketplace` shows only intended changes
- Clean working directory after staging

### Phase 8: Finalization
**Goal:** Commit transformation and establish rollback capability

**Components:**
- Stage: `git add .` - Stage all changes
- Commit with descriptive message documenting transformation
- Tag: `git tag v1.0.0` - Mark initial marketplace release
- Verify: `git status` shows clean working directory
- Document rollback: Procedure to revert if critical issues found

**Dependencies:** Phase 7 complete (validation passed)

**Testing:**
- Commit includes all intended changes
- Tag `v1.0.0` points to transformation commit
- Backup branch `backup-pre-marketplace` exists for rollback
- Rollback procedure documented and verified: `git checkout main && git reset --hard backup-pre-marketplace`

**Commit message:**
```
feat: transform datapeeker into tilmon-eng-skills marketplace

Transform single-plugin repository into monorepo marketplace structure.

Changes:
- Create marketplace structure with .claude-plugin/marketplace.json
- Move datapeeker to plugins/datapeeker/ with full git history
- Preserve all 14 skills and 14 agents in plugin structure
- Untrack user data (data/, analysis/) from git distribution
- Update references in Justfile and configuration
- Add marketplace and plugin documentation

DataPeeker v1.0.0 is first plugin in marketplace.
Future plugins: security analysis, customer service, knowledge management.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

## Additional Considerations

**Git history preservation:** Using `git mv` preserves full commit history automatically. Verification with `git log --follow` ensures blame and bisect continue working. No need for complex `git filter-repo` operations given single-step moves.

**Rollback safety:** Backup branch `backup-pre-marketplace` provides immediate rollback path if critical issues discovered. Can revert entire transformation with `git reset --hard backup-pre-marketplace`.

**Future plugin additions:** New plugins added to `plugins/` directory with same structure as datapeeker. Update `marketplace.json` to include new plugin entries. Can mix local plugins (relative paths) and external plugins (git URLs) as needed on case-by-case basis.

**Testing validation:** Validation phase (Phase 7) critical before commit. Catching structural issues before finalization prevents need to rewrite git history. `claude plugin validate .` provides automated check for configuration correctness.

**Settings file handling:** `.claude/settings.local.json` may need adaptation for plugin context. Review during Phase 5 to determine if permissions transfer to plugin structure or if new approach needed. Consult Claude Code plugin documentation for settings in plugin context.
