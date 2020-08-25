"""
w3resource.com homework 
Visualization #13

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

g = sns.jointplot(x="sepal_length", y="sepal_width", data=iris, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=40, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$sepal_length$", "$sepal_width$")
plt.show()
