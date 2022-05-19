#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with all values multiplied by 2.
    Description: All values are only integers.
    """
    new = {x: a_dictionary[x] * 2 for x in a_dictionary}
    return new
