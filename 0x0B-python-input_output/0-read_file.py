#!/usr/bin/python3
""" Function that reads a text file """


def read_file(filename=""):
    """ prints to stdout """

    with open('my_file_0.txt', encoding='utf-8') as f:
        for line in f:
            print(line, end="")
