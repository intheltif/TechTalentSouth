"""
w3resource.com homework 
Visualization #8

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

fig=sns.jointplot(x='sepal_length', y='sepal_width', kind="hex", color="red", data=iris)
plt.show()
