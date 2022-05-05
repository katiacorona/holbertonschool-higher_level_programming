#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list, like in C.

    Return: None if idx < 0 or if idx is out of range.
    """
    if 0 > idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
