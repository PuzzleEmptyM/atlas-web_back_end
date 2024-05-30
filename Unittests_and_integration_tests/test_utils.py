#!/usr/bin/env python3
"""
Unit tests for utils module.
Includes tests for access_nested_map, get_json, and memoize functions.
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class to test access_nested_map
    function from utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map returns expected result for given inputs.

        Arg1: nested_map - dict; nested dictionary to access.
        Arg2: path - tuple; path of keys to follow in nested dictionary.
        Arg3: expected - any; expected result from accessing nested dictionary.

        Return: None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test that access_nested_map raises KeyError for invalid paths.

        Arg1: nested_map - dict; The nested dictionary to access.
        Arg2: path - tuple; The path of keys to follow in nested dictionary.

        Return: None
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class to test the get_json function from utils module.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test that get_json returns the expected result.

        Arg1: test_url - str; The URL to pass to get_json.
        Arg2: test_payload - dict; The expected payload returned by get_json.

        Return: None
        """
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = Mock(**{'json.return_value': test_payload})

            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class to test the memoize decorator from utils module.
    """

    def test_memoize(self):
        """
        Test that a_property returns the correct result
        and a_method is called only once.

        Return: None
        """

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=42) as mock_a_method:
            test_instance = TestClass()
            result1 = test_instance.a_property
            result2 = test_instance.a_property
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
