############################ Copyrights and license ############################
#                                                                              #
# Copyright 2024 Austin Lucas Lake <53884490+austinlucaslake@users.noreply.github.com>#
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


class UserGPGKey(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.gpg_key = self.g.get_user().get_gpg_key("TODO")

    def testAttributes(self):
        self.assertEqual(self.gpg_key.id, "TODO")
        self.assertEqual(
            self.gpg_key.key_id,
            "TODO",
        )
        self.assertEqual(self.gpg_key.name, "GPG key added through PyGithub")
        self.assertEqual(
            repr(self.gpg_key),
            'UserGPGKey(name="GPG key added through PyGithub", id=TODO)',
        )

    def testDelete(self):
        self.gpg_key.delete()
