#!/usr/bin/python3
"""Define a class Rectangle that inherits
from BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle"""

    def __init__(self, width, height):
        """Creates new instances of Rectangle.

        Args:
            width (int): width of rectangle.
            height (int): height of rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
