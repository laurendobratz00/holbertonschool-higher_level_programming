#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    for x in my_list:
        if x not in unique:
            unique.append(x)
    result = sum(unique)
    return result
