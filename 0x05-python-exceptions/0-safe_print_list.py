#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """ Prints x elements of a list
    Args:
        my_list (list): list with elements to be printed.
        x (int): number of elements in my_list to be printed.

    Return: the number of printed elements. """
    printed_elem = 0
    for elem in range(x):
        try:
            print("{}".format(my_list[elem]), end='')
            printed_elem += 1
        except IndexError:
            break
    print('')
    return (printed_elem)
