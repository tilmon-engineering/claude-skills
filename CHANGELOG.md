# Changelog

## autonomy 1.1.0

Convert command wrappers to user-invocable skills. The 14 wrapper commands in `plugins/autonomy/commands/` were thin pass-throughs to skills with no additional logic; they have been removed and the underlying skills renamed to match the old slash names. User-facing slash names are unchanged (`/start-iteration`, `/slime`, `/fork-iteration`, etc.) but now resolve directly to skills.

**Changed:**
- Removed all 14 wrapper commands; renamed skills to match old command names (e.g. `starting-an-iteration` → `start-iteration`, `slime-strategy` → `slime`).
- Marked all autonomy skills `user-invocable: true` explicitly in frontmatter.
- Updated cross-references in skills, agents, and README to use new skill names.

## autonomy 1.0.0

Initial release of the autonomy plugin. Enables AI agents to iteratively self-direct in pursuit of open-ended goals with state continuity across conversations through iteration journals.

**New:**
- Core iteration workflow: `/create-goal`, `/start-iteration`, `/end-iteration`, `/checkpoint-iteration`, `/review-progress` for goal pursuit with journal-based state continuity.
- Git integration: automatic journal commits, 4-digit iteration numbering (0001-9999), branch-aware annotated tags (`autonomy/<branch>/iteration-NNNN`), structured commit metadata (status, metrics, blockers, next steps).
- Slime mold strategy: `/slime` one-command setup for parallel exploration workflows with cooperative branch genealogy.
- Branch management: `/list-branches`, `/fork-iteration`, `/branch-status`, `/compare-branches`, `/analyze-branch` for cross-branch learning and idea reincorporation.
- Worktree support: `/fork-worktree`, `/list-worktrees`, `/remove-worktree` for running parallel agents on different branches simultaneously.
- `branch-analyzer` agent (Haiku) for computational analysis of branch state via generated Python scripts.
- `journal-reader` and `journal-summarizer` agents for context loading and milestone summarization.
