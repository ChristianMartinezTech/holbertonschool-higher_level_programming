#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        print(''.join(map(str, my_list[0:x])))

        j = 0

        for i in my_list:
            j += 1

            if x > j:
                return my_list[-1]
            else:
                return(x)
    except (TypeError, IndexError):
        return(x)
