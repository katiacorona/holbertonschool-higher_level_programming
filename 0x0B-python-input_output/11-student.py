#!/usr/bin/python3
# 9-student.py
"""
Defines my Student class.
"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Get/retrieve a dictionary representation of a Student.

        Args:
            attrs (list): The optional attributes to represent.
        Returns:
            If attrs is a list of strings, the attribute names in the list.
            All attributes, otherwise.
        """
        if (type(attrs) is list and
                all(type(item) is str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): The key/value pairs to replace the existing attributes
        """
        for k, v in json.items():
            setattr(self, k, v)
