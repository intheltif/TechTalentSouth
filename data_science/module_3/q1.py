"""
Exercise 1 of Module 3.

The program guesses a number between 1 and 9 given by the user.

Author: Evert Ball
Date: July 10th, 2020
"""
import random

def main():
    """ The main entry point into the program """
    userNum = -1
    randNum = random.randint(1,9)
    try:
        userNum = int(input("Please enter a number between 1 and 9. I'll try to guess it! >> "))
        if userNum < 1 or userNum > 9:
            raise ValueError("You did not enter a number between 1 and 9")
    except ValueError:
        print("Incorrect value entered. Exiting program...")
        exit(1)

    print(f'Your number was {userNum} and I guessed {randNum}')
    if userNum == randNum:
        print("I guessed right!")
    else:
        print("Aw, man! I guessed wrong...")

if __name__ == "__main__":
    main()
