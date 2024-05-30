#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class to test the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch('client.get_json', return_value={"login": "test"})
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Arg1: org_name - str; The name of the organization to fetch.
        Arg2: expected - dict; The expected result returned by the org method.
        Arg3: mock_get_json - Mock; Mock of the get_json function.

        Return: None
        """
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
