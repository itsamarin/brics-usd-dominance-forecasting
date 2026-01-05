# Complete Figures Guide

This guide explains all the prediction figures available in this project.

## Quick Start

```bash
cd predictive-analysis-forecasts
python generate_prediction_figures.py
```

All figures will be saved to the `../figures/` directory.

## Generated Figures (8 total)

### 1️⃣ Forecast Figures (with predictions)

These show the last 24 months + 3-month forecasts using moving averages.

| File | Content | Charts |
|------|---------|--------|
| `btc_forecast.pdf` | Bitcoin USD trading volume forecast | 1 |
| `gold_brics_forecast.pdf` | BRICS gold imports forecast (quantity & value) | 2 |
| `oil_brics_forecast.pdf` | BRICS oil imports forecast (quantity & value) | 2 |

**Use for**: Short-term predictions, trend analysis, forecasting models

---

### 2️⃣ Time Series Figures (historical analysis)

These show complete historical data with statistical analysis.

| File | Content | Period |
|------|---------|--------|
| `btc_reserves_timeseries.pdf` | BTC USD trading volume over time | 2020-2025 |
| `gold_reserves_timeseries.pdf` | BRICS gold imports over time | 2021-2025 |
| `oil_reserves_timeseries.pdf` | BRICS oil imports over time | 2021-2025 |

**Each includes**:
- Complete historical data
- Statistical summary (mean, std dev)
- Trend indicator (Increasing/Decreasing)

**Use for**: Long-term pattern analysis, historical context, baseline establishment

---

### 3️⃣ Comparative Analysis

| File | Content | Purpose |
|------|---------|---------|
| `comparative_analysis.pdf` | All 3 commodities on normalized scale (0-100) | Direct comparison |

**Shows**:
- BTC trading (Blue line)
- Gold imports (Gold line)
- Oil imports (Black line)

**Use for**:
- Identifying correlations between commodities
- Understanding relative trends
- Spotting divergences and convergences
- Multi-factor analysis

---

### 4️⃣ Combined Document

| File | Content | Pages |
|------|---------|-------|
| `all_predictions_combined.pdf` | All forecast charts in one file | 3 |

**Use for**: Presentations, printing, easy sharing

---

## Visual Summary

```
Forecast Figures        Time Series Figures       Comparative
(3 files)              (3 files)                 (1 file)
─────────────          ──────────────            ────────────
📈 BTC Forecast        📊 BTC History            📊 All Together
📈 Gold Forecast       📊 Gold History           (normalized)
📈 Oil Forecast        📊 Oil History

                    +  Combined PDF (1 file)
                       ────────────────
                       📑 All Forecasts
```

---

## Understanding Each Figure Type

### Forecast Figures Explained

**What you see**:
- Solid blue/gold/black line: Actual historical data
- Solid green line: 3-month moving average (smoothed trend)
- Dashed red line: 3-month forecast (prediction)

**How to read**:
- If forecast line goes UP → Increasing trend expected
- If forecast line goes DOWN → Decreasing trend expected
- If forecast line is FLAT → Stable conditions expected

---

### Time Series Figures Explained

**What you see**:
- Single solid line showing all historical data
- Statistics box with:
  - Mean: Average value over entire period
  - Std Dev: How much variation exists
  - Trend: Overall direction (Increasing/Decreasing)

**How to read**:
- Upward slope → Growing reserves/activity
- Downward slope → Declining reserves/activity
- High volatility → Unstable market conditions
- Low volatility → Stable, predictable patterns

---

### Comparative Analysis Explained

**What you see**:
- Three lines on same chart (normalized to 0-100)
- Blue = BTC, Gold = Gold, Black = Oil

**How to read**:
- **Lines moving together** → Commodities responding to same economic factors
- **Lines diverging** → Different market dynamics at play
- **Gold rising alone** → Pure reserve diversification (de-dollarization)
- **All rising together** → Broad economic/geopolitical shift

**Key Patterns**:
- Gold ↑ + Oil stable → BRICS hedging against USD
- BTC stable + Gold ↑ → USD strong in crypto, weak in reserves
- All three ↑ → Major de-dollarization movement

---

## Using Figures in Your Work

### For Academic Papers
- **Introduction**: Use time series to show historical context
- **Methodology**: Reference forecast figures for your prediction model
- **Results**: Use comparative analysis to show relationships
- **Conclusion**: Include key forecast figure

### For Presentations
- **Opening**: Show comparative analysis (big picture)
- **Deep Dive**: Show individual time series for each commodity
- **Predictions**: Show forecast figures with your analysis
- **Summary**: Use combined PDF

### For Reports
- **Executive Summary**: Comparative analysis + key forecast
- **Detailed Analysis**: All time series figures
- **Forecasts**: All three forecast figures
- **Appendix**: Combined PDF for reference

---

## Technical Specifications

All figures are:
- **Format**: PDF (vector graphics, scalable)
- **Resolution**: 300 DPI (publication quality)
- **Size**: 14" × 7" (single charts), 14" × 12" (dual charts)
- **Colors**: Colorblind-friendly palette
- **Fonts**: Clear, readable, professional

---

## Interpretation Quick Reference

### BTC Figures
| Pattern | Meaning |
|---------|---------|
| Rising | USD dominance in crypto strong |
| Stable | USD maintains gateway position |
| Declining | Shift to other currencies beginning |

### Gold Figures
| Pattern | Meaning |
|---------|---------|
| Rising quickly | Active de-dollarization |
| Rising slowly | Gradual reserve diversification |
| Stable | Satisfied with current reserves |
| Declining | Selling reserves (rare, concerning) |

### Oil Figures
| Pattern | Meaning |
|---------|---------|
| Quantity ↑ | Growing energy demand |
| Value ↑ (more than qty) | Oil prices rising OR currency shift |
| Both stable | Balanced energy market |

---

## Next Steps

After generating figures:

1. **Review** each figure in the [figures/](figures/) directory
2. **Select** the most relevant ones for your use case
3. **Insert** into your document/presentation
4. **Cite** data sources (see main README.md)

---

## Questions?

- See [figures/README.md](figures/README.md) for detailed figure descriptions
- See main [README.md](README.md) for project overview
- Check [predictive-analysis-forecasts/](predictive-analysis-forecasts/) for script documentation

---

**Last Updated**: January 2026
