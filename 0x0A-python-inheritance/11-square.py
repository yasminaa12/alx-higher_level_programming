#!/usr/bin/python3
"""Defines a Rectangle subclass Square
class Square that inherits from Rectangle (9-rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Representation of a square"""

    def __init__(self, size):
        """Initialization of a new square"""

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
