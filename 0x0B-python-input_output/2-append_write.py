#!/usr/bin/python3
"""
Defines a function that appends text at the end of a file.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a file text (UTF8).

    Args:
        filename (str): The name of the file.
        text (str): The text to be written to filename.
    Returns:
        The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
