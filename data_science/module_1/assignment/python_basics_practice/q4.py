"""
Question 4 of Python Basics Practice from Module 1.

Author: Evert Ball
Date: 06/27/2020
"""
# Constant to avoid magic numbers
MULTIPLICAND = 4
# Range is exclusive so we use 0 through 11
for multiplier in range(0, 11):
    product = MULTIPLICAND * multiplier
    print(f'{MULTIPLICAND} multiplied by {multiplier} is {product}')
