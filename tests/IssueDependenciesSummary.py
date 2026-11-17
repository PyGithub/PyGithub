############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Claire Johns <42869556+johnsc1@users.noreply.github.com>      #
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

from __future__ import annotations

from . import Framework


class IssueDependenciesSummary(Framework.TestCase):
    def setUp(self):
        super().setUp()
        with self.replayData("Issue.setUp.txt"):
            self.repo = self.g.get_repo("PyGithub/PyGithub")
            self.issue = self.repo.get_issue(28)
            self.ids = self.issue.issue_dependencies_summary

    def testAttributes(self):
        self.assertEqual(self.ids.blocked_by, 0)
        self.assertEqual(self.ids.blocking, 0)
        self.assertEqual(self.ids.total_blocked_by, 1)
        self.assertEqual(self.ids.total_blocking, 1)
