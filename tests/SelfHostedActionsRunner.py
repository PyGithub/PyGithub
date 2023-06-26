############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Victor Zeng <zacker150@hotmail.com>                           #
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


class SelfHostedActionsRunner(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.user = self.g.get_user("ReDASers")
        self.repo = self.user.get_repo("Phishing-Detection")

    def testAttributes(self):
        runner = self.repo.get_self_hosted_runner(2217)
        self.assertEqual(2217, runner.id)
        self.assertEqual("linux", runner.os)
        self.assertEqual("4306125c7c84", runner.name)
        self.assertEqual("offline", runner.status)
        self.assertFalse(runner.busy)
        labels = runner.labels()
        self.assertEqual(3, len(labels))
        self.assertEqual("self-hosted", labels[0]["name"])
        self.assertEqual("X64", labels[1]["name"])
        self.assertEqual("Linux", labels[2]["name"])
