#!/usr/bin/python3
"""
Provides a class Rectangle that inherits from Base.
"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The position in x for the new Rectangle.
            y (int): The position in y for the new Rectangle.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieves and sets the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """Retrieves and sets the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """Retrieves and sets the position in x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """Retrieves and sets the position in y of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
