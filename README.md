# Claude Skills Marketplace

Institutional knowledge marketplace for AI agent teams, maintained by Tilmon Engineering.

## Overview

This marketplace hosts a collection of Claude Code plugins that capture institutional knowledge and enable AI agents to perform specialized tasks with rigorous, repeatable methodologies.

## Plugins

### DataPeeker - Structured Research Methods

Structured research methods for AI agents conducting rigorous, reproducible data analysis and qualitative research.

**Version:** 1.0.0

**Key capabilities:**
- Hypothesis testing with statistical rigor
- Exploratory data analysis following systematic patterns
- Comparative analysis across segments and time periods
- Guided investigation for open-ended business questions
- Qualitative research with bias prevention protocols
- Data preparation pipeline (importing, cleaning, validation)

[View plugin documentation →](./plugins/datapeeker/README.md)

### Autonomy - Open-Ended Goal Pursuit

Enable AI agents to iteratively self-direct in pursuit of open-ended goals with state continuity across conversations through iteration journals.

**Version:** 1.0.0

**Key capabilities:**
- Iteration journals for state continuity across conversations
- Slime mold strategy for parallel exploration via git branches
- Branch management for comparing and cross-pollinating experiments
- Git worktree support for parallel agent workflows

[View plugin documentation →](./plugins/autonomy/README.md)

## Installation

Install from GitHub:

```bash
claude plugin install tilmon-engineering/claude-skills
```

**Strongly recommended dependency:** [ed3d-plugins](https://github.com/ed3dai/ed3d-plugins) provides plan-and-execute workflows, brainstorming, TDD, and other development skills that complement these plugins.

```bash
claude plugin install ed3dai/ed3d-plugins
```

## Contributing

### Adding New Plugins

To add a new plugin to this marketplace:

1. Create plugin directory structure in `plugins/[plugin-name]/`
2. Add `.claude-plugin/plugin.json` with metadata
3. Implement skills in `skills/` and/or agents in `agents/`
4. Update `/.claude-plugin/marketplace.json` to include new plugin
5. Create plugin README documenting capabilities
6. Validate with `claude plugin validate .`

### Plugin Structure

```
plugins/[plugin-name]/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata
├── skills/                  # Optional: Claude Code skills
├── agents/                  # Optional: Specialized agents
├── templates/              # Optional: Template files
└── README.md               # Plugin documentation
```

## License

MIT - See [LICENSE](./LICENSE) for details.
