#!/usr/bin/python3
"""Write a class Square that defines a square by:
    - Private instance attribute: size
    - Instantiation with size (no type/value verification)
"""


class Square:
    """Defines a square"""
    def __init__(self, size):
        self.__size = size
