# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import datetime

import Framework

class Issue54( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.repo = self.g.get_user().get_repo( "PyGithub" )

    def testPositiveIntegerTimezone( self ):
        commit = self.repo.get_git_commit( "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( commit.author.timezone, datetime.timedelta( hours = 7 ) )

    def testNegativeIntegerTimezone( self ):
        commit = self.repo.get_git_commit( "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( commit.author.timezone, datetime.timedelta( hours = -7 ) )

    # I was not able to find a real commit with an half integer timezone, so I *forged* the associated responses from Github.
    # I *hope* they are what Github would send in that case
    def testPositiveHalfIntegerTimezone( self ):
        commit = self.repo.get_git_commit( "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( commit.author.timezone, datetime.timedelta( hours = 7, minutes = 30 ) )

    def testNegativeHalfIntegerTimezone( self ):
        commit = self.repo.get_git_commit( "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( commit.author.timezone, datetime.timedelta( hours = -7, minutes = -30 ) )
