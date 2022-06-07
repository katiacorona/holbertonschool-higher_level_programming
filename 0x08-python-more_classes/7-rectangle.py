#!/usr/bin/python3
"""
Suplies class Rectangle.
"""


class Rectangle:
    """Defines a rectangle.

    Attributes:
        number_of_instances (int): the number of instances for Rectangle.
        print_symbol (char): symbol used for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """Print a message when an instane of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Getter: retrieves the width of a rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Property setter: sets the width of a rectangle.

        Raises:
            TypeError: if width is not an int.
            ValueError: if width < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter: retrieves the height of a rectangle."""
        return (self.__height)

    @height.setter
    def height(self, value):
        """Property setter: sets the width of a rectangle.

        Raises:
            TypeError: if height is not an int
            ValueError: if height < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (self.__width * 2 + self.__height * 2)

    def __str__(self):
        """Returns a printable representation of the Rectangle.

        Represents the Rectangle with # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")
        r = []
        for i in range(self.__height):
            [r.append(str(self.print_symbol)) for j in range(self.__width)]
            if i < self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """Return the string representation of Rectangle."""
        r = "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
        return (r)
