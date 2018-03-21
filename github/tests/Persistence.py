# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
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
import github

from io import BytesIO as IO


class Persistence(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_repo("akfish/PyGithub")

        self.dumpedRepo = IO()
        self.g.dump(self.repo, self.dumpedRepo)
        self.dumpedRepo.seek(0)

    def tearDown(self):
        self.dumpedRepo.close()

    def testLoad(self):
        loadedRepo = self.g.load(self.dumpedRepo)
        self.assertTrue(isinstance(loadedRepo, github.Repository.Repository))
        self.assertTrue(loadedRepo._requester is self.repo._requester)
        self.assertTrue(loadedRepo.owner._requester is self.repo._requester)
        self.assertEqual(loadedRepo.name, "PyGithub")
        self.assertEqual(loadedRepo.url, "https://api.github.com/repos/akfish/PyGithub")

    def testLoadAndUpdate(self):
        loadedRepo = self.g.load(self.dumpedRepo)
        self.assertTrue(loadedRepo.update())
