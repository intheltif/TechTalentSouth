"""
w3resource.com homework 
Visualization #3

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

ax = plt.subplots(1,1)
iris['species'].value_counts().plot.pie(
  explode=[0.1,0.1,0.1],
  autopct='%1.1f%%',
  shadow=True,
)

plt.title('Iris Species %')
plt.show()
