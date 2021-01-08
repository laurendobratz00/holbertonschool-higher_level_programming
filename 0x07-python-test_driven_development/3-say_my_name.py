#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    if isinstance(first_name, str) == False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) == False:
        raise TypeError("last_name must be a string")

    if first_name is None:
        raise TypeError("first_name must be a string")
    if last_name is None:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
