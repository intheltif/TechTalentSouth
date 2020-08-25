import pandas as pd
import matplotlib.pyplot as plt

# Creat the dataframe
filename = "~/techtalentsouth/datascience/python/11_mod_matplotlib/data/\
company_sales_data.csv"
sales = pd.read_csv(filename)

# Plot the data
plt.plot(sales.month_number, sales.total_profit,\
color='red', marker='o', linestyle='dotted', linewidth=3, label='Profits')

# Set labels
plt.xlabel('Month Number')
plt.ylabel('Sold Units Number')

# Show grid, legend, and plot
plt.grid()
plt.legend(loc='lower right')
plt.show()


