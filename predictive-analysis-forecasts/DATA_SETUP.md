# Data Setup Instructions

Before generating figures, you need to place your cleaned CSV data files in this directory.

## Required Files

Place these 3 cleaned CSV files in the `predictive-analysis-forecasts/` directory:

```
predictive-analysis-forecasts/
├── Btc_5y_Cleaned.csv           ← Bitcoin trading data (2020-2025)
├── Gold_TradeData_Cleaned.csv   ← Gold trade data (2021-2025)
├── Oil_TradeData_Cleaned.csv    ← Oil trade data (2021-2025)
└── generate_prediction_figures.py
```

## File Requirements

### 1. Btc_5y_Cleaned.csv

Required columns:
- `time` - Date/timestamp of trading data
- `currency` - Currency code (must include 'USD')
- `trading_volume_btc` - BTC trading volume

### 2. Gold_TradeData_Cleaned.csv

Required columns:
- `refDate` - Reference date for the trade
- `reporterISO` - ISO country code (must include: BRA, RUS, IND, CHN, ZAF)
- `flowDesc` - Flow description (must include 'Import')
- `qty` - Quantity in kilograms
- `primaryValue` - Value in USD

### 3. Oil_TradeData_Cleaned.csv

Required columns:
- `refDate` - Reference date for the trade
- `reporterISO` - ISO country code (must include: BRA, RUS, IND, CHN, ZAF)
- `flowDesc` - Flow description (must include 'Import')
- `qty` - Quantity in kilograms
- `primaryValue` - Value in USD

## Data Sources

As documented in the main README:

1. **Bitcoin Trading Volume**: [Bitcoinity.org](https://data.bitcoinity.org/markets/volume/30d?c=e&t=b)
   - Period: December 2020 - December 2025

2. **Gold Trade Data**: [UN Comtrade Plus](https://comtradeplus.un.org/)
   - Period: January 2021 - October 2025
   - HS Code: 7108 (Gold, unwrought or semi-manufactured)

3. **Crude Oil Trade Data**: [UN Comtrade Plus](https://comtradeplus.un.org/)
   - Period: January 2021 - October 2025
   - HS Code: 2709 (Petroleum oils, crude)

## After Placing Files

Once you've placed all 3 CSV files in this directory, run:

```bash
python3 generate_prediction_figures.py
```

Or simply:

```bash
python generate_prediction_figures.py
```

## Expected Output

The script will:
1. Load and process your 3 CSV files
2. Generate 8 PDF figures
3. Save all PDFs to the `../figures/` directory
4. Display progress and success messages

## Troubleshooting

**Error: "No such file or directory: 'Btc_5y_Cleaned.csv'"**
- Make sure the CSV files are in the `predictive-analysis-forecasts/` directory
- Check that filenames match exactly (case-sensitive)

**Error: "KeyError: 'time'" or similar**
- Verify your CSV has the required columns listed above
- Check column names match exactly (case-sensitive)

**Error: "No data found"**
- Ensure your CSV files contain data for the expected date ranges
- Check that BRICS country codes (BRA, RUS, IND, CHN, ZAF) are present

## Sample Data Structure

### Bitcoin CSV (Btc_5y_Cleaned.csv):
```csv
time,currency,trading_volume_btc
2020-12-01,USD,125000.50
2020-12-01,EUR,45000.25
2020-12-02,USD,128000.75
...
```

### Gold CSV (Gold_TradeData_Cleaned.csv):
```csv
refDate,reporterISO,flowDesc,qty,primaryValue
2021-01-01,CHN,Import,50000,2500000
2021-01-01,IND,Import,30000,1500000
...
```

### Oil CSV (Oil_TradeData_Cleaned.csv):
```csv
refDate,reporterISO,flowDesc,qty,primaryValue
2021-01-01,CHN,Import,1000000,50000000
2021-01-01,IND,Import,800000,40000000
...
```

## Need Help?

- See [FIGURES_GUIDE.md](../FIGURES_GUIDE.md) for figure descriptions
- See [README.md](../README.md) for project overview
- Check [figures/README.md](../figures/README.md) for output details
