#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    return int(number[len(number) - 1])
    print(print_last_digit(int(input())))
