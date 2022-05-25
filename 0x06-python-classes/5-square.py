#!/usr/bin/python3
"""Write a class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0)
    - Private instance method: def area(self):
"""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initializes a square.

        Args:
            size: size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Getter: retrieves the size of a square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter: sets the size of a square.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size < 0.
        """
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Computes the square area.

        Returns:
            The current square area.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
