#!/usr/bin/python3
""" Python interpreter location
This makes the script run by default in python3"""

import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
