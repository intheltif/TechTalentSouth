"""
Group Exercise 1 from the Jupyter Notebooks for GS Jackson's TTS Data Science
course.

Finds all integers from a given string taht are enclosed in brackets.

Author: Evert Ball
Date: 20 July 2020
"""
import re

def main():
    " The main entry point into the program. "
    sample_str = "  afd [asd] [12 ] [a34]  [ -43 ]tt [+12]xxx"
    integers_in_brackets(sample_str)

def integers_in_brackets(string):
    " Finds all the integers in a given string contained within brackets. "
    y = re.findall("\[(.*?)\]", x)

    for i in range(len(y)):
        re.findall('[1-2+-]\d+', y(i))
      
        print(y[i])
        print(z)

    for i in range(len(y)):
        print(y[i].isdigit())
        print(y[i])

    z = re.findall('-?\d+', x)

    y = re.findall('\W', x)

    print(z)

if __name__ == "__main__":
    main()
