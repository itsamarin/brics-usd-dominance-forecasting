# Complete Setup Guide - Predictive Analysis Forecasts

## 📦 What You'll Need

- Python 3.8 or higher
- Git (for version control)
- LibreOffice (for Excel formula recalculation)
- Text editor or IDE (VS Code, PyCharm, etc.)
- Your cleaned data files (CSV format)

## 🚀 Step-by-Step Setup

### Step 1: Install Python

**Windows:**
1. Download from [python.org](https://www.python.org/downloads/)
2. Run installer, **check "Add Python to PATH"**
3. Verify: Open CMD and type `python --version`

**macOS:**
```bash
# Using Homebrew
brew install python3

# Verify
python3 --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verify
python3 --version
```

### Step 2: Install Git

**Windows:**
Download from [git-scm.com](https://git-scm.com/downloads)

**macOS:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt install git
```

### Step 3: Install LibreOffice

**Windows:**
Download from [libreoffice.org](https://www.libreoffice.org/download/)

**macOS:**
```bash
brew install --cask libreoffice
```

**Linux:**
```bash
sudo apt install libreoffice
```

### Step 4: Clone or Download This Repository

**Option A: Using Git (Recommended)**
```bash
# Navigate to where you want the project
cd ~/Documents

# Clone the repository
git clone https://github.com/yourusername/predictive-analysis-forecasts.git
cd predictive-analysis-forecasts
```

**Option B: Download ZIP**
1. Go to GitHub repository page
2. Click "Code" → "Download ZIP"
3. Extract to your desired location
4. Open terminal/CMD in that folder

### Step 5: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# You should see (venv) in your terminal prompt
```

### Step 6: Install Python Packages

```bash
# Make sure virtual environment is activated
pip install -r requirements.txt

# Verify installation
pip list
```

Expected packages:
- pandas
- numpy
- openpyxl

### Step 7: Prepare Your Data Files

1. **Get your cleaned CSV files:**
   - `Btc_5y_Cleaned.csv`
   - `Gold_TradeData_Cleaned.csv`
   - `Oil_TradeData_Cleaned.csv`

2. **Place them in the project folder:**
   ```
   predictive-analysis-forecasts/
   ├── predictive_analysis_forecast.py
   ├── recalc.py
   ├── Btc_5y_Cleaned.csv          ← Your data file
   ├── Gold_TradeData_Cleaned.csv  ← Your data file
   └── Oil_TradeData_Cleaned.csv   ← Your data file
   ```

3. **Verify data format:**

   **Bitcoin CSV should have columns:**
   - `time` (datetime)
   - `currency` (string)
   - `trading_volume_btc` (float)

   **Gold/Oil CSV should have columns:**
   - `refDate` (datetime)
   - `reporterISO` (string, country code)
   - `flowDesc` (string, "Import" or "Export")
   - `qty` (float, quantity)
   - `primaryValue` (float, USD value)

### Step 8: Run the Analysis

```bash
# Make sure virtual environment is activated
# You should see (venv) in your prompt

# Run the script
python predictive_analysis_forecast.py
```

Expected output:
```
======================================================================
SECTION D: PREDICTIVE ANALYSIS - 3-Month Moving Average Forecasts
======================================================================

[1/5] Loading and processing data...
  ✓ BTC data: 61 months
  ✓ Gold BRICS data: 58 months
  ✓ Oil BRICS data: 58 months

[2/5] Creating Excel workbook...

[3/5] Generating forecast sheets...
  ✓ USD Dominance Analysis sheet created
  ✓ BTC Forecast sheet created
  ✓ Gold BRICS Forecast sheet created
  ✓ Oil BRICS Forecast sheet created

[4/5] Saving workbook...
  ✓ Workbook saved: Predictive_Analysis_Forecasts.xlsx

[5/5] Formula recalculation...
  ! Run: python recalc.py Predictive_Analysis_Forecasts.xlsx

======================================================================
SUCCESS! Predictive analysis workbook generated.
======================================================================
```

### Step 9: Recalculate Excel Formulas

```bash
# Recalculate formulas (requires LibreOffice)
python recalc.py Predictive_Analysis_Forecasts.xlsx
```

Expected output:
```json
{
  "status": "success",
  "message": "Formulas recalculated"
}
```

### Step 10: Open and Review Results

```bash
# Open the Excel file
# Windows:
start Predictive_Analysis_Forecasts.xlsx

# macOS:
open Predictive_Analysis_Forecasts.xlsx

# Linux:
libreoffice Predictive_Analysis_Forecasts.xlsx
```

## ✅ Verification Checklist

- [ ] Python 3.8+ installed
- [ ] Git installed (optional but recommended)
- [ ] LibreOffice installed
- [ ] Virtual environment created and activated
- [ ] Python packages installed
- [ ] Data CSV files in correct location
- [ ] Script runs without errors
- [ ] Excel file created successfully
- [ ] Formulas recalculated
- [ ] All sheets visible in Excel

## 🔧 Troubleshooting

### Problem: "python: command not found"

**Solution:** Use `python3` instead of `python`
```bash
python3 -m venv venv
python3 predictive_analysis_forecast.py
```

### Problem: "No module named 'pandas'"

**Solution:** Activate virtual environment and reinstall
```bash
# Activate venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows

# Reinstall
pip install -r requirements.txt
```

### Problem: "FileNotFoundError: Btc_5y_Cleaned.csv"

**Solution:** Check file location
```bash
# List files in current directory
ls -la  # macOS/Linux
dir     # Windows

# Move files to correct location
mv /path/to/Btc_5y_Cleaned.csv .
```

### Problem: "Permission denied" on Linux/macOS

**Solution:** Make scripts executable
```bash
chmod +x recalc.py
chmod +x predictive_analysis_forecast.py
```

### Problem: Formulas not calculating

**Solution:**
1. Verify LibreOffice is installed
2. Try opening file in Excel/LibreOffice manually
3. Check if formulas are present (view cell contents)
4. Re-run recalc.py with verbose output

### Problem: Excel file won't open

**Solution:**
1. Try opening in LibreOffice Calc instead of Excel
2. Check file isn't corrupted: `file Predictive_Analysis_Forecasts.xlsx`
3. Re-run script to regenerate

## 📊 What the Output Contains

Your Excel file will have **4 sheets**:

### Sheet 1: USD_Dominance_Analysis
- Executive summary
- Key findings on USD dominance post-July 2027
- Investment recommendations

### Sheet 2: BTC_Forecast
- 24 months historical USD trading volume
- 3-month moving averages
- 3-month forecasts (Jan-Mar 2026)

### Sheet 3: Gold_BRICS_Forecast
- BRICS gold import data
- Quantity (kg) and Value (USD)
- 3-month forecasts

### Sheet 4: Oil_BRICS_Forecast
- BRICS crude oil import data
- Quantity (kg) and Value (USD)
- 3-month forecasts

## 🎓 Next Steps

1. **Review the Analysis:**
   - Read the USD Dominance Analysis summary
   - Check forecast values
   - Review insights on each sheet

2. **Customize (Optional):**
   - Modify forecast horizon (3 → 6 months)
   - Change moving average window
   - Add additional countries/currencies

3. **Share Your Work:**
   - Save to Google Drive
   - Export to PDF for presentations
   - Share on GitHub

4. **Publish on GitHub:**
   ```bash
   # Initialize git repository
   git init
   
   # Add files
   git add .
   
   # Commit
   git commit -m "Initial commit: Predictive analysis forecasts"
   
   # Push to GitHub
   git remote add origin https://github.com/yourusername/repo-name.git
   git branch -M main
   git push -u origin main
   ```

## 📞 Getting Help

If you're stuck:

1. Check this setup guide again
2. Review USAGE.md for detailed usage
3. Check CONTRIBUTING.md if you want to modify code
4. Create an issue on GitHub
5. Contact project maintainer

## 🎉 Congratulations!

You've successfully set up and run the predictive analysis! You now have:

- ✅ Working Python environment
- ✅ All dependencies installed
- ✅ Analysis running successfully
- ✅ Professional Excel output
- ✅ 3-month forecasts for BTC, Gold, and Oil

Your contribution to Section D is complete! 🚀

---

**Project:** Predictive Analysis - Oil, Gold, and Crypto  
**Course:** Global Economic Signals Analysis  
**Institution:** University of Europe & Avron Global Consultancy  
**Last Updated:** December 31, 2025
