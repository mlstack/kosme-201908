#!/c/Apps/Anaconda3/python
# -*- coding: utf-8 -*-
"""
[Title] Histogram
[Author] Yibeck Lee(yibec.Lee@gmail.com)
[Contents] 
 - Histogram & Descriptive Statistics(기술통계)
"""
# %matplotlib inline
import pandas as pd

df = pd.read_csv("WIP_HISTORY.csv")

print('\n[df.info()]')
print(df.info())

print(list(df))

print('\n[df.columns]')
print(df.columns)


print('\n[df.columns --> list]')
column_list = df.columns.tolist()
print(column_list,'\n')
print('[type(column_list)]', type(column_list))


print('[df.head')
print(df.head)

print('[df.tail')
print(df.tail)



