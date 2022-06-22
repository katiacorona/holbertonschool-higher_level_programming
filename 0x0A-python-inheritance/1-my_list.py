#!/usr/bin/python3
"""Defines a class MyList that inherits from list.
"""


class MyList(list):
    """Defines a print method for list class."""
    def print_sorted(self):
        """Prints a list in sorted ascending order."""
        print(sorted(self))
