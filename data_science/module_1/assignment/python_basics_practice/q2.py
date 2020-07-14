"""
Question 2 of Python Basics Practice from Module 1.

PLEASE NOTE: The way I understood the question was to only add the sums of 
             single digit integers (ie 0..9) such as 4 + 44 + 444 
             not 4 + 4*4 + 4*4*4.

Author: Evert Ball
Date: 06/27/2020
"""
import sys

# Constants to avoid magic numbers
INPUT_INDEX = 1
NUM_EXPECTED_ARGS = 2
ERR_ARGS_LEN = 3 # Error code for exiting from incorrect num command line args
ERR_NO_CONVERT = 4 # Error code for not being able to convert to an int

# Global
n = 0

# Check if first and last names provided as command line args, prompt if not
if len(sys.argv) < NUM_EXPECTED_ARGS: 
    prompt = "Please provide an integer >> "
    n = input(prompt)
elif len(sys.argv) == NUM_EXPECTED_ARGS:
    n = sys.argv[INPUT_INDEX]
else:
    print("Too many command line arguments provided...")
    print("Please provide only one integer as a command line argument.")
    sys.exit(ERR_ARGS_LEN)

# Remove spaces and convert to an int
n = n.strip()
try:
    n = int(n)
except:
    print("Could not convert " + n + " into an integer")
    exit(ERR_NO_CONVERT)
# Do operations
n_tens = (n * 10) + n
n_hundreds = (n_tens * 10) + n
summation = n_hundreds + n_tens + n
print(summation)

