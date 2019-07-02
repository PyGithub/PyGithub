# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Kelvin Wong (https://github.com/netsgnut)                     #
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


class Issue945(Framework.TestCase):  # https://github.com/PyGithub/PyGithub/issues/945
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_user("openframeworks").get_repo("openFrameworks")
        self.list = self.repo.get_issues()
        self.list_with_headers = self.repo.get_stargazers_with_dates()

    def testReservedPaginatedListAttributePreservation(self):
        r1 = self.list.reversed
        self.assertEqual(self.list._PaginatedList__contentClass, r1._PaginatedList__contentClass)
        self.assertEqual(self.list._PaginatedList__requester, r1._PaginatedList__requester)
        self.assertEqual(self.list._PaginatedList__firstUrl, r1._PaginatedList__firstUrl)
        self.assertEqual(self.list._PaginatedList__firstParams, r1._PaginatedList__firstParams)
        self.assertEqual(self.list._PaginatedList__headers, r1._PaginatedList__headers)
        self.assertEqual(self.list._PaginatedList__list_item, r1._PaginatedList__list_item)

        self.assertTrue(self.list_with_headers._PaginatedList__headers is not None)
        r2 = self.list_with_headers.reversed
        self.assertEqual(self.list_with_headers._PaginatedList__contentClass, r2._PaginatedList__contentClass)
        self.assertEqual(self.list_with_headers._PaginatedList__requester, r2._PaginatedList__requester)
        self.assertEqual(self.list_with_headers._PaginatedList__firstUrl, r2._PaginatedList__firstUrl)
        self.assertEqual(self.list_with_headers._PaginatedList__firstParams, r2._PaginatedList__firstParams)
        self.assertEqual(self.list_with_headers._PaginatedList__headers, r2._PaginatedList__headers)
        self.assertEqual(self.list_with_headers._PaginatedList__list_item, r2._PaginatedList__list_item)
