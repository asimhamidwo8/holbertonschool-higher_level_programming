#!/usr/bin/python3
"""Unittest for max_integer function."""

import unittest
import importlib

max_integer = importlib.import_module("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty(self):
        self.assertIsNone(max_integer([]))

    def test_single(self):
        self.assertEqual(max_integer([7]), 7)

    def test_negative(self):
        self.assertEqual(max_integer([-1, -3, -2]), -1)
