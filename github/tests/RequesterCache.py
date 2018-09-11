# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2012 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2012 Zearin <zearin@gonk.net>                                      #
# Copyright 2013 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2014 Vincent Jacques <vincent@vincent-jacques.net>                 #
# Copyright 2015 Kyle Hornberg <khornberg@users.noreply.github.com>            #
# Copyright 2016 Jannis Gebauer <ja.geb@me.com>                                #
# Copyright 2016 Peter Buckley <dx-pbuckley@users.noreply.github.com>          #
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


class ActualRequest():
    def single(self, g):
        g.get_user().login
        limit = g.rate_limiting
        g.get_user().login
        new_limit = g.rate_limiting
        return (limit[0], new_limit[0])

    def loop(self, g, num_requests=10):
        g.get_user().login
        limit = g.rate_limiting
        for i in range(num_requests):
            g.get_user().login
        new_limit = g.rate_limiting
        return (limit[0], new_limit[0])

    def repo(self, g):
        repo = g.get_repo('PyGithub/PyGithub')
        repo.id
        limit = g.rate_limiting
        repo_again = g.get_repo('PyGithub/PyGithub')
        repo_again.id
        new_limit = g.rate_limiting
        return ((limit[0], new_limit[0]), (repo, repo_again))


class AggressiveCache(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.g.setCachePolicy(github.RequesterCache.AggressiveCache())
        self.action = ActualRequest()

    def testSingle(self):
        limits = self.action.single(self.g)
        self.assertEqual(limits[0], limits[1])

    def testLoop(self):
        limits = self.action.loop(self.g)
        self.assertEqual(limits[0], limits[1])

    def testRepo(self):
        limits, repos = self.action.repo(self.g)
        self.assertEqual(limits[0], limits[1])
        self.assertEqual(repos[0], repos[1])


class ClockCache(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.g.setCachePolicy(github.RequesterCache.ClockCache())
        self.action = ActualRequest()

    def testSingle(self):
        limits = self.action.single(self.g)
        self.assertEqual(limits[0], limits[1])

    def testLoop(self):
        limits = self.action.loop(self.g)
        self.assertEqual(limits[0], limits[1])

    def testRepo(self):
        limits, repos = self.action.repo(self.g)
        self.assertEqual(limits[0], limits[1])
        self.assertEqual(repos[0], repos[1])


class NoCache(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.action = ActualRequest()

    def testSingle(self):
        limits = self.action.single(self.g)
        self.assertEqual(limits[0], limits[1] + 1)

    def testLoop(self):
        limits = self.action.loop(self.g, 10)
        self.assertEqual(limits[0], limits[1] + 10)

    def testRepo(self):
        limits, repos = self.action.repo(self.g)
        self.assertEqual(limits[0], limits[1] + 1)
        self.assertEqual(repos[0], repos[1])
