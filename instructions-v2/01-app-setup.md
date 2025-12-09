# 🏗️ Step 1: App Setup & Header

**Goal:** Create the basic Streamlit app structure with the "Cool Electric Co." header.

**Create these files in `/wind-farm-app`:**

**`app.py`**
- Set page config: `page_title="Cool Electric Co."`, `layout="wide"`
- Display centered header: "Cool Electric Co." in blue (#0066CC)
- Add a thin horizontal line below the header

**`requirements.txt`**
```
streamlit
plotly
pandas
databricks-sdk
databricks-sql-connector
```

**`app.yaml`**
```yaml
command: ["streamlit", "run", "app.py"]
env:
  - name: "DATABRICKS_WAREHOUSE_ID"
    valueFrom: "sql-warehouse"
```

**Expected Result:** A clean page with just the blue "Cool Electric Co." header centered at the top.

