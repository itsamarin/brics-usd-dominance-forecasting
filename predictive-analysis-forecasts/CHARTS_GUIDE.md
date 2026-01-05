# Charts and Visualizations Guide

## Overview

The predictive analysis workbook includes **5 professional charts** that visualize historical data, moving averages, and forecasts across BTC, Gold, and Oil markets.

## Chart Types and Locations

### 1. **BTC Forecast Sheet - Trading Volume Chart**

**Location:** BTC_Forecast sheet, columns H-T

**Chart Type:** Multi-series Line Chart

**Data Visualized:**
-  **Blue Line**: Actual Bitcoin USD trading volume (historical)
-  **Green Line**: 3-month moving average (smoothed trend)
-  **Red Dashed Line**: 3-month forecast (predicted values)

**Purpose:** Shows Bitcoin trading volume trends and helps identify whether USD dominance in crypto markets is stable or declining.

**Key Insights to Look For:**
- Upward trend = Growing BTC adoption
- Stable USD volume = USD maintains crypto gateway position
- Forecast divergence = Potential market shift

---

### 2. **Gold BRICS Forecast - Quantity Chart**

**Location:** Gold_BRICS_Forecast sheet, columns I-U (top)

**Chart Type:** Line Chart

**Data Visualized:**
-  **Gold Line**: Actual BRICS gold imports in kg (historical)
-  **Red Dashed Line**: 3-month MA forecast (predicted quantities)

**Purpose:** Tracks central bank gold accumulation by BRICS nations as a hedge against USD.

**Key Insights to Look For:**
- Rising trend = De-dollarization strategy
- Accelerating accumulation = Reduced confidence in USD
- High forecasts = Continued diversification

---

### 3. **Gold BRICS Forecast - Value Chart**

**Location:** Gold_BRICS_Forecast sheet, columns I-U (bottom)

**Chart Type:** Line Chart

**Data Visualized:**
-  **Gold Line**: Actual BRICS gold import value in USD (historical)
-  **Red Dashed Line**: 3-month MA forecast (predicted values)

**Purpose:** Shows the monetary value of gold accumulation and investment scale.

**Key Insights to Look For:**
- Value vs. quantity ratio = Price trends
- Large value increases = Strategic positioning
- Forecast vs. actual = Market expectations

---

### 4. **Oil BRICS Forecast - Quantity Chart**

**Location:** Oil_BRICS_Forecast sheet, columns I-U (top)

**Chart Type:** Line Chart

**Data Visualized:**
-  **Black Line**: Actual BRICS crude oil imports in kg (historical)
-  **Red Dashed Line**: 3-month MA forecast (predicted quantities)

**Purpose:** Tracks energy security and consumption patterns in BRICS economies.

**Key Insights to Look For:**
- Growing demand = Economic expansion
- Stable imports = Energy security maintained
- Seasonal patterns = Normal vs. abnormal demand

---

### 5. **Oil BRICS Forecast - Value Chart**

**Location:** Oil_BRICS_Forecast sheet, columns I-U (bottom)

**Chart Type:** Line Chart

**Data Visualized:**
-  **Black Line**: Actual BRICS crude oil import value in USD (historical)
-  **Red Dashed Line**: 3-month MA forecast (predicted values)

**Purpose:** Shows energy expenditure and potential for non-USD settlements.

**Key Insights to Look For:**
- Value spikes = Oil price volatility
- Consistent high values = Strategic stockpiling
- Currency settlement patterns = De-dollarization in energy

---

## How to Generate Charts

### Method 1: Generate All-in-One (Recommended)

Run both scripts in sequence:

```bash
# Step 1: Generate base forecasts
python predictive_analysis_forecast.py

# Step 2: Add charts
python add_charts_to_forecasts.py
```

**Output:** `Predictive_Analysis_Forecasts_with_Charts.xlsx`

### Method 2: Custom Chart Generation

Generate charts for existing workbook:

```bash
# Use custom file names
python add_charts_to_forecasts.py input.xlsx output.xlsx

# Example:
python add_charts_to_forecasts.py MyForecasts.xlsx MyForecasts_Charts.xlsx
```

### Method 3: Manual Chart Creation (Excel)

If scripts fail, create charts manually:

1. Open Excel file
2. Select data range (e.g., C6:C30 for actuals)
3. Insert  Chart  Line Chart
4. Add additional series (MA, Forecast)
5. Format lines (colors, dash styles)
6. Add titles and axis labels

---

## Chart Customization

### Changing Chart Colors

Edit `add_charts_to_forecasts.py`:

```python
# Change BTC chart colors
chart.series[0].graphicalProperties.line.solidFill = "YOUR_COLOR"  # Hex code

# Common colors:
# Blue: "4472C4"
# Green: "70AD47"
# Red: "FF0000"
# Gold: "FFC000"
# Black: "000000"
```

### Changing Chart Size

```python
# Adjust chart dimensions
chart.height = 10  # Change to desired height
chart.width = 20   # Change to desired width
```

### Changing Chart Position

