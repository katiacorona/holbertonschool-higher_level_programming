#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Defines unittests for max_integer() module."""
    def test_ordered_list(self):
        """Tests a regular case with an ordered list of ints."""
        ordered_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered_list), 4)

    def test_unordered_middle(self):
        """Tests an unordered list with max in the middle."""
        unordered_mid_list = [2, 3, 4, 1]
        self.assertEqual(max_integer(unordered_mid_list), 4)

    def test_unordered_begginning(self):
        """Tests an unordered list with max at the beginning."""
        unordered_beg_list = [4, 2, 3, 1]
        self.assertEqual(max_integer(unordered_beg_list), 4)

    def test_one_element(self):
        """Tests a list with one element."""
        one_list = [1]
        self.assertEqual(max_integer(one_list), 1)

    def test_negative_list(self):
        """Tests a list with negative integers."""
        negative_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative_list), -1)

    def test_float_list(self):
        """Tests a list with only floating point numbers."""
        float_list = [1.1, 2.2, 3.3, -4.4]
        self.assertEqual(max_integer(float_list), 3.3)

    def test_mixed_list(self):
        """Tests a list with both integer and floating point numbers."""
        mixed_list = [1, 2.7, -3, -4.6]
        self.assertEqual(max_integer(mixed_list), 2.7)

    def test_inf_list(self):
        """Tests a list with float(inf)."""
        inf_list = [1, 2.0, -4, float('inf')]
        self.assertEqual(max_integer(inf_list), float('inf'))

    def test_one_string_list(self):
        """Tests a list with a string."""
        str_list = ["Max"]
        self.assertEqual(max_integer(str_list), "Max")

    def test_strings_list(self):
        """Tests a list of strings."""
        strings_list = ['1', '2', 'hi', 'Hello']
        self.assertEqual(max_integer(strings_list), 'hi')


    def test_empty_list(self):
        """Tests an empty list."""
        empty_list = []
        self.assertEqual(max_integer(empty_list), None)
