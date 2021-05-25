#!/usr/bin/python3
def add_integer(a, b=98):
    a = int(a) #turning a and b in int
    b = int(b)

    if isinstance(a, int):
        if isinstance(b, int):
            return a + b #return statement
        else:
            raise TypeError('b must be an integer')
    else:
        raise TypeError('a must be an integer')
