"""
Group Exercise 2 from the Jupyter Notebooks for GS Jackson's TTS Data Science
course.

Finds all files in the given directory from command line argument and prints
them to the screen in a sorted order.

Author: Evert Ball
Date: 20 July 2020
"""
import sys
import os

def main():
    " The main entry point into the program. "
    dirName = sys.argv[1]
    listOfFiles = getListOfFiles(dirName)
    for f in sorted(listOfFiles):
        print(f)

def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()

    # Iterate over all the entries
    for entry in listOfFile:

        # Create full path
        fullPath = os.path.join(dirName, entry)

        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
    return allFiles


if __name__ == "__main__":
    main()
