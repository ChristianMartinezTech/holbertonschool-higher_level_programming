#!/usr/bin/python3
def no_c(my_string):
    final_string = ''

    for a in range(len(my_string)):
        if (my_string[a] != 'c') and (my_string[a] != 'C'):
            final_string = final_string + my_string[a]
    return(final_string)
