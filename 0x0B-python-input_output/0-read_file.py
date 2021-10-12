#!/usr/bin/python3
""" Python interpreter location"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open('my_file_0.txt', encoding='utf=8') as file:
        print(file.read())
