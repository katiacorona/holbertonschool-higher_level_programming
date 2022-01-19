#!/usr/bin/python3
def safe_print_integer(value):
    """ Prints an integer with "{:d}.format()
    Parameters:
    value (int): the value to be printed.

    Returns:
    True if it's an integer; False otherwise. """

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
