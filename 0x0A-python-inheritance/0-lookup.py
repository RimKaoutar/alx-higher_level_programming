#!/usr/bin/python3
"""Returns a function lookup()"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
        obj (class): object

    Returns:
        list: list of available attributes and methods of an object
    """
    return dir(obj)
