############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Amador Pahim <apahim@redhat.com>                              #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2024 Enrico Minack <github@enrico.minack.dev>                      #
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

from typing import Any, Dict

from github import Github

from . import Framework


class GraphQl(Framework.TestCase):
    def setUp(self):
        super().setUp()

    def expected(self, base_url: str = "https://github.com") -> Dict[Any, Any]:
        return {
            "data": {
                "disablePullRequestAutoMerge": {
                    "actor": {
                        "avatarUrl": "https://avatars.githubusercontent.com/u/14806300?u=786f9f8ef8782d45381b01580f7f7783cf9c7e37&v=4",
                        "login": "heitorpolidoro",
                        "resourcePath": "/heitorpolidoro",
                        "url": f"{base_url}/heitorpolidoro",
                    },
                    "clientMutationId": None,
                }
            }
        }

    def testDefaultUrl(self):
        pull = self.g.get_repo("PyGithub/PyGithub").get_pull(31)
        response = pull.disable_automerge()
        assert response == self.expected()

    def testOtherUrl(self):
        base_url = "https://my.enterprise.com/path/to/github"
        gh = Github(base_url=base_url)
        pull = gh.get_repo("PyGithub/PyGithub").get_pull(31)
        response = pull.disable_automerge()
        assert response == self.expected(base_url)

    def testOtherPort(self):
        base_url = "https://my.enterprise.com:8080/path/to/github"
        gh = Github(base_url=base_url)
        pull = gh.get_repo("PyGithub/PyGithub").get_pull(31)
        response = pull.disable_automerge()
        assert response == self.expected(base_url)
