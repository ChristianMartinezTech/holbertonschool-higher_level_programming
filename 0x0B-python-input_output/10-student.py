#!/usr/bin/python3
"""Python3 Interpreter Location"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor, instance attributes declaration"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        
        if type(attrs) == list:
            for i in attrs:
                return self.__dict__
