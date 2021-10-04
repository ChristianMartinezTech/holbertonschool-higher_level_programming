#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        int(a) #turning a and b in int
    except:
        raise TypeError('a must be an integer')

    try:
        int(b)
    except:
        raise TypeError('b must be an integer')

    return int(a) + int(b)
