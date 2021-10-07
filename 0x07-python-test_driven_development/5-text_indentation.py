#!/usr/bin/python3
"""Python 3 Executable"""


def text_indentation(text):
    """function that prints a text with 2 new lines"""

    if type(text) != str:
        raise TypeError("text must be a string")

    for x in text:
        if x == "." or x == "?" or x == ":":
            print(x.strip())
            print("\n")

        else:
            print(x, end="")
