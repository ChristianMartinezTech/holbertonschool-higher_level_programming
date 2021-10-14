#!/usr/bin/python3
"""Program that sets a class Square that defines a square"""


class Square:
    """Square class definition"""
    def __init__(self, size=0):
        """Definition of size"""
        self.__size = size

    def area(self):
        """definition of area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            i = 0
            for i in range(self.__size):
                for i in range(self.__size):
                    print('#', end="")
                print()

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(self.__size, int):
            raise TypeError('size must be an integer')
        if self.__size < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
