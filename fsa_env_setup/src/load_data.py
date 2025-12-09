# Databricks notebook source
# MAGIC %md
# MAGIC # Load CSV Data to Unity Catalog
# MAGIC This notebook reads all CSV files from the data folder and saves each as a Delta table.

# COMMAND ----------

# Get parameters from job
dbutils.widgets.text("catalog", "")
dbutils.widgets.text("schema", "")

catalog = dbutils.widgets.get("catalog")
schema = dbutils.widgets.get("schema")

print(f"Target location: {catalog}.{schema}")

# COMMAND ----------

# Find all CSV files in the data folder
import os
import pandas as pd

# Get the directory where this notebook is located
notebook_path = dbutils.notebook.entry_point.getDbutils().notebook().getContext().notebookPath().get()
base_path = "/Workspace" + "/".join(notebook_path.rsplit("/", 2)[:-2])
data_folder = f"{base_path}/data"

# List all CSV files
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]
print(f"Found {len(csv_files)} CSV files: {csv_files}")

# COMMAND ----------

# Load each CSV file as a table
for csv_file in csv_files:
    csv_path = f"{data_folder}/{csv_file}"
    table_name_base = csv_file.replace('.csv', '')
    table_name = f"{catalog}.{schema}.{table_name_base}"
    
    print(f"\n--- Loading: {csv_file} -> {table_name} ---")
    
    # Read CSV using pandas
    pdf = pd.read_csv(csv_path)
    df = spark.createDataFrame(pdf)
    
    print(f"Rows: {df.count()}, Columns: {len(df.columns)}")
    display(df.limit(5))
    
    # Write to Unity Catalog as Delta table
    df.write.mode("overwrite").saveAsTable(table_name)
    print(f"Successfully saved: {table_name}")

# COMMAND ----------

# Summary: List all created tables
print("\n=== Tables Created ===")
for csv_file in csv_files:
    table_name_base = csv_file.replace('.csv', '')
    table_name = f"{catalog}.{schema}.{table_name_base}"
    count = spark.sql(f"SELECT COUNT(*) as cnt FROM {table_name}").collect()[0].cnt
    print(f"  {table_name}: {count} rows")
