#!/usr/bin/python3
"""Defines the fonction append_write()"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text
    file (UTF8) and returns the number of characters added

    Args:
        filename (str, optional): name of the file. Defaults to "".
        text (str, optional): string of text to write to file. Defaults to "".

    Returns:
        int: number of characters appended to file.
        """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
