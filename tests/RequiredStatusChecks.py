# -*- coding: utf-8 -*-

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

import Framework


class RequiredStatusChecks(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.required_status_checks = self.g.get_user().get_repo("PyGithub").get_branch("integrations").get_required_status_checks()

    def testAttributes(self):
        self.assertTrue(self.required_status_checks.strict)
        self.assertEqual(self.required_status_checks.contexts, ["foo/bar"])
        self.assertEqual(self.required_status_checks.url, "https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_status_checks")
        self.assertEqual(self.required_status_checks.__repr__(), 'RequiredStatusChecks(url="https://api.github.com/repos/jacquev6/PyGithub/branches/integrations/protection/required_status_checks", strict=True)')
