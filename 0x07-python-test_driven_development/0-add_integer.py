#!/usr/bin/python3
def add_integer(a, b=98):
    try:
        a = int(a) #turning a and b in int
    except:
        raise TypeError('a must be an integer')

    try:
        b = int(b)
    except:
        raise TypeError('b must be an integer')

    return a + b
