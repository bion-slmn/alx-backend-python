#!/usr/bin/env python3
'''test the functionality of client.py'''
from client import GithubOrgClient
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
from typing import (
            List,
            Dict,
                )
from utils import (
        get_json,
        access_nested_map,
        memoize,
            )


class TestGithubOrgClient(unittest.TestCase):
    '''test the method of class GithubOrgClient'''
    @parameterized.expand([
        ('google', {'login': "google"}),
        ('abc', {'login': "abc"}),
        ])
    @patch('client.get_json')
    def test_org(self, args: str, resp: Dict, mock_get: MagicMock) -> None:
        '''test org method functionality'''
        mock_get.return_value = MagicMock(return_value=resp)

        obj = GithubOrgClient(args)
        self.assertEqual(obj.org(), resp)
        url = "https://api.github.com/orgs/{}".format(args)
        mock_get.assert_called_once_with(url)

    def test_public_repos_url(self) -> None:
        '''test for public repos url'''
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:

            mock_org.return_value.__getitem__.return_value = MagicMock(
                    return_value=1
                    )
            obj = GithubOrgClient('string')
            self.assertEqual(obj._public_repos_url(), 1)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json: MagicMock) -> None:
        ''' test pulic repos function'''
        mock_get_json.return_value = [{'name': 'repo1'}, {'name': 'repo2'}]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_repo_url:
            mock_repo_url.return_value = 'fake_url'

            obj = GithubOrgClient('google')
            result = obj.public_repos()
            self.assertEqual(result, ['repo1', 'repo2'])
            mock_repo_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
        ])
    def test_has_license(self, repo: Dict[str, Dict], license_key: str,
                         expected: bool) -> None:
        '''tests the has_licence '''
        self.assertIsNotNone(license_key)
        result = GithubOrgClient('google').has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class([
         {
             'org_payload': TEST_PAYLOAD[0][0],
             'repos_payload': TEST_PAYLOAD[0][1],
             'expected_repos': TEST_PAYLOAD[0][2],
             'apache2_repos': TEST_PAYLOAD[0][3]
             },
        ])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''testing inteegration in public repo '''
    @classmethod
    def setUpClass(cls) -> None:
        '''start a patcher before every test'''
        def side_effect(url):
            route_payload = {
                    'https://api.github.com/orgs/google': cls.org_payload,
                    'https://api.github.com/orgs/google/repos':
                    cls.repos_payload,
                    }
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch('client.requests.get', side_effect=side_effect)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls) -> None:
        '''close a patcher'''
        cls.get_patcher.stop()
