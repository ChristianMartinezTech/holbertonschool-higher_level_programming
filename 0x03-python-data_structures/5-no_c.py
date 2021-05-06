#!/usr/bin/python3
if __name__ == "__main__":
    def no_c(my_string):
        for a in range(len(my_string)):
            if (my_string[a] == c) or (my_string[a] == C):
                continue
            else:
                print('{}'.format(my_string[a]))
