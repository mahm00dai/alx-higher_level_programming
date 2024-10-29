#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_cases(self):
        """Test with normal cases"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(max_integer([42]), 42)

    def test_floats_and_integers(self):
        """Test with floats and integers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 2]), 3.5)
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_string_elements(self):
        """Test with a list of strings (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

    def test_mixed_types(self):
        """Test with mixed types (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, 'a', 3])

if __name__ == '__main__':
    unittest.main()
