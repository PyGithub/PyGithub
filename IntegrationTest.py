#!/bin/env python

from github import Github
import GithubCredentials

g = Github( GithubCredentials.login, GithubCredentials.password )

u = g.get_user()
print u.login, u.name
print

u = g.get_user( "nvie" )
print u.login, u.name
print
