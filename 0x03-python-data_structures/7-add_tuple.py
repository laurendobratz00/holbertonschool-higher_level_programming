#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    i = len(tuple_a)
    j = len(tuple_b)
    sum0 = 0
    sum1 = 0
    if i >= 2:
        sum0 = tuple_a[0] + sum0
        sum1 = tuple_a[1] + sum1
    elif i == 1:
        sum0 = tuple_a[0] + sum0
    if j >= 2:
        sum0 = tuple_b[0] + sum0
        sum1 = tuple_b[1] + sum1
    elif j == 1:
        sum0 = tuple_b[0] + sum0
    return (sum0, sum1)
