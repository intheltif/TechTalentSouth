"""
Exercise 5 of Module 3.

Takes inter as user input to determine if user is weird or not weird.

Exit Codes:
    1 - User input was not an integer.

Author: Evert Ball
Date: July 15th, 2020
"""
import sys

def main():
    """ The main entry point into the program. """
    try:
        userInput = int(input("Input a number to see if you are weird or not weird. >> "))
    except ValueError:
        print("\nPlease input an integer...\n")
        sys.exit(1)
    # Check even or odd
    if (userInput % 2) == 0:
        # Even so do further checks
        if userInput in range(2, 6):
            print("Not Weird")
        elif userInput in range(6, 21):
            print("Weird")
        elif userInput > 20:
            print("Not Weird")
    else:
        print("weird")

if __name__ == "__main__":
    main()
