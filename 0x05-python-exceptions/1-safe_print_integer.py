#!/usr/bin/python3
def safe_print_integer(value):
    if value:
        try:
            print("{:d}".format(int(value)))
            return True
        except (AttributeError, ValueError):
            return False
