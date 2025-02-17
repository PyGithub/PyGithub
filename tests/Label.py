############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Mateusz Loskot <mateusz@loskot.net>                           #
# Copyright 2018 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
# Copyright 2023 Jirka Borovec <6035284+Borda@users.noreply.github.com>        #
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

from . import Framework


class Label(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.label = self.g.get_repo("PyGithub/PyGithub").get_label("Bug")

    def testAttributes(self):
        self.assertEqual(self.label.color, "e10c02")
        self.assertEqual(self.label.default, True)
        self.assertIsNone(self.label.description)
        self.assertEqual(self.label.id, 3330121)
        self.assertEqual(self.label.name, "bug")
        self.assertIsNone(self.label.description)
        self.assertEqual(self.label.node_id, "MDU6TGFiZWwzMzMwMTIx")
        self.assertEqual(self.label.url, "https://api.github.com/repos/PyGithub/PyGithub/labels/bug")
        self.assertEqual(repr(self.label), 'Label(name="bug")')

    def testEdit(self):
        self.label.edit("LabelEditedByPyGithub", "0000ff", "Description of LabelEditedByPyGithub")
        self.assertEqual(self.label.color, "0000ff")
        self.assertEqual(self.label.description, "Description of LabelEditedByPyGithub")
        self.assertEqual(self.label.name, "LabelEditedByPyGithub")
        self.assertEqual(
            self.label.url,
            "https://api.github.com/repos/PyGithub/PyGithub/labels/LabelEditedByPyGithub",
        )

    def testDelete(self):
        self.label.delete()
