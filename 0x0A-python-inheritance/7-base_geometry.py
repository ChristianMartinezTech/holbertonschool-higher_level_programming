#!/usr/bin/python3
"""Python3 Execution"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Public instance method that raises an Exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method that validates value"""
        if isinstance(value, int):
            if value > 0:
                return value
            else:
                raise ValueError('{} must be greater than 0'.format(name))
        else:
            raise TypeError('{} must be an integer'.format(name))
