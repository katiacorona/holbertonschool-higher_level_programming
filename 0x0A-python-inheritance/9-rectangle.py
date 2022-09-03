#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a Rectangle"""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle object.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """Return the area of the Rectangle object."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = '[{}] '.format(type(self).__name__)
        string += '{}/{}'.format(self.__width, self.__height)
        return string
