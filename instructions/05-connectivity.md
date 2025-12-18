# 🔗 Step 5: Databricks Connection Test

**Goal:** Add a connection test section at the bottom of the dashboard.

**Add to top of `app.py` (after imports):**

Read values from `../config.yaml` and hardcode them as constants in app.py:

```python
CATALOG = "..."  # Replace with catalog value from config.yaml
SCHEMA = "..."   # Replace with schema value from config.yaml
WAREHOUSE_ID = "..."  # Replace with warehouse_id value from config.yaml
METADATA_TABLE = "..."  # Replace with tables.metadata value from config.yaml
TELEMETRY_TABLE = "..."  # Replace with tables.telemetry value from config.yaml

def quote_identifier(identifier):
    """Wrap identifier in backticks if it contains dashes or spaces"""
    if '-' in identifier or ' ' in identifier:
        return f"`{identifier}`"
    return identifier

default_warehouse_id = WAREHOUSE_ID
default_table_name = f"{quote_identifier(CATALOG)}.{quote_identifier(SCHEMA)}.{quote_identifier(METADATA_TABLE)}"
```

**Add to bottom of `app.py`:**

- Divider
- Header: "🔗 Databricks Connection Test"
- Text input for Warehouse ID with default value of default_warehouse_id
- Text input for Table Name with default value of default_table_name
- Button: "Test Connection"

**When button clicked:**
- Show spinner while connecting
- Use this connection pattern:
```python
from databricks.sdk.core import Config
from databricks import sql

cfg = Config()
http_path = f"/sql/1.0/warehouses/{warehouse_id}"
with sql.connect(server_hostname=cfg.host, http_path=http_path, 
                 credentials_provider=lambda: cfg.authenticate) as connection:
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT COUNT(*) as row_count FROM {table_name}")
        result = cursor.fetchall_arrow().to_pandas()
```
- Show green success with row count or red error message
