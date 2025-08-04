############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Amador Pahim <apahim@redhat.com>                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

import github

from . import Framework

REPO_NAME = "PyGithub/PyGithub"


class PoolSize(Framework.TestCase):
    def setUp(self):
        self.setPoolSize(20)
        super().setUp()

    def testReturnsRepoAfterSettingPoolSize(self):
        repository = self.g.get_repo(REPO_NAME)
        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)

    def testReturnsRepoAfterSettingPoolSizeHttp(self):
        g = github.Github(
            auth=self.oauth_token,
            base_url="http://my.enterprise.com",
            pool_size=20,
        )
        repository = g.get_repo(REPO_NAME)
        self.assertIsInstance(repository, github.Repository.Repository)
        self.assertEqual(repository.full_name, REPO_NAME)
