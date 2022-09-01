#!/usr/bin/python3
"""
Defines a class-checking function
"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of the given class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to match the obj to.
    Returns:
        True if obj is exacly an instance of a_class;
        False otherwise.
    """
    if type(obj) is a_class:
        return True
    return False
