#!/c/Apps/Anaconda3/python
# -*- coding: utf-8 -*-
"""
[Title] Histogram
[Author] Yibeck Lee(yibec.Lee@gmail.com)
[Contents] 
 - Histogram & Descriptive Statistics(기술통계)
"""
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("WIP_HISTORY.csv")
print('[기술통계량(Gas Pressure)]')
print(df['GAS_PRESSURE'].describe())


plt.rcParams["figure.figsize"] = (20, 10)

plt.subplot(1,3,1)
plt.title("Histogram(Gas Pressure. bins=3)")
plt.ylabel("frequency")
plt.xlabel("gas Pressure")
df['GAS_PRESSURE'].hist(bins=3)

plt.subplot(1,3,2)
plt.title("Histogram(Gas Pressure. bins=5)")
plt.ylabel("frequency")
plt.xlabel("gas Pressure")
df['GAS_PRESSURE'].hist(bins=5)

plt.subplot(1,3,3)
plt.title("Histogram(Gas Pressure. bins=10)")
plt.ylabel("frequency")
plt.xlabel("gas Pressure")
df['GAS_PRESSURE'].hist(bins=10)

plt.show()

