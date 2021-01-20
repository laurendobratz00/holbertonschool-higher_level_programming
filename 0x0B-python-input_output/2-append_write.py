#!/usr/bin/python3
""" funct appends string at end of a txt file, returns # of chars added """


def append_write(filename="", text=""):
    """ returns # of characters added"""

    with open(filename, mode='a', encoding='utf-8') as filename:
        filename.write("Holberton School is so cool!\n")
        count = len(text)
        return count
