#!/c/Apps/Anaconda3/python
# -*- coding: utf-8 -*-
"""
[Title] CP, CPK
[Author] Yibeck Lee(yibec.Lee@gmail.com)
[Contents] 
 - Python Version : CP, CPK
[Reference]
 - https://matplotlib.org/3.1.0/gallery/statistics/histogram_features.html
 - https://gist.github.com/countrymarmot/8413981
"""
# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def Cp(values, usl, lsl):
    arr = np.array(values)
    arr = arr.ravel()
    sigma = np.std(arr)
    Cp = float(usl - lsl) / (6*sigma)
    return Cp


def Cpk(values, usl, lsl):
    arr = np.array(values)
    arr = arr.ravel()
    sigma = np.std(arr)
    m = np.mean(arr)

    Cpu = float(usl - m) / (3*sigma)
    Cpl = float(m - lsl) / (3*sigma)
    Cpk = np.min([Cpu, Cpl])
    return Cpk


if __name__ == "__main__":

	# example data
	mu = 100  # mean of distribution
	sigma = 15  # standard deviation of distribution
	x = mu + sigma * np.random.randn(437)
	LSL = 0
	USL = 150
	CP = Cp(values=x, usl=USL, lsl=LSL)
	print('CP = ', CP)
	CPK = Cpk(values=x, usl=USL, lsl=LSL)
	print('CPK = ', CPK)


	num_bins = 50

	fig, ax = plt.subplots()

	# the histogram of the data
	n, bins, patches = ax.hist(x, num_bins, density=1)

	# add a 'best fit' line
	y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
	     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
	ax.plot(bins, y, '--')
	ax.set_xlabel('Smarts')
	ax.set_ylabel('Probability density')
	ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')
	ax.axvline(LSL, color='k', linestyle='dashed', linewidth=3)
	ax.axvline(USL, color='k', linestyle='dashed', linewidth=3)
	ax.text(120, .03, r'CP={}'.format(CP))
	ax.text(120, .025, r'CPK={}'.format(CPK))
	# Tweak spacing to prevent clipping of ylabel
	fig.tight_layout()
	plt.show()


	df = pd.read_csv("WIP_HISTORY.csv")
	print(df.describe())

	PARAMETER_VALUES = df['GAS_PRESSURE'].tolist()
	PARAMETER_LABEL = 'Gas Pressure'
	mu = np.average(PARAMETER_VALUES)
	sigma = np.std(PARAMETER_VALUES)
	LSL = 0
	USL = 500
	print(mu,sigma, LSL, USL)
	n, bins, patches = plt.hist(PARAMETER_VALUES, 50, density=True)
	CP = Cp(values=PARAMETER_VALUES, usl=USL, lsl=LSL)
	print('CP = ', CP)
	CPK = Cpk(values=PARAMETER_VALUES, usl=USL, lsl=LSL)
	print('CPK = ', CPK)
	y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
	     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

 
	plt.xlabel(PARAMETER_LABEL)
	plt.ylabel('Probability')
	plt.title('Intensity')
	plt.axvline(LSL, color='k', linestyle='dashed', linewidth=3)
	plt.axvline(USL, color='k', linestyle='dashed', linewidth=3)
	plt.text(450, .007, r'CP={}'.format(CP))
	plt.text(450, .008, r'CPK={}'.format(CPK))
	plt.axis([0, 500, 0, 0.01])
	plt.grid(True) # True or False
	plt.plot(bins, y, '--') 
	fig.tight_layout()
	plt.show()
