import pandas as pd
import numpy as np

chip = pd.read_csv("~/Desktop/en.openfoodfacts.org.products.tsv", sep="\t")

print("=========================HEAD=========================")
print(chip.head())
print("=========================TAIL=========================")
