#!/usr/bin/python3
"""This module determine a text file-reading (UTF8) function"""


def read_file(filename=""):
    """displays the text in a UTF8 file."""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
