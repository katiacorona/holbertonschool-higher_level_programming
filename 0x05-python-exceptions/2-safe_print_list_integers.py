#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """ Prints the first x elements of a list and only integers.

    Parameters:
    my_list (list): the list of elements to be evaluated and printed.
    x (int): the number of elements to access in my_list.

    Returns:
    (int): the real number of integers printed. """
    count = 0
    for elem in range(x):
        try:
            print("{:d}".format(my_list[elem]), end='')
            count += 1
        except (ValueError, TypeError):
            pass
    print('')
    return (count)
