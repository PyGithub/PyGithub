#!/bin/env python

from github import Github
import GithubCredentials

g = Github( GithubCredentials.login, GithubCredentials.password )

u = g.get_user()
print u.login, "(" + u.name + ")"
for r in u.get_repos():
    print " ", r.name,
    if r.fork:
        print "<-", r.parent.owner.login + "/" + r.parent.name,
        print "<-", r.source.owner.login + "/" + r.source.name,
    print
print

u = g.get_user( "nvie" )
print u.login, u.name
print ", ".join( r.name for r in u.get_repos() )
print
