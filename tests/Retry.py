############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Justin Kufro <jkufro@andrew.cmu.edu>                          #
# Copyright 2019 Isac Souza <isouza@daitan.com>                                #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Liuyang Wan <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Amador Pahim <apahim@redhat.com>                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2025 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2025 Maja Massarini <2678400+majamassarini@users.noreply.github.com>#
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
import responses
import urllib3

import github

from . import Framework

REPO_NAME = "PyGithub/PyGithub"


class Retry(Framework.TestCase):
    def setUp(self):
        # status codes returned on random github server errors
        status_forcelist = (500, 502, 504)
        retry = urllib3.Retry(total=3, read=3, connect=3, status_forcelist=status_forcelist)
        self.setRetry(retry)
        super().setUp()

    def testShouldNotRetryWhenStatusNotOnList(self):
        with self.assertRaises(github.GithubException):
            self.g.get_repo(REPO_NAME)
        self.assertEqual(len(responses.calls), 1)

    def testReturnsRepoAfter3Retries(self):
        repository = self.g.get_repo(REPO_NAME)
        self.assertEqual(len(responses.calls), 4)
        for call in responses.calls:
            self.assertEqual(call.request.path_url, "/repos/" + REPO_NAME)

        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)

    def testReturnsRepoAfter1Retry(self):
        repository = self.g.get_repo(REPO_NAME)
        self.assertEqual(len(responses.calls), 2)
        for call in responses.calls:
            self.assertEqual(call.request.path_url, "/repos/" + REPO_NAME)

        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)

    def testRaisesRetryErrorAfterMaxRetries(self):
        with self.assertRaises(requests.exceptions.RetryError):
            self.g.get_repo("PyGithub/PyGithub")
        self.assertEqual(len(responses.calls), 4)
        for call in responses.calls:
            self.assertEqual(call.request.path_url, "/repos/PyGithub/PyGithub")

    def testReturnsRepoAfterSettingRetryHttp(self):
        g = github.Github(
            auth=self.oauth_token,
            base_url="http://my.enterprise.com",
            retry=0,
        )  # http here
        repository = g.get_repo(REPO_NAME)
        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)
