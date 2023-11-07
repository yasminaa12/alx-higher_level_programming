#!/usr/bin/python3
"""Defines a function that adds a new attributes to an objects
if it's possible."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible."""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
