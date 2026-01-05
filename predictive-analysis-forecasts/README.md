# Section D: Predictive Analysis - 3-Month Moving Average Forecasts

**Author:** [Your Name]  
**Course:** Oil, Gold, and Crypto: How Global Tensions are linked to Commodities  
**Institution:** University of Europe & Avron Global Consultancy Initiative  
**Semester:** Winter 2025

## Project Overview

This project implements **Section D: Predictive Analysis** of the case study "Understanding Global Economic Signals Using Real-World Data." The analysis uses 3-month moving average forecasting to predict future trends in:

- **Bitcoin (USD) Trading Volume** - Tracking USD dominance in cryptocurrency markets
- **BRICS Gold Imports** - Central bank diversification and de-dollarization trends
- **BRICS Crude Oil Imports** - Energy security and alternative currency settlements

### Central Research Question

> **"Will USD still remain the dominant currency in the world post-July 2027?"**

## Repository Structure

```
.
├── predictive_analysis_forecast.py    # Main analysis script
├── add_charts_to_forecasts.py         # Chart generation script
├── recalc.py                           # Excel formula recalculation utility
├── README.md                           # This file
├── CHARTS_GUIDE.md                     # Chart documentation
├── requirements.txt                    # Python dependencies
├── sample_outputs/
│   └── Predictive_Analysis_Forecasts_with_Charts.xlsx
└── data/
    ├── Btc_5y_Cleaned.csv
    ├── Gold_TradeData_Cleaned.csv
    └── Oil_TradeData_Cleaned.csv
```

## Key Features

### 1. **USD Dominance Analysis**
- Executive summary with probability assessment (75% USD remains dominant but weakened)
- Key indicators dashboard tracking BTC trading, BRICS reserves, and payment systems
- Timeline analysis from 2025-2030
- Portfolio management recommendations

### 2. **Bitcoin Forecast**
- USD trading volume trends (2020-2025)
- 3-month moving average calculations
- Q1 2026 forecasts
- Insights on USD's role in crypto markets

### 3. **Gold BRICS Forecast**
- Import quantities and values for Brazil, Russia, India, China, South Africa
- Central bank diversification patterns
- De-dollarization indicators
- 3-month ahead projections

### 4. **Oil BRICS Forecast**
- Crude oil import patterns
- Energy security strategies
- Alternative settlement currency analysis
- Economic growth indicators

## Installation & Setup

### Prerequisites
- Python 3.8+
- pandas
- openpyxl
- numpy
- LibreOffice (for formula recalculation)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/predictive-analysis-forecasts.git
cd predictive-analysis-forecasts

# Install dependencies
pip install -r requirements.txt

# Install LibreOffice (for recalc.py)
# Ubuntu/Debian:
sudo apt-get install libreoffice

# macOS:
brew install --cask libreoffice
```

## Data Sources

1. **Bitcoin Trading Volume**
   - Source: [Bitcoinity.org](https://data.bitcoinity.org/markets/volume/30d?c=e&t=b)
   - Period: December 2020 - December 2025
   - Granularity: Daily, aggregated to monthly

2. **Gold Import Data**
   - Source: [UN Comtrade Plus](https://comtradeplus.un.org/)
   - Countries: BRICS (BRA, RUS, IND, CHN, ZAF) vs US/EU
   - Period: January 2021 - October 2025

3. **Crude Oil Import Data**
   - Source: [UN Comtrade Plus](https://comtradeplus.un.org/)
   - Countries: BRICS vs US/EU
   - Period: January 2021 - October 2025

## Visualizations

The analysis includes **5 professional charts** visualizing forecasts:

1. **BTC Trading Volume Chart** - Shows USD dominance in crypto markets
2. **Gold BRICS Quantity Chart** - Tracks central bank accumulation
3. **Gold BRICS Value Chart** - Shows investment scale in USD
4. **Oil BRICS Quantity Chart** - Energy security patterns
5. **Oil BRICS Value Chart** - Energy expenditure trends

All charts include:
- Historical data (solid lines)
- 3-month moving averages (smoothed trends)
- 3-month forecasts (dashed lines)

See [CHARTS_GUIDE.md](CHARTS_GUIDE.md) for detailed chart documentation.

## Usage

### Basic Usage

```bash
# Run the main analysis script
python predictive_analysis_forecast.py

# Add professional charts to visualize forecasts
python add_charts_to_forecasts.py

