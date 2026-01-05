"""
Create sample data for testing figure generation.
This creates realistic-looking sample data based on typical patterns.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# === CREATE SAMPLE BTC DATA ===
print("Creating sample BTC data...")
start_date = pd.Timestamp('2020-12-01')
end_date = pd.Timestamp('2025-12-01')
dates = pd.date_range(start=start_date, end=end_date, freq='D')

btc_data = []
base_volume = 100000
for date in dates:
    # Add some trend and seasonality
    trend = base_volume * (1 + 0.0001 * (date - start_date).days)
    seasonal = 20000 * np.sin(2 * np.pi * (date - start_date).days / 365)
    noise = np.random.normal(0, 15000)

    usd_volume = max(0, trend + seasonal + noise)
    eur_volume = usd_volume * 0.3 * (1 + np.random.normal(0, 0.1))

    btc_data.append({
        'time': date,
        'currency': 'USD',
        'trading_volume_btc': usd_volume
    })
    btc_data.append({
        'time': date,
        'currency': 'EUR',
        'trading_volume_btc': eur_volume
    })

btc_df = pd.DataFrame(btc_data)
btc_df.to_csv('Btc_5y_Cleaned.csv', index=False)
print(f"  ✓ Created Btc_5y_Cleaned.csv with {len(btc_df)} rows")

# === CREATE SAMPLE GOLD DATA ===
print("Creating sample Gold data...")
start_date = pd.Timestamp('2021-01-01')
end_date = pd.Timestamp('2025-10-01')
dates = pd.date_range(start=start_date, end=end_date, freq='M')

brics_codes = ['BRA', 'RUS', 'IND', 'CHN', 'ZAF']
us_eu_codes = ['USA', 'DEU', 'FRA', 'ITA', 'ESP']

gold_data = []
for date in dates:
    for country in brics_codes:
        # BRICS countries increasing gold imports over time
        base_qty = {'BRA': 5000, 'RUS': 8000, 'IND': 12000, 'CHN': 25000, 'ZAF': 3000}
        trend_factor = 1 + 0.01 * (date - start_date).days / 365  # Growing trend
        qty = base_qty[country] * trend_factor * (1 + np.random.normal(0, 0.15))
        value = qty * 60 * (1 + np.random.normal(0, 0.1))  # ~$60/gram

        gold_data.append({
            'refDate': date,
            'reporterISO': country,
            'flowDesc': 'Import',
            'qty': max(0, qty),
            'primaryValue': max(0, value)
        })

    for country in us_eu_codes:
        # US/EU relatively stable
        base_qty = {'USA': 8000, 'DEU': 4000, 'FRA': 3000, 'ITA': 2000, 'ESP': 1500}
        qty = base_qty[country] * (1 + np.random.normal(0, 0.12))
        value = qty * 60 * (1 + np.random.normal(0, 0.1))

        gold_data.append({
            'refDate': date,
            'reporterISO': country,
            'flowDesc': 'Import',
            'qty': max(0, qty),
            'primaryValue': max(0, value)
        })

gold_df = pd.DataFrame(gold_data)
gold_df.to_csv('Gold_TradeData_Cleaned.csv', index=False)
print(f"  ✓ Created Gold_TradeData_Cleaned.csv with {len(gold_df)} rows")

# === CREATE SAMPLE OIL DATA ===
print("Creating sample Oil data...")
oil_data = []
for date in dates:
    for country in brics_codes:
        # BRICS countries with high oil imports
        base_qty = {'BRA': 500000, 'RUS': 100000, 'IND': 1200000, 'CHN': 2500000, 'ZAF': 300000}
        trend_factor = 1 + 0.005 * (date - start_date).days / 365
        qty = base_qty[country] * trend_factor * (1 + np.random.normal(0, 0.12))
        value = qty * 0.7 * (1 + np.random.normal(0, 0.15))  # Variable oil prices

        oil_data.append({
            'refDate': date,
            'reporterISO': country,
            'flowDesc': 'Import',
            'qty': max(0, qty),
            'primaryValue': max(0, value)
        })

    for country in us_eu_codes:
        # US/EU with different patterns
        base_qty = {'USA': 800000, 'DEU': 400000, 'FRA': 300000, 'ITA': 250000, 'ESP': 200000}
        qty = base_qty[country] * (1 + np.random.normal(0, 0.1))
        value = qty * 0.7 * (1 + np.random.normal(0, 0.15))

        oil_data.append({
            'refDate': date,
            'reporterISO': country,
            'flowDesc': 'Import',
            'qty': max(0, qty),
            'primaryValue': max(0, value)
        })

oil_df = pd.DataFrame(oil_data)
oil_df.to_csv('Oil_TradeData_Cleaned.csv', index=False)
print(f"  ✓ Created Oil_TradeData_Cleaned.csv with {len(oil_df)} rows")

print("\n" + "="*70)
print("SUCCESS! Sample data created.")
print("="*70)
print("\nYou can now run: python3 generate_prediction_figures.py")
print("\nNote: This is sample data for demonstration.")
print("Replace these files with your actual cleaned data for real analysis.")
