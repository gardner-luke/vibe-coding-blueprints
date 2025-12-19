# ⚡ Step 6: Connect to Live Data

**Goal:** Replace all mock data with live Databricks queries.

---

**Configuration (at top of `app.py`, keep existing constants from Step 5):**

The configuration constants should already exist from Step 5. Keep them as-is:

```python
# Databricks Configuration (from config.yaml)
CATALOG = "..."  # Value from config.yaml
SCHEMA = "..."   # Value from config.yaml
WAREHOUSE_ID = "..."  # Value from config.yaml
METADATA_TABLE = "..."  # Value from config.yaml (tables.metadata)
TELEMETRY_TABLE = "..."  # Value from config.yaml (tables.telemetry)
```

**IMPORTANT:** Do NOT import yaml or read config.yaml at runtime. These values should be hardcoded constants that were read from `../config.yaml` during the build process and embedded directly into the app code.

---

**Tables:**

- `turbines_metadata` (use `METADATA_TABLE` constant) — `turbine_id, latitude, longitude, model, status, last_maintenance`
- `turbine_telemetry` (use `TELEMETRY_TABLE` constant) — `timestamp, turbine_id, power_output_mw, expected_output_mw, wind_speed_mps, vibration_level`

---

**Create cached query functions with `@st.cache_data(ttl=60)`:**

Use the `quote_identifier()` helper function (already defined in Step 5) to wrap identifiers that may contain dashes.

1. `get_turbines_metadata()` — `SELECT * FROM {quote_identifier(CATALOG)}.{quote_identifier(SCHEMA)}.{quote_identifier(METADATA_TABLE)}`

2. `get_telemetry()` — `SELECT timestamp, turbine_id, power_output_mw, expected_output_mw FROM {quote_identifier(CATALOG)}.{quote_identifier(SCHEMA)}.{quote_identifier(TELEMETRY_TABLE)} ORDER BY timestamp`
   - **Important:** Convert timestamp with `df['timestamp'] = pd.to_datetime(df['timestamp'])`

3. `get_kpis()` — Returns dict with:
   - `total_devices` = `COUNT(DISTINCT turbine_id)` from METADATA_TABLE
   - `maintenance_required` = `COUNT WHERE status IN ('Error', 'Warning')` from METADATA_TABLE
   - `healthy_pct` = `100 * COUNT(status='Active') / total` from METADATA_TABLE
   - `current_output` = `SUM` of latest `power_output_mw` per turbine from TELEMETRY_TABLE (use `ROW_NUMBER()` window function)

---

**Update Chart:**
- Group telemetry by timestamp, SUM `power_output_mw` and `expected_output_mw`
- **Sort by timestamp** before plotting
- Plot as two lines: Real Output (purple) and Expectation (green dashed)

---

**Update Map:**
- Use `latitude`/`longitude` from metadata
- Color by status: Active=green, Warning=yellow, Error=red

---

**Update GenAI Summary:**
- Pull actual turbine IDs from metadata for error/warning turbines
- Keep static analysis text

---

**Error handling:** Wrap data loading in try/except, show `st.error()` if connection fails.
