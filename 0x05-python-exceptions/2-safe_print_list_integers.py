#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    counter = 0

    try:
        while i <= x:
            for i in my_list:
                print("{:d}".format(my_list[i], end=''))
                counter += 1
    except (IndexError, TypeError, ValueError):
        counter -= 1
    return(counter)
