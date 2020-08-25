import pandas as pd
import matplotlib.pyplot as plt

# Read in the file
filename = "~/techtalentsouth/datascience/python/11_mod_matplotlib/data/\
company_sales_data.csv"
sales = pd.read_csv(filename)

# Create scatter plot and set title and labels
plt.bar(sales['month_number'], sales['facewash'], label="facewash", width=0.25)
plt.bar(sales['month_number'] + 0.25, sales['facecream'], label="facecream", width=0.25)

# Set title, labels
plt.title("Exercise 5")
plt.xlabel("Month Number")
plt.ylabel("Number of Units Sold")

# Apply grid and show
plt.grid()
plt.legend()
plt.show()
