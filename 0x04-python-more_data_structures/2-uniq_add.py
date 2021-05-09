#!/usr/bin/python3
def uniq_add(my_list=[]):
    for x in range(len(my_list)):
        if (my_list.count(x) >= 2):
            my_list.remove(x)
        else:
            continue
    return(sum(my_list))
