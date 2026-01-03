# Autonomy Worktree Support Design

## Overview

Add optional git worktree support to the autonomy plugin, enabling multiple Claude agents to work in parallel on different autonomy branches. Each worktree provides an isolated working directory for a separate autonomy branch, allowing concurrent iteration work without context switching.

**Goals:**
- Enable running multiple Claude agents simultaneously on different autonomy branches
- Maintain full backward compatibility with existing autonomy workflows
- Provide simple git worktree wrapper commands specifically for autonomy branches
- Organize worktrees consistently in `.worktrees/autonomy/<branch-name>/` following existing project patterns

**Success Criteria:**
- Can create autonomy branch + worktree with single command
- Multiple agents can work independently in separate worktrees
- All existing autonomy commands work unchanged in both main repo and worktrees
- Worktree cleanup preserves branch and iteration history

## Architecture

Simple git wrapper approach with minimal integration. Three new commands (`/fork-worktree`, `/remove-worktree`, `/list-worktrees`) orchestrate native git worktree commands specifically for autonomy branches.

**Core Components:**

1. **`/fork-worktree <strategy-name>` command** - Creates autonomy branch and worktree simultaneously
   - Validates strategy-name (kebab-case)
   - Detects repository root (works from within worktrees)
   - Creates branch + worktree: `git worktree add -b autonomy/<strategy-name> .worktrees/autonomy/<strategy-name>/ [<fork-point>]`
   - All worktrees created at repository root regardless of invocation location

2. **`/remove-worktree <strategy-name>` command** - Safely removes worktree while preserving branch
   - Validates uncommitted changes (fails unless `--force`)
   - Removes worktree: `git worktree remove .worktrees/autonomy/<strategy-name>/`
   - Prunes metadata: `git worktree prune`
   - Branch and iteration history persist

3. **`/list-worktrees` command** - Lists all autonomy worktrees with status
   - Filters to autonomy worktrees only
   - Shows path, branch, HEAD commit
   - Identifies locked worktrees

**Repository Root Detection:**

Commands detect repository root using `git rev-parse --git-common-dir` to ensure all worktrees created at `.worktrees/autonomy/` regardless of where command is invoked. This prevents nested worktrees when forking from within an existing worktree.

**Data Flow:**

User invokes `/fork-worktree experiment-a` → Command detects repo root → Validates branch doesn't exist → Creates branch and worktree at `.worktrees/autonomy/experiment-a/` → User navigates to worktree → Runs `/start-iteration` → All existing autonomy skills work unchanged using relative paths within worktree.

## Existing Patterns

Investigation found existing worktree usage in project: `.worktrees/` directory already used by datapeeker plugin. This design follows that pattern for consistency.

**Autonomy Plugin Patterns:**
- Commands in `plugins/autonomy/commands/` invoke skills via Skill tool
- Skills in `plugins/autonomy/skills/` orchestrate git operations and file management
- Git operations use Bash tool (pattern from `plugins/autonomy/skills/ending-an-iteration/SKILL.md:300-375`)
- Branch validation uses `git branch -a` (pattern from `plugins/autonomy/skills/forking-iteration/SKILL.md:68-76`)
- Relative paths throughout (`autonomy/goal-name/iteration-NNNN.md`)

**Git Worktree Pattern:**
- Single command creation: `git worktree add -b <branch> <path> [<commit>]` (verified via `git worktree add --help`)
- Safe removal: `git worktree remove <path>` with uncommitted change detection
- Metadata cleanup: `git worktree prune` after removal

**No Divergence:**
This design extends existing patterns without modification. Existing skills work unchanged because they use relative paths that resolve correctly within any worktree.

## Implementation Phases

### Phase 1: Create `/fork-worktree` Command and Skill

**Goal:** Enable creating autonomy branch + worktree with single command

**Components:**
- Create: `plugins/autonomy/commands/fork-worktree.md` (command declaration)
- Create: `plugins/autonomy/skills/forking-worktree/SKILL.md` (implementation)

**Dependencies:** None (first phase)

**Testing:**
- Run `/fork-worktree test-strategy` from main repo → creates `.worktrees/autonomy/test-strategy/`
- Run `/fork-worktree test-strategy-2` from within first worktree → creates `.worktrees/autonomy/test-strategy-2/` at root level (not nested)
- Verify branch `autonomy/test-strategy` exists
- Navigate to worktree, run `/start-iteration` → successfully creates iteration journal

**Implementation Details:**
- Command model: Sonnet, allowed tools: Bash, Glob, Skill
- Skill validates strategy-name (kebab-case), checks branch/worktree don't exist
- Skill detects repo root: `git rev-parse --git-common-dir | xargs dirname`
- Skill creates worktree: `git worktree add -b autonomy/<strategy> .worktrees/autonomy/<strategy>/ [<fork-point>]`
- Optional fork point like `/fork-iteration`: `/fork-worktree 0015 new-strategy`

### Phase 2: Create `/remove-worktree` Command and Skill

**Goal:** Enable safe worktree cleanup while preserving branch and history

