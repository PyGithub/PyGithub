#!/bin/env python

import unittest

from github import Github
import GithubCredentials

class TestCase( unittest.TestCase ):
    def setUp( self ):
        self.g = Github( GithubCredentials.login, GithubCredentials.password )

    def testAuthenticatedUser( self ):
        u = self.g.get_user()
        self.assertEqual( u.login, "jacquev6" )
        self.assertEqual( u.name, "Vincent Jacques" )

unittest.main()
