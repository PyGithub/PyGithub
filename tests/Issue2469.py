############################ Copyrights and license ############################
#                                                                              #
# Copyright 2023 Mauricio Martinez <mauricio.martinez@premise.com>             #
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


class Issue2469(Framework.TestCase):  # https://github.com/PyGithub/PyGithub/issues/2469
    tokenAuthMode = True

    def setUp(self):
        super().setUp()
        self.user = self.g.get_user()
        self.repo = self.user.get_repo("PyGithub")
        self.org = self.g.get_organization("tecnoly")

    def testRepoVariable(self):
        self.assertTrue(self.repo.create_variable("variable_name", "variable-value"))
        self.assertTrue(self.repo.update_variable("variable_name", "variable-value123"))
        self.assertTrue(self.repo.delete_variable("variable_name"))

    def testOrgVariable(self):
        self.assertTrue(self.org.create_variable("variable_name", "variable-value"))
        self.assertTrue(self.org.update_variable("variable_name", "variable-value123"))
        self.assertTrue(self.org.delete_variable("variable_name"))
