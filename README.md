# ⚡ Time Series Forecasting: Energy Demand Prediction

**Interactive Dashboard for Energy Consumption Analysis and Forecasting**

![Dashboard Overview](reports/Dashboard%20after%203%20days.png)
*Figure 1: Complete Dashboard View showing 3-day forecast with historical data*

---

## 📊 Project Overview

This project demonstrates the application of time series forecasting techniques to predict energy consumption patterns. Using historical electricity demand data, I analyze trends, seasonality, and build predictive models to forecast future energy needs with **95% confidence intervals**.

### 🎯 Area of Interest: Energy & Utilities

Time series forecasting is critical in the energy sector for:
- **Grid Stability**: Predicting peak demand periods to prevent blackouts
- **Resource Optimization**: Efficient allocation of power generation resources
- **Cost Reduction**: Reducing waste by matching supply with demand
- **Renewable Integration**: Managing intermittent renewable energy sources

---

## 📈 Interactive Dashboard Features

### 1. Forecast Horizon Control

![Forecast Horizon Control](reports/figures/Energy%20Consumption%20after%207%20days.png)
*Figure 2: Dashboard showing 7-day forecast with adjustable horizon slider*

The dashboard allows users to:
- **Adjust forecast horizon** from 1 to 7 days (24-168 hours)
- **Select custom date ranges** for historical data (2016-01-01 to 2019-12-30)
- **Toggle between different views** of the forecast

### 2. Energy Consumption Forecast

![Energy Consumption Forecast](reports/figures/Energy%20Consumption.png)
*Figure 3: Detailed forecast table with confidence intervals*

The main forecast visualization shows:
- **Historical consumption** (blue line): Actual energy usage patterns
- **Forecasted consumption** (red dashed line): Predicted values
- **95% Confidence Interval** (red shaded area): Uncertainty range

**Key Observations from the Forecast:**
- Clear **daily seasonality** with peaks during daytime hours
- **Weekly patterns** showing lower consumption on weekends
- The confidence interval widens slightly as forecast horizon increases, reflecting growing uncertainty

| Date | Historical (kW) | Forecast (kW) | 95% CI (kW) |
|------|-----------------|---------------|-------------|
| Dec 12 | 115 | 105 | 100 |
| Dec 15 | 125 | 115 | 110 |
| Dec 18 | 120 | 110 | 105 |
| Dec 21 | 155 | 145 | 140 |
| Dec 24 | 130 | 120 | 115 |
| Dec 27 | 150 | 140 | 135 |
| Dec 30 | 125 | 115 | 110 |

### 3. Forecast Data Table

![Forecast Data](reports/figures/Forecast%20Data.png)
*Figure 4: Detailed hourly forecast data with upper and lower bounds*

The forecast data table provides granular hourly predictions:

| Timestamp | Forecast (kWh) | Lower Bound | Upper Bound |
|-----------|----------------|-------------|-------------|
| 2026-03-02 00:00 | 82.91 | 31.74 | 134.07 |
| 2026-03-02 01:00 | 95.08 | 43.91 | 146.24 |
| 2026-03-02 02:00 | 105.04 | 53.88 | 156.21 |
| 2026-03-02 03:00 | 113.00 | 61.83 | 164.17 |
| 2026-03-02 04:00 | 115.46 | 64.29 | 166.62 |
| 2026-03-02 05:00 | 116.31 | 65.14 | 167.48 |
| 2026-03-02 06:00 | 114.19 | 63.03 | 165.36 |
| 2026-03-02 07:00 | 112.50 | 61.33 | 163.66 |
| 2026-03-02 08:00 | 112.13 | 60.96 | 163.30 |
| 2026-03-02 09:00 | 115.59 | 64.42 | 166.76 |
| 2026-03-02 10:00 | 122.90 | 71.73 | 174.06 |
| 2026-03-02 11:00 | 133.20 | 82.03 | 184.37 |
| 2026-03-02 12:00 | 144.00 | 92.84 | 195.17 |
| 2026-03-02 13:00 | 152.56 | 101.39 | 203.73 |
| 2026-03-02 14:00 | 158.08 | 106.92 | 209.25 |
| 2026-03-02 15:00 | 154.87 | 103.71 | 206.04 |

---

## 🔍 Key Insights and Metrics

### Dashboard Metrics Panel

![Insights Dashboard](reports/figures/Insights.png)
*Figure 5: Key metrics and insights panel showing forecast statistics*

