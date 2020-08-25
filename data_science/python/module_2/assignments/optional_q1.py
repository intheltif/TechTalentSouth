"""
Optional Exercise 1 from Module 2.

Converts a tuple to a string.

Author: Evert Ball
Date: July 7th, 2020
"""

import math

def main():
    """
    The main entry point into the program.
    """
    sampleTuple = ("this", 1, "is", "a", "tuple")
    print(convertTupleToStr(sampleTuple))

def convertTupleToStr(tupl):
    """
    Converts a tuple to a string with spaces between each element.
    """
    string = ""
    for element in tupl:
        string += str(element) + " "
    return string

if __name__ == "__main__":
    main()
