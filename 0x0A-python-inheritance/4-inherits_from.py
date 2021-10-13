#!/usr/bin/python3
"""Python3 Execute statement"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
     that inherited (directly or indirectly) from the specified class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
