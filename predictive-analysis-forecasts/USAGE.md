# Usage Guide - Predictive Analysis Forecasts

## Quick Start

### 1. Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/predictive-analysis-forecasts.git
cd predictive-analysis-forecasts

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Prepare Your Data

Place the following cleaned CSV files in the same directory as the script:

- `Btc_5y_Cleaned.csv` - Bitcoin trading volume data
- `Gold_TradeData_Cleaned.csv` - Gold import trade data
- `Oil_TradeData_Cleaned.csv` - Crude oil import trade data

**Data Format Requirements:**

**Bitcoin CSV:**
```
time,currency,trading_volume_btc
2020-12-21 00:00:00+00:00,USD,123456.78
```

**Gold/Oil CSV:**
```
refDate,reporterISO,reporterDesc,flowDesc,qty,primaryValue,...
2021-01-01,CHN,China,Import,1000.5,50000000,...
```

### 3. Run the Analysis

```bash
# Generate the forecast workbook
python predictive_analysis_forecast.py
```

### 4. Recalculate Formulas

```bash
# Install LibreOffice (if not already installed)
# Ubuntu/Debian:
sudo apt-get install libreoffice

# macOS:
brew install --cask libreoffice

# Recalculate formulas
python recalc.py Predictive_Analysis_Forecasts.xlsx
```

### 5. View Results

Open `Predictive_Analysis_Forecasts.xlsx` in Excel, LibreOffice Calc, or Google Sheets.

## Detailed Usage

### Customizing Data Paths

Edit the `main()` function in `predictive_analysis_forecast.py`:

```python
def main():
    # Update these paths to match your file locations
    btc_path = 'path/to/your/Btc_5y_Cleaned.csv'
    gold_path = 'path/to/your/Gold_TradeData_Cleaned.csv'
    oil_path = 'path/to/your/Oil_TradeData_Cleaned.csv'
    output_path = 'path/to/output/Predictive_Analysis_Forecasts.xlsx'
    # ...
```

### Changing Forecast Horizon

To forecast more than 3 months ahead:

```python
# In each create_*_forecast_sheet() function, modify:

# Forecast next 3 months (change to desired number)
for i in range(1, 4):  # Change 4 to (desired_months + 1)
    forecast_date = last_date + pd.DateOffset(months=i)
    # ...
```

### Changing Historical Data Window

To use more/less historical data:

```python
# In each create_*_forecast_sheet() function, modify:

# Get last 24 months of data (change to desired number)
btc_data = btc_monthly.sort_values('Date').tail(24)  # Change 24
```

### Modifying Moving Average Window

To use a different moving average window (e.g., 6-month):

```python
# Change the formula from 3-month to 6-month MA:

# Old (3-month):
ws.cell(row=row_num, column=4, value=f'=AVERAGE(C{row_num-2}:C{row_num})')

# New (6-month):
ws.cell(row=row_num, column=4, value=f'=AVERAGE(C{row_num-5}:C{row_num})')

# Also update forecast formula:
ws.cell(row=row_num, column=5, value=f'=AVERAGE(C{row_num-6}:C{row_num-1})')
```

## Advanced Usage

### Adding Custom Analysis

You can extend the script with additional analysis:

```python
def create_custom_analysis_sheet(wb, data):
    """Create a custom analysis sheet"""
    ws = wb.create_sheet('Custom_Analysis')
    
    # Your custom analysis code here
    # ...
    
    return ws

# In main():
def main():
    # ... existing code ...
    
    # Add custom analysis
    create_custom_analysis_sheet(wb, custom_data)
    
    wb.save(output_path)
```

### Batch Processing Multiple Scenarios

```python
scenarios = [
    {'name': 'Conservative', 'months': 3, 'window': 24},
    {'name': 'Moderate', 'months': 6, 'window': 36},
    {'name': 'Aggressive', 'months': 12, 'window': 48}
]

for scenario in scenarios:
    output = f"Forecast_{scenario['name']}.xlsx"
    # Modify parameters and run analysis
    # ...
```

