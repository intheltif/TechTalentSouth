import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame
filename = "~/techtalentsouth/datascience/python/11_mod_matplotlib/data/\
company_sales_data.csv"
sales = pd.read_csv(filename)

# Create scatter plot
plt.scatter(sales['month_number'], sales['toothpaste'])

# title and label axis
plt.title("All Product Sales")
plt.xlabel("Month Number")
plt.ylabel("Sold Units Number")

# Axis limits
plt.xlim(0,12)
plt.ylim(4000, 10000)

# show grid and plot
plt.grid()
plt.show()
