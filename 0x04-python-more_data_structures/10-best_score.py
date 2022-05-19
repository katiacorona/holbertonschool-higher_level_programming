#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Return a key with the biggest integer value.
    Description: All values are only integers. All students have different
    scores.
    Return: If no score found, None.
    """
    if a_dictionary and len(a_dictionary):
        v, k = list(a_dictionary.values()), list(a_dictionary.keys())
        s = sorted(v)
        return (k[v.index(s[-1])])
    return None