### Exporting to Other Formats

```python
# Export forecasts to CSV
btc_monthly.to_csv('btc_forecast.csv', index=False)

# Export to JSON
btc_monthly.to_json('btc_forecast.json', orient='records', date_format='iso')
```

## Troubleshooting

### Common Issues

**Issue: "FileNotFoundError: [Errno 2] No such file or directory"**

**Solution:** Ensure CSV files are in the correct location. Update file paths in the script.

```python
# Use absolute paths if needed
btc_path = '/full/path/to/Btc_5y_Cleaned.csv'
```

**Issue: "ValueError: time data '...' does not match format"**

**Solution:** Check date format in CSV files. Should be ISO format (YYYY-MM-DD).

```python
# If dates are in different format, parse manually:
btc_df['time'] = pd.to_datetime(btc_df['time'], format='%d/%m/%Y')
```

**Issue: "KeyError: 'trading_volume_btc'"**

**Solution:** Verify column names match exactly. Case-sensitive.

```python
# Check column names:
print(btc_df.columns.tolist())
```

**Issue: "Formula recalculation failed"**

**Solution:** 
1. Ensure LibreOffice is installed
2. Try opening file manually in Excel/LibreOffice
3. Check formula syntax in Excel

**Issue: "Empty forecast values"**

**Solution:** Ensure you have at least 3 months of historical data for 3-month MA.

### Performance Optimization

For large datasets:

```python
# Use chunking for large CSV files
chunk_size = 10000
chunks = pd.read_csv('large_file.csv', chunksize=chunk_size)

processed_data = pd.concat([process_chunk(chunk) for chunk in chunks])
```

### Debugging

Enable verbose output:

```python
# Add debug prints in main():
print(f"BTC data shape: {btc_monthly.shape}")
print(f"Date range: {btc_monthly['Date'].min()} to {btc_monthly['Date'].max()}")
print(f"\nFirst 5 rows:\n{btc_monthly.head()}")
```

## Best Practices

### 1. Data Validation

Always validate your input data before running analysis:

```python
# Check for missing values
print(btc_df.isnull().sum())

# Check date ranges
print(f"Date range: {btc_df['time'].min()} to {btc_df['time'].max()}")

# Check data types
print(btc_df.dtypes)
```

### 2. Version Control

Commit your analysis scripts but consider excluding large data files:

```bash
# Add data files to .gitignore
echo "*.csv" >> .gitignore
echo "*.xlsx" >> .gitignore

# Commit code only
git add *.py README.md requirements.txt
git commit -m "Add predictive analysis script"
```

### 3. Documentation

Document any modifications to the original script:

```python
# Custom modification - [Your Name] - [Date]
# Modified moving average window from 3 to 6 months
# for better trend stability in volatile markets
```

### 4. Reproducibility

Always specify package versions:

```bash
pip freeze > requirements.txt
```

## Integration with Other Tools

### Jupyter Notebook

```python
# Create notebook version
jupyter nbconvert --to notebook predictive_analysis_forecast.py
```

### Automated Reporting

```python
# Schedule with cron (Linux/Mac)
# Run every 1st of month at 9am
# 0 9 1 * * /path/to/venv/bin/python /path/to/predictive_analysis_forecast.py
```

### Power BI / Tableau Integration

Export data in formats compatible with BI tools:

```python
# Export for Power BI
btc_monthly.to_csv('btc_powerbi.csv', index=False)

# Export for Tableau
btc_monthly.to_csv('btc_tableau.csv', index=False, date_format='%Y-%m-%d')
```

## Getting Help

1. Check this usage guide
2. Review error messages carefully
3. Check GitHub Issues
4. Contact project maintainer

## Contributing

If you develop useful extensions or improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

Academic use - See LICENSE file for details.
