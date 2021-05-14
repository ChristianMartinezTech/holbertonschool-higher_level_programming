#!/usr/bin/python3
def max_integer(my_list=[]):
    sorted_list = sorted(my_list)
    if not my_list:
        return None
    else:
        return(sorted_list[-1])
