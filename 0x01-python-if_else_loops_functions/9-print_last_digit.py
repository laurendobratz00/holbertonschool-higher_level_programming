#!/usr/bin/python3
def print_last_digit(number):
    return number % 10
    num = int(input())
    last_digit = print_last_digit(num)
    print("{}".format(last_digit))
