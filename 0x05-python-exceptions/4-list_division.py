#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        new_list = [a / b for a, b in zip(my_list_1, my_list_2)]
        print(new_list)
    except ZeroDivisionError:
        print('division by 0')
    except TypeError:
        print('wrong type')
