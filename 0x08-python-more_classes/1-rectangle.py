#!/usr/bin/python3
"""
Suplies class Rectangle.
"""


class Rectangle:
    """Defines a rectangle."""
    def __init__(self, width=0, height=0):
        """Initializes a rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter: retrieves the width of a rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Property setter: sets the width of a rectangle.

        Raises:
            TypeError: if width is not an int or width < 0.
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Getter: retrieves the height of a rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Property setter: sets the width of a rectangle.

        Raises:
            TypeError: if height is not an int or height < 0.
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value
