
"""
Optional Exercise 1 of Module 3.

Reverses a string.

Author: Evert Ball
Date: July 10th, 2020
"""
import random

def main():
    """ The main entry point into the program """

    # get the input from the user
    string = input("Input a string to reverse. >> ")
    
    # print the string in reverse.
    print(string[::-1])


if __name__ == "__main__":
    main()
