# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

from PaginatedList import PaginatedListBase

class PaginatedList( PaginatedListBase ):
    def __init__( self, url, args, requester, key, convert, contentClass ):
        PaginatedListBase.__init__( self, list() )
        self.__url = url
        self.__args = args
        self.__requester = requester
        self.__key = key
        self.__convert = convert
        self.__contentClass = contentClass
        self.__nextPage = 1
        self.__continue = True
        self.__elements = list()

    def _couldGrow( self ):
        return self.__continue

    def _fetchNextPage( self ):
        if self.__nextPage != 1:
            self.__args[ "start_page" ] = self.__nextPage
        self.__nextPage += 1
        headers, data = self.__requester.requestAndCheck(
            "GET",
            self.__url,
            self.__args,
            None
        )
        self.__continue = len( data[ self.__key ] ) > 0
        return [
            self.__contentClass( self.__requester, self.__convert( element ), completed = False )
            for element in data[ self.__key ]
        ]

def convertUser( attributes ):
    login = attributes[ "login" ]
    return {
        "login": login,
        "url": "/users/" + login,
    }

def convertRepo( attributes ):
    owner = attributes[ "owner" ]
    name = attributes[ "name" ]
    return {
        "owner": { "login": owner },
        "name": name,
        "url": "/repos/" + owner + "/" + name,
    }

def convertIssue( attributes ):
    number = attributes[ "number" ]
    title = attributes[ "title" ]
    html_url = attributes[ "html_url" ]
    assert html_url.startswith( "https://github.com/" )
    url = html_url.replace( "https://github.com/", "/repos/" )
    return {
        "title": title,
        "number": number,
        "url": url,
    }
