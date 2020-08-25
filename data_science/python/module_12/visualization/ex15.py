"""
w3resource.com homework 
Visualization #15

Author: Evert Ball
Version: 18 August 2020
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Read in the data and print out basic info
url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv'
iris = pd.read_csv(url)

sns.kdeplot(
    iris['petal_length'],
    iris['petal_width'],
    cmap="plasma",
    shade=True,
    shade_lowest=False
)

plt.title('Setosa')
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.show()
