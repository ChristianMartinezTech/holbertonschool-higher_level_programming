#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    dic = {search: replace}

    return([dic.get(n, n) for n in new_list])
