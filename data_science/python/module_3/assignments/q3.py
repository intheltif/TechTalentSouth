"""
Exercise 3 of Module 3.

Asks the user for the ages of 3 people and determines who is oldest and 
who is the youngest.

Author: Evert Ball
Date: July 14th, 2020
"""

def main():
    """ The main entry point into the program. """
    ageOne = input("Enter First Person's Age : ")
    ageTwo = input("Enter First Person's Age : ")
    ageThree = input("Enter First Person's Age : ")

    if(ageOne >= ageTwo) and (ageOne >= ageThree):
        largest = age2
    elif (ageTwo >= ageOne) and (ageTwo >= ageThree):
        largest = ageTwo
    else:
        largest = ageThree
    print(f"The oldest of all three people is : {largest}")

    if(ageOne <= ageTwo) and (ageOne <= ageThree):
        smallest = age2
    elif (ageTwo <= ageOne) and (ageTwo <= ageThree):
        smallest = ageTwo
    else:
        smallest = ageThree
    print(f"The youngest of all three people is : {smallest}")

if __name__ == "__main__":
    main()
