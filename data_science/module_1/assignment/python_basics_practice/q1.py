"""
Question 1 of Python Basics Practice from Module 1.

Author: Evert Ball
Date: 06/27/2020
"""
import sys

# Constants to avoid magic numbers
FIRST_NAME_INDEX = 1
LAST_NAME_INDEX = 2
NUM_EXPECTED_ARGS = 3
ERR_ARGS_LEN = 4 # Error code for exiting from incorrect num command line args

# Globals for first and last name
firstName = ""
lastName = ""

# Check if first and last names provided as command line args, prompt if not
if len(sys.argv) < NUM_EXPECTED_ARGS: 
    firstPrompt = "What is your first name? >> "
    lastPrompt = "Okay! What is your last name? >> "
    firstName = input(firstPrompt)
    lastName = input(lastPrompt)
elif len(sys.argv) == NUM_EXPECTED_ARGS:
    firstName = sys.argv[FIRST_NAME_INDEX]
    lastName = sys.argv[LAST_NAME_INDEX]
else:
    print("Too many command line arguments provided...")
    print("Please provide only first and last name as command line arguments.")
    sys.exit(ERR_ARGS_LEN)

print(lastName.strip() + " " + firstName.strip())
