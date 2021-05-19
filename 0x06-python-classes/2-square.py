#!/usr/bin/python3
"""Functions that creates class Square that defines a square"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """definition made, will do the if cicles"""
        self.__size = size
        if isinstance(size, int):
            if size < 0:
                raise ValueError('size must be >= 0')
        else:
            raise TypeError('size must be an integer')
