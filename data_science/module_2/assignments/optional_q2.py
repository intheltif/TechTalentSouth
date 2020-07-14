"""
Optional Exercise 2 from Module 2.

Checks whether an element exists within a tuple.

Author: Evert Ball
Date: July 7th, 2020
"""

import math

def main():
    """
    The main entry point into the program.
    """
    sampleTuple = ("this", 1, "is", "a", "tuple")
    print(doesTupleContain(sampleTuple, "this"))

def doesTupleContain(tupl, check):
    """
    Converts a tuple to a string with spaces between each element.
    """
    for element in tupl:
        if element == check:
            return True
    return False

if __name__ == "__main__":
    main()
