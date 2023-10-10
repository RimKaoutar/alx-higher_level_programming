#!/usr/bin/python3
"""Defines a class MyInt that inherits from int.
MyInt is a rebel. MyInt has == and != operators inverted
"""


class MyInt(int):
    """Defines a class MyInt.

    Args:
        int (int): value
    """
    def __int__(self):
        """Creates new instances of class MyInt.

        Args:
            value (int): integer.
        """
        return self

    def __eq__(self, value):
        """The method equal

        Args:
            other (int): integer.

        Returns:
            boolean: True or False.
        """
        return self is value

    def __ne__(self, value):
        """The method not equal

        Args:
            other (int): integer.

        Returns:
            boolean: True or False
        """
        return self is not value
