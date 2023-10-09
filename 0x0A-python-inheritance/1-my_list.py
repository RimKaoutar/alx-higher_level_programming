#!/usr/bin/python3
"""Defines a class Mylist that inherits from list"""


class MyList(list):
    """Class that inherits from list.

    Args:
        list (list): list to sort.
    """

    def print_sorted(self):
        """prints the list, but sorted (ascending sort)."""
        print(sorted(self))
