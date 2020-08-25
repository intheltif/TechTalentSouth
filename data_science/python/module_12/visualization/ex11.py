"""
w3resource.com homework 
Visualization #1

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

sns.jointplot("sepal_length", "sepal_width", data=iris, color="b").plot_joint(sns.kdeplot, zorder=0, n_levels=6)
plt.show()
