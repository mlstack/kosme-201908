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

print(df.describe())
percentile = df.quantile([0.,0.001,0.1,0.25,0.5,0.75,0.999,1.0], numeric_only=False)

print(percentile)

