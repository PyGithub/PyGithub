############################ Copyrights and license ############################
#                                                                              #
# Copyright 2019 Olof-Joachim Frahm <olof@macrolet.net>                        #
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
import pytest

from github import GithubException

from . import Framework


class PullRequest2816(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("PyGithub/PyGithub")
        self.pull = self.repo.get_pull(31)

    def testMergeWithAutomerge(self):
        self.pull.enable_automerge()

    def testMergeWithAutomergeError(self):
        with pytest.raises(GithubException) as error:
            self.pull.enable_automerge()

        assert error.value.status == 400
        assert error.value.data == {
            "data": {"enablePullRequestAutoMerge": None},
            "errors": [
                {
                    "locations": [{"column": 81, "line": 1}],
                    "message": "Pull request Auto merge is not allowed for this repository",
                    "path": ["enablePullRequestAutoMerge"],
                    "type": "UNPROCESSABLE",
                }
            ],
        }
