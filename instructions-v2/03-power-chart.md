# 📈 Step 3: Power Output Chart

**Goal:** Add a line chart showing power output over the past 24 hours.

**Add to `app.py`:**

Create a Plotly line chart titled "Total Power Output (Past 24 Hours)" with:

**Two lines:**
- **Real Output** (blue/purple) - Actual power readings
- **Expectation** (green) - Expected power output

**Mock data pattern:**
- X-axis: timestamps over 24 hours (hourly intervals)
- Y-axis: Power Output (MW), range 0-100
- Real output should hover around 90 MW, then drop to ~75 MW around midnight
- Expectation stays steady around 90 MW

**Chart styling:**
- White background with card styling (border, shadow, rounded corners)
- Grid lines visible
- Legend showing both series

**Layout:** Place in the right column (we'll add the GenAI summary to the left column next).

**Expected Result:** A professional line chart showing the power drop pattern visible in the reference.

