"""
Exercise 1 of Module 10 of GS Jackson's Data Science course through TTS.

Add more docs here.

Author: Evert Ball
Date: 28 July 2020
"""
# Step 1
import numpy as np
import pandas as pd

# Step 2
print("Step 2")
uri = "https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv"

# Step 3
print("Step 3")
chipo = pd.read_csv(uri, sep = "\t")

# Step 4
print("Step 4")
print("=============================================\n",chipo.head(10))

# Step 5
print("Step 5")
print("=============================================\n",chipo.info())

# Step 6
print("Step 6")
print("=============================================\n",chipo.shape[1])

# Step 7
print("Step 7")
print("=============================================\n",chipo.columns)

# Step 8
print("Step 8")
print("=============================================\n",chipo.index)

# Step 9 & Step 10
print("Step 9")
print("Step 10")
item = chipo.groupby("item_name")
item = item.sum()
item = item.sort_values(["quantity"], ascending=False)
print("=============================================\n",item.head(1))

# Step 11
print("Step 11")
item = chipo.groupby("choice_description").sum()
item = item.sort_values(['quantity'], ascending=False)
print("=============================================\n",item.head(1))

# Step 12
print("Step 12")
total_items_ordered = chipo.quantity.sum()
print("=============================================\n",total_items_ordered)

# Step 13
print("Step 13")
# 13.a
print("=============================================\n",chipo.item_price.dtype)
# 13.b
change = lambda x: float(x[1:-1])
chipo.item_price = chipo.item_price.apply(change)
# 13.c
print(chipo.item_price.dtype)

# Step 14
print("Step 14")
revenue = (chipo['quantity']* chipo['item_price']).sum()
print("=============================================\n")
print("Revenue was: $" + str(np.round(revenue,2)))

# Step 15
orders = chipo.order_id.value_counts().count()
print("Step 15")
print("=============================================\n", orders)

# Step 16
print("Step 16")
chipo['revenue'] = chipo['quantity'] * chipo['item_price']
order_grouped = chipo.groupby(by=['order_id']).sum()
print("=============================================\n",order_grouped.mean()['revenue'])

# Step 17
print("Step 17")
print("=============================================\n",chipo.item_name.value_counts().count())

