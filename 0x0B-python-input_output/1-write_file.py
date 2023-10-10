#!/usr/bin/python3
"""Defines a fonction write_file()"""


def write_file(filename="", text=""):
    """ function that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters written to file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
