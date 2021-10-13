#!/usr/bin/python3
"""Python3 Location"""


import json
import sys


def reading_argv(sys):
    """reads argv"""
    arguments = sys.argv[1:]
    print(arguments)


def save_to_json_file(arguments):
    """Save the arguments in json"""
    with open('add_item.json', 'w') as file:
        json.dumps(arguments, file)
