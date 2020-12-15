# ########################## Copyrights and license ############################
#                                                                              #
# Copyright 2020 Anuj Bansal <bansalanuj1996@gmail.com>                        #
#                                                                              #
# This file is part of PyGithub.                                               #
# http://pygithub.github.io/PyGithub/v1/index.html                             #
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
# ##############################################################################

from . import Framework


class Project1434(Framework.TestCase):
    def setUp(self):
        super().setUp()

    def testDelete(self):
        project = self.g.get_project(4102095)
        project.delete()

    def testEditWithoutParameters(self):
        project = self.g.get_project(4101939)
        old_name = project.name
        project.edit()
        self.assertEqual(project.name, old_name)

    def testEditWithAllParameters(self):
        project = self.g.get_project(4101939)
        project.edit("New Name", "New Body", "open")
        self.assertEqual(project.name, "New Name")
        self.assertEqual(project.body, "New Body")
        self.assertEqual(project.state, "open")
