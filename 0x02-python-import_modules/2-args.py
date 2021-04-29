#!/usr/bin/python3
import sys

if len(sys.argv) < 1:
    print('{} arguments.'.format(len(sys.argv))

elif len(sys.argv) == 1:
    print('{} argument:'.format(len(sys.argv)))
    print('{} {}'.format(len(sys.argv), str(sys.argv[1]))

else:
    print('{} arguments:'.format(len(sys.argv)))
    print('{} {}'.format(len(sys.argv), str(sys.argv))
