"""
Question 5 of Python Basics Practice from Module 1.

    Please refer to PEP 498 for details about f-string and 
    literal string interpolation.

Author: Evert Ball
Date: 06/27/2020
"""

# Nested for loop that uses f-strings to easily print the table
for i in range(1, 11):
    for j in range(1, 11):
        # Using f-string to find the product, format into a table, and print 
        # without a newline
        print(f'{i*j:4d}', end = "")
    # Print a new line for each multiplicand
    print("") 
