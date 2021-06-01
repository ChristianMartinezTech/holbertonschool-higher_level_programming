#!/usr/bin/python3
"""Excute statement"""


def is_same_class(obj, a_class):
    """returns True if the object is an instance"""
    data_type = type(obj)
    if data_type == a_class:
        return True
