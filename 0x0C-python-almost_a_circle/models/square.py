#!/usr/bin/python3
""" class Square that inherits from Rectangle """


Rectangle = __import__('rectangle.py').Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id)
        super().__init__(x)
        super().__init__(y)
        super().__init__(width) = size
        super().__init__(height) = size
