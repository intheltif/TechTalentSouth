"""
Exercise 1 of module 8 of GS Jackson's data science course through TTS.

Exemplifies how class inheritance works in Python 3 by using a Student class
that inherits from a Person class to calculate the student's grades and print
the student's information to STDOUT.

NOTE:
    Comments in this file are verbose. I'm attempting to learn how to properly
    comment python code according to Google's style guide and the PEP.

Author: Evert Ball
Date: 07/25/2020
"""
import sys

# Constant to represent exiting with failed exit status from a value error.
VALUE_ERR_EXIT = 1

class Person:
    """ Class to represent a person.
    
    Attributes:
        fname (str): The person's first name.
        lname (str): The person's surname.
    """

    def __init__(self, fname, lname):
        """ The __init__ method that initializes a person object.

        Args:
            fname (str): The first name of the person.
            lname (str): The suranme of the person.
        """
        self.fname = fname
        self.lname = lname

class Student(Person):
    """ A class to represent a student, derived from the person class.

    Provides methods necessary to calculate a persons GPA as a letter grade.

    Attributes:
        fname (str): The first name of the student, derived from Person class.
        lname (str): The surname of the student, derived from Person class.
        id (int): The student's unique ID number.
        scores (:obj:'list' of :obj:'int'): A list of student scores.
    """
    def __init__(self, fname, lname, id, scores=None):
        super().__init__(fname, lname)
        self.id = id
        if scores is None:
            self.scores = []
        else:
            self.scores = scores
    
    def calculate(self):
        """Calculates the average of the student's grades as a letter grade.

        Note:
            This method only handles integer values. Floats will be ignored.

        Returns:
            str: A string value representation of the student's grade average.
        """
        avg = 0
        if self.scores is not None:
            for score in self.scores:
                avg += score
            avg /= len(self.scores)
        return self.__getLetterGrade(avg)

    def __getLetterGrade(self, finalAvg):
        """Private helper method to convert an int average to a letter grade.
        
        Helper method that returns the letter grade for the students average
        based on a ten point scale as follows:
            A: 90 - 100
            B: 80 - 90
            C: 70 - 80
            D: 60 - 70
            F:  0 - 59

        Args:
            finalAvg (int): The final average of the students grades in the 
                course.

        Returns:
            str: A string value representation of the student's grade according 
            to the description above.
        """
        letterGrade = ""

        if finalAvg < 60:
            letterGrade = "F"
        elif finalAvg < 70:
            letterGrade = "D"
        elif finalAvg < 80:
            letterGrade = "C"
        elif finalAvg < 90:
            letterGrade = "B"
        else:
            letterGrade = "A"

        return letterGrade

    def __str__(self):
        """ Returns a string representation of the student. """
        return self.fname + " " + self.lname + " Student ID " + str(self.id)
try:
    # Get user input
    firstName = input("First name: ")
    surname = input("Last name: ")
    unqID = int(input("Student ID: "))
    scores = input("Enter a list of grades seperated by space: ").split()
    scores = [int(n) for n in scores] # Convert scores to ints

    # Create student object from user input
    student1 = Student(firstName, surname, unqID, scores)

    # Print information out neatly
    print(str(student1) + ", you got a", student1.calculate() + ".")

except ValueError as v:
    # Exit if values entered for ints cannot be converted to ints
    print("Error: ", v)
    sys.exit(VALUE_ERR_EXIT)
