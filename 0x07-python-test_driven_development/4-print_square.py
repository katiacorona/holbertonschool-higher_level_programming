#!/usr/bin/python3
"""
Suplies a function that prints a square with the character #.
"""


def print_square(size):
    """Prints a square with the character #.

    Args:
        size: the size lenght of the square.

    Raises:
        TypeError: if size is not an integer, if size < 0.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise TypeError('size must be >= 0')
    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
