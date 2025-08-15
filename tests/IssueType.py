############################ Copyrights and license ############################
#                                                                              #
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
        # TODO: create an instance of type IssueType and assign to self.attr, then run:
        #   pytest tests/IssueType.py -k testAttributes --record
        #   ./scripts/update-assertions.sh tests/IssueType.py testAttributes
        #   pre-commit run --all-files
        self.attr = None

    def testAttributes(self):
        self.assertEqual(self.attr.color, "")
        self.assertEqual(self.attr.created_at, datetime(2020, 1, 2, 12, 34, 56, tzinfo=timezone.utc))
        self.assertEqual(self.attr.description, "")
        self.assertEqual(self.attr.id, 0)
        self.assertEqual(self.attr.is_enabled, False)
        self.assertEqual(self.attr.name, "")
        self.assertEqual(self.attr.node_id, "")
        self.assertEqual(self.attr.updated_at, datetime(2020, 1, 2, 12, 34, 56, tzinfo=timezone.utc))
        self.assertEqual(self.attr.url, "")
