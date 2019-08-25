#!/c/Apps/Anaconda3/python
# -*- coding: utf-8 -*-
"""
[Title] Multi-Dimension Chart
[Author] Yibeck Lee(yibec.Lee@gmail.com)
[Contents] 
 - Multi-Dimension Chart for FDC Parameters
[Reference]
 - https://matplotlib.org/3.1.0/gallery/images_contours_and_fields/image_annotated_heatmap.html
[requirememt]
 - conda install -c anaconda pandasql 
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd
from pandasql import sqldf

# font_path = 'C:/Windows/Fonts/나눔고딕코딩.ttf'
font_path = 'C:/Windows/Fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

pysqldf = lambda q: sqldf(q, globals())

df = pd.read_csv("WIP_HISTORY.csv")

# print(df.columns)
# Index(['TARGET_VALUE', 'GOOD_BAD', 'LINE', 'EQUIPMENT', 'GAS_PRESSURE',
       # 'TEMPERATURE', 'THICKNESS', 'WAITING_TIME', 'PROCESS_TIME', 'INTENSITY',
       # 'RPM', 'TIME_GAP', 'SPEED']
# df = df[['TARGET_VALUE','GAS_PRESSURE', 'TEMPERATURE', 'THICKNESS','WAITING_TIME','PROCESS_TIME','INTENSITY','RPM','TIME_GAP','SPEED']]

# sqlDf = pysqldf("select * from df  limit 10;")
# print(sqlDf)
sqlDf = pysqldf("select LINE, EQUIPMENT, avg(TIME_GAP) as AVG_TIME_GAP from df group by LINE, EQUIPMENT ;")
print(sqlDf)
pivotDf = sqlDf.pivot(index='LINE', columns='EQUIPMENT', values='AVG_TIME_GAP')
pivotDf = pivotDf.round(0)

print(pivotDf.values)

matrix = pivotDf.values
LINE = ['LIME_1', 'LINE_2', 'LIME_3']
EQUIPMENT = ['EQP_1', 'EQP_2', 'EQP_3', 'EQP_4']

fig, ax = plt.subplots()
im = ax.imshow(matrix)

# We want to show all ticks...
ax.set_xticks(np.arange(len(EQUIPMENT)))
ax.set_yticks(np.arange(len(LINE)))
# ... and label them with the respective list entries
ax.set_xticklabels(EQUIPMENT)
ax.set_yticklabels(LINE)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(LINE)):
    for j in range(len(EQUIPMENT)):
        text = ax.text(j, i, matrix[i, j],
                       ha="center", va="center", color="w")

ax.set_title("라인/설비 평균 Time Gap")
fig.tight_layout()
plt.show()


def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (N, M).
    row_labels
        A list or array of length N with the labels for the rows.
    col_labels
        A list or array of length M with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # We want to show all ticks...
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_yticks(np.arange(data.shape[0]))
    # ... and label them with the respective list entries.
    ax.set_xticklabels(col_labels)
    ax.set_yticklabels(row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    for edge, spine in ax.spines.items():
        spine.set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar


def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=["black", "white"],
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A list or array of two color specifications.  The first is used for
        values below a threshold, the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

fig, ax = plt.subplots()
im, cbar = heatmap(matrix, LINE, EQUIPMENT, ax=ax,
                   cmap="YlGn", cbarlabel="평균 Time Gap")
texts = annotate_heatmap(im, valfmt="{x:.1f} t")
fig.tight_layout()
plt.show()