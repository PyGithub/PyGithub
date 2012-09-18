# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import base64

import Framework

import github
import datetime

class ContentFile( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.file = self.g.get_user().get_repo( "PyGithub" ).get_readme()

    def testAttributes( self ):
        self.assertEqual( self.file.type, "file" )
        self.assertEqual( self.file.encoding, "base64" )
        self.assertEqual( self.file.size, 7531 )
        self.assertEqual( self.file.name, "ReadMe.md" )
        self.assertEqual( self.file.path, "ReadMe.md" )
        self.assertEqual( len( base64.b64decode( self.file.content ) ), 7531 )
        self.assertEqual( self.file.sha, "5628799a7d517a4aaa0c1a7004d07569cd154df0" )
