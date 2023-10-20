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

        Raises:
            TypeError: If the value is not a positive integer.
        """
        self.validator("width", value, False)
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

        Raises:
            TypeError: If the value is not a positive integer.
        """
        self.validator("height", value, False)
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

        Raises:
            TypeError: If the value is not a non-negative integer.
        """
        self.validator("x", value)
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

        Raises:
            TypeError: If the value is not a non-negative integer.
        """
        self.validator("y", value)
        self.__y = value

    def validator(self, name, value, eq=True):
        """Method for validating an integer value.

        Args:
            name (str): The name of the value being
            validated, used in error messages.
            value (int): The value to be validated.
            eq (bool, optional): Whether the value
            should be greater than or equal to zero
            (default) or strictly greater than zero.

        Raises:
            TypeError: If the value is not of type int.
            ValueError: If the value does not meet
            the specified condition (non-negative or positive).

        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if eq and value < 0:
            raise ValueError(f"{name} must be >= 0")
        if not eq and value <= 0:
            raise ValueError(f"{name} must be > 0")
