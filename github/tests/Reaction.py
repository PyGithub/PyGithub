# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2017 Nicolas Agustín Torres <nicolastrres@gmail.com>              #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
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

import datetime


class Reaction(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.reactions = self.g.get_user('PyGithub').get_repo("PyGithub").get_issue(28).get_reactions()

    def testAttributes(self):
        self.assertEqual(self.reactions[0].content, "+1")
        self.assertEqual(self.reactions[0].created_at, datetime.datetime(2017, 12, 5, 1, 59, 33))
        self.assertEqual(self.reactions[0].id, 16916340)
        self.assertEqual(self.reactions[0].user.login, "nicolastrres")

        self.assertEqual(self.reactions[0].__repr__(), 'Reaction(user=NamedUser(login="nicolastrres"), id=16916340)')

    def testDelete(self):
        self.reactions[0].delete()
