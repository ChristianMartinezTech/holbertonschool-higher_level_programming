#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 99):
        if x % 3 == 0 and x % 5 == 0:
            print('FizzBuzz')
        elif x % 5 == 0:
            print('Buzz')
        elif x % 3 == 0:
            print('Fizz')
        else:
            print(x)
