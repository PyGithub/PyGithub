#!/bin/env python

# Copyright 2012 Vincent Jacques
# vincent@vincent-jacques.net

# This file is part of PyGithub. http://vincent-jacques.net/PyGithub

# PyGithub is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License
# as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

# PyGithub is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License along with PyGithub.  If not, see <http://www.gnu.org/licenses/>.

import sys
import re

developerDotGithubDotComContentFiles = sys.argv[ 1: ]

verbsByUrl = dict()
for fileName in developerDotGithubDotComContentFiles:
    # print fileName
    with open( fileName ) as f:
        for line in f:
            m = re.match( "^.*(HEAD|GET|POST|PATCH|PUT|DELETE)\s+(/[^ \n]*).*$", line )
            if m:
                verb = m.group( 1 )
                url = m.group( 2 )
                
                # Normalize
                if url == "/gists/:gist_id/comments":
                    url = "/gists/:id/comments"
                if url == "/repos/:user/:repo/issues/:issue_number/events":
                    url = "/repos/:user/:repo/issues/:number/events"
                if url == "/users/:user/gists`":
                    url = "/users/:user/gists"
                if url in [
                    "/repos/:user/:repo/git/refs/heads/sc/featureA",
                    "/repos/:user/:repo/git/refs/tags",
                    "/repos/:user/:repo/git/trees/:sha?recursive=1",
                    "/repos/octocat/Hello-World/git/refs/heads/feature-a",
                    "/repos/octocat/Hello-World/git/refs/tags/v1.0",
                    "/repos/:user/:repo/git/refs/heads/skunkworkz/featureA",
                ]:
                    continue
                
                if url not in verbsByUrl:
                    verbsByUrl[ url ] = set()
                verbsByUrl[ url ].add( verb )

functionsByUrlVerb = dict()
url = None
with open( "doc/ReferenceOfApis.md" ) as f:
    for line in f:
        m = re.match( "^API `(.*)`$", line )
        if m:
            url = m.group( 1 )
        m = re.match( "^\* (.*): (.*)\n$", line )
        if m:
            verb = m.group( 1 )
            function = m.group( 2 )
            functionsByUrlVerb[ ( url, verb ) ] = function
                
for url in sorted( verbsByUrl.keys() ):
    header = "API `" + url + "`"
    print header
    print "=" * len( header )
    for verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ]:
        if verb in verbsByUrl[ url ]:
            if ( url, verb ) in functionsByUrlVerb:
                function = functionsByUrlVerb[ ( url, verb ) ]
            else:
                function = "(TODO)"
            print "* " + verb + ": " + function
    print
