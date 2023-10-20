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
        self.validator("width", value, False)
        self.width = value
        self.height = value

    def __str__(self):
        """Returns a string representation of the Square instance.

        Returns:
            str: A string in the format "[Square] (id) x/y - size".
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the instance
        based on positional and keyword arguments.

        Args:
            *args: Variable number of positional arguments.
            **kwargs: Variable number of keyword arguments.

        Note:
            This method allows updating attributes using a
            combination of both positional and keyword arguments.
        """
        if args and len(args) > 0:
            attribut_list = ['id', 'size', 'x', 'y']
            for key, value in enumerate(args):
                setattr(self, attribut_list[key], value)

        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square.

        Returns:
            dict: square.
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
