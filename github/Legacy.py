# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

def PaginatedList( url, args, requester, key, convert, contentClass ):
    headers, data = requester.requestAndCheck(
        "GET",
        url,
        args,
        None
    )
    return [
        contentClass( requester, convert( element ), completed = False )
        for element in data[ key ]
    ]

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
