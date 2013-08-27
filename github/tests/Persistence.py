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

# damn you, 2.5!
if Framework.atLeastPython26:
    from io import BytesIO as IO
else:
    from io import StringIO as IO

class Persistence(Framework.TestCase):
    def setUp(self):
        Framework.TestCase.setUp(self)
        self.repo = self.g.get_repo("akfish/PyGithub")
        # Python 2 and Python 3's pickle format is not compatible
        # should flush every time
        # or just do this in-memory
        # though modifications to Framework will go wasted :(
        # let's pretend this is not meaningless for now
        with self._openStorage('wb') as f:
            self.repo.save(f)
        with self._openStorage('rb') as expectedF:
            self._expected = IO(expectedF.read())

    def tearDown(self):
        self._expected.close()

    def assertLoaded(self, loaded, klass, is_dead):
        isRightType = isinstance(loaded, klass)
        isDead = loaded._requester is None
        deadMsg = "Expected dead == %r. But actually dead == %r" % (is_dead, isDead)
        self.assertTrue(isRightType, msg = "Unexpected type")
        self.assertEqual(is_dead, isDead, msg = deadMsg)
        
    def testSave(self):
        actual = IO()
        self.repo.save(actual)
        # self._expected.seek(0)
        actual.seek(0)
        # self._expected can no longer be trusted, since it is also created by save()
        # self.assertEqual(self._expected.readlines(), actual.readlines())

        # instead:
        # load again
        loaded = self.g.load(actual)
        # and compare headers and rawData
        self.assertEqual(self.repo._rawData, loaded._rawData)
        self.assertEqual(self.repo._headers, loaded._headers)
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
