#!/usr/bin/python3
"""Define a class Rectangle that inherits
from BaseGeometry (7-base_geometry.py)."""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
