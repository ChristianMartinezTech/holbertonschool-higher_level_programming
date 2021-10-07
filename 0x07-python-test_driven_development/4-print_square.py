#!/usr/bin/python3
"""Python3 executable"""


def print_square(size):
    """function that prints a square with the character #"""

    if type(size) is int:
        if size >= 0:
            for a in range(size):
                for b in range(size):
                    print("#", end="")
                print("")
        else:
            raise ValueError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
