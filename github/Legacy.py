# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

def PaginatedList( convert, contentClass, requester, headers, data ):
    return [
        contentClass( requester, convert( element ), completed = False )
        for element in data
    ]

def convertUser( attributes ):
    attributes[ "created_at" ] = attributes[ "created_at" ][ : 19 ] + "Z"
    if not isinstance( attributes[ "id" ], int ):
        attributes[ "id" ] = int( attributes[ "id" ][ 5 : ] )
    return attributes

def convertRepo( attributes ):
    attributes[ "created_at" ] = attributes[ "created_at" ][ : 19 ] + "Z"
    if "pushed_at" in attributes:
        attributes[ "pushed_at" ] = attributes[ "pushed_at" ][ : 19 ] + "Z"
    attributes[ "owner" ] = { "login": attributes[ "owner" ] }
    if "organization" in attributes:
        attributes[ "organization" ] = { "login": attributes[ "organization" ] }
    attributes[ "url" ] = "https://api.github.com/repos/" + "/".join( attributes[ "url" ].split( "/" )[ -2 : ] )
    return attributes

def convertIssue( attributes ):
    attributes[ "created_at" ] = attributes[ "created_at" ][ : 19 ] + "Z"
    attributes[ "updated_at" ] = attributes[ "updated_at" ][ : 19 ] + "Z"
    attributes[ "labels" ] = [ { "name": label } for label in attributes[ "labels" ] ]
    attributes[ "user" ] = { "login": attributes[ "user" ] }
    return attributes
