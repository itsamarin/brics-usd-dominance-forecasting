# Data Format Requirements

This document explains the required format for your CSV data files.

## Required Files

You need **3 CSV files**:

1. `Btc_5y_Cleaned.csv` - Bitcoin trading volume data
2. `Gold_TradeData_Cleaned.csv` - Gold import/export data
3. `Oil_TradeData_Cleaned.csv` - Crude oil import/export data

## File Format Specifications

### 1. Bitcoin Data (Btc_5y_Cleaned.csv)

**Required Columns:**
- `time` - Date/timestamp (YYYY-MM-DD or ISO format)
- `currency` - Currency code (e.g., "USD", "EUR", "GBP")
- `trading_volume_btc` - Trading volume in BTC (numeric)

**Example:**
```csv
time,currency,trading_volume_btc
2020-12-21 00:00:00+00:00,USD,123456.78
2020-12-22 00:00:00+00:00,USD,234567.89
2020-12-23 00:00:00+00:00,EUR,45678.90
2020-12-24 00:00:00+00:00,USD,345678.12
```

**Important:**
- Date format can be flexible (pandas will parse it)
- Must include "USD" currency for analysis
- Values should be positive numbers
- Daily or monthly granularity accepted

**Minimum Data:**
- At least 12 months of USD trading data
- Recommended: 24+ months for better forecasts

---

### 2. Gold Trade Data (Gold_TradeData_Cleaned.csv)

**Required Columns:**
- `refDate` - Reference date (YYYY-MM-DD)
- `reporterISO` - Country ISO code (e.g., "CHN", "USA", "BRA")
- `reporterDesc` - Country name (e.g., "China", "United States")
- `flowDesc` - Trade flow ("Import" or "Export")
- `partnerDesc` - Trading partner (can be "World")
- `cmdCode` - Commodity code
- `cmdDesc` - Commodity description
- `qtyUnitAbbr` - Quantity unit (e.g., "kg")
- `qty` - Quantity (numeric)
- `isQtyEstimated` - Boolean (True/False)
- `netWgt` - Net weight
- `isNetWgtEstimated` - Boolean
- `grossWgt` - Gross weight
- `isGrossWgtEstimated` - Boolean
- `primaryValue` - Trade value in USD (numeric)
- `value_per_unit` - Value per unit (numeric)

**Example:**
```csv
refDate,reporterISO,reporterDesc,flowDesc,partnerDesc,cmdCode,cmdDesc,qtyUnitAbbr,qty,isQtyEstimated,netWgt,isNetWgtEstimated,grossWgt,isGrossWgtEstimated,primaryValue,value_per_unit
2021-01-01,CHN,China,Import,World,7108,Gold unwrought,kg,9874.528,False,9874.528,False,0.0,False,555991059.0,56305.58
2021-01-01,BRA,Brazil,Import,World,7108,Gold unwrought,kg,60.752,True,60.752,True,0.0,False,631026.0,10386.92
2021-01-01,USA,United States,Import,World,7108,Gold unwrought,kg,1234.56,False,1234.56,False,0.0,False,67890123.0,54987.65
```

**Important:**
- Must include BRICS countries: BRA, RUS, IND, CHN, ZAF
- Should include US/EU countries for comparison
- `flowDesc` should be "Import" for analysis
- `qty` in kilograms
- `primaryValue` in USD

**Minimum Data:**
- At least 12 months of monthly data
- Include BRICS nations (BRA, RUS, IND, CHN, ZAF)
- Recommended: 24+ months

---

### 3. Crude Oil Trade Data (Oil_TradeData_Cleaned.csv)

**Required Columns:**
- `refDate` - Reference date (YYYY-MM-DD)
- `reporterISO` - Country ISO code
- `reporterDesc` - Country name
- `flowDesc` - Trade flow ("Import" or "Export")
- `partnerDesc` - Trading partner
- `cmdCode` - Commodity code (2709 for crude oil)
- `cmdDesc` - Commodity description
- `qtyUnitAbbr` - Quantity unit (typically "kg")
- `qty` - Quantity in kg (numeric)
- `isQtyEstimated` - Boolean
- `netWgt` - Net weight
- `isNetWgtEstimated` - Boolean
- `grossWgt` - Gross weight
- `isGrossWgtEstimated` - Boolean
- `primaryValue` - Trade value in USD (numeric)

**Example:**
```csv
refDate,reporterISO,reporterDesc,flowDesc,partnerDesc,cmdCode,cmdDesc,qtyUnitAbbr,qty,isQtyEstimated,netWgt,isNetWgtEstimated,grossWgt,isGrossWgtEstimated,primaryValue
2021-01-01,CHN,China,Import,World,2709,Petroleum oils crude,kg,44569078200.0,False,44569078200.0,False,0.0,False,16909177521.0
2021-01-01,IND,India,Import,World,2709,Petroleum oils crude,kg,18622912000.0,False,18622912000.0,False,0.0,False,6937450162.22
2021-01-01,BRA,Brazil,Import,World,2709,Petroleum oils crude,kg,191646650.0,False,191646650.0,False,0.0,False,100452582.0
```

