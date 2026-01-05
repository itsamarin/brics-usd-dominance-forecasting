# BRICS USD Dominance Forecasting

**Research Question:** *"Will USD still remain the dominant currency in the world post-July 2027?"*

This project analyzes USD dominance through predictive forecasting of Bitcoin trading volume, BRICS gold imports, and BRICS crude oil imports.

## 🚀 Quick Start - Generate Figures

### 1. Install Dependencies

```bash
pip install pandas matplotlib numpy openpyxl
```

### 2. Add Your Data Files

Place your 3 cleaned CSV files in `predictive-analysis-forecasts/`:
- `Btc_5y_Cleaned.csv`
- `Gold_TradeData_Cleaned.csv`
- `Oil_TradeData_Cleaned.csv`

### 3. Generate All Figures

```bash
cd predictive-analysis-forecasts
python3 generate_prediction_figures.py
```

**Output:** 9 PDF files in `figures/` directory (ready for publication)

## 📊 Generated Figures (9 PDFs)

### Forecast Figures (with 3-month predictions)
1. **btc_forecast.pdf** - Bitcoin trading volume + forecast
2. **gold_brics_forecast.pdf** - Gold imports + forecast (2 charts)
3. **oil_brics_forecast.pdf** - Oil imports + forecast (2 charts)

### Time Series Figures (complete historical analysis)
4. **btc_reserves_timeseries.pdf** - BTC over time with statistics
5. **gold_reserves_timeseries.pdf** - Gold over time with statistics
6. **oil_reserves_timeseries.pdf** - Oil over time with statistics

### Comparative Analysis
7. **comparative_analysis.pdf** - All 3 commodities normalized together
8. **comparative_forecast.pdf** - All 3 commodities with 3-month forecasts

### Combined Document
9. **all_predictions_combined.pdf** - All forecasts in one PDF

All figures include:
- ✓ 300 DPI publication quality
- ✓ Professional formatting with grids and legends
- ✓ Statistical analysis (mean, std dev, trends)
- ✓ Vector PDFs (scale to any size)

## 📁 Project Structure

```
brics-usd-dominance-forecasting/
├── README.md                                    # This file
├── figures/                                     # Generated PDFs (output)
│   ├── btc_forecast.pdf
│   ├── gold_brics_forecast.pdf
│   ├── oil_brics_forecast.pdf
│   ├── btc_reserves_timeseries.pdf
│   ├── gold_reserves_timeseries.pdf
│   ├── oil_reserves_timeseries.pdf
│   ├── comparative_analysis.pdf
│   └── all_predictions_combined.pdf
└── predictive-analysis-forecasts/              # Analysis scripts
    ├── generate_prediction_figures.py          # Main script
    ├── Btc_5y_Cleaned.csv                      # Your data (add here)
    ├── Gold_TradeData_Cleaned.csv              # Your data (add here)
    └── Oil_TradeData_Cleaned.csv               # Your data (add here)
```

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

## 🔧 Troubleshooting

**Missing modules:**
```bash
pip install pandas matplotlib numpy openpyxl
```

**Data files not found:**
- Place CSV files in `predictive-analysis-forecasts/` directory
- Check filenames match exactly (case-sensitive)

**Column errors:**
- Verify your CSV files have required columns (see [DATA_SETUP.md](predictive-analysis-forecasts/DATA_SETUP.md))

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
