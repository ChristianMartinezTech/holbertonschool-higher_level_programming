#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for a in reversed(range(len(my_list))):
            print('{:d}'.format(my_list[a]))
