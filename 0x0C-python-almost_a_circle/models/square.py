#!/usr/bin/python3
""" class Square that inherits from Rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ instantiation """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ getter for the method """
        return (self.width)

    @size.setter
    def size(self, value):
        """ setting the width """
        self.width = value
        self.height = value

    def __str__(self):
        """ str method """
        return ("[Rectangle] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width))
