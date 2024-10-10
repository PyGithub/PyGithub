############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
# Copyright 2017 Hugo <hugovk@users.noreply.github.com>                        #
# Copyright 2018 sfdye <tsfdye@gmail.com>                                      #
# Copyright 2019 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2019 TechnicalPirate <35609336+TechnicalPirate@users.noreply.github.com>#
# Copyright 2019 Wan Liuyang <tsfdye@gmail.com>                                #
# Copyright 2020 Steve Kowalik <steven@wedontsleep.org>                        #
# Copyright 2023 Enrico Minack <github@enrico.minack.dev>                      #
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

from io import BytesIO as IO

import github

from . import Framework


class Persistence(Framework.TestCase):
    def setUp(self):
        super().setUp()
        self.repo = self.g.get_repo("akfish/PyGithub")

        self.dumpedRepo = IO()
        self.g.dump(self.repo, self.dumpedRepo)
        self.dumpedRepo.seek(0)

    def tearDown(self):
        self.dumpedRepo.close()
        super().tearDown()

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
