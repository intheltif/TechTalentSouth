import pandas as pd
import matplotlib.pyplot as plt

# Create DataFrame from csv
filename = "~/techtalentsouth/datascience/python/11_mod_matplotlib/data/\
company_sales_data.csv"
sales = pd.read_csv(filename)

# Create the line plot
plt.plot(sales.month_number, sales.total_profit)

# Set title, axis labels
plt.title('Total Profit of All Months')
plt.xlabel('Month')
plt.ylabel('Total Profit')

# Set axis limits
plt.xlim(1,12)
plt.ylim(150000, 450000)

# Apply grid and show the lineplot
plt.grid()
plt.show()
