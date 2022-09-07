#!/usr/bin/python3
"""
Defines a function that writes to a text file.
"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8), create the file if it doesn't exist,
    and overwrite the content of the file if it does.

    Args:
        filename (str): A string containing the name of the file.
        text (str): The string to be written to a text file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
