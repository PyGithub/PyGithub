import pickle
import unittest

import github
from github.Repository import Repository

REPO_NAME = "PyGithub/PyGithub"


class Pickle(unittest.TestCase):
    def testPickleGithub(self):
        gh = github.Github()
        gh2 = pickle.loads(pickle.dumps(gh))
        self.assertIsInstance(gh2, github.Github)
        self.assertIsNotNone(gh2._Github__requester._Requester__connection_lock)
        self.assertIsNone(gh2._Github__requester._Requester__connection)
        self.assertEqual(len(gh2._Github__requester._Requester__custom_connections), 0)

    def testPickleRepository(self):
        gh = github.Github()
        repo = gh.get_repo(REPO_NAME, lazy=True)
        repo2 = pickle.loads(pickle.dumps(repo))
        self.assertIsInstance(repo2, Repository)
        self.assertIsNotNone(repo2._requester._Requester__connection_lock)
        self.assertIsNone(repo2._requester._Requester__connection)
        self.assertEqual(len(repo2._requester._Requester__custom_connections), 0)
