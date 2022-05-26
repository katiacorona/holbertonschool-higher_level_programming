#!/usr/bin/python3
"""
Suplies a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """Return an integer with the addition of a and b.

    Raises:
        TypeError: if either a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
