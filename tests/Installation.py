############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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
from github.Auth import AppAuth

from . import Framework, GithubIntegration


class Installation(Framework.BasicTestCase):
    def setUp(self):
        super().setUp()
        app_id = 36541767
        private_key = GithubIntegration.PRIVATE_KEY
        self.auth = AppAuth(app_id, private_key)
        self.integration = github.GithubIntegration(auth=self.auth)
        self.installations = list(self.integration.get_installations())

    def testGetRepos(self):
        self.assertEqual(len(self.installations), 1)
        installation = self.installations[0]

        repos = list(installation.get_repos())
        self.assertEqual(len(repos), 2)
        self.assertListEqual(
            [repo.full_name for repo in repos], ["EnricoMi/sandbox", "EnricoMi/python"]
        )
