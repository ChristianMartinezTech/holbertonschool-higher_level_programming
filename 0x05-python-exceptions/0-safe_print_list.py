#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(''.join(map(str, my_list[0:x])))
        print('\n')
        return(x)
    except TypeError:
        exit
