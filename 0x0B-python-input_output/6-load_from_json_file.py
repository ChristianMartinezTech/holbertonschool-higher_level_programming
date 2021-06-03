#!/usr/bin/python3
""" Python interpreter location
This makes the script run by default in python3"""

import json


def load_from_json_file(filename):
    """function that creates an Object from a JSON file"""
    with open(filename, mode='r') as MyFile:
        json.dumps(MyFile)
