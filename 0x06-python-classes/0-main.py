#!/usr/bin/python3
Square = __import__('0-square').Square
"""module that imports the square function"""

my_square = Square()
print(type(my_square))
print(my_square.__dict__)
