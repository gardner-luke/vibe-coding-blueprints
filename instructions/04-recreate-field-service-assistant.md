# Create a Wind Farm Operations Dashboard UI

**Goal**  
Design a single-page dashboard interface for "Cool Electric Co." showing operational metrics and analytics for a wind farm monitoring system. The interface should display real-time power generation data, turbine health status, and AI-powered insights.

**Layout & Structure**  
- Clean, card-based design with blue accent colors (#0066CC)
- White background with light gray borders (#E0E0E0) 
- Professional, enterprise-style interface
- Responsive grid layout

**Top Navigation Bar**
- Company name "Cool Electric Co." centered in blue
- "Open AI Assistant" button on the left with robot icon
- Home icon and user avatar on the right

**Key Metrics Row (4 cards)**
Display these metrics in horizontally-aligned cards with large, bold numbers:
- Devices under Management: 6
- Maintenance Required: 1  
- Healthy Turbine %: 83.33%
- Current Device Energy Production: 73.01 MWH/hr

**Main Content Area (2 columns)**

Left Column - "GenAI Summary" Panel:
- Header with sparkles icon
- "Power output analysis" section with magnifying glass icon
  - Warning indicator: "Drop in overall output from 21:00 (last night) to now"
  - Status indicator: "Power output is stable at ~75 MW post-drop"
- "Turbine analysis" section with magnifying glass icon
  - Red alert: "A1234 shut off at 21:00"
  - Yellow warning: "C7890 requires verification of binding device"
- Orange "Continue the conversation" button with chat icon at bottom

Right Column - "Total Power Output (Past 24 Hours)" Chart:
- Line graph with dual lines:
  - Blue line for "Real Output" 
  - Green line for "Expectation"
- Y-axis: Power Output (MW) from 0-100
- X-axis: Time from Nov 5, 2025 06:00 to Nov 6, 2025 06:00
- Show notable drop in blue line around midnight to ~75 MW
- Grid lines and clean axis labels

**Bottom Section - "Map of Turbines"**
- Interactive map showing offshore location near Nantucket
- Ocean blue background color
- Green location pin marker for turbine farm
- Zoom in/out controls (+/-) in top left
- Map should show coastline and water

**Visual Style Guidelines**
- Use clean, modern sans-serif font (like Inter or Segoe UI)
- Subtle shadows on cards (box-shadow: 0 2px 4px rgba(0,0,0,0.1))
- Rounded corners on cards (border-radius: 8px)
- Consistent spacing and padding
- Professional color scheme: blues, grays, with red/yellow for alerts

**Deliverable**
A polished, professional dashboard interface that clearly displays wind farm operational data with AI-powered insights, suitable for energy sector operations monitoring.