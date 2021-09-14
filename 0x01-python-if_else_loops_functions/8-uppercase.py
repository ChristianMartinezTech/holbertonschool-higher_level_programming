#!/usr/bin/python3
def uppercase(str):
    x = ord(str)
    mayus = (x - 32)

    for a in len(str):
        if (x >= 97) and (x <= 122):
            print('{}'.format(chr(mayus), end='')
        else:
            continue
