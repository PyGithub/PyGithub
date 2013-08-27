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
import io


class Persistence(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_repo("akfish/PyGithub")
        with self._openStorage('rb') as expectedF:
            self._expected = io.BytesIO(expectedF.read())

    def tearDown(self):
        self._expected.close()

    def assertLoaded(self, loaded, klass, is_dead):
        isRightType = isinstance(loaded, klass)
        isDead = loaded._requester is None
        deadMsg = "Expected dead == %r. But actually dead == %r" % (is_dead, isDead)
        self.assertTrue(isRightType, msg = "Unexpected type")
        self.assertEqual(is_dead, isDead, msg = deadMsg)
        
    def testSave(self):
        actual = io.BytesIO()
        self.repo.save(actual)
        self._expected.seek(0)
        actual.seek(0)
        self.assertEqual(self._expected.readlines(), actual.readlines())
        actual.close()
        
    def testLoadDead(self):
        self._expected.seek(0)

        loaded = github.GithubObject.GithubObject.load(self._expected)
        self.assertLoaded(loaded, self.repo.__class__, True)
    
    def testLoadDeadAndRevive(self):
        self._expected.seek(0)

        dead = github.GithubObject.GithubObject.load(self._expected)
        self.assertLoaded(dead, self.repo.__class__, True)
        live = self.g.revive(dead)
        self.assertLoaded(live, self.repo.__class__, False)

    def testGithubLoad(self):
        self._expected.seek(0)
        loaded = self.g.load(self._expected)
        self.assertLoaded(loaded, self.repo.__class__, False)

    def testLoadAndUpdate(self):
        self._expected.seek(0)

        loaded = self.g.load(self._expected)
        self.assertLoaded(loaded, self.repo.__class__, False)

        self.assertTrue(loaded.update(), msg="The repo should be changed by now. But update() != True")
