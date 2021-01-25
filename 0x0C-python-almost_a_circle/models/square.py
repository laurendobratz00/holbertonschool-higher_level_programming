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
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.width))

    def update(self, *args, **kwargs):
        """ adding public method that assigns attributes """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ adding public method that returns the dict repr of a square """
        mySquare = {}
        mySquare["id"] = self.id
        mySquare["size"] = self.size
        mySquare["x"] = self.x
        mySquare["y"] = self.y
        return mySquare
