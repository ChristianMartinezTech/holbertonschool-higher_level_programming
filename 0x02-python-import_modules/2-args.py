#!/usr/bin/python3
import sys
lng = (len(sys.argv) - 1)
arg = sys.argv

if lng < 1:
    print('0 arguments.')

elif lng == 1:
    print('1 argument:'.format(lng))
    print('{}: {:s}'.format(lng, arg[1]))

else:
    print('{:d} arguments:'.format(lng))
    for x in range(1, len(sys.argv)):
        print('{:d}: {:s}'.format(lng, arg[x]))
