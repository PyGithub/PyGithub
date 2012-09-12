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
    convertedAttributes = {
        "name": attributes[ "name" ],
        "created_at": attributes[ "created_at" ],
        "location": attributes[ "location" ],

        "login": attributes[ "login" ],
        "url": "/users/" + attributes[ "login" ],
    }
    if "gravatar_id" in attributes: convertedAttributes[ "gravatar_id" ] = attributes[ "gravatar_id" ]
    if "followers" in attributes: convertedAttributes[ "followers" ] = attributes[ "followers" ]
    if "repos" in attributes: convertedAttributes[ "public_repos" ] = attributes[ "repos" ]
    return convertedAttributes

def convertRepo( attributes ):
    convertedAttributes = {
        "created_at": attributes[ "created_at" ],
        "watchers": attributes[ "watchers" ],
        "has_downloads": attributes[ "has_downloads" ],
        "fork": attributes[ "fork" ],
        "has_issues": attributes[ "has_issues" ],
        "has_wiki": attributes[ "has_wiki" ],
        "forks": attributes[ "forks" ],
        "size": attributes[ "size" ],
        "private": attributes[ "private" ],
        "open_issues": attributes[ "open_issues" ],
        "description": attributes[ "description" ],
        "language": attributes[ "language" ],
        "name": attributes[ "name" ],

        "owner": { "login": attributes[ "owner" ], "url": "/users/" + attributes[ "owner" ] },
        "url": "/repos/" + attributes[ "owner" ] + "/" + attributes[ "name" ],
    }
    if "pushed_at" in attributes: convertedAttributes[ "pushed_at" ] = attributes[ "pushed_at" ]
    if "homepage" in attributes: convertedAttributes[ "homepage" ] = attributes[ "homepage" ]
    return convertedAttributes

def convertIssue( attributes ):
    html_url = attributes[ "html_url" ]
    assert html_url.startswith( "https://github.com/" )
    url = html_url.replace( "https://github.com/", "/repos/" )
    return {
        "title": attributes[ "title" ],
        "number": attributes[ "number" ],
        "created_at": attributes[ "created_at" ],
        "comments": attributes[ "comments" ],
        "body": attributes[ "body" ],
        "updated_at": attributes[ "updated_at" ],
        "state": attributes[ "state" ],

        "url": url,
        "user": { "login": attributes[ "user" ], "url": "/users/" + attributes[ "user" ] },
        "labels": [ { "name": label } for label in attributes[ "labels" ] ],
    }
