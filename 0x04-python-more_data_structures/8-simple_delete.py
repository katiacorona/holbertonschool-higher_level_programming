#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete a key in a dictionary.
    @key: Always a string.
    Description: If a key does not exist, the dictionary won't change.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
