#!/usr/bin/python3
"""
Defines a function that returns a serialized object.
"""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (str).

    Args:
        my_obj (obj): the object to be serialized.
    """
    return json.dumps(my_obj)
