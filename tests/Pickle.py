############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Andrew Dawes <53574062+AndrewJDawes@users.noreply.github.com> #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Hemslo Wang <hemslo.wang@gmail.com>                           #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
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

import inspect
import pickle
import sys
from abc import ABC

import github
from github.Auth import AppAuth, AppAuthToken, AppInstallationAuth, AppUserAuth, Auth, Login, NetrcAuth, Token
from github.PaginatedList import PaginatedList
from github.Repository import Repository

from . import Framework

REPO_NAME = "PyGithub/PyGithub"


class Pickle(Framework.TestCase):
    def testPickleGithub(self):
        gh = github.Github()
        gh2 = pickle.loads(pickle.dumps(gh))
        self.assertIsInstance(gh2, github.Github)
        self.assertIsNotNone(gh2._Github__requester._Requester__connection_lock)
        self.assertIsNone(gh2._Github__requester._Requester__connection)
        self.assertEqual(len(gh2._Github__requester._Requester__custom_connections), 0)

    def testPickleRepository(self):
        gh = github.Github(lazy=True)
        repo = gh.get_repo(REPO_NAME)
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

    auths = [
        Login("login", "password"),
        Token("token"),
        AppAuth("id", "key"),
        AppAuthToken("token"),
        AppInstallationAuth(AppAuth("id", "key"), 123),
        AppUserAuth("client_id", "client_secret", "access_token"),
        NetrcAuth(),
    ]

    def testPickleAuthSetup(self):
        # check we are testing *all* exiting auth classes
        auth_module = sys.modules[github.Auth.__name__]
        existing_auths = [
            clazz_type.__name__
            for clazz, clazz_type in inspect.getmembers(auth_module, inspect.isclass)
            if Auth in clazz_type.mro() and ABC not in clazz_type.__bases__
        ]
        tested_auths = [type(auth).__name__ for auth in self.auths]
        self.assertSequenceEqual(sorted(existing_auths), sorted(tested_auths))

    def testPickleAuth(self):
        for auth in self.auths:
            with self.subTest(auth=type(auth).__name__):
                auth2 = pickle.loads(pickle.dumps(auth))
                self.assertIsInstance(auth2, type(auth))
