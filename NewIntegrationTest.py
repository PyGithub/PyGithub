#!/bin/env python

import os
import sys
import unittest
import httplib
import traceback

import github

class FakeHttpResponse:
    def __init__( self, status, headers, output ):
        self.status = status
        self.__headers = headers
        self.__output = output

    def getheaders( self ):
        return self.__headers

    def read( self ):
        return self.__output

class RecordingHttpsConnection:
    __realHttpsConnection = httplib.HTTPSConnection

    def __init__( self, file, *args, **kwds ):
        self.__file = file
        self.__cnx = self.__realHttpsConnection( *args, **kwds )

    def request( self, verb, url, input, headers ):
        print verb, url
        self.__cnx.request( verb, url, input, headers )
        del headers[ "Authorization" ] # Do not let sensitive info in git :-p
        self.__file.write( verb + " " + url + " " + str( headers ) + " " + input + "\n" )

    def getresponse( self ):
        res = self.__cnx.getresponse()

        status = res.status
        headers = res.getheaders()
        output = res.read()

        self.__file.write( str( status ) + "\n" )
        self.__file.write( str( headers ) + "\n" )
        self.__file.write( str( output ) + "\n" )

        return FakeHttpResponse( status, headers, output )

    def close( self ):
        self.__file.write( "\n" )
        return self.__cnx.close()

class ReplayingHttpsConnection:
    def __init__( self, testCase, file ):
        self.__testCase = testCase
        self.__file = file

    def request( self, verb, url, input, headers ):
        del headers[ "Authorization" ]
        expectation = self.__file.readline().strip()
        self.__testCase.assertEqual( verb + " " + url + " " + str( headers ) + " " + input, expectation )

    def getresponse( self ):
        status = int( self.__file.readline().strip() )
        headers = eval( self.__file.readline().strip() )
        output = self.__file.readline().strip()

        return FakeHttpResponse( status, headers, output )

    def close( self ):
        self.__file.readline()

class TestCase( unittest.TestCase ):
    recordMode = False

    def setUp( self ):
        unittest.TestCase.setUp( self )
        self.__fileName = ""
        self.__file = None
        if self.recordMode:
            import GithubCredentials
            httplib.HTTPSConnection = lambda *args, **kwds: RecordingHttpsConnection( self.__openFile( "w" ), *args, **kwds )
            self.g = github.Github( GithubCredentials.login, GithubCredentials.password )
        else:
            httplib.HTTPSConnection = lambda *args, **kwds: ReplayingHttpsConnection( self, self.__openFile( "r" ) )
            self.g = github.Github( "login", "password" )

    def tearDown( self ):
        unittest.TestCase.tearDown( self )
        self.__closeReplayFileIfNeeded()

    def __openFile( self, mode ):
        for ( _, _, functionName, _ ) in traceback.extract_stack():
            if functionName.startswith( "test" ) or functionName == "setUp" or functionName == "tearDown":
                fileName = os.path.join( "ReplayDataForNewIntegrationTest", self.__class__.__name__ + "." + functionName + ".txt" )
        if fileName != self.__fileName:
            self.__closeReplayFileIfNeeded()
            self.__fileName = fileName
            self.__file = open( self.__fileName, mode )
        return self.__file

    def __closeReplayFileIfNeeded( self ):
        if self.__file is not None:
            if not self.recordMode:
                self.assertEqual( self.__file.readline(), "" )
            self.__file.close()

