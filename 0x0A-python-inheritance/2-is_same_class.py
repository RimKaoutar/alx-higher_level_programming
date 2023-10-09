#!/usr/bin/python3
"""Defines the fonction is_same_class()"""


def is_same_class(obj, a_class):
    """function that returns True if the object
    is exactly an instance of the specified class;
    otherwise False.

    Args:
        obj (a_class): object to verify
        a_class (type): the type to verify

    Returns:
        boolean: True or False
    """
    return type(obj) == a_class
