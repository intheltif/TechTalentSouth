import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame
filename = "~/techtalentsouth/datascience/python/11_mod_matplotlib/data/\
company_sales_data.csv"
sales = pd.read_csv(filename)

# Create list of column names and iterate over them creating a lineplot for each
cols = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]
for col in cols:
    plt.plot("month_number", col, data=sales)

# show grid and legend and show plot
plt.grid()
plt.legend()
plt.show()
