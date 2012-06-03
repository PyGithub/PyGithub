# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import GithubException

class _NotSetType:
    pass
NotSet = _NotSetType()

class BasicGithubObject( object ):
    def __init__( self, requester, attributes, completed ): ### 'completed' may be removed if I find a way
        self._requester = requester
        self._initAttributes()
        self._useAttributes( attributes )

    @staticmethod
    def _parentUrl( url ):
        return "/".join( url.split( "/" )[ : -1 ] )

    @staticmethod
    def _NoneIfNotSet( value ):
        if value is NotSet:
            return None
        else:
            return value

class GithubObject( BasicGithubObject ):
    def __init__( self, requester, attributes, completed ):
        BasicGithubObject.__init__( self, requester, attributes, completed )
        self.__completed = completed

    def _completeIfNotSet( self, value ):
        if not self.__completed and value is NotSet:
            self.__complete()

    def __complete( self ):
        headers, data = self._requester.requestAndCheck(
            "GET",
            self._url,
            None,
            None
        )
        self._useAttributes( data )
        self._completed = True
