# Project Summary

## What This Does

Generates 8 publication-quality PDF figures analyzing USD dominance through Bitcoin trading, BRICS gold imports, and BRICS oil imports.

## Usage (3 Steps)

### 1. Install
```bash
pip install pandas matplotlib numpy openpyxl
```

### 2. Add Data
Place your 3 CSV files in `predictive-analysis-forecasts/`:
- Btc_5y_Cleaned.csv
- Gold_TradeData_Cleaned.csv
- Oil_TradeData_Cleaned.csv

### 3. Run
```bash
cd predictive-analysis-forecasts
python3 generate_prediction_figures.py
```

## Output

8 PDFs in `figures/` directory:
1. btc_forecast.pdf
2. gold_brics_forecast.pdf
3. oil_brics_forecast.pdf
4. btc_reserves_timeseries.pdf
5. gold_reserves_timeseries.pdf
6. oil_reserves_timeseries.pdf
7. comparative_analysis.pdf
8. all_predictions_combined.pdf

All figures are:
- 300 DPI publication quality
- Vector PDFs (scale to any size)
- Professional formatting
- Ready for papers/presentations

## Files

- **README.md** - Main documentation
- **figures/README.md** - Figure descriptions
- **predictive-analysis-forecasts/DATA_SETUP.md** - Data requirements
- **predictive-analysis-forecasts/generate_prediction_figures.py** - Main script

That's it!
