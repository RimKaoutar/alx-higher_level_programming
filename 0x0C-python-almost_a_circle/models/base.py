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
