#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return
    my_list2 = my_list.copy()
    my_list2 = [x if x != search else replace for x in my_list]
    return my_list2