class AuthenticatedUser( TestCase ):
    def setUp( self ):
        TestCase.setUp( self )
        self.u = self.g.get_user()

    def testAttributes( self ):
        self.assertEqual( self.u.avatar_url, "https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" )
        self.assertEqual( self.u.bio, "" )
        self.assertEqual( self.u.blog, "http://vincent-jacques.net" )
        self.assertEqual( self.u.collaborators, 0 )
        self.assertEqual( self.u.company, "Criteo" )
        self.assertEqual( self.u.created_at, "2010-07-09T06:10:06Z" )
        self.assertEqual( self.u.disk_usage, 16692 )
        self.assertEqual( self.u.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.u.followers, 13 )
        self.assertEqual( self.u.following, 24 )
        self.assertEqual( self.u.gravatar_id, "b68de5ae38616c296fa345d2b9df2225" )
        self.assertEqual( self.u.hireable, False )
        self.assertEqual( self.u.html_url, "https://github.com/jacquev6" )
        self.assertEqual( self.u.id, 327146 )
        self.assertEqual( self.u.location, "Paris, France" )
        self.assertEqual( self.u.login, "jacquev6" )
        self.assertEqual( self.u.name, "Vincent Jacques" )
        self.assertEqual( self.u.owned_private_repos, 5 )
        self.assertEqual( self.u.plan.name, "micro" )
        self.assertEqual( self.u.plan.collaborators, 1 )
        self.assertEqual( self.u.plan.space, 614400 )
        self.assertEqual( self.u.plan.private_repos, 5 )
        self.assertEqual( self.u.private_gists, 5 )
        self.assertEqual( self.u.public_gists, 1 )
        self.assertEqual( self.u.public_repos, 10 )
        self.assertEqual( self.u.total_private_repos, 5 )
        self.assertEqual( self.u.type, "User" )
        self.assertEqual( self.u.url, "https://api.github.com/users/jacquev6" )

    def testEditWithoutArguments( self ):
        self.u.edit()

    def testEditWithAllArguments( self ):
        oldName = self.u.name
        newName = "Name edited by PyGithub"

        oldEmail = self.u.email
        newEmail = "Email edited by PyGithub"

        oldBlog = self.u.blog
        newBlog = "Blog edited by PyGithub"

        oldCompany = self.u.company
        newCompany = "Company edited by PyGithub"

        oldLocation = self.u.location
        newLocation = "Location edited by PyGithub"

        oldHireable = self.u.hireable
        newHireable = not oldHireable

        oldBio = self.u.bio
        newBio = "Bio edited by PyGithub"

        self.u.edit( newName, newEmail, newBlog, newCompany, newLocation, newHireable, newBio )
        self.assertEqual( self.u.name, newName )
        self.assertEqual( self.u.email, newEmail )
        self.assertEqual( self.u.blog, newBlog )
        self.assertEqual( self.u.company, newCompany )
        self.assertEqual( self.u.location, newLocation )
        self.assertEqual( self.u.hireable, newHireable )
        self.assertEqual( self.u.bio, newBio )

        self.u.edit( oldName, oldEmail, oldBlog, oldCompany, oldLocation, oldHireable, oldBio )
        self.assertEqual( self.u.name, oldName )
        self.assertEqual( self.u.email, oldEmail )
        self.assertEqual( self.u.blog, oldBlog )
        self.assertEqual( self.u.company, oldCompany )
        self.assertEqual( self.u.location, oldLocation )
        self.assertEqual( self.u.hireable, oldHireable )
        self.assertEqual( self.u.bio, oldBio )

class GitBlob( TestCase ):
    def setUp( self ):
        TestCase.setUp( self )
        self.b = self.g.get_user().get_repo( "PyGithub" ).get_git_blob( "53bce9fa919b4544e67275089b3ec5b44be20667" )

    def testAttributes( self ):
        self.assertTrue( self.b.content.startswith( "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCgpmcm9tIGRpc3R1dGlscy5jb3JlIGlt\ncG9ydCBzZXR1cAppbXBvcnQgdGV4dHdyYXAKCnNldHVwKAogICAgbmFtZSA9\n" ) )
        self.assertTrue( self.b.content.endswith( "Z3JhbW1pbmcgTGFuZ3VhZ2UgOjogUHl0aG9uIiwKICAgICAgICAiVG9waWMg\nOjogU29mdHdhcmUgRGV2ZWxvcG1lbnQiLAogICAgXSwKKQo=\n" ) )
        self.assertEqual( len( self.b.content ), 1757 )
        self.assertEqual( self.b.encoding, "base64" )
        self.assertEqual( self.b.size, 1295 )
        self.assertEqual( self.b.sha, "53bce9fa919b4544e67275089b3ec5b44be20667" )
        self.assertEqual( self.b.url, "https://api.github.com/repos/jacquev6/PyGithub/git/blobs/53bce9fa919b4544e67275089b3ec5b44be20667" )

