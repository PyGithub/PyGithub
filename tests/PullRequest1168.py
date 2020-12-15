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

from . import Framework


class PullRequest1168(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.notifications = self.g.get_repo("PyGithub/PyGithub").get_notifications(
            all=True
        )

    def testGetPullRequest(self):
        p = self.notifications[0].get_pull_request()
        self.assertEqual(p.id, 297582636)
        self.assertEqual(p.number, 1171)
        self.assertEqual(p.title, "Fix small issues for Python 3 compatibility.")

    def testGetIssue(self):
        i = self.notifications[0].get_issue()
        self.assertEqual(i.id, 297582636)
        self.assertEqual(i.number, 1171)
        self.assertEqual(i.title, "Fix small issues for Python 3 compatibility.")
