"""
w3resource.com homework 
Visualization #17

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

X = iris.iloc[:, 0:4]
f, ax = plt.subplots()
corr = X.corr()
print(corr)
sns.heatmap(
    corr, mask=np.zeros_like(corr, dtype=np.bool), 
    cmap=sns.diverging_palette(220, 10, as_cmap=True),
    square=True, ax=ax, linewidths=.5)
plt.show()
