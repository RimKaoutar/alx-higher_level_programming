#!/usr/bin/python3
"""Module for Base class."""


import json
import os
import csv
import turtle

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

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances.

        If the file doesn’t exist, return an empty list.
        Otherwise, return a list of instances - the type of these instances,
        depends on cls (current class using this method).
        You must use the from_json_string and create methods (implemented,
        previously).
        Args:
            cls (any): class.

        Returns:
            list: list of instances.
        """
        cwd = os.getcwd()
        file_exists = os.path.exists('{}/{}.json'.format(cwd, cls.__name__))
        if file_exists is False:
            return []
        else:
            file_name = "{}.json".format(cls.__name__)
            with open(file_name, "r", encoding="utf-8") as file:
                return [cls.create(**dictionary)
                        for dictionary in cls.from_json_string(file.read())]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save ti file csv"""
        try:
            csvs = [x.to_dictionary() for x in list_objs]
        except FileNotFoundError:
            csvs = '[]'
        keys = csvs[0].keys()
        with open(cls.__name__ + '.csv', 'w') as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(csvs)

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        if not os.path.isfile(cls.__name__ + '.csv'):
            return []

        csvs = []
        with open(cls.__name__ + '.csv', 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                for key, val in row.items():
                    try:
                        row[key] = int(val)
                    except ValueError:
                        pass
                csvs.append(row)
        return [cls.create(**dic) for dic in csvs]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Method that draws the shape with turtle module
        Args:
           list_squares(list): List of square objects
           list_rectangles(list): List of rectangle objects
        Return:
           Always nothing
        """
        # Open screen and set the turtle in the center
        s = turtle.getscreen()
        t = turtle.Turtle()

        # Add a title to my screen
        turtle.title("My first draw with python and tutle module")

        # Customize turtle and screen background
        t.shape("turtle")
        turtle.bgcolor("black")

        # Customize pen for rectangle
        t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
        # Extract the data from the instance rectangle list
        for instance in list_rectangles:
            # Customize pen for rectangle
            t.pen(pencolor="blue", fillcolor="white", pensize=5, speed=1)
            data = instance.to_dictionary()
            # Set the position acording the rectangle object
            t.home()
            t.setpos(data['x'], data['y'])
            # Draw process
            t.pd()
            for i in range(2):
                t.forward(data['width'])
                t.left(90)
                t.forward(data['height'])
                t.left(90)
            t.pu()

        # Customize pen for square
        t.pen(pencolor="red", fillcolor="white", pensize=5, speed=0.5)
        # Extract the data from the instance square list
        for instance in list_squares:
            data = instance.to_dictionary()
            # Set the position acording the square object
            t.home()
            t.setpos(data['x'], data['y'])
            # Draw process
            t.pd()
            for i in range(4):
                t.forward(data['size'])
                t.left(90)
            t.pu()

        # Keeps window open
        turtle.getscreen()._root.mainloop()
