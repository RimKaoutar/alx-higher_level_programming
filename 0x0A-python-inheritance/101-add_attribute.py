#!/usr/bin/python3
"""Funtion add_attribute"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attribute to an object if it's possible.

    Args:
        object (__main__.MyClass): name of the object.
        attr_name ('str): name of the attribute.
        value (str): value of the attribute.

    Raises:
        TypeError:  if the object can’t have new attribute.
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attr_name, attr_value)
