############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Steve Kowalik <steven@wedontsleep.org>                        #
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


class BranchProtection(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.branch_protection = self.g.get_repo("curvewise-forks/PyGithub").get_branch("master").get_protection()

    def testAttributes(self):
        self.assertTrue(self.branch_protection.required_status_checks.strict)
        self.assertEqual(self.branch_protection.required_status_checks.contexts, ["build (3.10)"])
        self.assertTrue(self.branch_protection.required_linear_history)
        self.assertEqual(
            self.branch_protection.url,
            "https://api.github.com/repos/curvewise-forks/PyGithub/branches/master/protection",
        )
        self.assertEqual(
            self.branch_protection.__repr__(),
            'BranchProtection(url="https://api.github.com/repos/curvewise-forks/PyGithub/branches/master/protection")',
        )
