"""
w3resource.com homework 
Visualization #14

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

sub=iris[iris['species']=='setosa']
sns.kdeplot(
    sub['sepal_length'],
    sub['sepal_width'],
    cmap="plasma", 
    shade=True, 
    shade_lowest=False
)
plt.title('Setosa')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.show()
