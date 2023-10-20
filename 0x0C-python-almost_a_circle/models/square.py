#!/usr/bin/python3
"""Defines a class Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines properties of Square.

     Attributes:
        width (int): width of rectangle.
        height (int): height of rectangle.
        x (int): x.
        y (int): y.
        id (int): identity of square.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square's sides.
            x (int, optional): The x-coordinate of
            the square's position. Defaults to 0.
            y (int, optional): The y-coordinate of
            the square's position. Defaults to 0.
            id (int, optional): The unique identifier
            for the square. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Property retriever for size.

        Returns:
            int: size of one side of square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size.

        Args:
            value (int): The size of the square's sides.

        Raises:
            TypeError: If the value is not of type int.
            ValueError: If the value does not meet
            the specified condition (non-negative or positive).
        """
        super().validation("width", value, False)
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square instance.

        Returns:
            str: A string in the format "[Square] (id) x/y - size".
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
