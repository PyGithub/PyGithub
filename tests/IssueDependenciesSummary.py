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

from . import Framework


class IssueDependenciesSummary(Framework.TestCase):
    def setUp(self):
        super().setUp()
        # TODO: create an instance of type IssueDependenciesSummary and assign to self.attr, then run:
        #   pytest tests/IssueDependenciesSummary.py -k testAttributes --record
        #   ./scripts/update-assertions.sh tests/IssueDependenciesSummary.py testAttributes
        #   pre-commit run --all-files
        self.attr = None

    def testAttributes(self):
        self.assertEqual(self.attr.blocked_by, 0)
        self.assertEqual(self.attr.blocking, 0)
        self.assertEqual(self.attr.total_blocked_by, 0)
        self.assertEqual(self.attr.total_blocking, 0)
        self.assertEqual(self.attr.url, "")
