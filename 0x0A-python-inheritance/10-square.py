#!/usr/bin/python3
"""
    Implementing a Geometry class
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Implementing a Square class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        calculates the area of a rectangle
        """
        return self.__size ** 2
