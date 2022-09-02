#!/usr/bin/python3
"""
Defines a function that checks for direct or indirect inheritance.
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited directly or
    indirectly from the given class.

    Args:
        obj: The object to be checked.
        a_class: The class to be matched to the object.
    Returns:
        True if obj is an instance of a class that inherited (directly or
        indirectly) from the given class.
        False otherwise.
    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