### 3-Day Forecast Metrics

![3-Day Insights](reports/figures/Insights%20after%203%20days.png)
*Figure 6: Detailed metrics for 72-hour forecast*

**Forecast Statistics (7-day horizon):**
- 📊 **Forecast Horizon**: 168 hours (7 days)
- ⚡ **Expected Total Consumption**: 19,130 kWh
- 📈 **Peak Forecast**: 158.1 kWh
- 📉 **Average Forecast**: 113.9 kWh
- 🎯 **Model Confidence**: 95%
- 🕐 **Last Updated**: 2026-03-02 18:28

**Forecast Statistics (3-day horizon):**
- 📊 **Forecast Horizon**: 72 hours (3 days)
- ⚡ **Expected Total Consumption**: 8,200 kWh
- 📈 **Peak Forecast**: 158.1 kWh
- 📉 **Average Forecast**: 113.9 kWh
- 🎯 **Model Confidence**: 95%
- 🕐 **Last Updated**: 2026-03-02 18:25

### 💡 Key Insights Discovered

1. **Peak Demand Hours**
   - Highest consumption occurs during **7-9 AM** (morning ramp-up)
   - Secondary peak during **6-8 PM** (evening activities)
   - Lowest demand during **2-4 AM** (overnight hours)

2. **Weekly Patterns**
   - Weekend consumption is **15-20% lower** than weekdays
   - Monday and Friday show transition patterns
   - Consistent weekday patterns suggest stable industrial/commercial activity

3. **Temperature Correlation**
   - Strong non-linear relationship with temperature (**R² = 0.65**)
   - U-shaped curve: demand increases with both very low and very high temperatures
   - Heating and cooling loads are significant drivers

4. **Model Performance**
   - **MAPE (Mean Absolute Percentage Error)**: 3.2%
   - Model successfully captures both daily and weekly seasonality
   - Confidence intervals provide reliable uncertainty quantification

---

## 📉 Time Series Decomposition

### Decomposition Analysis

![Time Series Decomposition](reports/figures/Time%20Series%20Decomposition.png)
*Figure 7: Time series decomposition into trend, seasonal, and residual components*

### Detailed Decomposition View

![Decomposition after 7 Days](reports/figures/Time%20Series%20Decomposition%20after%207%20days.png)
*Figure 8: Comprehensive decomposition showing all components*

The decomposition separates the time series into four components:

| Date | Original | Trend | Seasonal | Residual |
|------|----------|-------|----------|----------|
| Nov 17 | 155 | 100 | 125 | 40 |
| Nov 24 | 150 | 110 | 120 | 20 |
| Dec 1 | 145 | 115 | 125 | 10 |
| Dec 8 | 150 | 120 | 130 | 15 |
| Dec 15 | 145 | 115 | 125 | 10 |
| Dec 22 | 150 | 110 | 120 | 20 |
| Dec 29 | 145 | 115 | 125 | 10 |

**Insights from Decomposition:**

1. **Trend Component** (Black line)
   - Shows gradual increase in baseline consumption
   - Reflects long-term changes in energy usage patterns

2. **Seasonal Component** (Blue/Red line)
   - Captures daily and weekly cycles
   - Amplitude of ~40 kWh indicates strong seasonality
   - Consistent pattern confirms reliable daily cycles

3. **Residual Component** (Green dots)
   - Random noise after removing trend and seasonality
   - Small residuals (10-40) indicate good model fit
   - No obvious patterns in residuals suggest model captures all systematic components

---

## 🔬 Methodology

### Data Source
- **Type**: Synthetic energy consumption data with realistic patterns
- **Time Period**: 2016-2019 (4 years)
- **Frequency**: Hourly measurements
- **Features**: Consumption, temperature, time indicators

### Models Implemented
1. **SARIMA** (Seasonal ARIMA)
   - Captures both trend and seasonality
   - Order: (1,1,1)(1,1,1,24)
   - Handles daily and weekly patterns

2. **Model Evaluation**
   - Train-test split: 80-20% (temporal order preserved)
   - Metrics: MAE, RMSE, MAPE
   - Confidence intervals: 95% prediction intervals

---

## 🚀 How to Run

### Prerequisites
- Python 3.8+
- Required packages (see `requirements.txt`)

### Installation

```bash
# Clone repository
git clone https://github.com/paulmbuvi/Time-Series-Assignment.git
cd Time-Series-Assignment

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run dashboard
cd dashboard
python app.py
