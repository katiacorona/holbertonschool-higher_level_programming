#!/usr/bin/python3
"""
Defines a function that writes an object to a text file.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file, using a JSON representation.

    Args:
        my_obj (obj): The object to be written to a text file.
        filename (str): The name of the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