**Components:**
- Create: `plugins/autonomy/commands/remove-worktree.md`
- Create: `plugins/autonomy/skills/removing-worktree/SKILL.md`

**Dependencies:** Phase 1 complete (needs worktrees to remove)

**Testing:**
- Create test worktree with `/fork-worktree`
- Make uncommitted changes → `/remove-worktree test-strategy` fails with warning
- Run `/remove-worktree --force test-strategy` → succeeds, worktree removed
- Verify `.worktrees/autonomy/test-strategy/` directory gone
- Verify branch `autonomy/test-strategy` still exists
- Verify iteration tags still exist

**Implementation Details:**
- Command model: Sonnet, allowed tools: Bash, Glob, Skill
- Skill validates worktree exists at `.worktrees/autonomy/<strategy>/`
- Skill checks uncommitted changes (fail unless `--force` flag)
- Skill removes: `git worktree remove [--force] .worktrees/autonomy/<strategy>/`
- Skill prunes: `git worktree prune`

### Phase 3: Create `/list-worktrees` Command and Skill

**Goal:** Enable discovery and status checking of autonomy worktrees

**Components:**
- Create: `plugins/autonomy/commands/list-worktrees.md`
- Create: `plugins/autonomy/skills/listing-worktrees/SKILL.md`

**Dependencies:** Phase 1 complete (needs worktrees to list)

**Testing:**
- Create 3 test worktrees with `/fork-worktree`
- Run `/list-worktrees` → shows all 3 worktrees with paths, branches, HEAD commits
- Lock one worktree: `git worktree lock .worktrees/autonomy/test-strategy`
- Run `/list-worktrees` → shows locked status
- Verify no non-autonomy worktrees shown (filters to `autonomy/*` only)

**Implementation Details:**
- Command model: Sonnet, allowed tools: Bash, Glob, Skill
- Skill runs: `git worktree list --porcelain`
- Skill filters output to worktrees matching `.worktrees/autonomy/` pattern
- Skill formats as markdown table with columns: Path, Branch, HEAD, Status
- Skill identifies locked worktrees from porcelain output

### Phase 4: Update `.gitignore` for Worktrees

**Goal:** Prevent accidentally committing worktree directories

**Components:**
- Modify: `.gitignore` (add `.worktrees/` entry)

**Dependencies:** None (independent task)

**Testing:**
- Create test worktree with `/fork-worktree`
- Run `git status` → verify `.worktrees/` not shown in untracked files
- Create file in worktree → run `git status` from main repo → verify worktree files not shown

**Implementation Details:**
- Check if `.gitignore` already contains `.worktrees/` (datapeeker may have added it)
- If not present, add `.worktrees/` entry
- If already present, verify correct pattern (should ignore entire directory)

### Phase 5: Update Plugin Manifest

**Goal:** Register new commands in plugin.json

**Components:**
- Modify: `plugins/autonomy/.claude-plugin/plugin.json` (add commands to manifest)

**Dependencies:** Phases 1-3 complete (all commands implemented)

**Testing:**
- Reload plugin or restart Claude
- Verify `/fork-worktree`, `/remove-worktree`, `/list-worktrees` available in command list
- Run each command to verify successful registration

**Implementation Details:**
- Add three new command entries following existing pattern from plugin.json
- Keywords: ["worktree", "parallel", "isolation", "branches"]
- Verify JSON syntax valid

### Phase 6: Document Worktree Support in README

**Goal:** Provide user documentation for worktree feature

**Components:**
- Modify: `plugins/autonomy/README.md` (add Worktree Support section)

**Dependencies:** Phases 1-5 complete (feature fully implemented)

**Testing:**
- Review README changes for clarity and completeness
- Verify all commands documented with examples
- Verify parallel agent workflow example included

**Implementation Details:**
- Add "Worktree Support" section after slime mold strategy documentation
- Document all three commands with syntax and examples
- Include parallel agent workflow example (3 terminals, 3 agents)
- Explain repository root detection and non-nested worktree guarantee
- Add cleanup best practices section

## Additional Considerations

**Git worktree limitations:**
A branch can only be checked out in one worktree at a time. This means `/fork-worktree experiment-a` will fail if branch `autonomy/experiment-a` is already checked out in main repo or another worktree. Error message should suggest either removing existing worktree or using different strategy-name.

**Disk space:**
Each worktree is a complete working copy of the repository. Large repositories with multiple worktrees consume significant disk space. Users should run `/remove-worktree` regularly to clean up completed experiments.

**Fork point validation:**
When using optional fork point (`/fork-worktree 0015 new-strategy`), the iteration tag must exist in current branch history. Validation should follow same pattern as `plugins/autonomy/skills/forking-iteration/SKILL.md:91-109` using `git tag --merged HEAD`.

**Parallel agent coordination:**
While worktrees provide isolation, they share the same `.git` directory. Commits made in any worktree are immediately visible to all others. This enables cross-pollination via `/analyze-branch` command, which reads journals from other branches' commit history without requiring worktree navigation.
