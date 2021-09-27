#!/usr/bin/python3
def safe_print_integer(value):

    try:
        if value != "" and value != "-":
            print("{:d}".format(int(value)))
            return True
        else:
            return False
    except (AttributeError, ValueError, TypeError):
        return False
