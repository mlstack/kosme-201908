#!/c/Apps/Anaconda3/python
# -*- coding: utf-8 -*-
"""
[Title] Histogram
[Author] Yibeck Lee(yibec.Lee@gmail.com)
[Contents] 
 - Histogram & Descriptive Statistics(기술통계)
"""
# %matplotlib inline

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

import pandas as pd

# font_path = 'C:/Windows/Fonts/나눔고딕코딩.ttf'
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


df = pd.read_csv("WIP_HISTORY.csv")

skew = df.skew(axis=0).tolist()
print('[왜도(skew)')
print(skew[4])

print('\n[첨도(kurt)]')
kurt = df.kurt(axis=0).tolist()
print(kurt[4])


plt.title("Histogram(Gas Pressure. bins=10) : 왜도={0:.3f}, 첨도={1:0.3f}".format(skew[4],kurt[4]))

plt.ylabel("frequency")
plt.xlabel("gas Pressure")
df['GAS_PRESSURE'].hist(bins=10)
plt.show()
