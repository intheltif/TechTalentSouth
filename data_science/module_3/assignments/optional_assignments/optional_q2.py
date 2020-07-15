"""
Optional Exercise 2 of Module 3.

Multipliese all numbers in a list

Author: Evert Ball
Date: July 10th, 2020
"""
import random

def main():
    """ The main entry point into the program """
    
    # the sample list provided in the Jupyter notebooks
    sampleList = [8, 2, 3, -1, 7]
    # multiples each element by the current product to get the product of all nums in the list
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


if __name__ == "__main__":
    main()
