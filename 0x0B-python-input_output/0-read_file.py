#!/usr/bin/python3
"""Defines the function read_file()"""


def read_file(filename=""):
    """function that reads a text file (UTF8)
    and prints it to stdout

    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
