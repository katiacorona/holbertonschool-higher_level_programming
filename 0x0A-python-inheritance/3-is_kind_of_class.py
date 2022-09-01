#!/usr/bin/python3
"""
Defines a function that checks for multiple inheritance.
"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of or inherited from a given class

    Args:
        obj: The object to be checked.
        a_class: The class to match the type of obj.
    Returns:
        True if obj is an instance of or inherited from a_class;
        False otherwise.
    """
    if (isinstance(obj, a_class) or issubclass(type(obj), a_class)):
        return True
    return False
