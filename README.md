# BRICS USD Dominance Forecasting

**Research Question:** *"Will USD still remain the dominant currency in the world post-July 2027?"*

This project analyzes USD dominance through predictive forecasting of Bitcoin trading volume, BRICS gold imports, and BRICS crude oil imports using 3-month moving averages.

## Quick Start - Generate Figures

### Prerequisites
- Python 3.8+
- Your data files: `Btc_5y_Cleaned.csv`, `Gold_TradeData_Cleaned.csv`, `Oil_TradeData_Cleaned.csv`

### Installation

```bash
# Navigate to the analysis directory
cd predictive-analysis-forecasts

# Install dependencies
pip install -r requirements.txt
```

### Generate All Figures

```bash
# Step 1: Generate forecasts and Excel workbook
python predictive_analysis_forecast.py

# Step 2: Add professional charts/figures
python add_charts_to_forecasts.py

# Output: Predictive_Analysis_Forecasts_with_Charts.xlsx
```

## What You'll Get

The analysis produces **5 professional figures** in an Excel workbook:

1. **Bitcoin USD Trading Volume Chart**
   - Historical trends (2020-2025)
   - 3-month moving average
   - Q1 2026 forecast

2. **BRICS Gold Imports - Quantity Chart**
   - Import volumes (kg) across BRICS nations
   - Central bank accumulation patterns

3. **BRICS Gold Imports - Value Chart**
   - Import values (USD) showing investment scale
   - De-dollarization indicators

4. **BRICS Crude Oil Imports - Quantity Chart**
   - Energy security patterns
   - Import volumes across BRICS

5. **BRICS Crude Oil Imports - Value Chart**
   - Energy expenditure trends
   - Alternative settlement currency analysis

All charts include:
- ✓ Historical data (solid lines)
- ✓ 3-month moving averages (smoothed trends)
- ✓ 3-month forecasts (dashed projection lines)

## File Structure

```
brics-usd-dominance-forecasting/
├── README.md                                    # This file
├── predictive-analysis-forecasts/              # Main analysis directory
│   ├── predictive_analysis_forecast.py         # Core forecasting script
│   ├── add_charts_to_forecasts.py              # Chart generation script
│   ├── recalc.py                               # Excel formula recalculation
│   ├── requirements.txt                        # Python dependencies
│   ├── README.md                               # Detailed documentation
│   ├── QUICKSTART.md                           # 5-minute setup guide
│   ├── CHARTS_GUIDE.md                         # Chart specifications
│   └── [Your CSV data files]                   # Place here
└── Predictive_Analysis_Forecasts_with_Charts.xlsx  # Final output
```

## Detailed Documentation

For more information, see the comprehensive guides in [predictive-analysis-forecasts/](predictive-analysis-forecasts/):

- [README.md](predictive-analysis-forecasts/README.md) - Full project documentation
- [QUICKSTART.md](predictive-analysis-forecasts/QUICKSTART.md) - 5-minute beginner guide
- [CHARTS_GUIDE.md](predictive-analysis-forecasts/CHARTS_GUIDE.md) - Chart specifications and customization
- [USAGE.md](predictive-analysis-forecasts/USAGE.md) - Advanced usage and customization
- [SETUP_GUIDE.md](predictive-analysis-forecasts/SETUP_GUIDE.md) - Detailed installation instructions

## Key Findings

**USD Dominance Probability: 75%** - USD will remain dominant post-July 2027, but with reduced power.

### Timeline Forecast
- **2025-2026:** Status quo with gradual erosion (5-10%)
- **July 2027:** BRICS payment system launch (critical inflection point)
- **2027-2030:** Transition to multi-polar currency system (USD at 50-60%)

### Indicator Summary
- **Bitcoin Trading:** USD maintains 60-70% dominance (Neutral)
- **Gold Accumulation:** BRICS imports rising +10% YoY (Negative for USD)
- **Oil Imports:** Growing +5% YoY with alternative settlements (Negative for USD)

## Data Sources

1. **Bitcoin Trading Volume** - [Bitcoinity.org](https://data.bitcoinity.org/markets/volume/30d?c=e&t=b) (Dec 2020 - Dec 2025)
2. **Gold Trade Data** - [UN Comtrade Plus](https://comtradeplus.un.org/) (Jan 2021 - Oct 2025)
3. **Crude Oil Trade Data** - [UN Comtrade Plus](https://comtradeplus.un.org/) (Jan 2021 - Oct 2025)

## Methodology

**3-Month Simple Moving Average (SMA) Forecast:**

```
Forecast(t+1) = [Actual(t) + Actual(t-1) + Actual(t-2)] / 3
```

This approach:
- ✓ Smooths short-term volatility
- ✓ Identifies underlying trends
- ✓ Simple and interpretable
- ⚠ Cannot predict sudden shocks
- ⚠ Assumes recent patterns continue

## Troubleshooting

**Missing modules:**
```bash
pip install pandas openpyxl numpy
```

**Data files not found:**
Ensure your CSV files are in the `predictive-analysis-forecasts/` directory.

**Charts not displaying:**
Open the Excel file in Microsoft Excel 2016+ or LibreOffice (Google Sheets may not display charts properly).

## Academic Context

**Course:** Oil, Gold, and Crypto: How Global Tensions are linked to Commodities
**Institution:** University of Europe & Avron Global Consultancy Initiative
**Semester:** Winter 2025
**Section:** D - Predictive Analysis

## License

This project is part of an academic case study for educational purposes.

## Contact

Project Repository: [https://github.com/itsamarin/brics-usd-dominance-forecasting](https://github.com/itsamarin/brics-usd-dominance-forecasting)

---

**Last Updated:** December 31, 2025
