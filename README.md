# Tilmon Engineering Skills Marketplace

Institutional knowledge marketplace powering Tilmon Engineering's AI agent team.

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

## Installation

This marketplace is designed for internal use by Tilmon Engineering teams. To install:

1. Clone this repository
2. Install the marketplace in Claude Code:
   ```bash
   claude plugin install /path/to/tilmon-eng-skills
   ```

## Future Plugins

Planned additions to the marketplace:

- **Security Analysis** - Security audit workflows and vulnerability assessment
- **Customer Service** - Customer interaction patterns and support protocols
- **Knowledge Management** - Documentation standards and knowledge capture methods

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

UNLICENSED - Internal use only for Tilmon Engineering

## Contact

**Tilmon Engineering**
Email: team@tilmonengineering.com
