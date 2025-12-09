# Databricks Manufacturing Apps - Vibe Coding Template

A template framework for building Streamlit applications on Databricks Apps using AI-assisted development with structured prompts.

## 🤔 What is This?

This is a **vibe coding template** that demonstrates how to use structured prompts with AI coding assistants (like Cursor) to rapidly build data-driven Streamlit applications. The `instructions/` folder contains carefully crafted prompts that guide AI to build complete applications incrementally.

## 📁 Repository Structure

```
databricks_mfg_apps/
├── fsa_env_setup/         # Databricks Asset Bundle for data setup
│   ├── data/              # CSV files to load
│   ├── src/               # Notebooks (load data, create app)
│   └── resources/         # Job definitions
└── instructions/          # Vibe coding prompts for AI assistants
    ├── 01-base-app.md
    ├── 02-databricks-integration.md
    ├── 03-live-metrics.md
    └── 04-recreate-field-service-assistant.md
```

## 🚀 How to Use

### 1. Set Up Your Environment

Run the Databricks Asset Bundle to load sample data and create your app:

```bash
cd fsa_env_setup
databricks bundle deploy --var="catalog=my_catalog" --var="schema=my_schema"
databricks bundle run load_data_job --var="catalog=my_catalog" --var="schema=my_schema"
```

### 2. Understand the Framework

**`instructions/`** - Sequential prompts to guide your AI assistant
- Start with `01-base-app.md` and progress through each file
- Simply tag the instruction file in your AI assistant
- Each prompt builds on the previous one

### 3. Customize for Your Project

Adapt the instruction prompts:
- Change table names and data sources
- Adjust UI/UX requirements
- Add or remove features

### 4. Build Your Application

1. Tag `instructions/01-base-app.md` in your AI assistant
2. Let the AI build the application structure
3. Progress through each instruction file sequentially
4. Customize and refine as needed

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
2. Run the Databricks Asset Bundle (`fsa_env_setup/`)
3. Tag `instructions/01-base-app.md` in your AI assistant
4. Progress through each instruction file
5. Customize for your needs

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
