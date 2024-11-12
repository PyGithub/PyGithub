############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Shinichi TAMURA <shnch.tmr@gmail.com>                         #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Min RK <benjaminrk@gmail.com>                                 #
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

from urllib3.exceptions import InsecureRequestWarning

import github
from github import Consts
from github.Auth import AppAuth, AppInstallationAuth

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
        self.assertListEqual([repo.full_name for repo in repos], ["EnricoMi/sandbox", "EnricoMi/python"])

    def testGetGithubForInstallation(self):
        # with verify=False, urllib3.connectionpool rightly may issue an InsecureRequestWarning
        # we ignore InsecureRequestWarning from urllib3.connectionpool
        with self.ignoreWarning(category=InsecureRequestWarning, module="urllib3.connectionpool"):
            kwargs = dict(
                auth=AppAuth(319953, GithubIntegration.PRIVATE_KEY),
                # http protocol used to deviate from default base url, recording data might require https
                base_url="http://api.github.com",
                timeout=Consts.DEFAULT_TIMEOUT + 10,
                user_agent="PyGithub/Python-Test",
                per_page=Consts.DEFAULT_PER_PAGE + 10,
                verify=False,
                retry=3,
                pool_size=10,
                seconds_between_requests=100,
                seconds_between_writes=1000,
            )

            # assert kwargs consists of ALL requester constructor arguments
            self.assertEqual(kwargs.keys(), github.Requester.Requester.__init__.__annotations__.keys())

            self.integration = github.GithubIntegration(**kwargs)
            installations = list(self.integration.get_installations())
            installation = installations[0]

            g = installation.get_github_for_installation()

            self.assertIsInstance(g._Github__requester.auth, AppInstallationAuth)

            actual = g._Github__requester.kwargs
            kwargs.update(auth=str(AppInstallationAuth))
            actual.update(auth=str(type(actual["auth"])))
            self.assertDictEqual(kwargs, actual)

            repo = g.get_repo("PyGithub/PyGithub")
            self.assertEqual(repo.full_name, "PyGithub/PyGithub")

    def testRequester(self):
        self.assertEqual(len(self.installations), 1)
        installation = self.installations[0]
        assert installation.requester is installation._requester
