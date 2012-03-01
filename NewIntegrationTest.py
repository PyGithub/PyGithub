#!/bin/env python

import time
import sys
import httplib
import base64

from github import Github

class RecordingHttpsConnection:
    class HttpResponse( object ):
        def __init__( self, file, res ):
            self.status = res.status
            self.__headers = res.getheaders()
            self.__output = res.read()
            file.write( str( self.status ) + "\n" )
            file.write( str( self.__headers ) + "\n" )
            file.write( str( self.__output ) + "\n" )

        def getheaders( self ):
            return self.__headers

        def read( self ):
            return self.__output

    __realHttpsConnection = httplib.HTTPSConnection

    def __init__( self, file, *args, **kwds ):
        self.__file = file
        self.__cnx = self.__realHttpsConnection( *args, **kwds )

    def request( self, verb, url, input, headers ):
        self.__cnx.request( verb, url, input, headers )
        del headers[ "Authorization" ] # Do not let sensitive info in git :-p
        self.__file.write( verb + " " + url + " " + str( headers ) + " " + input + "\n" )

    def getresponse( self ):
        return RecordingHttpsConnection.HttpResponse( self.__file, self.__cnx.getresponse() )

    def close( self ):
        self.__file.write( "\n" )
        return self.__cnx.close()

class ReplayingHttpsConnection:
    class HttpResponse( object ):
        def __init__( self, file ):
            self.status = int( file.readline().strip() )
            self.__headers = eval( file.readline().strip() )
            self.__output = file.readline().strip()

        def getheaders( self ):
            return self.__headers

        def read( self ):
            return self.__output

    def __init__( self, file ):
        self.__file = file

    def request( self, verb, url, input, headers ):
        del headers[ "Authorization" ]
        assert self.__file.readline().strip() == verb + " " + url + " " + str( headers ) + " " + input

    def getresponse( self ):
        return ReplayingHttpsConnection.HttpResponse( self.__file )

    def close( self ):
        self.__file.readline()

class RecordReplayException( Exception ):
    pass

class IntegrationTest:
    cobayeNamedUserLogin = "cjuniet"

    def main( self, argv ):
        if len( argv ) >= 1:
            if argv[ 0 ] == "--record":
                print "Record mode: this script is really going to do requests to github.com"
                argv = argv[ 1: ]
                record = True
            elif argv[ 0 ] == "--list":
                print "List of available tests:"
                print "\n".join( self.listTests() )
                return
        else:
            print "Replay mode: this script will used requests to and replies from github.com recorded in previous runs in record mode"
            record = False

        if len( argv ) == 0:
            tests = self.listTests()
        else:
            tests = argv
        self.runTests( tests, record )

    def prepareRecord( self, test ):
        self.avoidError500FromGithub = lambda: time.sleep( 1 )
        try:
            import GithubCredentials
            self.g = Github( GithubCredentials.login, GithubCredentials.password )
            file = open( self.__fileName( test ), "w" )
            httplib.HTTPSConnection = lambda *args, **kwds: RecordingHttpsConnection( file, *args, **kwds )
        except ImportError:
            raise RecordReplayException( textwrap.dedent( """\
                Please create a 'GithubCredentials.py' file containing:"
                login = '<your github login>'"
                password = '<your github password>'""" ) )

    def prepareReplay( self, test ):
        self.avoidError500FromGithub = lambda: 0
        try:
            file = open( self.__fileName( test ) )
            httplib.HTTPSConnection = lambda *args, **kwds: ReplayingHttpsConnection( file )
            self.g = Github( "login", "password" )
        except IOError:
            raise RecordReplayException( "Please re-run this script with argument '--record' to be able to replay the integration tests based on recorded first execution" )

    def __fileName( self, test ):
        return "ReplayDataForIntegrationTest." + test + ".txt"

    def listTests( self ):
        return [ f[ 4: ] for f in dir( self ) if f.startswith( "test" ) ]

    def runTests( self, tests, record ):
        for test in tests:
            print
            print test
            try:
                if record:
                    self.prepareRecord( test )
                else:
                    self.prepareReplay( test )
                getattr( self, "test" + test )()
            except RecordReplayException, e:
                print "*" * len( str( e ) )
                print e
                print "*" * len( str( e ) )

    def testAuthenticatedUserEdition( self ):
        print "Changing your user name (and reseting it)"
        u = self.g.get_user()
        originalName = u.name
        tmpName = u.name + " (edited by PyGithub)"
        print self.g.get_user().name, "->",
        u.edit( name = tmpName )
        print self.g.get_user().name, "->",
        u.edit( name = originalName )
        print self.g.get_user().name

    def testNamedUserDetails( self ):
        u = self.g.get_user( self.cobayeNamedUserLogin )
        print u.login, "(" + u.name + ") is from", u.location

    def testOrganizationDetails( self ):
        o = self.g.get_organization( "github" )
        print o.login, "(" + o.name + ") is in", o.location

IntegrationTest().main( sys.argv[ 1: ] )
