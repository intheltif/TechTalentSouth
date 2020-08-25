"""
w3resource.com homework 
Visualization #1

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

iris.describe().plot(
  kind='area', 
  fontsize=16, 
  table=True, 
  colormap="Accent"
)

plt.xlabel('Statistics')
plt.ylabel('Value')
plt.title('General Statistics of Iris Dataset')

plt.show()