```python
# Move chart location
ws.add_chart(chart, "H5")  # Change cell reference (e.g., "A10")
```

### Adding More Chart Types

```python
from openpyxl.chart import BarChart, ScatterChart

# Create bar chart instead
chart = BarChart()
# ... configure bar chart
```

---

## Chart Interpretation Guide

### Reading Forecast Charts

**Solid Lines = Historical Data (Actual)**
- Shows what actually happened
- Real market data
- Used to calculate trends

**Dashed Lines = Forecast (Predicted)**
- Shows predicted future values
- Based on 3-month moving average
- Assumes recent trends continue

**Green/Red Colors:**
- Green = Moving average (smoothed trend)
- Red = Forecast (future prediction)

### Analyzing Trends

**Upward Trend:**
- Market growing
- Increasing demand
- Potential bullish signal

**Downward Trend:**
- Market contracting
- Decreasing demand
- Potential bearish signal

**Flat/Stable Trend:**
- Market equilibrium
- Consistent demand
- Status quo maintained

**Volatility:**
- High variance = Uncertain market
- Low variance = Stable conditions
- Spikes = Exceptional events

---

## Common Chart Issues

### Issue: Charts Not Displaying

**Causes:**
- File opened in Google Sheets (limited chart support)
- Corrupted workbook
- Excel compatibility mode

**Solutions:**
1. Open in desktop Excel or LibreOffice Calc
2. Re-run chart generation script
3. Use "Open and Repair" in Excel

### Issue: Chart Data Wrong

**Causes:**
- Incorrect data ranges
- Missing formulas
- Data not recalculated

**Solutions:**
1. Run `python recalc.py filename.xlsx`
2. Check data ranges in chart settings
3. Verify source data columns

### Issue: Chart Formatting Lost

**Causes:**
- File format conversion
- Excel version incompatibility

**Solutions:**
1. Save as .xlsx (not .xls)
2. Don't open in Google Sheets
3. Use Excel 2016 or later

---

## Exporting Charts

### Export as Images

**In Excel:**
1. Right-click chart
2. "Save as Picture"
3. Choose format (PNG recommended)

**In LibreOffice:**
1. Right-click chart
2. "Export as Image"
3. Save as PNG/SVG

### Export for Presentations

**PowerPoint:**
1. Copy chart (Ctrl+C)
2. Paste in PowerPoint (Ctrl+V)
3. Chart remains editable

**PDF:**
1. File  Save As  PDF
2. Charts embedded in PDF
3. High-quality printing

### Export Data

**CSV Export:**
```python
# Export chart data
import pandas as pd
df = pd.read_excel('Forecasts.xlsx', sheet_name='BTC_Forecast')
df.to_csv('btc_chart_data.csv', index=False)
```

---

## Best Practices

### For Presentations

1. **Use consistent colors** across all charts
2. **Add clear titles** explaining what's shown
3. **Label axes** with units (BTC, kg, USD)
4. **Highlight forecast periods** to distinguish predictions
5. **Add data labels** for key points

### For Reports

1. **Reference charts** in text ("See Figure 1")
2. **Explain trends** observed in charts
3. **Compare charts** across commodities
4. **Note limitations** of forecasts

### For Analysis

1. **Check forecast accuracy** against actual values later
2. **Compare MA periods** (3-month vs 6-month)
3. **Look for patterns** across BTC, Gold, Oil
4. **Correlate with events** (policy changes, market news)

---

## Advanced Visualization

### Combining Charts

Create comparison charts in Excel:

1. Create new sheet "Comparison"
2. Pull data from multiple sheets
3. Create multi-commodity chart
4. Compare USD dominance across markets

### Interactive Dashboards

Use Excel features:

1. **Slicers**: Filter data by date/country
2. **Pivot Charts**: Dynamic aggregations
3. **Conditional Formatting**: Highlight trends
4. **Sparklines**: Mini in-cell charts

### Python Visualization (Alternative)

For custom analysis:

```python
import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_excel('Forecasts.xlsx', sheet_name='BTC_Forecast')

# Create plot
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Actual BTC Volume'], label='Actual')
plt.plot(df['Date'], df['3-Month MA'], label='3-MA')
plt.plot(df['Date'], df['Forecast'], '--', label='Forecast')
plt.legend()
plt.title('Bitcoin USD Trading Volume Forecast')
plt.xlabel('Date')
plt.ylabel('Volume (BTC)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('btc_forecast.png', dpi=300)
plt.show()
```

---

## Summary

**5 Charts Created:**
1. BTC Trading Volume (1 chart)
2. Gold BRICS Quantity (1 chart)
3. Gold BRICS Value (1 chart)
4. Oil BRICS Quantity (1 chart)
5. Oil BRICS Value (1 chart)

**All charts include:**
-  Historical actual data
-  3-month moving averages
-  3-month forecasts
-  Professional styling
-  Clear labels and titles

**Use these charts to:**
-  Visualize trends and patterns
-  Communicate forecasts clearly
- 📉 Identify market shifts
-  Support investment decisions

---

**Questions?** Check USAGE.md or open an issue on GitHub!
