#!/usr/bin/python3
"""Defines an inherited class-checking function -
checks if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class -
    Returns true if object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False
    """

    return (issubclass(type(obj), a_class) and type(obj) != a_class)
