#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    if len(list_of_integers) != 0:
        list_of_integers.sort()
        return list_of_integers[-1]
    else:
        return None
