############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Mikhail f. Shiryaev <mr.felixoid@gmail.com>                   #
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

from . import Framework


class PullRequest2408(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("ReDASers/Phishing-Detection")

    def test_get_workflow_runs(self):
        runs = self.repo.get_workflow_runs(
            head_sha="7aab33f4294ba5141f17bed0aeb1a929f7afc155"
        )
        self.assertEqual(720994709, runs[0].id)

        runs = self.repo.get_workflow_runs(exclude_pull_requests=True)
        self.assertEqual(3519037359, runs[0].id)
