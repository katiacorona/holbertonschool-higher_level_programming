#!/usr/bin/python3
"""Write a class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0)
    - Private instance method: def area(self):
"""


class Square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square.

        Args:
            size (int): size of the square.
            position (int, int): position of the square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Getter: retrieves the position of a square."""
        return (self.__position)

    @size.setter
    def position(self, value):
        """Setter: sets the position of a square.

        Raises:
            TypeError: if position is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Computes the square area.

        Returns:
            The current square area.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints the square with the character #"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")
