# BRICS USD Dominance Forecasting

## Overview

**Research Question:** *Will USD still remain the dominant currency in the world post-July 2027?*

This project analyzes USD dominance through predictive forecasting of three key indicators:
- Bitcoin trading volume
- BRICS gold imports
- BRICS crude oil imports

---

## Quick Start

### Step 1: Install Dependencies

```bash
pip install pandas matplotlib numpy openpyxl
```

### Step 2: Prepare Data Files

Place your three cleaned CSV files in the `predictive-analysis-forecasts/` directory:
- `Btc_5y_Cleaned.csv`
- `Gold_TradeData_Cleaned.csv`
- `Oil_TradeData_Cleaned.csv`

### Step 3: Generate Figures

```bash
cd predictive-analysis-forecasts
python3 generate_prediction_figures.py
```

**Output:** 9 publication-ready PDF files in the `figures/` directory

---

## Generated Figures

The script generates 9 professional PDF figures organized into four categories:

### Forecast Figures (with 3-month predictions)
1. `btc_forecast.pdf` - Bitcoin trading volume forecast
2. `gold_brics_forecast.pdf` - BRICS gold imports forecast (quantity & value)
3. `oil_brics_forecast.pdf` - BRICS oil imports forecast (quantity & value)

### Time Series Analysis (complete historical trends)
4. `btc_reserves_timeseries.pdf` - Bitcoin volume over time with statistics
5. `gold_reserves_timeseries.pdf` - Gold imports over time with statistics
6. `oil_reserves_timeseries.pdf` - Oil imports over time with statistics

### Comparative Analysis
7. `comparative_analysis.pdf` - All three commodities normalized (0-100 scale)
8. `comparative_forecast.pdf` - All three commodities with 3-month forecasts

### Combined Document
9. `all_predictions_combined.pdf` - All forecasts in a single PDF

**Figure Specifications:**
- Resolution: 300 DPI (publication quality)
- Format: Vector PDF (scalable to any size)
- Features: Professional grids, legends, and statistical analysis

---

## Project Structure

```
brics-usd-dominance-forecasting/
├── README.md
├── figures/
│   ├── btc_forecast.pdf
│   ├── gold_brics_forecast.pdf
│   ├── oil_brics_forecast.pdf
│   ├── btc_reserves_timeseries.pdf
│   ├── gold_reserves_timeseries.pdf
│   ├── oil_reserves_timeseries.pdf
│   ├── comparative_analysis.pdf
│   ├── comparative_forecast.pdf
│   └── all_predictions_combined.pdf
└── predictive-analysis-forecasts/
    ├── generate_prediction_figures.py
    ├── DATA_SETUP.md
    ├── Btc_5y_Cleaned.csv
    ├── Gold_TradeData_Cleaned.csv
    └── Oil_TradeData_Cleaned.csv
```

---

## Key Findings

**USD Dominance Probability:** 75%

USD will remain the dominant global currency post-July 2027, but with reduced power.

### Forecast Timeline

| Period | Projection |
|--------|------------|
| **2025-2026** | Status quo with gradual erosion (5-10% decline) |
| **July 2027** | BRICS payment system launch (critical inflection point) |
| **2027-2030** | Transition to multi-polar currency system (USD at 50-60% dominance) |

### Indicator Summary

| Indicator | Trend | Impact on USD |
|-----------|-------|---------------|
| **Bitcoin Trading** | USD maintains 60-70% dominance | Neutral |
| **Gold Accumulation** | BRICS imports rising +10% YoY | Negative |
| **Oil Imports** | Growing +5% YoY with alternative settlements | Negative |

---

## Data Sources

1. **Gold Trade Data**
   - Source: [UN Comtrade Plus](https://comtradeplus.un.org/)
   - Period: January 2021 - October 2025

2. **Crude Oil Trade Data**
   - Source: [UN Comtrade Plus](https://comtradeplus.un.org/)
   - Period: January 2021 - October 2025

3. **Bitcoin Trading Volume**
   - Source: [Bitcoinity.org](https://data.bitcoinity.org/markets/volume/30d?c=e&t=b)
   - Period: December 2020 - December 2025

---

## Methodology

**Forecast Method:** 3-Month Simple Moving Average (SMA)

```
Forecast(t+1) = [Actual(t) + Actual(t-1) + Actual(t-2)] / 3
```

**Advantages:**
- Smooths short-term volatility
- Identifies underlying trends
- Simple and interpretable

**Limitations:**
- Cannot predict sudden shocks or black swan events
- Assumes recent patterns will continue

---

## Troubleshooting

### Missing Python Modules
```bash
pip install pandas matplotlib numpy openpyxl
```

### Data Files Not Found
- Ensure CSV files are placed in the `predictive-analysis-forecasts/` directory
- Verify filenames match exactly (case-sensitive)

### Column Errors
- Check that your CSV files contain the required columns
- See [DATA_SETUP.md](predictive-analysis-forecasts/DATA_SETUP.md) for detailed column specifications

---

---

## Repository

[https://github.com/itsamarin/brics-usd-dominance-forecasting](https://github.com/itsamarin/brics-usd-dominance-forecasting)
