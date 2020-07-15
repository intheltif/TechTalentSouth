"""
Optional Exercise 3 of Module 3.

Determines the number of uppercase and lowercase letters in a string.

Author: Evert Ball
Date: July 10th, 2020
"""
import re

def main():
    """ The main entry point into the program """

    # get the input from the user
    userInput = input("Input a sentence to caluclate the number of upper and lower case letters. >> ")
    print(f"Original String: {userInput}")

    print(f"No. of Upper case characters: {countUpperCase(userInput)}")
    print(f"No. of Lower case characters: {countLowerCase(userInput)}")
    
def countUpperCase(string):
    """ 
    Counts the number of upper case letters in a string and returns that number.
    """
    numUpperCase = 0
    for letter in string:
        if re.match("[A-Z]", letter):
            numUpperCase += 1
    return numUpperCase

def countLowerCase(string):
    """ 
    Counts the number of lower case letters in a string and returns that number.
    """
    numUpperCase = 0
    for letter in string:
        if re.match("[a-z]", letter):
            numUpperCase += 1
    return numUpperCase

if __name__ == "__main__":
    main()
