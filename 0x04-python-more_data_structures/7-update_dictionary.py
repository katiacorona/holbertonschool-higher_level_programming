#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replace or add key/value in a dictionary.
    @key: Always a string.
    @value: Any type.
    Description: If a key exists, the value will be replaced. If a key does not
    exist, it will be created.
    """
    a_dictionary[key] = value
    return (a_dictionary)
