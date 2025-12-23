# Databricks Manufacturing Apps - Vibe Coding Template

A template framework for building Streamlit applications on Databricks Apps using AI-assisted development with structured prompts.

## 🤔 What is This?

This is a **vibe coding template** that demonstrates how to use structured prompts with AI coding assistants (like Cursor) to rapidly build data-driven Streamlit applications. The `instructions/` folder contains carefully crafted prompts that guide AI to build a complete wind farm monitoring dashboard incrementally.

<div align="center">
  <img src="assets/images/FieldServiceAssistant.png" width="800" alt="Field Service Assistant">
</div>

## 👋 Getting Started

**Prerequisites:** You should be running this in **[Cursor](https://cursor.com)** (the AI-powered code editor). This template is specifically designed for Cursor's Agent/Composer mode.

**Time commitment:** ~30 minutes

### What Makes This Different

This template demonstrates the power of using detailed, natural language prompts in a **modular, composable fashion** to build an app **brick by brick** 🧱😉. Each instruction file contains a precise prompt that tells the AI exactly what to build next, allowing you to construct a complete application incrementally without writing code yourself.

**What to expect:**
- You'll provide instructions to Cursor, and it handles the implementation
- Cursor acts as your coding partner - if something doesn't look right, just ask it to fix it
- Each step builds on the previous one, adding new features progressively
- You stay in control: review changes and verify results at each step

**New to Cursor?** Don't worry - the instructions are detailed and sequential. Just follow them one at a time and let the AI do the heavy lifting.

## 📁 Repository Structure

```
databricks_mfg_apps/
├── config.yaml              # Databricks connection settings (catalog, schema, warehouse)
├── setup_data.py            # Script to deploy data using config.yaml
├── fsa_env_setup/           # Databricks Asset Bundle for data setup
│   ├── data/                # Sample CSV files (turbine metadata & telemetry)
│   ├── src/                 # Notebooks (load_data.py)
│   └── resources/           # Job definitions
└── instructions/            # Vibe coding prompts for AI assistants
    ├── 01-app-setup.md      # Create basic Streamlit app structure
    ├── 02-kpi-cards.md      # Add KPI metric cards
    ├── 03-power-chart.md    # Add power output chart
    ├── 04-summary-map.md    # Add GenAI summary & turbine map
    ├── 05-connectivity.md   # Add Databricks connection testing
    └── 06-live-data.md      # Connect to live Databricks data
```

## 🚀 How to Use

### 0. Prerequisites

Before you begin, ensure you have the following:

1. **Databricks CLI installed and authenticated**:
   - Follow the [official tutorial](https://docs.databricks.com/aws/en/dev-tools/cli/tutorial) to install and set up the Databricks CLI.
   - **Note:** Ensure your CLI is correctly authenticated (`databricks auth login`) and targeted to your workspace.
2. **Databricks Permissions**:
   - Access to an existing **Catalog** (or permission to create one).
   - Access to a **Schema** (or permission to create one).
   - A **SQL Warehouse** available for use (you will need its ID).
     - **Recommended:** Use an existing warehouse if available, or create a Serverless 2X-Small warehouse for demo purposes.
     - Find warehouse IDs in your Databricks workspace under **SQL Warehouses** → Click on a warehouse → Copy the **Server hostname** path or **ID** from the URL.

#### Authentication Setup & Troubleshooting

The Databricks CLI should be authenticated to your workspace. Most users can simply run:

```bash
databricks auth login
```

**Note:** Some users, especially in SSO environments, may need to specify a profile:

```bash
databricks auth login --host <workspace_url> --profile DEFAULT
```

**Common authentication issues:**
- "Profile not found" → Use the command above to set a DEFAULT profile
- "Token expired" → Re-run the auth login command
- If you have multiple Databricks workspaces, ensure you're authenticated to the correct one

Verify your authentication with: `databricks auth profiles`

### 1. Configure Environment

Edit `config.yaml` with your Databricks settings:

```yaml
catalog: "CATALOG_NAME"
schema: "SCHEMA_NAME"
warehouse_id: "WAREHOUSE_ID"
```

> **💡 Tip:** Use only letters, numbers, and underscores in your catalog and schema names (e.g., `my_catalog`, `wind_farm_schema`). Avoid dashes or special characters to prevent SQL identifier issues.

### 2. Set Up Data

Run the setup script to deploy the sample data to your Databricks environment:

```bash
python setup_data.py
```

**What this script does:**
1. Creates a Python virtual environment (`.venv`) for the app you'll build in Step 3
2. Reads your configuration from `config.yaml`
3. Deploys the Databricks Asset Bundle to create tables in Unity Catalog
4. Runs the data loading job to populate the tables from CSV files

**Once the script completes successfully and you see the data in your catalog, you are ready to proceed to the next step.**

### 3. Build the App with AI

Use the **Cursor Agent** to build the application. In the Chat window, ensure you are using the "Agent" mode (or "Composer" with Agent capabilities) so it can execute terminal commands and create files.

> **💡 Note about config.yaml:** The AI will read your `config.yaml` values and embed them directly into the `app.py` file as constants. This means the app has no runtime dependency on `config.yaml` - the configuration file is only used as a reference during the build process.

**How to "Tag" Files:**
To provide instructions to the AI, type `@` followed by the filename (e.g., `@01-app-setup.md`) in the chat input. This gives the AI the specific context it needs for that step. You may also drag and drop the files from your explorer into the Cursor Chat window.

Run the following prompts sequentially in the Agent chat:

**1. Initialize the App:**

```bash
@instructions/01-app-setup.md    # Creates wind-farm-app/ with basic structure
```

**✨ Verify it works:**
After this first step is complete, activate the virtual environment and start the app:

```bash
# Activate the virtual environment (created in Step 2)
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Navigate to the app directory and install dependencies
cd wind-farm-app
pip install -r requirements.txt
streamlit run app.py
```

*Tip: Keep the app running in your terminal. As you apply the next steps, just refresh your browser to see the changes.*

**2. Add Features (run each step individually):**

Add KPI Cards:
```bash
@instructions/02-kpi-cards.md
```

Add Power Chart:
```bash
@instructions/03-power-chart.md
```

Add GenAI Summary & Map:
```bash
@instructions/04-summary-map.md
```

Add Databricks Connection Testing:
```bash
@instructions/05-connectivity.md
```

Connect to Live Data:
```bash
@instructions/06-live-data.md
```

> **Important:** Run each prompt **one at a time** in sequence. Wait for the AI to complete each step before moving to the next.

## 🏗️ What Gets Built

Following all 6 instruction prompts creates a **wind-farm-app/** directory containing a Streamlit dashboard for "Cool Electric Co." with:

| Step | Feature | Description |
|------|---------|-------------|
| 01 | App Setup | Basic Streamlit app with header and deployment config |
| 02 | KPI Cards | 4 metric cards (devices, maintenance, health %, output) |
| 03 | Power Chart | Plotly line chart showing real vs expected power output |
| 04 | GenAI Summary & Map | AI insights panel + interactive turbine location map |
| 05 | Connection Test | Databricks SQL Warehouse connectivity verification |
| 06 | Live Data | All components connected to Unity Catalog tables |

## 🛠️ Technologies

- **Cursor AI (Agent mode)** - AI-assisted development that executes commands and creates files based on natural language instructions
- **Streamlit** - Python web framework for the dashboard
- **Databricks Apps** - Deployment platform
- **Databricks SDK & SQL Connector** - Data access
- **Databricks CLI** - Command-line tool for interacting with Databricks from your terminal
- **Unity Catalog** - Data governance and data management
- **Plotly** - Interactive visualizations
- **Databricks Asset Bundles** - Infrastructure as code for data setup

## 💡 Philosophy

This template follows vibe coding principles:
- **Modular Prompts** - Each instruction file is a self-contained, detailed prompt
- **Composable Architecture** - Features build on each other incrementally
- **Brick by Brick** - Add one capability at a time, verifying as you go
- **Simplicity-first** - Build minimally, add incrementally
- **Progressive complexity** - Each step builds on the previous
- **AI-friendly** - Prompts optimized for AI assistant interpretation
- **Human-in-the-Loop** - You guide the direction, AI handles implementation

## 🔧 Troubleshooting

### Common Issues

**Authentication errors or "Profile not found"**
- Run: `databricks auth login --host <workspace_url> --profile DEFAULT`
- Verify with: `databricks auth profiles`
- Ensure you're authenticated to the workspace where you created your catalog/schema

**Map doesn't display / connection errors**
- **Cause:** App may not know which Databricks profile to use
- **Solution:** Ensure your Databricks CLI is authenticated (see above)
- If you have multiple profiles, verify your default profile is set correctly

**Setup script fails**
- Verify your `config.yaml` has no special characters in catalog/schema names (use only letters, numbers, underscores)
- Check that you have CREATE permissions for the catalog and schema
- Ensure the Databricks CLI is properly installed: `databricks --version`

**Getting different results than expected**
- Check that you completed each previous step in order
- Verify your data loaded correctly by checking your Databricks catalog in the UI
- Ask Cursor: "Can you verify that my implementation matches the instruction file?"

## 📚 Resources

- [Databricks Apps Cookbook](https://apps-cookbook.dev/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Databricks App Templates](https://github.com/databricks/app-templates)

## 📄 License

Use as a starting point for your own projects. Adapt freely.
