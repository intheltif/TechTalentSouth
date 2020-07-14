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
    sampleTuple = (100, 200, 300)
    print(tupleStrFormat(sampleTuple))

def tupleStrFormat(tupl):
    """
    Converts a tuple to a string with spaces between each element.
    """
    string = "this is a tuple ("
    for element in tupl:
        string += str(element) + ", "
    string += ")"
    return string

if __name__ == "__main__":
    main()
