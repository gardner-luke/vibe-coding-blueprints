# ⚡ Step 6: Connect to Live Data

**Goal:** Replace all mock data with live Databricks queries.

**Use values from `config.yaml` for catalog, schema, and warehouse_id.**

---

**Tables:**

**`turbines_metadata`** — turbine info and status
```
turbine_id, latitude, longitude, model, status, last_maintenance
```

**`turbine_telemetry`** — time-series power data
```
timestamp, turbine_id, power_output_mw, expected_output_mw, wind_speed_mps, vibration_level
```

---

**Update KPIs (from `turbines_metadata`):**
- **Devices under Management** = COUNT(DISTINCT turbine_id)
- **Maintenance Required** = COUNT WHERE status IN ('Error', 'Warning')
- **Healthy Turbine %** = (COUNT WHERE status = 'Active') / total * 100
- **Current Energy Production** = SUM of latest power_output_mw from telemetry

---

**Update Chart (from `turbine_telemetry`):**
- Query last 24 hours of data
- Group by timestamp, SUM power_output_mw as "Real Output"
- Group by timestamp, SUM expected_output_mw as "Expectation"

---

**Update Map (from `turbines_metadata`):**
- Plot each turbine using latitude/longitude
- Color markers by status: Active=green, Warning=yellow, Error=red

---

**Update GenAI Summary:**
- Keep the static text for now (GenAI integration is a future step)
- Update turbine IDs to match actual data

---

**Add caching:** Use `@st.cache_data(ttl=60)` on query functions.

**Expected Result:** A fully live dashboard pulling real data from Databricks Unity Catalog.

