"""
Exercise 2 of Module 2. This program computes the hash value of a tuple of 
integers entered by the user.

Author: Evert Ball
Date: July 7th, 2020
"""

import math

def main():
    """
    The main entry point into the program.
    """

    userInput = input("Please enter a list of space separated integers: ")
    numsArray = userInput.split(" ")
    index = 0
    for num in numsArray:
        numsArray[index] = int(num)
        index += 1
    t = tuple(numsArray)
    print(hash(t))

if __name__ == "__main__":
    main()
