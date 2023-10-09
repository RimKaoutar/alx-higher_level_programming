#!/usr/bin/python3
"""Defines a fonction is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """fonction that checks the inheritance

    Args:
        obj (a_class): object to check.
        a_class (type): type to check with.

    Returns:
        boolean: True or False.
    """
    return isinstance(obj, a_class)
