#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a Square."""

    def __init__(self, size):
        """
        Initialize a new Square object.

        Args:
            sieze (int): The size of the new Square object.
        """
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Return the area of the Square object."""
        return self.__size * self.__size
