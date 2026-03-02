"""
Data loading and preprocessing module for time series forecasting.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_sample_data(n_points=35040):  # 4 years of hourly data
    """
    Generate synthetic energy consumption data for demonstration.
    In practice, replace this with actual data loading.
    """
    np.random.seed(42)
    
    # Create date range
    start_date = datetime(2016, 1, 1, 0, 0)
    dates = [start_date + timedelta(hours=i) for i in range(n_points)]
    
    # Generate base components
    time_idx = np.arange(n_points)
    
    # Trend: gradual increase over years
    trend = 100 + 0.001 * time_idx
    
    # Daily seasonality
    daily_pattern = 30 * np.sin(2 * np.pi * time_idx / 24 - np.pi/2)
    daily_pattern += 20 * np.sin(2 * np.pi * time_idx / 12)
    
    # Weekly seasonality
    weekly_pattern = 15 * np.sin(2 * np.pi * time_idx / (24*7))
    
    # Yearly seasonality
    yearly_pattern = 25 * np.sin(2 * np.pi * time_idx / (24*365) - np.pi/2)
    
    # Temperature effect (external factor)
    temp_base = 15 + 10 * np.sin(2 * np.pi * time_idx / (24*365) - np.pi/2)
    temp_effect = 2 * (temp_base - 15) ** 2 / 20
    
    # Noise
    noise = np.random.normal(0, 5, n_points)
    
    # Holiday effect (weekends and holidays)
    is_weekend = [d.weekday() >= 5 for d in dates]
    holiday_effect = [-15 if w else 0 for w in is_weekend]
    
    # Combine components
    consumption = (trend + daily_pattern + weekly_pattern + 
                   yearly_pattern + temp_effect + noise + holiday_effect)
    
    # Create DataFrame
    df = pd.DataFrame({
        'timestamp': dates,
        'consumption': np.maximum(consumption, 0),  # Ensure non-negative
        'temperature': temp_base + np.random.normal(0, 2, n_points),
        'is_weekend': is_weekend,
        'hour': [d.hour for d in dates],
        'day_of_week': [d.weekday() for d in dates],
        'month': [d.month for d in dates]
    })
    
    return df

def load_and_preprocess_data(filepath=None):
    """
    Load data from file or generate sample data.
    Preprocess for time series analysis.
    """
    if filepath and os.path.exists(filepath):
        # Load actual data
        df = pd.read_csv(filepath)
        df['timestamp'] = pd.to_datetime(df['timestamp'])
    else:
        # Generate sample data for demonstration
        print("No data file found. Generating sample data...")
        df = generate_sample_data()
    
    # Sort by timestamp
    df = df.sort_values('timestamp')
    
    # Set timestamp as index
    df.set_index('timestamp', inplace=True)
    
    # Handle missing values - FIXED THIS LINE
    df = df.ffill().bfill()  # Replaces fillna(method='ffill').fillna(method='bfill')
    
    # Add time features
    df['hour'] = df.index.hour
    df['day_of_week'] = df.index.dayofweek
    df['month'] = df.index.month
    df['year'] = df.index.year
    df['day_of_year'] = df.index.dayofyear
    
    return df

if __name__ == "__main__":
    # Test the loader
    df = load_and_preprocess_data()
    print(f"Data shape: {df.shape}")
    print(f"Date range: {df.index.min()} to {df.index.max()}")
    print(df.head())