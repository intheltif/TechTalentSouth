"""
Exercise 5 of Module 2.

Iterates through a given list and checks if a given element already exists in
the dictionary as a keys value. If not, it deletes it from the list.

Author: Evert Ball
Date: July 7th, 2020
"""

import math

def main():
    """
    The main entry point into the program.
    """
    sampleDict = {"Zach":47, "Emma":69, "Kelly":76, "Jason":97}
    rollNumber = [47, 64, 69, 37, 76, 83, 95, 97]
    newList = []
    for num in rollNumber:
        if num in sampleDict.values():
            newList.append(num)
    print(newList)

if __name__ == "__main__":
    main()
