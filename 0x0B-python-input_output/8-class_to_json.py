#!/usr/bin/python3
"""
Defines a dictionary-descriptor function.
"""


def class_to_json(obj):
    """
    Return the dictionary description with simple data structure for JSON
    serialization of an object.

    Args:
        obj (obj): An instance of a Class with serializable attributes (list,
                   dict, str, int, bool).
    """
    return obj.__dict__
