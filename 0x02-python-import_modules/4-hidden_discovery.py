#!/usr/bin/python3
if __name__ == '__main__':
    from hidden_4 import *

    for x in dir():
        if dir(x[0]) == '_':
            continue
        else:
            print(dir(x))
