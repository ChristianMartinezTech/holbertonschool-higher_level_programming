#!/usr/bin/python3
for num1 in range(0, 9):
    for num2 in range(0, 10):
        if num1 == num2 or num1 > num2:
            continue
        if num1 == 8 and num2 == 9:
            continue
        print("{}{}".format(num1, num2), end=', ')
print("{}{}".format(num1, num2))
