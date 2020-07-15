"""
Exercise 4 of Module 3.

Determines whether a student is allowed to sit for an exam. A student is 
not allowed to take the exam if their attendance is less than 75%.

Author: Evert Ball
Date: July 15th, 2020
"""

MIN_ATTENDANCE_PERCENTAGE = 75
PERFECT_ATTENDANCE = 100
ZERO = 0
ONE = 1

def main():
    """ The main entry point into the program. """
    # Define the variables to be used later
    numClasses  = 0
    numAttended = 0
    repeat = True

    # Continually ask for user input until it is valid.
    # The only valid input is integers.
    while repeat:
        try:
            numClasses = int(input("How many classes are held? >> "))
            numAttended = int(input("How many classes have you attended? >> "))
            # Do some basic input checks
            if numClasses < ONE:
                print("\nNumber of classes held must be greater than 0...\n")
                continue
            elif numAttended < ZERO:
                print("\nYou cannot attended a negative number of classes...\n")
                continue
            elif numAttended > numClasses:
                print("\nYou cannot attend more classes than are held...\n")
                continue
            repeat = False
        except ValueError:
            print("\nPlease enter the values as an integer.\n")
            continue

    # Get the percentage of the course attended
    percentAttended = ((numAttended / numClasses) * 100)

    # Determine if user can sit for the exam, print a message
    if percentAttended < MIN_ATTENDANCE_PERCENTAGE:
        print(f"\nI'm sorry, you have only attended {int(percentAttended)}% of the course.\nYou cannot take the exam.")
    elif(percentAttended == PERFECT_ATTENDANCE):
        print("\nSuperb! You have attended every class.\nYou may certainly take the exam!")
    else:
        print(f"\nCongratulations, you have attended {int(percentAttended)}% of the course.\nYou may take the exam.")

if __name__ == "__main__":
    main()
