#!/usr/bin/python3
"""This module determine a file-writing (UTF8)function."""


def write_file(filename="", text=""):
    """Writes a string to an UTF8 text document"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
