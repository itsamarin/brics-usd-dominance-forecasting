# Figures Directory

This directory contains all generated prediction figures for the BRICS USD Dominance Forecasting project.

## Generated Figures

When you run `generate_prediction_figures.py`, the following **8 PDF files** will be created here:

### Forecast Figures (with 3-month predictions)

1. **btc_forecast.pdf**
   - Bitcoin USD trading volume forecast
   - Single chart showing historical data, 3-month MA, and 3-month forecast
   - Analyzes USD dominance in cryptocurrency trading

2. **gold_brics_forecast.pdf**
   - BRICS gold imports forecast
   - Two charts: Quantity (kg) and Value (USD)
   - Shows de-dollarization trends through gold accumulation

3. **oil_brics_forecast.pdf**
   - BRICS crude oil imports forecast
   - Two charts: Quantity (kg) and Value (USD)
   - Indicates energy security and alternative settlement patterns

### Time Series Figures (historical trends)

4. **btc_reserves_timeseries.pdf**
   - Bitcoin USD trading volume over complete historical period (2020-2025)
   - Shows long-term trends with statistical analysis
   - Includes mean, standard deviation, and trend indicators

5. **gold_reserves_timeseries.pdf**
   - BRICS gold imports over time (2021-2025)
   - Central bank reserve accumulation patterns
   - Statistical analysis of gold hoarding behavior

6. **oil_reserves_timeseries.pdf**
   - BRICS crude oil imports over time (2021-2025)
   - Energy security and import dependency trends
   - Shows evolving energy trade patterns

### Comparative Analysis

7. **comparative_analysis.pdf**
   - All three commodities (BTC, Gold, Oil) on one chart
   - Normalized to 0-100 scale for direct comparison
   - Reveals correlations and divergences between indicators
   - Shows relative strength of de-dollarization signals

### Combined Document

8. **all_predictions_combined.pdf**
   - All forecasts in a single multi-page PDF
   - Convenient for presentations and sharing
   - Contains forecast charts only (3 pages)

## How to Generate

From the `predictive-analysis-forecasts/` directory:

```bash
python generate_prediction_figures.py
```

## Figure Specifications

- **Format:** PDF (vector graphics, publication-quality)
- **Resolution:** 300 DPI
- **Size:** 14" × 7" (single charts), 14" × 12" (dual charts)
- **Style:** Professional with grid, legends, and insights
- **Colors:**
  - Blue (#4472C4): Bitcoin actual data
  - Gold (#FFC000): Gold actual data
  - Black (#000000): Oil actual data
  - Green (#70AD47): 3-month moving averages
  - Red (#FF0000): 3-month forecasts (dashed lines)

## Chart Features

Each figure includes:
- ✓ Historical data points (solid lines with markers)
- ✓ 3-month moving averages (smoothed trend lines)
- ✓ 3-month forecasts (dashed projection lines)
- ✓ Date formatting (YYYY-MM)
- ✓ Grid for easy reading
- ✓ Legends and axis labels
- ✓ Key insights boxes (on some charts)

## Figure Descriptions

### What Each Figure Type Shows

**Forecast Figures** (1-3):
- Last 24 months of historical data
- 3-month moving averages to smooth volatility
- 3-month ahead predictions (dashed red lines)
- Best for short-term forecasting and trend analysis

**Time Series Figures** (4-6):
- Complete historical data available
- Statistical summaries (mean, standard deviation)
- Trend indicators (Increasing/Decreasing)
- Best for understanding long-term patterns

**Comparative Analysis** (7):
- All commodities normalized to same scale
- Enables direct visual comparison
- Shows which indicators move together
- Best for identifying correlations and causality

## Usage

These figures are designed for:
- Academic presentations and thesis defense
- Research papers and journal submissions
- Executive summaries for stakeholders
- Portfolio analysis reports for investors
- Policy briefings on de-dollarization trends
- Educational materials on commodity markets

All figures can be directly inserted into:
- LaTeX documents (PDF vector format)
- PowerPoint/Keynote presentations
- Google Slides or similar tools
- Printed reports (300 DPI high quality)

## Interpretation Guide

### BTC Figures
- **Rising trend**: USD maintains crypto trading dominance
- **Stable volume**: Confidence in USD as crypto gateway
- **Declining volume**: Potential shift to other currencies

### Gold Figures
- **Rising imports**: BRICS hedging against USD weakness
- **Accelerating accumulation**: Active de-dollarization
- **Stable/declining**: Satisfaction with current reserves

### Oil Figures
- **Rising imports**: Growing energy demand from BRICS
- **Stable value**: Consistent oil prices
- **Value > Quantity growth**: Increasing oil prices or currency shifts

### Comparative Chart
- **Parallel trends**: Commodities responding to same factors
- **Diverging trends**: Different market dynamics at play
- **Gold rising + Oil stable**: Pure reserve diversification
- **All rising**: Broad de-dollarization movement

## Last Updated

Generated: [Run date will appear in script output]