class GitCommit( TestCase ):
    def setUp( self ):
        TestCase.setUp( self )
        self.c = self.g.get_user().get_repo( "PyGithub" ).get_git_commit( "4303c5b90e2216d927155e9609436ccb8984c495" )

    def testAttributes( self ):
        self.assertEqual( self.c.author, { "date": "2012-04-17T10:55:16-07:00", "email": "vincent@vincent-jacques.net", "name": "Vincent Jacques" } ) ### @todo Structure
        self.assertEqual( self.c.committer, { "date": "2012-04-17T10:55:16-07:00", "email": "vincent@vincent-jacques.net", "name": "Vincent Jacques" } ) ### @todo Structure
        self.assertEqual( self.c.message, "Merge branch 'develop'\n" )
        self.assertEqual( self.c.parents, [{u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/commits/936f4a97f1a86392637ec002bbf89ff036a5062d', u'sha': u'936f4a97f1a86392637ec002bbf89ff036a5062d'}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/commits/2a7e80e6421c5d4d201d60619068dea6bae612cb', u'sha': u'2a7e80e6421c5d4d201d60619068dea6bae612cb'}] ) ### @todo Structure
        self.assertEqual( self.c.sha, "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( self.c.tree.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( self.c.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495" )

class GitTree( TestCase ):
    def setUp( self ):
        TestCase.setUp( self )
        self.t = self.g.get_user().get_repo( "PyGithub" ).get_git_tree( "f492784d8ca837779650d1fb406a1a3587a764ad" )

    def testAttributes( self ):
        self.assertEqual( self.t.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( len( self.t.tree ), 11 )
        self.assertEqual( self.t.url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees/f492784d8ca837779650d1fb406a1a3587a764ad" )

class Repository( TestCase ):
    def setUp( self ):
        TestCase.setUp( self )
        self.r = self.g.get_user().get_repo( "PyGithub" )

    def testAttributes( self ):
        self.assertEqual( self.r.clone_url, "https://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( self.r.created_at, "2012-02-25T12:53:47Z" )
        self.assertEqual( self.r.description, "Python library implementing the full Github API v3" )
        self.assertEqual( self.r.fork, False )
        self.assertEqual( self.r.forks, 2 )
        self.assertEqual( self.r.git_url, "git://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( self.r.has_downloads, True )
        self.assertEqual( self.r.has_issues, True )
        self.assertEqual( self.r.has_wiki, False )
        self.assertEqual( self.r.homepage, "http://vincent-jacques.net/PyGithub" )
        self.assertEqual( self.r.html_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( self.r.id, 3544490 )
        self.assertEqual( self.r.language, "Python" )
        self.assertEqual( self.r.master_branch, None ) ### @todo Why does this trigger a new request to github ? Because the object does not know that it is already completed, and it tries to de-None-ify master_branch
        self.assertEqual( self.r.mirror_url, None )
        self.assertEqual( self.r.name, "PyGithub" )
        self.assertEqual( self.r.open_issues, 15 )
        self.assertEqual( self.r.organization, None )
        self.assertEqual( self.r.owner.login, "jacquev6" )
        self.assertEqual( self.r.parent, None )
        self.assertEqual( self.r.permissions, { "admin": True, "pull": True, "push": True } ) ### @todo Create a Permission class
        self.assertEqual( self.r.private, False )
        self.assertEqual( self.r.pushed_at, "2012-05-08T19:27:43Z" )
        self.assertEqual( self.r.size, 212 )
        self.assertEqual( self.r.source, None )
        self.assertEqual( self.r.ssh_url, "git@github.com:jacquev6/PyGithub.git" )
        self.assertEqual( self.r.svn_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( self.r.updated_at, "2012-05-08T19:27:43Z" )
        self.assertEqual( self.r.url, "https://api.github.com/repos/jacquev6/PyGithub" )
        self.assertEqual( self.r.watchers, 13 )

if "--record" in sys.argv:
    TestCase.recordMode = True

unittest.main( argv = [ arg for arg in sys.argv if arg != "--record" ] )
