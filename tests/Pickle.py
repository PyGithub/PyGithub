import pickle
import unittest

import github
from github.Repository import Repository

REPO_NAME = "PyGithub/PyGithub"


class TestPickle(unittest.TestCase):
    def test_pickle_github(self):
        gh = github.Github()
        gh2 = pickle.loads(pickle.dumps(gh))
        self.assertIsInstance(gh2, github.Github)
        self.assertIsNotNone(gh2._Github__requester._Requester__connection_lock)

    def test_pickle_repository(self):
        gh = github.Github()
        repo = gh.get_repo(REPO_NAME)
        repo2 = pickle.loads(pickle.dumps(repo))
        self.assertIsInstance(repo2, Repository)
        self.assertIsNotNone(repo2._requester._Requester__connection_lock)
