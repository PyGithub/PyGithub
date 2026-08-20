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


class RepositoryRulesetBypassActor(Framework.TestCase):
    def setUp(self):
        super().setUp()
        repo = self.g.get_repo("PyGithub/PyGithub")
        ruleset = repo.get_ruleset(3474546)
        self.rrba = ruleset.bypass_actors[0]

    def testAttributes(self):
        rrba = self.rrba
        self.assertEqual(rrba.actor_id, 5)
        self.assertEqual(rrba.actor_type, "RepositoryRole")
        self.assertEqual(rrba.bypass_mode, "always")
