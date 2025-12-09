# 🔗 Step 5: Databricks Connectivity Test

**Goal:** Add a page to verify Databricks SQL connectivity before going live.

**Create `pages/1_🔗_Connectivity.py`:**

Follow the [Apps Cookbook](https://apps-cookbook.dev/docs/streamlit/tables/tables_read) connection pattern:

```python
from databricks.sdk.core import Config
from databricks import sql

def sql_query(query: str):
    cfg = Config()
    with sql.connect(
        server_hostname=cfg.host,
        http_path=f"/sql/1.0/warehouses/{os.getenv('DATABRICKS_WAREHOUSE_ID')}",
        credentials_provider=lambda: cfg.authenticate
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall_arrow().to_pandas()
```

**UI Elements:**
- Text input for table name (default: value from `config.yaml`)
- "Test Connection" button
- On click: run `SELECT COUNT(*) FROM {table}` and display result
- Show success/error message with row count

**Expected Result:** A working connectivity test page that confirms access to Unity Catalog tables.

