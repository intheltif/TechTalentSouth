"""
Exercise 4 of Module 2.

Slices a provided list into three equal chunks and reverses each list.

Author: Evert Ball
Date: July 7th, 2020
"""

import math

def main():
    """
    The main entry point into the program.
    """
    sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    newList = splitList(sampleList, 3)
    for lst in newList:
        # The below statement reverses a list
        print(lst[::-1])


def splitList(lst, n):
    """
    Using float arithmetic, splits a list into n equal parts.
    """
    div = len(lst) / float(n)
    return [lst[round(div * i):round(div * (i + 1))] for i in range(n)]

if __name__ == "__main__":
    main()
