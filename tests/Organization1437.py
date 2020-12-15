############################ Copyrights and license ############################
#                                                                              #
# Copyright 2020 Anuj Bansal <bansalanuj1996@gmail.com>                        #
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


class Organization1437(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.org = self.g.get_organization("PyGithubSampleOrg")

    def testCreateProject(self):
        project = self.org.create_project("Project title", "This is the body")
        self.assertEqual(project.id, 4115694)
