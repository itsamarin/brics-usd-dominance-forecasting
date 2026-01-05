# Quick Start Guide

Get your predictive analysis up and running in **5 minutes**!

##  Fast Track (For Experienced Users)

```bash
# 1. Clone repository
git clone https://github.com/yourusername/predictive-analysis-forecasts.git
cd predictive-analysis-forecasts

# 2. Install dependencies
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Add your CSV data files
# - Btc_5y_Cleaned.csv
# - Gold_TradeData_Cleaned.csv
# - Oil_TradeData_Cleaned.csv

# 4. Run analysis
python predictive_analysis_forecast.py
python add_charts_to_forecasts.py

# 5. Done! Open Predictive_Analysis_Forecasts_with_Charts.xlsx
```

##  Step-by-Step (For Beginners)

### 1. Download This Repository

**Option A: Using Git**
```bash
git clone https://github.com/yourusername/predictive-analysis-forecasts.git
cd predictive-analysis-forecasts
```

**Option B: Download ZIP**
1. Click green "Code" button  "Download ZIP"
2. Extract to your Documents folder
3. Open terminal/command prompt in that folder

### 2. Install Python (If Not Installed)

**Check if you have Python:**
```bash
python --version
# or
python3 --version
```

**Need to install?**
- Windows: [python.org/downloads](https://python.org/downloads)
- Mac: `brew install python3`
- Linux: `sudo apt install python3`

### 3. Set Up Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate

# You should see (venv) in your prompt
```

### 4. Install Required Packages

```bash
pip install -r requirements.txt
```

This installs:
- pandas (data processing)
- openpyxl (Excel handling)
- numpy (calculations)

### 5. Add Your Data Files

Place these 3 CSV files in the repository folder:

```
predictive-analysis-forecasts/
├── Btc_5y_Cleaned.csv          ← Your file here
├── Gold_TradeData_Cleaned.csv  ← Your file here
├── Oil_TradeData_Cleaned.csv   ← Your file here
└── predictive_analysis_forecast.py
```

### 6. Run the Analysis

```bash
# Generate forecasts
python predictive_analysis_forecast.py

# Add charts
python add_charts_to_forecasts.py
```

**Expected output:**
```
======================================================================
SECTION D: PREDICTIVE ANALYSIS - 3-Month Moving Average Forecasts
======================================================================

[1/5] Loading and processing data...
   BTC data: 61 months
   Gold BRICS data: 58 months
   Oil BRICS data: 58 months
...
SUCCESS! Predictive analysis workbook generated.
```

### 7. Open Your Results

```bash
# Windows
start Predictive_Analysis_Forecasts_with_Charts.xlsx

# Mac
open Predictive_Analysis_Forecasts_with_Charts.xlsx

# Linux
libreoffice Predictive_Analysis_Forecasts_with_Charts.xlsx
```

##  What You'll Get

An Excel file with **4 sheets** and **5 professional charts**:

1. **USD_Dominance_Analysis** - Executive summary
2. **BTC_Forecast** - Bitcoin forecasts with chart
3. **Gold_BRICS_Forecast** - Gold forecasts with 2 charts
4. **Oil_BRICS_Forecast** - Oil forecasts with 2 charts

##  Next Steps

1. **Review the analysis** - Check USD dominance assessment
2. **Customize if needed** - See USAGE.md for modifications
3. **Share your work** - Export to PDF or push to GitHub
4. **Add to your report** - Use for Section D submission

##  Troubleshooting

**"No module named 'pandas'"**
```bash
# Make sure venv is activated (you should see (venv))
pip install -r requirements.txt
```

**"File not found: Btc_5y_Cleaned.csv"**
```bash
# Check files are in the right place
ls -la  # Mac/Linux
dir     # Windows
```

**"Python not found"**
```bash
# Try python3 instead
python3 predictive_analysis_forecast.py
```

**Charts not showing**
```bash
# Open in desktop Excel or LibreOffice (not Google Sheets)
# If needed, install LibreOffice: sudo apt install libreoffice
```

##  More Information

- **Detailed Setup**: See [SETUP_GUIDE.md](SETUP_GUIDE.md)
- **Usage Examples**: See [USAGE.md](USAGE.md)
- **Chart Guide**: See [CHARTS_GUIDE.md](CHARTS_GUIDE.md)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

##  Tips

- Run in virtual environment to avoid package conflicts
- Keep CSV files in same folder as scripts
- Use Excel 2016+ or LibreOffice for best compatibility
- Save your customizations before re-running scripts

##  For Your Assignment

This completes **Section D: Predictive Analysis** of your case study:
-  3-month moving average forecasts
-  BTC, Gold, and Oil analysis
-  USD dominance assessment
-  Professional visualizations
-  Investment recommendations

Ready to submit! 

---

**Time to complete:** ~5 minutes  
**Difficulty:** Easy  
**Prerequisites:** Python 3.8+, CSV data files  
**Output:** Professional Excel report with charts

Happy analyzing! 
