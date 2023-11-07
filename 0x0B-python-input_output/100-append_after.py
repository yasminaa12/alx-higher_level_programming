#!/usr/bin/python3
"""Defines a line of text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts text after each line containing a specific given string in a file
    """

    Text = ""

    with open(filename) as r:
        for line in r:
            Text += line
            if search_string in line:
                Text += new_string
    with open(filename, "w") as w:
        w.write(Text)
