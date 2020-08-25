"""
w3resource.com homework 
Basic #1

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd

# The number of rows to show.
ROWS = 3

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)
print("Shape:", iris.shape)
print("Data Type:", type(iris))
print("First 3 Rows:\n", iris.head(ROWS))
