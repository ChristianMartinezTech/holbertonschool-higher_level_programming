#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        if type(a) == bool:
            raise TypeError('a must be an integer')
        else:
            a = int(a)
    except:
        raise TypeError('a must be an integer')

    try:
        if type(b) == bool:
            raise TypeError('b must be an integer')
        else:
            b = int(b)
    except:
        raise TypeError('b must be an integer')

    return a + b
