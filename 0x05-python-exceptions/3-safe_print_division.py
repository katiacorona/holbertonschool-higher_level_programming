#!/usr/bin/python3
def safe_print_division(a, b):
    """ Divides two integers and prints the result.

    Parameters:
    a (int): dividend.
    b (int): divisor.

    Returns:
    (int): the value of the division; None otherwise. """
    result = 0
    try:
        result = a / b
    except (ValueError, TypeError, ZeroDivisionError):
        result = None
        return None
    finally:
        print("Inside result: {}".format(result))
        return (result)
