# Figures Directory

This directory contains all generated prediction figures.

## Generated Files (9 PDFs)

When you run `generate_prediction_figures.py`, these files are created:

### Forecast Figures
1. **btc_forecast.pdf** - Bitcoin USD trading forecast (1 chart)
2. **gold_brics_forecast.pdf** - BRICS gold imports forecast (2 charts: quantity & value)
3. **oil_brics_forecast.pdf** - BRICS oil imports forecast (2 charts: quantity & value)

### Time Series Figures
4. **btc_reserves_timeseries.pdf** - Complete BTC history + statistics
5. **gold_reserves_timeseries.pdf** - Complete gold history + statistics
6. **oil_reserves_timeseries.pdf** - Complete oil history + statistics

### Comparative Analysis
7. **comparative_analysis.pdf** - All 3 commodities normalized on one chart
8. **comparative_forecast.pdf** - All 3 commodities with 3-month forecasts (normalized)

### Combined Document
9. **all_predictions_combined.pdf** - All forecasts in single PDF

## Figure Features

- **Format:** PDF (vector graphics, publication-quality)
- **Resolution:** 300 DPI
- **Charts:** Professional with grids, legends, and statistics
- **Size:** 14" × 7" (single), 14" × 12" (dual charts), 16" × 8" (comparative)

## Usage

These figures are ready for:
- Academic papers and presentations
- Research reports
- Portfolio analysis
- Policy briefings

Simply insert the PDFs into your document or presentation software.

## How to Generate

From the `predictive-analysis-forecasts/` directory:

```bash
python3 generate_prediction_figures.py
```

All 8 PDFs will be automatically saved to this directory.
