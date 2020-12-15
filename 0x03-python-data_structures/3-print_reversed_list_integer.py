#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    new_list = my_list[::-1]
    for x in range(len(new_list)):
        print("{:d}".format(new_list[x]))
