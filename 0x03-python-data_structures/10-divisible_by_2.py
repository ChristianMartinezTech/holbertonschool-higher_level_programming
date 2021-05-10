#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = my_list.copy()
    for x in range(len(my_list)):
        if (my_list[x] % 2) == 0:
            return(True)
        else:
            return(False)
