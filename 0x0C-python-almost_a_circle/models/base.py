#!/usr/bin/python3
"""Module for Base class."""


import json


class Base:
    """A representation of the base of our OOP hierarchy."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of Base.

        Args:
            id (int, optional): The unique identifier
            for the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): list of dictionaries.

        Returns:
            str: jason string representation.
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file.

        Args:
            cls: The class calling the method.
            list_objs (list): List of instances inheriting from Base.

        Notes:
            If list_objs is None, saves an empty list.
            The filename is automatically generated as "<Class name>.json."
            The method overwrites the file if it already exists.
        """
        if list_objs is not None:
            json_list = [obj.to_dictionary() for obj in list_objs]
        else:
            json_list = []
        with open("{}.json".format(cls.__name__), "w") as file:
            file.write(cls.to_json_string(json_list))

    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): _description_

        Returns:
            list: JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of the class with attributes set using a dictionary.

        Args:
            cls (type): The class type to create an instance of.
            **dictionary (dict): A dictionary containing
            attribute-value pairs for the instance.

        Returns:
            object: An instance of the class with
            attributes set based on the provided dictionary.

        Note:
            This method is used to create an instance
            of a class (e.g., Rectangle or Square)
            with its attributes initialized using a
            dictionary. It first determines the class type,
            creates a "dummy" instance with default values,
            and then updates the attributes of the
            dummy instance with values from the dictionary.
            The resulting instance is returned.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            dummy = Rectangle(1, 1)
        elif cls is Square:
            dummy = Square(1)
        else:
            dummy = None
        dummy.update(**dictionary)
        return dummy
