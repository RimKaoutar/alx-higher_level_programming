#!/usr/bin/python3
"""Define a class Rectangle that inherits
from BaseGeometry (7-base_geometry.py)."""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """Public instance method that raises an Exception
        with the message area() is not implemented.

        Raises:
            Exception: when area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method hat validates value.

        Args:
            name (str): name of the variable.
            value (int): value to assign to name.

        Raises:
            TypeError: when the value is not integer.
            ValueError: when value is less than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
