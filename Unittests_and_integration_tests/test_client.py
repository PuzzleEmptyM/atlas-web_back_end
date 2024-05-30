#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient class.
"""

import unittest
from unittest.mock import patch, PropertyMock
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
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Arg1: org_name - str; The name of the organization to fetch.
        Arg2: expected - dict; The expected result returned by the org method.
        Arg3: mock_get_json - Mock; Mock of the get_json function.

        Return: None
        """
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns the
        expected value based on mocked org.

        Arg1: mock_org - PropertyMock; Mocked property for GithubOrgClient.org.

        Return: None
        """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = payload

        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
