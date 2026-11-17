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

from datetime import datetime, timezone

from . import Framework


class IssueType(Framework.TestCase):
    def setUp(self):
        super().setUp()
        with self.replayData("Issue.setUp.txt"):
            self.repo = self.g.get_repo("PyGithub/PyGithub")
            self.issue = self.repo.get_issue(28)
            self.type = self.issue.type

    def testAttributes(self):
        self.assertEqual(self.type.color, "red")
        self.assertEqual(self.type.created_at, datetime(2024, 1, 25, 12, 55, 41, tzinfo=timezone.utc))
        self.assertEqual(self.type.description, "An unexpected problem or behavior")
        self.assertEqual(self.type.id, 1386163)
        self.assertEqual(self.type.is_enabled, True)
        self.assertEqual(self.type.name, "Bug")
        self.assertEqual(self.type.node_id, "IT_kwDOAKxBpM4AFSaz")
        self.assertEqual(self.type.updated_at, datetime(2024, 7, 26, 10, 24, 51, tzinfo=timezone.utc))
