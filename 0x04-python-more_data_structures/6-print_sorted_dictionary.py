#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary by ordered keys.
    Description: All keys are strings. Keys should be sorted by alphabetic or-
    der. Only sort keys of the first level (not from a dictionary insed the
    main dictionary).
    """
    for k in sorted(a_dictionary.keys()):
        print("{:s}: {}".format(k, a_dictionary[k]))
