#!/usr/bin/python3
def no_c(my_string):
    """ Removes all c and C characters from a string. """
    new_string = ''
    for letter in my_string:
        if 'C' != letter != 'c':
            new_string += letter
    return new_string
