#!/usr/bin/python3
"""Program that creates an empty class Rectangle that defines a rectangle"""


class Rectangle:
    """Class statement"""
    def __init__(self, width=0, height=0):
        """Instantiation with width and height"""
        if isinstance(height, int):
            self.__height = height
            if height < 0:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('height must be an integer')

        if isinstance(width, int):
            self.__width = width
            if width < 0:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')

    @property
    def height(self):
        """Height property retriever"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height property setter"""
        if isinstance(value, int):
            self.__height = value
            if value < 0:
                raise ValueError('height must be >= 0')
        else:
            raise TypeError('height must be an integer')

    @property
    def width(self):
        """Width property to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width property setter"""
        if isinstance(value, int):
            self.__width = value
            if value < 0:
                raise ValueError('width must be >= 0')
        else:
            raise TypeError('width must be an integer')
