#!/usr/bin/python3
"""
Module text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """
    skip = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for letter in text:
        if skip:
            if letter == " ":
                continue
            skip = False
        print(letter, end="")
        if letter in [".", "?", ":"]:
            print("\n")
            skip = True
