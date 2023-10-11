#!/usr/bin/python3
"""Defines the function class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure,
    (list, dictionary, string, integer and boolean) for JSON serialization,
    of an object.

    Args:
        obj (MyClass): object.

    Returns:
        dict: dictionary.
    """
    return obj.__dict__
