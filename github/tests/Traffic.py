# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2018 Justin Kufro <jkufro@andrew.cmu.edu>                          #
# Copyright 2018 Ivan Minno <iminno@andrew.cmu.edu>                            #
# Copyright 2018 Zilei Gu <zileig@andrew.cmu.edu>                              #
# Copyright 2018 Yves Zumbach <yzumbach@andrew.cmu.edu>                        #
# Copyright 2018 Leying Chen <leyingc@andrew.cmu.edu>                          #
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

import github

class Traffic(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.user = self.g.get_user()
        self.repo = self.user.get_repo("PyGithub")

    def testGetReferrers(self):
        referrerResponse = self.repo.get_top_referrers()
        #self.assertEqual()

    def testGetPaths(self):
        pathsResponse = self.repo.get_top_paths()
        #self.assertEqual()

    def testGetViews(self):
        viewsResponse = self.repo.get_views_traffic()
        #self.assertEqual()

    def testGetClones(self):
        clonesResponse = self.repo.get_clones_traffic()
        #self.assertEqual()