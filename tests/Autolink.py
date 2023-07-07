############################ Copyrights and license ############################
#                                                                              #
# Copyright 2021 Marco Köpcke  <hello@parakoopa.de>                            #
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
from tests import Framework


class Autolink(Framework.TestCase):
    def setUp(self):
        super().setUp()
        # When recording test, be sure to create a autolink for yourself on
        # Github and update it here.
        links = [
            x
            for x in self.g.get_user("theCapypara").get_repo("PyGithub").get_autolinks()
            if x.id == 209614
        ]
        self.assertEqual(
            1, len(links), "There must be exactly one autolink with the ID 209614."
        )
        self.link = links[0]

    def testAttributes(self):
        self.assertEqual(self.link.id, 209614)
        self.assertEqual(self.link.key_prefix, "DUMMY-")
        self.assertEqual(
            self.link.url_template, "https://github.com/PyGithub/PyGithub/issues/<num>"
        )
