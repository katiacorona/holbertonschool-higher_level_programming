#!/usr/bin/python3
"""
Defines a function that reads a file.
"""


def read_file(filename=""):
    """
    Read a text file (UTF-8) and print it to stdout.

    Args:
        filename (str): A string containing the name of the file to be read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end='')
