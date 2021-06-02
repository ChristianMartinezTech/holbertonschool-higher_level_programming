#!/usr/bin/python3
""" Python interpreter location
This makes the script run by default in python3"""


def read_file(filename=""):
    """  function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, encoding='utf-8') as store:
        print(store.read())
