#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.
    Return: An integer. If the roman_string is not a string or None, return 0.
    """
    roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    n = 0

    if (roman_string is None or not isinstance(roman_string, str)
            or len(roman_string) == 0):
        return 0

    for idx in range(len(roman_string)):
        if idx == len(roman_string) - 1:
            n += roman_dict[roman_string[idx]]
            break

        if (roman_dict[roman_string[idx]] < roman_dict[roman_string[idx + 1]]
                and idx != len(roman_string) - 1):
            n -= roman_dict[roman_string[idx]]

        else:
            n += roman_dict[roman_string[idx]]

    return n
