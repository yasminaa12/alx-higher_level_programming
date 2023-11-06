#!/usr/bin/python3
""" module doc """


class MyList(list):
    """ class doc """

    def print_sorted(self):
        clone = self.copy()
        clone.sort()
        print(clone)
