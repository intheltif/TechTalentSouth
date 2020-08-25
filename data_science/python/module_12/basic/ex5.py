"""
w3resource.com homework 
Basic #5

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

print(iris.describe())
