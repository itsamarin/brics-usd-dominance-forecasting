# Data Setup Guide

Place your 3 cleaned CSV files in this directory before running the script.

## Required Files

```
predictive-analysis-forecasts/
├── Btc_5y_Cleaned.csv
├── Gold_TradeData_Cleaned.csv
└── Oil_TradeData_Cleaned.csv
```

## File Requirements

### Btc_5y_Cleaned.csv
Required columns:
- `Time` - Date/timestamp
- `USD` - USD trading volume (and other currency columns like EUR, GBP, etc.)

### Gold_TradeData_Cleaned.csv
Required columns:
- `refDate` - Reference date
- `reporterISO` - ISO country code (BRA, RUS, IND, CHN, ZAF)
- `flowDesc` - Flow description ('Import')
- `qty` - Quantity in kilograms
- `primaryValue` - Value in USD

### Oil_TradeData_Cleaned.csv
Required columns:
- `refDate` - Reference date
- `reporterISO` - ISO country code (BRA, RUS, IND, CHN, ZAF)
- `flowDesc` - Flow description ('Import')
- `qty` - Quantity in kilograms
- `primaryValue` - Value in USD

## After Adding Files

Run the script:
```bash
python3 generate_prediction_figures.py
```

All figures will be saved to `../figures/` directory.
