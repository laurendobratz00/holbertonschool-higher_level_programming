#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            count += 1
        except IndexError:
            pass
    print("")
    return count
