#!/usr/bin/python3
"""
Defines a function that deserializes JSON string.
"""
import json


def from_json_string(my_str):
    """
    Return an object (Python data structure) represented by a JSON string.

    Args:
        my_str (str): The string to be deserialized.
    """
    return json.loads(my_str)
