#!/usr/bin/python3
"""Program that sets a class Square that defines a square"""


class Square:
    """Square class definition"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()

        else:
            a = self.__position[0]

            for i in range(self.__size):
                if self.__position[1] > 1:
                    pass
                else:
                    for j in range(a):
                        print(' ', end="")
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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(self.__position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if self.__position[0] < 0 or self.__position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
