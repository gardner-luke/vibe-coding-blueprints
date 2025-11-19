# Databricks Manufacturing Apps - Vibe Coding Template

A template framework for building Streamlit applications on Databricks Apps using AI-assisted development with structured prompts.

## 🤔 What is This?

This is a **vibe coding template** that demonstrates how to use structured prompts with AI coding assistants (like Cursor) to rapidly build data-driven Streamlit applications. The `instructions/` folder contains carefully crafted prompts that guide AI to build complete applications incrementally.

## 📁 Repository Structure

```
databricks_mfg_apps/
├── examples/              # Reference applications (READ-ONLY)
│   └── streamlit-data-app/
└── instructions/          # Vibe coding prompts for AI assistants
    ├── 01-base-app.md
    ├── 02-databricks-integration.md
    ├── 03-live-metrics.md
    └── 04-recreate-field-service-assistant.md
```

## 🚀 How to Use

### 1. Understand the Framework

**`instructions/`** - Sequential prompts to guide your AI assistant
- Start with `01-base-app.md` and progress through each file
- Simply tag the instruction file in your AI assistant
- Each prompt builds on the previous one

**`examples/`** - Reference implementations (READ-ONLY)
- Study these patterns but don't edit them
- AI references these when implementing features

### 2. Customize for Your Project

Modify the Cursor rules in `.cursor/rules/` directory:
- Adjust coding standards
- Update naming conventions
- Add domain-specific requirements

Adapt the instruction prompts:
- Change table names and data sources
- Adjust UI/UX requirements
- Add or remove features

### 3. Build Your Application

1. Tag `instructions/01-base-app.md` in your AI assistant
2. Let the AI build the application structure
3. Progress through each instruction file sequentially
4. Customize and refine as needed

### 4. Use as a Pattern

Clone this framework and adapt it for your own projects. Create your own vibe coding instruction sets for any domain.

## 🏗️ What Gets Built

Following the instruction prompts creates a Streamlit application with:

**01. Base App**
- Single-page Streamlit app with mock data
- Proper file structure for Databricks Apps

**02. Databricks Integration**
- Unity Catalog connectivity testing
- SQL Warehouse connection verification

**03. Live Metrics**
- Real-time data from Unity Catalog
- Dynamic KPIs and time-series analysis

**04. Wind Farm Dashboard**
- Professional enterprise UI
- AI-powered insights and interactive visualizations

## 🛠️ Technologies

- Streamlit - Python web framework
- Databricks Apps - Deployment platform
- Databricks SDK & SQL Connector - Data access
- Unity Catalog - Data governance
- Plotly - Interactive visualizations

## 💡 Philosophy

This template follows vibe coding principles:
- **Simplicity-first** - Build minimally, add incrementally
- **Progressive complexity** - Each step builds on the previous
- **Clear instructions** - Specific and actionable prompts
- **AI-friendly** - Optimized for AI assistant interpretation

## 🎯 Getting Started

1. Clone this repository
2. Review the examples folder
3. Tag `instructions/01-base-app.md` in your AI assistant
4. Progress through each instruction file
5. Customize for your needs

## 🎨 Customization

**For Cursor**: Modify `.cursor/rules/*.mdc` files to change behavior

**For Other AI Assistants**: The instruction files work with any AI coding assistant

## 📋 Example Workflow

```bash
# Tag the first instruction in your AI assistant
@instructions/01-base-app.md

# Continue with the next instruction
@instructions/02-databricks-integration.md

# Keep progressing through each file
```

## 🎯 Use Cases

- Manufacturing applications
- Field service management
- IoT monitoring dashboards
- Energy sector operations
- Supply chain visibility
- Any data-driven Streamlit application

## 📚 Resources

- [Databricks Apps Cookbook](https://apps-cookbook.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Databricks App Templates](https://github.com/databricks/app-templates)

## 🤝 Contributing

Fork it, customize it, make it your own. Share your vibe coding instruction patterns with the community.

## 📄 License

Use as a starting point for your own projects. Adapt freely.
