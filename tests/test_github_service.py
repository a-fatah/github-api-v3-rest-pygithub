import sys
import unittest
from unittest.mock import patch, Mock

from app.api.services.github_service import GithubService


class TestGithubService(unittest.TestCase):
    @patch('app.api.services.github_service.Github')
    def setUp(self, GithubMock):
        self.github_mock = GithubMock()
        self.github_service = GithubService()

    def test_create_repository(self):
        self.github_service.create_repository('test-repo')
        self.github_mock.get_user().create_repo.assert_called_once_with('test-repo')

    def test_create_issue(self):
        self.github_service.create_issue('test-repo', 'test issue')
        self.github_mock.get_user().get_repo().create_issue.assert_called_once_with(title='test issue', body=None, assignee=None, labels=None)

    def test_create_gist(self):
        self.github_service.create_gist('test gist', {'file1.txt': {'content': 'Test content'}}, True)
        self.github_mock.get_user().create_gist.assert_called_once_with(True, {'file1.txt': {'content': 'Test content'}}, 'test gist')

if __name__ == '__main__':
    unittest.main()