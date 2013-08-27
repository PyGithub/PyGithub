# -*- coding: utf-8 -*-

############################ Copyrights and license ############################
#                                                                              #
# Copyright 2013 AKFish <akfish@gmail.com>                                     #
#                                                                              #
# This file is part of PyGithub. http://jacquev6.github.com/PyGithub/          #
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

from __future__ import with_statement
import Framework
import github
import StringIO


class Persistence(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_repo("akfish/PyGithub")
        with self._openStorage('r') as expectedF:
            self._expected = StringIO.StringIO(expectedF.read())

    def tearDown(self):
        self._expected.close()
    
    def testSave(self):
        actual = StringIO.StringIO()
        self.repo.save(actual)
        self._expected.seek(0)
        actual.seek(0)
        self.assertEqual(self._expected.readlines(), actual.readlines())
        actual.close()
        
    def testLoadDead(self):
        self._expected.seek(0)

        loaded = github.GithubObject.GithubObject.load(self._expected)
        self.assertIsInstance(loaded, self.repo.__class__, msg = "Unexpected type")
        self.assertIsNone(loaded._requester, msg = "No requester should be saved")
    
    def testLoadDeadAndRevive(self):
        self._expected.seek(0)

        dead = github.GithubObject.GithubObject.load(self._expected)
        self.assertIsInstance(dead, self.repo.__class__, msg = "Unexpected type")
        self.assertIsNone(dead._requester, msg = "No requester should be saved")
        live = self.g.revive(dead)
        self.assertIsNotNone(live._requester, msg = "Expect a live one")

    def testGithubLoad(self):
        self._expected.seek(0)

        loaded = self.g.load(self._expected)
        self.assertIsInstance(loaded, self.repo.__class__, msg = "Unexpected type")
        self.assertIsNotNone(loaded._requester, msg = "Expect a live one")

    def testLoadAndUpdate(self):
        self._expected.seek(0)

        loaded = self.g.load(self._expected)
        self.assertIsInstance(loaded, self.repo.__class__, msg = "Unexpected type")
        self.assertIsNotNone(loaded._requester, msg = "Expect a live one")

        self.assertTrue(loaded.update(), msg="The repo should be changed by now. But update() != True")
