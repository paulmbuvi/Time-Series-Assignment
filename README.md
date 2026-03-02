# Time Series Forecasting: Energy Demand Prediction

## 📊 Project Overview
This project demonstrates the application of time series forecasting techniques to predict energy consumption patterns. Using historical electricity demand data, we analyze trends, seasonality, and build predictive models to forecast future energy needs.

## 🎯 Area of Interest: Energy & Utilities
Time series forecasting is critical in the energy sector for:
•⁠  ⁠*Grid Stability*: Predicting peak demand periods to prevent blackouts
•⁠  ⁠*Resource Optimization*: Efficient allocation of power generation resources
•⁠  ⁠*Cost Reduction*: Reducing waste by matching supply with demand
•⁠  ⁠*Renewable Integration*: Managing intermittent renewable energy sources

## 📈 Dataset
•⁠  ⁠*Source*: [Electricity Consumption Dataset from UCI/OpenTS-Bench]
•⁠  ⁠*Time Period*: 2016-2019
•⁠  ⁠*Frequency*: Hourly measurements
•⁠  ⁠*Features*: 
  - Timestamp
  - Energy consumption (kWh)
  - Temperature (external factor)
  - Holiday indicators

## 🔬 Methodology

### Exploratory Data Analysis
1.⁠ ⁠*Time Series Decomposition*: Separated data into trend, seasonal, and residual components
2.⁠ ⁠*Stationarity Testing*: Used ADF test to check for stationarity
3.⁠ ⁠*Autocorrelation Analysis*: ACF/PACF plots to identify AR/MA terms

### Forecasting Models Implemented
1.⁠ ⁠*SARIMA* (Seasonal ARIMA): Captures both trend and seasonality
2.⁠ ⁠*Prophet*: Facebook's forecasting tool for business time series
3.⁠ ⁠*LSTM*: Deep learning approach for complex patterns

### Key Insights
1.⁠ ⁠*Daily Seasonality*: Clear morning (7-9 AM) and evening (6-8 PM) consumption peaks
2.⁠ ⁠*Weekly Patterns*: 15-20% lower consumption on weekends
3.⁠ ⁠*Temperature Correlation*: Strong non-linear relationship (R² = 0.65) with cooling demand
4.⁠ ⁠*Holiday Effect*: 25% reduction on major holidays

## 📊 Interactive Dashboard Features
•⁠  ⁠*Historical Data Viewer*: Visualize consumption patterns over time
•⁠  ⁠*Forecast Horizon Control*: Adjust prediction window (1-30 days)
•⁠  ⁠*Model Comparison*: Toggle between different forecasting models
•⁠  ⁠*Decomposition View*: Separate trend and seasonality components
•⁠  ⁠*Export Functionality*: Download forecasts as CSV

## 🚀 How to Run

### Prerequisites
•⁠  ⁠Python 3.8+
•⁠  ⁠VS Code with Python extension
•⁠  ⁠Git

### Installation

1.⁠ ⁠*Clone the repository*
```bash
git clone https://github.com/yourusername/time-series-forecasting-assignment.git
cd time-series-forecasting-assignment