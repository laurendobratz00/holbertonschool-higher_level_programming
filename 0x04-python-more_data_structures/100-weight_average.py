#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum(my_list[i] * my_list[i] for i in range(len(my_list))) / sum(my_list)
