"""
w3resource.com homework 
Visualization #18

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

box_data = iris #variable representing the data array
box_target = iris.species #variable representing the labels array
sns.boxplot(data = box_data,width=0.5,fliersize=5)
sns.set(rc={'figure.figsize':(2,15)})
plt.show()
