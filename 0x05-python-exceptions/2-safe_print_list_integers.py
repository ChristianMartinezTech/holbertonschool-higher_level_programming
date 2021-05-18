#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0

    for iter in range(my_list):
        try:
            print("{:d}".format(my_list[iter], end=''))
            counter += 1
        except (IndexError, TypeError):
            counter -= 1
        print('')
        return(counter)
