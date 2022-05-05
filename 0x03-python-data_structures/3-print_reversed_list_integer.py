#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list, in reverse order.

    Format: one integer per line. The list only contains integers.
    """
    if my_list:
        my_list.reverse()
        for n in my_list:
            print(n)
