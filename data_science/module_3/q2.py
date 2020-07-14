"""
Exercise 2 of Module 3.

Checks the validity of a password input by the user.
A valued password contains the following:
    *At least 1 letter between [a-z] and 1 letter between [A-Z].
    *At least 1 number between [0-9].
    *At least 1 character from [$#@].
    *Minimum length of 6 characters.
    *Maximum length of 16 characters.

Author: Evert Ball
Date: July 10th, 2020
"""
import re

def main():
    """ The main entry point into the program. """
    # TODO: This can be done better. Change it.
    userInput = input("Please enter a password: ")
    flag = 0
    if len(userInput) <= 6 or len(userInput) >= 16:
        flag = -1
    elif not re.search("[a-z]", userInput):
        flag = -1
    elif not re.search("[A-Z]", userInput):
        flag = -1
    elif not re.search("[0-9]", userInput):
        flag = -1
    elif not re.search("[$#@]", userInput):
        flag = -1
    elif re.search("\s", userInput):
        flag = -1
    else:
        flag = 0
        print("Your password is valid!")

    if flag == -1: 
        print("Not a valid password...")


if __name__ == "__main__":
    main()
    
