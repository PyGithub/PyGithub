# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

class PaginatedList:
    def __init__( self, url, args, requester, key, convert, contentClass ):
        self.__url = url
        self.__args = args
        self.__requester = requester
        self.__key = key
        self.__convert = convert
        self.__contentClass = contentClass
        self.__nextPage = 1
        self.__continue = True
        self.__elements = list()

    class __Slice:
        def __init__( self, theList, theSlice ):
            self.__list = theList
            self.__start = theSlice.start or 0
            self.__stop = theSlice.stop
            self.__step = theSlice.step or 1

        def __iter__( self ):
            index = self.__start
            while not self.__finished( index ) :
                if self.__list._isBiggerThan( index ):
                    yield self.__list[ index ]
                    index += self.__step
                else:
                    return

        def __finished( self, index ):
            return self.__stop is not None and index >= self.__stop

    def __iter__( self ):
        for element in self.__elements:
            yield element
        while self.__continue:
            newElements = self.__fetchNextPage()
            self.__continue = len( newElements ) > 0
            for element in newElements:
                yield element

    def __fetchNextPage( self ):
        if self.__nextPage != 1:
            self.__args[ "start_page" ] = self.__nextPage
        self.__nextPage += 1
        headers, data = self.__requester.requestAndCheck(
            "GET",
            self.__url,
            self.__args,
            None
        )
        newElements = [
            self.__contentClass( self.__requester, self.__convert( element ), completed = False )
            for element in data[ self.__key ]
        ]
        self.__elements += newElements
        return newElements

    def __getitem__( self, index ):
        assert isinstance( index, ( int, slice ) )
        if isinstance( index, int ):
            self.__fetchToIndex( index )
            return self.__elements[ index ]
        else:
            return self.__Slice( self, index )

    def _isBiggerThan( self, index ):
        return len( self.__elements ) > index or self.__continue

    def __fetchToIndex( self, index ):
        while len( self.__elements ) <= index and self.__continue:
            self.__fetchNextPage()

def convertUser( attributes ):
    login = attributes[ "login" ]
    return {
        "login": login,
        "url": "https://api.github.com/users/" + login,
    }

def convertRepo( attributes ):
    owner = attributes[ "owner" ]
    name = attributes[ "name" ]
    return {
        "owner": { "login": owner },
        "name": name,
        "url": "https://api.github.com/repos/" + owner + "/" + name,
    }

def convertIssue( attributes ):
    number = attributes[ "number" ]
    title = attributes[ "title" ]
    html_url = attributes[ "html_url" ]
    assert html_url.startswith( "https://github.com/" )
    url = html_url.replace( "https://github.com/", "https://api.github.com/repos/" )
    return {
        "title": title,
        "number": number,
        "url": url,
    }
