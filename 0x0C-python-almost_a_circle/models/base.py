#!/usr/bin/python3
"""
Provides a Base model class.
"""


class Base:
    """
    Base class model for all other classes.

    Attributes:
        __nb_objects (int): The number of Base instances.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base.

        Args:
            id (int): The identity of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
