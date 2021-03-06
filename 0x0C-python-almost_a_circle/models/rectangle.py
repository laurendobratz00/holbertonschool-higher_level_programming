#!/usr/bin/python3
""" class Rectangle that inherits from Base """


from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ instantiation """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter for the method """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setting the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter for the method """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ setting the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for the method """
        return(self.__x)

    @x.setter
    def x(self, value):
        """ setting x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for the method """
        return(self.__y)

    @y.setter
    def y(self, value):
        """ setting y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ finding the area """
        return self.height * self.width

    def display(self):
        """ public instance method printing rectangle with # """
        output = ""
        if self.__width is 0:
            return ""
        if self.__height is 0:
            return ""
        print("\n" * self.__y, end="")
        for a in range(self.__height):
            print(" " * self.__x, end="")
            for h in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ returning rectangle """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ assigns an arg to each attribute """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.width = j
                if i == 2:
                    self.height = j
                if i == 3:
                    self.x = j
                if i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """ adding public method that returns the dictionary repr of a Rectangle
        """
        myRect = {}
        myRect["id"] = self.id
        myRect["width"] = self.width
        myRect["height"] = self.height
        myRect["x"] = self.x
        myRect["y"] = self.y

        return myRect
