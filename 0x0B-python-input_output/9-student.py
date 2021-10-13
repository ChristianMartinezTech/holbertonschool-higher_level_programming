#!/usr/bin/python3
"""Python3 Interpreter location"""


class Student:
    """Class student"""
    def __init__(self, first_name, last_name, age):
        """Constructor, initializing instance atributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return (self.__dict__)
