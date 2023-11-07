#!/usr/bin/python3
"""This module determines a file-appending (adding files) function"""


def append_write(filename="", text=""):
    """Appends (Add) a string to the end of a UTF8 text file
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