**Important:**
- Must include BRICS countries: BRA, RUS, IND, CHN, ZAF
- Commodity code 2709 for crude oil
- `qty` in kilograms
- `primaryValue` in USD
- Import flows for analysis

**Minimum Data:**
- At least 12 months of monthly data
- Include BRICS nations
- Recommended: 24+ months

---

## Country Codes Reference

### BRICS Countries (Required)
- `BRA` - Brazil
- `RUS` - Russian Federation  
- `IND` - India
- `CHN` - China
- `ZAF` - South Africa

### US/EU Countries (For Comparison)
- `USA` - United States
- `DEU` - Germany
- `FRA` - France
- `ITA` - Italy
- `ESP` - Spain
- `NLD` - Netherlands
- `BEL` - Belgium

## Data Quality Checklist

Before running the analysis, verify:

** File Names Match Exactly**
```
Btc_5y_Cleaned.csv          (case-sensitive)
Gold_TradeData_Cleaned.csv  (case-sensitive)
Oil_TradeData_Cleaned.csv   (case-sensitive)
```

** Required Columns Present**
- All column names match exactly (case-sensitive)
- No extra spaces in column names
- No missing required columns

** Data Types Correct**
- Dates in YYYY-MM-DD format (or parseable by pandas)
- Numeric values are numbers (not text)
- No currency symbols in numeric columns ($, €, etc.)
- Booleans are True/False (not 1/0 or Yes/No)

** No Missing Critical Data**
- No blank/null values in key columns (refDate, qty, primaryValue)
- At least 12 months of data
- BRICS countries present in Gold/Oil data
- USD currency present in BTC data

** Reasonable Values**
- No negative quantities
- No zero or negative values in primaryValue
- Dates within expected range (2020-2025)

## Common Issues and Fixes

### Issue: "KeyError: 'trading_volume_btc'"

**Cause:** Column name mismatch

**Fix:** Check column names exactly match (case-sensitive)
```python
import pandas as pd
df = pd.read_csv('Btc_5y_Cleaned.csv')
print(df.columns.tolist())  # Check actual column names
```

### Issue: "ValueError: time data does not match format"

**Cause:** Date format not recognized

**Fix:** Standardize dates to YYYY-MM-DD format
```python
df['refDate'] = pd.to_datetime(df['refDate'], format='%d/%m/%Y')
df['refDate'] = df['refDate'].dt.strftime('%Y-%m-%d')
```

### Issue: Empty forecasts or NaN values

**Cause:** Insufficient data (less than 3 months)

**Fix:** Ensure at least 12 months of data for meaningful forecasts

### Issue: "No data for BRICS countries"

**Cause:** Missing or incorrect country codes

**Fix:** Verify BRICS codes: BRA, RUS, IND, CHN, ZAF
```python
df = pd.read_csv('Gold_TradeData_Cleaned.csv')
print(df['reporterISO'].unique())  # Check country codes
```

## Data Validation Script

Use this to check your data before running analysis:

```python
import pandas as pd

# Check Bitcoin data
btc = pd.read_csv('Btc_5y_Cleaned.csv')
print("BTC Columns:", btc.columns.tolist())
print("BTC Shape:", btc.shape)
print("BTC Currencies:", btc['currency'].unique())
print("BTC Date Range:", btc['time'].min(), "to", btc['time'].max())
print()

# Check Gold data
gold = pd.read_csv('Gold_TradeData_Cleaned.csv')
print("Gold Columns:", gold.columns.tolist())
print("Gold Shape:", gold.shape)
print("Gold Countries:", gold['reporterISO'].unique())
print("Gold Date Range:", gold['refDate'].min(), "to", gold['refDate'].max())
print()

# Check Oil data
oil = pd.read_csv('Oil_TradeData_Cleaned.csv')
print("Oil Columns:", oil.columns.tolist())
print("Oil Shape:", oil.shape)
print("Oil Countries:", oil['reporterISO'].unique())
print("Oil Date Range:", oil['refDate'].min(), "to", oil['refDate'].max())
```

## Getting the Data

### Bitcoin Data
**Source:** [Bitcoinity.org](https://data.bitcoinity.org/markets/volume/30d?c=e&t=b)

1. Visit website
2. Select time range (5 years)
3. Download CSV
4. Ensure columns: time, currency, trading_volume_btc

### Gold/Oil Data
**Source:** [UN Comtrade Plus](https://comtradeplus.un.org/)

1. Visit website
2. Select commodity (Gold: 7108, Crude Oil: 2709)
3. Select reporters (BRICS + US/EU)
4. Select time period (2021-2025)
5. Download as CSV
6. Ensure all required columns present

---

**Need Help?** Open an issue on GitHub or check USAGE.md for more details!
