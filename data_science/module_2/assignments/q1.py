"""
The Quadratic Equation Solver!
Exercise 1 of Module 2.

This program only accepts input from the keyboard, not from stdin or the 
command line.

Please note: This program does not provide safety for unexpected data types.
             It has mainly been created as a proof of concept.

Author: Evert Ball
Date: July 7th, 2020
"""

import math

def main():
    """
    The main entry point into the program.
    """
    a = int(input("Enter a number for the coefficient a: "))
    b = int(input("Enter a number for the coefficient b: "))
    c = int(input("Enter a number for the coefficient c: "))
    print(solve_quadratic(a, b, c))

def solve_quadratic(a, b, c):
    """
    Solves a quadratic funciton for x, using the quadratic equation.

    Returns: A 2-tuple for the answers of x.
    """
    # Find the discriminate
    d = (b**2) - (4*a*c)
    # Solve for both solutions
    first_answer = ( -b + math.sqrt(d) ) / (2*a)
    second_answer = ( -b - math.sqrt(d) ) / (2*a)

    return (first_answer, second_answer)

if __name__ == "__main__":
    main()
