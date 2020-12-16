#!/usr/bin/python3
def no_c(my_string):

    if not my_string:
        return None
    return (my_string.translate({ord(i): None for i in 'cC'}))
