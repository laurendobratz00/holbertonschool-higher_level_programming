#!/usr/bin/python3
l = 00
u = 100
for num in range(l, u):
    if num != 99:
        print("{0:02d},".format(num), end=" ")
    else:
        print("{}".format(num))
