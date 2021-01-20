#!/usr/bin/python3
""" Function that reads a text file """


def read_file(filename=""):
    """ prints to stdout """

    with open(filename, encoding='utf-8') as filename:
        for line in filename:
            print(line, end="")
