#!/usr/bin/python3
""" Python interpreter location
This makes the script run by default in python3"""


import json


def from_json_string(my_str):
    """a function that returns an object (Python data structure)
    represented by a JSON string:"""
    return json.loads(my_str)