# Recalculate Excel formulas
python recalc.py Predictive_Analysis_Forecasts_with_Charts.xlsx
```

### Expected Output

The script generates `Predictive_Analysis_Forecasts.xlsx` with 4 sheets:

1. **USD_Dominance_Analysis** - Executive summary and final assessment
2. **BTC_Forecast** - Bitcoin USD trading volume forecasts
3. **Gold_BRICS_Forecast** - BRICS gold import forecasts
4. **Oil_BRICS_Forecast** - BRICS crude oil import forecasts

### Sample Output Structure

```
Predictive_Analysis_Forecasts.xlsx
│
├── USD_Dominance_Analysis
│   ├── Executive Summary
│   ├── Forecast Methodology
│   ├── Key Indicators Dashboard
│   └── Final Assessment
│
├── BTC_Forecast
│   ├── 24 months historical data
│   ├── 3-month moving averages
│   ├── 3-month forecasts (Jan-Mar 2026)
│   └── Key insights
│
├── Gold_BRICS_Forecast
│   ├── Quantity (kg) and Value (USD)
│   ├── 3-month moving averages
│   ├── 3-month forecasts
│   └── De-dollarization insights
│
└── Oil_BRICS_Forecast
    ├── Quantity (kg) and Value (USD)
    ├── 3-month moving averages
    ├── 3-month forecasts
    └── Energy security insights
```

## Methodology

### 3-Month Simple Moving Average (SMA)

The forecast uses a simple moving average approach:

```
Forecast(t+1) = [Actual(t) + Actual(t-1) + Actual(t-2)] / 3
```

**Advantages:**
- Smooths short-term volatility
- Identifies underlying trends
- Simple and interpretable

**Limitations:**
- Cannot predict sudden shocks
- Assumes recent patterns continue
- Linear extrapolation may miss inflection points

### Analysis Framework

```
Historical Data (24 months)

3-Month Moving Average Calculation

Trend Identification

3-Month Ahead Forecast

Insights & Interpretation
```

## Key Findings

### BTC Trading Volume
- **Current:** USD maintains 60-70% dominance in BTC trading
- **Forecast:** Stable USD-BTC trading patterns through Q1 2026
- **Impact:** Neutral - USD holds cryptocurrency gateway position

### BRICS Gold Accumulation
- **Current:** Rising +10% year-over-year
- **Forecast:** Continued acceleration (+8-12% next 3 months)
- **Impact:** Negative for USD - Signals diversification strategy

### BRICS Oil Imports
- **Current:** Growing +5% year-over-year
- **Forecast:** Sustained high demand through Q1 2026
- **Impact:** Negative for USD - Alternative settlements increasing

### USD Dominance Assessment

**Probability: 75%** - USD will remain dominant post-July 2027, but with reduced power

**Timeline:**
- **2025-2026:** Status quo holds, gradual USD erosion (5-10%)
- **2027:** BRICS payment system launch (inflection point)
- **2027-2030:** Multi-polar currency system emerges (USD at 50-60%)

## Investment Implications

### Portfolio Recommendations
1. Maintain USD exposure but hedge with 15-25% in gold
2. Allocate 5-10% to alternative currencies (EUR, CNY)
3. Diversify across commodities (gold, oil)
4. Monitor BRICS payment system development

### Risk Factors
- Accelerated BRICS payment system adoption
- US fiscal deterioration
- Geopolitical shocks (wars, sanctions)
- Energy market restructuring

## Code Structure

### Main Functions

```python
load_and_process_data()      # Load CSV files and aggregate monthly data
create_btc_forecast_sheet()  # Generate BTC forecast sheet
create_gold_forecast_sheet() # Generate Gold forecast sheet
create_oil_forecast_sheet()  # Generate Oil forecast sheet
create_usd_dominance_sheet() # Generate summary analysis
main()                        # Orchestrate full workflow
```

### Customization

To modify the forecast parameters:

```python
# Change forecast horizon (default: 3 months)
for i in range(1, 4):  # Change 4 to desired months + 1
    forecast_date = last_date + pd.DateOffset(months=i)
    
# Change historical data window (default: 24 months)
btc_data = btc_monthly.sort_values('Date').tail(24)  # Change 24
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is part of an academic case study for educational purposes.

## Acknowledgments

- **University of Europe** - Academic supervision
- **Avron Global Consultancy** - Industry partnership
- **Dr./Prof. Anjuman Patil** - Project supervisor
- **Prof. E. George** - Project supervisor
- **UN Comtrade** - Trade data provision
- **Bitcoinity.org** - Cryptocurrency data

## Contact

[Your Name] - [your.email@example.com]

Project Link: [https://github.com/yourusername/predictive-analysis-forecasts](https://github.com/yourusername/predictive-analysis-forecasts)

## References

1. UN Comtrade Plus. (2025). *International Trade Statistics*. https://comtradeplus.un.org/
2. Bitcoinity.org. (2025). *Bitcoin Trading Volume Data*. https://data.bitcoinity.org/
3. SWIFT. (2024). *RMB Tracker*. https://www.swift.com/products/rmb-tracker
4. Case Study: "Oil, Gold, and Crypto: How Global Tensions are linked to Commodities"

---

**Last Updated:** December 31, 2025
