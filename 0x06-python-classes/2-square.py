#!/usr/bin/python3
"""Write a class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with optional size: def __init__(self, size=0)
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        try:
            if size >= 0 and isinstance(size, int):
                self.__size = size
        except TypeError:
            print('size must be an integer')
        except ValueError:
            print('size must be >= 0')
