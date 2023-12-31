#!/usr/bin/python3
"""Define a class BaseGeometry based on 5-base_geometry.py"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Public instance method that raises an Exception
        with the message area() is not implemented.

        Raises:
            Exception: when area is not implemented.
        """
        raise Exception("area() is not implemented")
