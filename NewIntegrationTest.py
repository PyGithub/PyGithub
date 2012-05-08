#!/bin/env python

import os
import sys
import unittest
import httplib
import traceback

import github

class RecordReplayException( Exception ):
    pass

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
        print verb, url
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
        expectation = self.__file.readline().strip()
        while expectation.startswith( "#" ):
            self.__file.readline()
            self.__file.readline()
            self.__file.readline()
            self.__file.readline()
            expectation = self.__file.readline().strip()
        if expectation != verb + " " + url + " " + str( headers ) + " " + input:
            print "Expected [", expectation, "] but got [", verb + " " + url + " " + str( headers ) + " " + input, "]"
            raise RecordReplayException( "This test has been changed since last record. Please re-run this script with argument '--record'" )

    def getresponse( self ):
        return ReplayingHttpsConnection.HttpResponse( self.__file )

    def close( self ):
        self.__file.readline()

class TestCase( unittest.TestCase ):
    def setUp( self ):
        unittest.TestCase.setUp( self )
        self.__file = None
        httplib.HTTPSConnection = lambda *args, **kwds: ReplayingHttpsConnection( self.__openFile() )
        self.g = github.Github( "login", "password" )

    def tearDown( self ):
        unittest.TestCase.tearDown( self )
        self.__file.close()

    def __openFile( self ):
        for ( _, _, functionName, _ ) in traceback.extract_stack():
            if functionName.startswith( "test" ):
                fileName = os.path.join( "ReplayDataForNewIntegrationTest", self.__class__.__name__ + "." + functionName[ 4: ] + ".txt" )
        if self.__file is None:
            self.__file = open( fileName )
        return self.__file

class AuthenticatedUser( TestCase ):
    def setUp( self ):
        TestCase.setUp( self )
        self.u = self.g.get_user()

    def tearDown( self ):
        TestCase.tearDown( self )

    def testAttributes( self ):
        self.assertEqual( self.u.login, "jacquev6" )
        self.assertEqual( self.u.name, "Vincent Jacques" )

if len( sys.argv ) > 1:
    pass
else:
    unittest.main()
