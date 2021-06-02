#!/usr/bin/python3
""" Python interpreter location
This makes the script run by default in python3"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    returns the number of characters written"""
    with open(filename, mode='w', encoding='utf-8') as MyFile:
        MyFile.write(text)
        return(len(text))
