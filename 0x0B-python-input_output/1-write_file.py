#!/usr/bin/python3
""" a function that writes a string to a text file """


def write_file(filename="", text=""):
    """ returns the number of characters written """

    with open(filename, mode="w", encoding='utf-8') as filename:
        return (filename.write(text))
