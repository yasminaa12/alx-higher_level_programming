#!/usr/bin/python3
""" rectangle """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ doc """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ doc """
        return self.__width

    @width.setter
    def width(self, width):
        """ doc """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """ doc """
        return self.__height

    @height.setter
    def height(self, height):
        """ doc """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """ doc """
        return self.__x

    @x.setter
    def x(self, x):
        """ doc """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """ doc """
        return self.__y

    @y.setter
    def y(self, y):
        """ doc """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """ doc """
        return self.__height * self.__width

    def display(self):
        """ doc """
        print("\n" * self.__y, end="")
        for rows in range(self.__height):
            print(" " * self.__x, "#" * self.__width, sep="")

    def __str__(self):
        """ doc """
        return ("[Rectangle] ({0:d}) {1:d}/{2:d} - {3:d}/{4:d}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ doc """
        if args is not None and len(args) != 0:
            attrs = ["id", "width", "height", "x", "y"]
            for arg, attr in zip(args, attrs):
                setattr(self, attr, arg)
        elif kwargs is not None:
            for attr, arg in kwargs.items():
                setattr(self, attr, arg)

    def to_dictionary(self):
        """ doc """
        attrs = ["id", "width", "height", "x", "y"]
        vals = [self.id, self.width, self.height, self.x, self.y]
        return dict(zip(attrs, vals))
