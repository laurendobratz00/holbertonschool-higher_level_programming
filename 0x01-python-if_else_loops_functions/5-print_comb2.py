#!/usr/bin/python3
l = 00
u = 100
for num in range(l, u):
    print("{0:0=2d},".format(num), end=" ")
if num == 99:
    print("{}".format(num))
