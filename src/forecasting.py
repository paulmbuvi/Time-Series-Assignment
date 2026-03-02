"""
Forecasting models for time series prediction.
"""

import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_absolute_error, mean_squared_error
import warnings
warnings.filterwarnings('ignore')

def prepare_forecast_data(df, target_col='consumption', test_size=0.2):
    """
    Prepare data for forecasting by creating train/test splits.
    """
    # Ensure data is sorted by date
    df = df.sort_index()
    
    # Split data (maintain temporal order)
    split_idx = int(len(df) * (1 - test_size))
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]
    
    return train, test

def fit_sarima_model(train, seasonal_periods=24):
    """
    Fit SARIMA model to the training data.
    """
    # SARIMA(1,1,1)(1,1,1,24) - example configuration
    model = SARIMAX(
        train['consumption'],
        order=(1, 1, 1),
        seasonal_order=(1, 1, 1, seasonal_periods),
        enforce_stationarity=False,
        enforce_invertibility=False
    )
    
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        results = model.fit(disp=False)
    
    return results

def generate_forecast(model, steps=168):  # 7 days of hourly data
    """
    Generate forecasts using trained model.
    """
    forecast = model.forecast(steps=steps)
    forecast_index = pd.date_range(
        start=pd.Timestamp.now().normalize(),
        periods=steps,
        freq='h'
    )
    
    forecast_df = pd.DataFrame({
        'timestamp': forecast_index,
        'forecast': forecast.values,
        'lower_bound': forecast.values - 2 * np.std(forecast.values),
        'upper_bound': forecast.values + 2 * np.std(forecast.values)
    })
    
    return forecast_df

def evaluate_forecast(y_true, y_pred):
    """
    Calculate forecast accuracy metrics.
    """
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    
    return {
        'MAE': mae,
        'MSE': mse,
        'RMSE': rmse,
        'MAPE': mape
    }

def decompose_time_series(df, period=24):
    """
    Perform time series decomposition into trend, seasonal, and residual components.
    """
    decomposition = seasonal_decompose(
        df['consumption'], 
        model='additive',
        period=period
    )
    
    return decomposition

if __name__ == "__main__":
    # Test the forecasting functions
    from data_loader import load_and_preprocess_data
    
    # Load data
    df = load_and_preprocess_data()
    
    # Prepare data
    train, test = prepare_forecast_data(df)
    
    # Fit model (using subset for speed)
    model = fit_sarima_model(train.iloc[-1000:])
    
    # Generate forecast
    forecast = generate_forecast(model, steps=24)
    
    print("Forecast for next 24 hours:")
    print(forecast.head())