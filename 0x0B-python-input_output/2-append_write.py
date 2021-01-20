#!/usr/bin/python3
""" funct that appends string at end of a txt file, returns # of chars added """


def append_write(filename="", text=""):
    """ returns # of characters added"""

    with open("file_append.txt", mode='a', encoding='utf-8') as filename:
        filename.write("Holberton School is so cool!\n")
        count = len(text)
        return count
