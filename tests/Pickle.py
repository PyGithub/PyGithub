############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Andrew Dawes <53574062+AndrewJDawes@users.noreply.github.com> #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Hemslo Wang <hemslo.wang@gmail.com>                           #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.readthedocs.io/                                              #
#                                                                              #
# PyGithub is free software: you can redistribute it and/or modify it under    #
# the terms of the GNU Lesser General Public License as published by the Free  #
# Software Foundation, either version 3 of the License, or (at your option)    #
# any later version.                                                           #
#                                                                              #
# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY  #
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS    #
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more #
# details.                                                                     #
#                                                                              #
# You should have received a copy of the GNU Lesser General Public License     #
# along with PyGithub. If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

import pickle
import unittest

import github
from github.PaginatedList import PaginatedList
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

    def testPicklePaginatedList(self):
        gh = github.Github()
        repo = gh.get_repo(REPO_NAME, lazy=True)
        branches = repo.get_branches()
        branches2 = pickle.loads(pickle.dumps(branches))
        self.assertIsInstance(branches2, PaginatedList)
