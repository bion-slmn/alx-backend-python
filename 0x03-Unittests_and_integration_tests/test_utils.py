#!/usr/bin/env python3
'''
This module defines tests for utils function
'''
import utils
from unittest.mock import MagicMock
from utils import access_nested_map, get_json, memoize
import unittest
from unittest.mock import patch
from parameterized import parameterized
from typing import (
            Mapping,
            Sequence,
            Any,
            Dict,
            Callable,
            )


class TestAccessNestedMap(unittest.TestCase):
    '''
    defines test case for access_nested_map using parameterized
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence,
                               expected: Any) -> None:
        '''test the access_nested_map function using different args'''
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        '''test that and exception is raised'''
        with self.assertRaises(KeyError) as error:
            self.assertEqual(access_nested_map(nested_map, path), 1)
            self.assertIn(error in path)


class TestGetJson(unittest.TestCase):
    '''test the get json function in utils.py'''
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: Mapping,
                      mock_request: MagicMock) -> None:
        '''test get_json using mock'''
        response = MagicMock()
        response.json.return_value = test_payload

        mock_request.return_value = response
        self.assertEqual(get_json(test_url), test_payload)
        mock_request.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    ''' test the memoise function'''
    def test_memoize(self) -> None:
        ''' Test that when calling a_property twice,
        the correct result is returned but a_method is only called once '''
        class TestClass:
            def a_method(self):
                return 42
            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass,'a_method') as test:
            test.return_value = 5
            obj = TestClass()

            self.assertEqual(obj.a_property, 5)
            self.assertNotEqual(obj.a_property, 4)
            test.assert_called_once()
