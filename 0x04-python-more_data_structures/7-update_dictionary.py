#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    upd_dic = {key: value}

    if (key is not None) or (value is not None):
        return a_dictionary.update(upd_dic)
    else:
        return a_dictionary
