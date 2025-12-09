# Databricks notebook source
# MAGIC %md
# MAGIC # Create Field Service App
# MAGIC This notebook creates an empty Databricks App for the current user.

# COMMAND ----------

# Get the current user's username
username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
# Extract just the name part (before @)
username_short = username.split("@")[0].replace(".", "-").replace("_", "-")

app_name = f"{username_short}-field-service-app"
print(f"Creating app: {app_name}")

# COMMAND ----------

# Create the app using Databricks SDK
from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

# Check if app already exists
existing_apps = [app.name for app in w.apps.list()]

if app_name in existing_apps:
    print(f"App '{app_name}' already exists!")
else:
    # Create empty app using the create API
    from databricks.sdk.service.apps import App
    app_def = App(name=app_name, description="Field Service Assistant App")
    app = w.apps.create(app_def)
    print(f"Successfully created app: {app.name}")
    print(f"App URL: {app.url}")

# COMMAND ----------

# Display app info
app_info = w.apps.get(name=app_name)
print(f"\n=== App Details ===")
print(f"Name: {app_info.name}")
print(f"URL: {app_info.url}")
print(f"State: {app_info.compute_status.state if app_info.compute_status else 'N/A'}")

