import pickle
import unittest

import github
from github.AppAuthentication import AppAuthentication
from github.Repository import Repository

REPO_NAME = "PyGithub/PyGithub"


# https://github.com/PyGithub/PyGithub/issues/2436
# https://github.com/PyGithub/PyGithub/pull/2437
class TestPickle(unittest.TestCase):
    def test_pickle_github(self):
        gh = github.Github("token")
        gh2 = pickle.loads(pickle.dumps(gh))
        self.assertIsInstance(gh2, github.Github)

    def test_pickle_github_with_app_auth(self):
        gh = github.Github("token", app_auth=AppAuthentication("id", "key", 123))
        gh2 = pickle.loads(pickle.dumps(gh))
        self.assertIsInstance(gh2, github.Github)

    def test_pickle_repository(self):
        gh = github.Github("token")
        repo = gh.get_repo(REPO_NAME, lazy=True)
        repo2 = pickle.loads(pickle.dumps(repo))
        self.assertIsInstance(repo2, Repository)
