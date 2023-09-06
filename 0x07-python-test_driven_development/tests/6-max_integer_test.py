#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for function max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_max_integer(unittest.TestCase):
    """Unit tests for max_integer([..])."""


    def test_orderedlist(self):
        """testing ordered lists"""
        self.assertEqual(max_integer([1, 2, 3]), 3)
    
    def test_list(self):
        """testing lists"""
        self.assertEqual(max_integer([3, 5, 1, 4]), 5)

    def test_empty_list(self):
        """testing empty lists"""
        self.assertEqual(max_integer([]), None)

    def test_length_one(self):
        """testing size one lists"""
        self.assertEqual(max_integer([5]), 5)

    def test_max_begin(self):
        """testing max at begin lists"""
        self.assertEqual(max_integer([5, 1, 4, 2]), 5)

    def test_float(self):
        """testing float lists"""
        self.assertEqual(max_integer([5.5, 1.2, 4.3, 2.1]), 5.5)

    def test_mixed_types(self):
        """testing mixed type lists"""
        self.assertEqual(max_integer([5.5, -1, 4, 2.1]), 5.5)

    def test_str(self):
        """testing str lists"""
        self.assertEqual(max_integer("zoo"), 'z')

    def test_list_strs(self):
        """testing list of strs"""
        self.assertEqual(max_integer(["zoo", "islam", "omar"]), 'zoo')

    def test_empty_str(self):
        """testing empty str list"""
        self.assertEqual(max_integer(""), None)
