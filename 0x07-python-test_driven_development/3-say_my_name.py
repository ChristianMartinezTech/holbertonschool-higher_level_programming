#!/usr/bin/python3
"""Python3 executable"""

def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name>"""
    if isinstance(first_name, str):
        if isinstance(last_name, str):
            print("My name is {} {}".format(first_name, last_name))
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
