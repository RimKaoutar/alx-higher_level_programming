#!/usr/bin/python3
"""Defines a fonction inherits_from()"""


def inherits_from(obj, a_class):
    """function that checks if an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj (a_class): object to verify.
        a_class (type): type to verify with.

    Returns:
        Boolean: True or False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
