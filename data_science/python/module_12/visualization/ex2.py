"""
w3resource.com homework 
Visualization #2

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)
ax=plt.subplots(1,1)
sns.countplot('species',data=iris)
plt.title("Iris Species Count")
plt.show()
