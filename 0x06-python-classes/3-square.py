#!/usr/bin/python3
"""Program that sets a class Square that defines a square"""


class Square:
    """Square class definition"""
    def __init__(self, size=0):
        """Definition of size"""
        self.__size = size
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """definition of area"""
        return(self.__size * self.__size)
