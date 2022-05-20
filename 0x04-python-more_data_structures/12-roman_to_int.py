#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.
    Return: An integer. If the roman_string is not a string or None, return 0.
    """
    roman_dic = {
                "I": 1,
                "V": 5,
                "X": 10,
                "L": 50,
                "C": 100,
                "D": 500,
                "M": 1000
              }
    n = 0

    if roman_string is None:
        return 0

    for idx in range(len(roman_string)):
        if roman_dic[roman_string[idx]] < roman_dic[roman_string[idx]]:
            n -= roman_dic[roman_string[idx]]
        else:
            n += roman_dic[roman_string[idx]]

    return n
