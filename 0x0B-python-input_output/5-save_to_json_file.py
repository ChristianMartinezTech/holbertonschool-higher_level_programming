#!/usr/bin/python3
""" Python interpreter location
This makes the script run by default in python3"""


import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file
    using a JSON representation"""
    with open(filename, mode='w', encoding='utf-8') as MyFile:
        json.dump(my_obj, MyFile)
