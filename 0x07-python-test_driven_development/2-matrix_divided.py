#!/usr/bin/python3
""" docstring """


def matrix_divided(matrix, div):
    """ this is a matrix divided by div """
    len1 = len(matrix[0])

    for x, y in enumerate(matrix):
        if len(y) != len1:
            raise TypeError("Each row of the matrix must have the same size")

#    if not isinstance(div, (int, float)):
#        raise TypeError("div must be a number")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div is 0:
        raise ZeroDivisionError("division by zero")

    if matrix:
        return [list(map(lambda x: (round(x / div, 2)), x)) for x in matrix]
