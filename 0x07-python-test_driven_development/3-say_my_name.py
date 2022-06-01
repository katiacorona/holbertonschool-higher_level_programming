#!/usr/bin/python3
"""
Suplies a function that prints a string with two arguments.
"""


def say_my_name(first_name, last_name=""):
    """Prints a string.

    Args:
        first_name: the first argument provided.
        last_name: the optional second argument.

    Raises:
        TypeError: if either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
