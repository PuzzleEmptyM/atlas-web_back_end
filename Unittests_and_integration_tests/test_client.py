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

        Args:
            org_name (str): The name of the organization.
            expected (dict): The expected organization data.
            mock_get_json (Mock): Mocked get_json function.

        Returns:
            None
        """
        mock_get_json.return_value = expected
        
        client = GithubOrgClient(org_name)
        result = client.org()
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url
        returns the expected value based on mocked org.

        Args:
            mock_org (PropertyMock): Mocked property for GithubOrgClient.org.

        Returns:
            None
        """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
        mock_org.return_value = payload

        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos returns
        the expected list of repositories.

        Args:
            mock_get_json (Mock): Mocked get_json function.

        Returns:
            None
        """
        repos_payload = [
            {"name": "repo1"},
            {"name": "repo2"}
        ]
        mock_get_json.return_value = repos_payload

        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"
            
            client = GithubOrgClient("google")
            result = client.public_repos()
            
            self.assertEqual(result, ["repo1", "repo2"])
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")


if __name__ == "__main__":
    unittest.main()
