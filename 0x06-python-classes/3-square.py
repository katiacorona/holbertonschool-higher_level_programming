#!/usr/bin/python3
"""Write a class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0)
    - Private instance method: def area(self):
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size: size of the square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is < 0
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Computes the square area.
        Returns:
            The current square area.
        """
        return (self.__size ** 2)
