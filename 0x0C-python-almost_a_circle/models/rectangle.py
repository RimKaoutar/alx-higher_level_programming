#!/usr/bin/python3
"""Defines a class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class, inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new instance of Rectangle.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of
            the rectangle's position. Defaults to 0.
            y (int, optional): The y-coordinate of
            the rectangle's position. Defaults to 0.
            id (int, optional): The unique identifier
            for the rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter property for the width attribute."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width attribute.

        Args:
            value (int): The width value to set.
        """
        self.__width = value

    @property
    def height(self):
        """Getter property for the height attribute."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height attribute.

        Args:
            value (int): The height value to set.
        """
        self.__height = value

    @property
    def x(self):
        """Getter property for the x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x attribute.

        Args:
            value (int): The x value to set.
        """
        self.__x = value

    @property
    def y(self):
        """Getter property for the y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y attribute.

        Args:
            value (int): The y value to set.
        """
        self.__y = value
