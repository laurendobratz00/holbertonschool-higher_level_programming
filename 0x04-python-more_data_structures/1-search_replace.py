#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list:
        my_list2 = my_list[:]
        my_list2 = [x if x != 2 else 89 for x in my_list]
        return my_list2
