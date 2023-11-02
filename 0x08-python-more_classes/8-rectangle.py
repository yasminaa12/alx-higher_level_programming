#!/usr/bin/python3
""" Module that contains the class of a rectangle """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ initialization of Rectangle class """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """ computes the area of the Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ computes the perimeter of the Rectangle """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ returns the Rectangle to be printed """
        string = ""
        if (self.__width == 0 or self.__height == 0):
            string += ""
        else:
            for rows in range(self.__height):
                string += str(self.print_symbol) * self.__width
                string += "\n"
        return string[:-1]

    def __repr__(self):
        """ returns the Rectangle class """
        return ("Rectangle(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        """ indicates deletion of an instance """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if (rect_1.area() < rect_2.area()):
            return rect_2
        else:
            return rect_1
