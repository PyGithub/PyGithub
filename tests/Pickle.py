import pickle
import unittest

import github

REPO_NAME = "PyGithub/PyGithub"


class TestPickle(unittest.TestCase):
    def test_pickle_github(self):
        gh = github.Github()
        gh2 = pickle.loads(pickle.dumps(gh))
        self.assertIsInstance(gh2, github.Github)
        self.assertIsNotNone(gh2._Github__requester._Requester__connection_lock)
