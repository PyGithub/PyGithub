############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Justin Kufro <jkufro@andrew.cmu.edu>                          #
# Copyright 2018 Ivan Minno <iminno@andrew.cmu.edu>                            #
# Copyright 2018 Zilei Gu <zileig@andrew.cmu.edu>                              #
# Copyright 2018 Yves Zumbach <yzumbach@andrew.cmu.edu>                        #
# Copyright 2018 Leying Chen <leyingc@andrew.cmu.edu>                          #
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

import requests
import urllib3  # type: ignore
from httpretty import httpretty  # type: ignore

import github

from . import Framework

REPO_NAME = "PyGithub/PyGithub"


class Retry(Framework.TestCase):
    def setUp(self):
        # status codes returned on random github server errors
        status_forcelist = (500, 502, 504)
        retry = urllib3.Retry(
            total=3, read=3, connect=3, status_forcelist=status_forcelist
        )

        Framework.enableRetry(retry)
        super().setUp()

    def testShouldNotRetryWhenStatusNotOnList(self):
        with self.assertRaises(github.GithubException):
            self.g.get_repo(REPO_NAME)
        self.assertEqual(len(httpretty.latest_requests), 1)

    def testReturnsRepoAfter3Retries(self):
        repository = self.g.get_repo(REPO_NAME)
        self.assertEqual(len(httpretty.latest_requests), 4)
        for request in httpretty.latest_requests:
            self.assertEqual(request.path, "/repos/" + REPO_NAME)

        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)

    def testReturnsRepoAfter1Retry(self):
        repository = self.g.get_repo(REPO_NAME)
        self.assertEqual(len(httpretty.latest_requests), 2)
        for request in httpretty.latest_requests:
            self.assertEqual(request.path, "/repos/" + REPO_NAME)

        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)

    def testRaisesRetryErrorAfterMaxRetries(self):
        with self.assertRaises(requests.exceptions.RetryError):
            self.g.get_repo("PyGithub/PyGithub")
        self.assertEqual(len(httpretty.latest_requests), 4)
        for request in httpretty.latest_requests:
            self.assertEqual(request.path, "/repos/PyGithub/PyGithub")

    def testReturnsRepoAfterSettingRetryHttp(self):
        g = github.Github(
            auth=self.login,
            base_url="http://my.enterprise.com",
            retry=0,
        )  # http here
        repository = g.get_repo(REPO_NAME)
        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)
