"""
Exercise 3 of Module 2. Takes two lists and computes a third list by picking 
odd-index values from list 1 and even-index values from list 2.

Author: Evert Ball
Date: July 7th, 2020
"""

import math

def main():
    """
    The main entry point into the program.
    """
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]
    listThree = []

    index = 0;
    while(index < len(listOne)):
        if((index % 2) == 0):
            listThree.append(listTwo[index])
        else:
            listThree.append(listOne[index])
        index += 1
    print(listThree)



if __name__ == "__main__":
    main()
