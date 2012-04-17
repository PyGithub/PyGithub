#!/bin/env python

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
                    "",
                ]:
                    continue
                
                if url not in verbsByUrl:
                    verbsByUrl[ url ] = set()
                verbsByUrl[ url ].add( verb )

functionsByUrlVerb = dict()
url = None
with open( "ReferenceOfApis.md" ) as f:
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
