#!/usr/bin/python3
"""Python3 Interpreter Location"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def update(self, *args, **kwargs):
        """Function to update the attribute values"""

        if "id" in kwargs:
            self.id = kwargs.get("id")

        if "width" in kwargs:
            self.__width = kwargs.get("width")

        if "height" in kwargs:
            self.__height = kwargs.get("height")

        if "x" in kwargs:
            self.__x = kwargs.get("x")

        if "y" in kwargs:
            self.__y = kwargs.get("y")

        if len(args) == 1:
            self.id = args[0]

        if len(args) == 2:
            self.id = args[0]
            self.__width = args[1]

        if len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]

        if len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]

        if len(args) == 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]

    def area(self):
        """Function to return the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Function to print # as the rectangle"""
        for a in range(self.__y):
            print()

        for b in range(self.__height):
            for c in range(self.__x):
                print(" ", end="")
            for d in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """Funtion to overide the str output"""
        text_1 = "[Rectangle] ({}) ".format(self.id)
        text_2 = "{}/{} - ".format(self.__x, self.__y)
        text_3 = "{}/{}".format(self.__width, self.__height)
        return text_1 + text_2 + text_3

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
