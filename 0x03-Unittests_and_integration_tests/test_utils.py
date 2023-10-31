#!/usr/bin/env python3
'''Parameterize a unit test'''

from typing import Dict, Tuple
import unittest
from utils import access_nested_map
from parameterized import parameterized
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in the nested map"),
        ({"a": 1}, ("a", "b"),
         "Key 'b' not found in the nested map at path ['a']")
    ])
    def test_access_nested_map_exception(self, nested_map: Dict, path: Tuple[str], expected_message: Exception):
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(
            Exception
        ) as context:
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
