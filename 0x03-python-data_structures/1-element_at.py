#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 1) or (my_list[idx] > len(my_list)):
        return (None)
    else:
        return my_list[idx]
