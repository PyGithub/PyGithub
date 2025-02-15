############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2018 Alice GIRARD <bouhahah@gmail.com>                             #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2021 Chris Keating <christopherkeating@gmail.com>                  #
# Copyright 2021 MeggyCal <MeggyCal@users.noreply.github.com>                  #
# Copyright 2021 Steve Kowalik <steven@wedontsleep.org>                        #
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


class PublicKey(Framework.TestCase):
    def testAttributes(self):
        self.public_key = self.g.get_user().get_repo("PyGithub").get_public_key()
        self.assertIsNone(self.public_key.created_at)
        self.assertIsNone(self.public_key.id)
        self.assertEqual(self.public_key.key, "u5e1Z25+z8pmgVVt5Pd8k0z/sKpVL1MXYtRAecE4vm8=")
        self.assertEqual(self.public_key.key_id, "568250167242549743")
        self.assertEqual(
            repr(self.public_key),
            'PublicKey(key_id="568250167242549743", key="u5e1Z25+z8pmgVVt5Pd8k0z/sKpVL1MXYtRAecE4vm8=")',
        )
        self.assertIsNone(self.public_key.title)
        self.assertIsNone(self.public_key.url)

    def testAttributes_with_int_key_id(self):
        self.public_key = self.g.get_user().get_repo("PyGithub").get_public_key()
        self.assertEqual(self.public_key.key, "u5e1Z25+z8pmgVVt5Pd8k0z/sKpVL1MXYtRAecE4vm8=")
        self.assertEqual(self.public_key.key_id, 568250167242549743)
        self.assertEqual(
            repr(self.public_key),
            'PublicKey(key_id=568250167242549743, key="u5e1Z25+z8pmgVVt5Pd8k0z/sKpVL1MXYtRAecE4vm8=")',
        )
