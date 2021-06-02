#!/usr/bin/python3
""" Python interpreter location
This makes the script run by default in python3"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)
    returns the number of characters added"""
    with open(filename, mode='a', encoding='utf-8') as MyFile:
        MyFile.write(text)
        return(len(text))
