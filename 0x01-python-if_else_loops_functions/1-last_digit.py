#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number:
    print("Last digit of {} is".format(number), end=" ")
    if (number % 10) > 5:
        print((number % 10), end=" ")
        print("and is greater than 5")
    elif (number % 10) == 0:
        print((number % 10), end=" ")
        print("and is 0")
    else:
        print((number % 10), end=" ")
        print("and is less than 6 and not 0")
