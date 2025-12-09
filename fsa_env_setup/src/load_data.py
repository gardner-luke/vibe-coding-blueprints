# Databricks notebook source
# MAGIC %md
# MAGIC # Load Sample Data to Unity Catalog
# MAGIC This notebook reads a CSV file and saves it as a Delta table.

# COMMAND ----------

# Get parameters from job
dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

print(f"Target location: {catalog}.{schema}")

# COMMAND ----------

# Read the CSV file from workspace files
import os

# Get the directory where this notebook is located
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
base_path = "/Workspace" + "/".join(notebook_path.rsplit("/", 2)[:-2])
csv_path = f"{base_path}/data/sample_data.csv"

print(f"Reading from: {csv_path}")

# Read CSV using pandas (works reliably with workspace files)
import pandas as pd
pdf = pd.read_csv(csv_path)
df = spark.createDataFrame(pdf)

display(df)

# COMMAND ----------

# Write to Unity Catalog as Delta table
table_name = f"{catalog}.{schema}.sample_data"

df.write.mode("overwrite").saveAsTable(table_name)

print(f"Successfully saved table: {table_name}")

# COMMAND ----------

# Verify the table was created
spark.sql(f"SELECT * FROM {table_name}").display()
