# -*- coding: utf-8 -*-

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import sys

atLeastPython27 = sys.hexversion >= 0x02070000

if atLeastPython27:
    import unittest
else:  # pragma no cover
    import unittest2 as unittest  # pragma no cover

import AllTests


def run():
    testLoader = unittest.loader.TestLoader()
    testRunner = unittest.runner.TextTestRunner(verbosity=1)
    test = testLoader.loadTestsFromModule(AllTests)
    return testRunner.run(test)
