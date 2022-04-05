# -*- coding: utf-8 -*-
"""Timeseries data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14XkU2gb2C6JqPosAaeEgJ1gnCtmfffWO
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#loading the dataset
df = pd.read_csv("https://github.com/HamoyeHQ/HDSC-Time-series-analysis-and-forecast/files/7768846/Time_series_analysis_and_forecast_DATASET.csv")
df.head()

#convert FullDate column to datetime
df["FullDate"] = pd.to_datetime(df["FullDate"])
df.set_index("FullDate", inplace=True)
plt.figure(figsize=(10,6))
plt.plot(df.index, df.ElecPrice, '--', marker='*',)
plt.grid()
plt.xlabel('Year')
plt.ylabel('ElecPrice')

#Downsampling to daily data points
df_daily = df.resample('3M').mean()
df_daily.plot()
plt.figure(figsize=(10,6))
plt.show()

from statsmodels.tsa.stattools import adfuller
adf_result = adfuller(df['SysLoad'])
print(f'ADF Statistic: {adf_result[0]}')
print(f'p_value: {adf_result[1]}')
print(f'No. of lags used: {adf_result[2]}')
print(f'No. of observations used: {adf_result[3]}')
print('Critical Values:')
for k, v in adf_result[4].items():
  print(f'   {k}: {v}')

from statsmodels.tsa.stattools import adfuller
adf_result = adfuller(df['GasPrice'])
print(f'ADF Statistic: {adf_result[0]}')
print(f'p_value: {adf_result[1]}')
print(f'No. of lags used: {adf_result[2]}')
print(f'No. of observations used: {adf_result[3]}')
print('Critical Values:')
for k, v in adf_result[4].items():
  print(f'   {k}: {v}')

from statsmodels.tsa.stattools import adfuller
adf_result = adfuller(df['ElecPrice'])
print(f'ADF Statistic: {adf_result[0]}')
print(f'p_value: {adf_result[1]}')
print(f'No. of lags used: {adf_result[2]}')
print(f'No. of observations used: {adf_result[3]}')
print('Critical Values:')
for k, v in adf_result[4].items():
  print(f'   {k}: {v}')