# Quick Start Guide

Get your prediction figures generated in 3 easy steps!

## Step 1: Add Your Data Files

Place your 3 cleaned CSV files in the `predictive-analysis-forecasts/` directory:

```bash
cd predictive-analysis-forecasts
```

Required files:
- `Btc_5y_Cleaned.csv` - Bitcoin trading data
- `Gold_TradeData_Cleaned.csv` - Gold import data
- `Oil_TradeData_Cleaned.csv` - Oil import data

See [DATA_SETUP.md](predictive-analysis-forecasts/DATA_SETUP.md) for column requirements.

## Step 2: Run the Script

```bash
python3 generate_prediction_figures.py
```

Or if `python` points to Python 3:
```bash
python generate_prediction_figures.py
```

## Step 3: Find Your Figures

All 8 PDF files will be in the `figures/` directory:

```
figures/
├── btc_forecast.pdf
├── gold_brics_forecast.pdf
├── oil_brics_forecast.pdf
├── btc_reserves_timeseries.pdf
├── gold_reserves_timeseries.pdf
├── oil_reserves_timeseries.pdf
├── comparative_analysis.pdf
└── all_predictions_combined.pdf
```

## What Each Figure Shows

| Figure | What It Shows | Use For |
|--------|---------------|---------|
| **btc_forecast.pdf** | BTC trading + 3-month forecast | Short-term BTC predictions |
| **gold_brics_forecast.pdf** | Gold imports + 3-month forecast | Gold accumulation trends |
| **oil_brics_forecast.pdf** | Oil imports + 3-month forecast | Energy security patterns |
| **btc_reserves_timeseries.pdf** | Complete BTC history + stats | Long-term BTC analysis |
| **gold_reserves_timeseries.pdf** | Complete Gold history + stats | De-dollarization evidence |
| **oil_reserves_timeseries.pdf** | Complete Oil history + stats | Energy dependency trends |
| **comparative_analysis.pdf** | All 3 normalized together | Cross-commodity comparison |
| **all_predictions_combined.pdf** | All forecasts in one PDF | Presentations/printing |

## Troubleshooting

**Files not found error?**
- Make sure CSV files are in `predictive-analysis-forecasts/` directory
- Check filenames match exactly (case-sensitive)

**Column errors?**
- Verify your CSV files have the required columns
- See [DATA_SETUP.md](predictive-analysis-forecasts/DATA_SETUP.md)

**Import errors?**
- Install required packages: `pip install pandas matplotlib numpy openpyxl`

## Need More Help?

- **Complete guide**: [FIGURES_GUIDE.md](FIGURES_GUIDE.md)
- **Figure details**: [figures/README.md](figures/README.md)
- **Data requirements**: [predictive-analysis-forecasts/DATA_SETUP.md](predictive-analysis-forecasts/DATA_SETUP.md)
- **Project overview**: [README.md](README.md)

---

**That's it!** Once you add your data files and run the script, you'll have 8 publication-quality figures ready to use.
