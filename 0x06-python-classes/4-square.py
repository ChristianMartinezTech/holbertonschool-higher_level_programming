#!/usr/bin/python3
"""Program that created a class Square that defines a square"""


class Square:
    """Square class definition"""
    def __init__(self, size=0):
        """Definition of size"""
        if isinstance(size, int):
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """definition of area"""
        return(self.__size * self.__size)

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size getter to change the value"""
        if isinstance(value, int):
            self.__size = value
            if value < 0:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError('size must be an integer')
