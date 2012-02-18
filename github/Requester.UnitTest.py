import unittest
import MockMockMock
import httplib
import base64

from Requester import Requester, UnknownGithubObject

class TestCase( unittest.TestCase ):
    def setUp( self ):
        unittest.TestCase.setUp( self )

        self.r = Requester( "login", "password" )
        self.b64_userpass = base64.b64encode( "login:password" )
        self.b64_userpass = self.b64_userpass.replace( '\n', '' )

        self.connectionFactory = MockMockMock.Mock( "httplib.HTTPSConnection" )
        self.connection = MockMockMock.Mock( "connection", self.connectionFactory )
        self.response = MockMockMock.Mock( "response", self.connectionFactory )

        httplib.HTTPSConnection = self.connectionFactory.object

    def tearDown( self ):
        self.connectionFactory.tearDown()
        unittest.TestCase.tearDown( self )

    def expect( self, verb, url, input, status, responseHeaders, output ):
        self.connectionFactory.expect( "api.github.com", strict = True ).andReturn( self.connection.object )
        self.connection.expect.request( verb, url, input, { "Authorization" : "Basic " + self.b64_userpass } )
        self.connection.expect.getresponse().andReturn( self.response.object )
        self.response.expect.status.andReturn( status )
        self.response.expect.getheaders().andReturn( responseHeaders )
        self.response.expect.read().andReturn( output )
        self.connection.expect.close()

    def testSimpleStatus( self ):
        self.expect( "GET", "/test", "null", 200, [], "" )
        self.assertEqual( self.r.statusRequest( "GET", "/test", None, None ), 200 )

    def testSimpleData( self ):
        self.expect( "GET", "/test", "null", 200, [], '{ "foo": "bar" }' )
        self.assertEqual( self.r.dataRequest( "GET", "/test", None, None ), { "foo" : "bar" } )

    def testDataOnBadStatus( self ):
        self.expect( "GET", "/test", "null", 404, [], '{ "foo": "bar" }' )
        with self.assertRaises( UnknownGithubObject ):
            self.r.dataRequest( "GET", "/test", None, None )

    def testDataWithParametersAndData( self ):
        self.expect( "GET", "/test?tata=tutu&toto=titi", '{"xxx": 42}', 200, [], '{ "foo": "bar" }' )
        self.assertEqual( self.r.dataRequest( "GET", "/test", { "toto" : "titi", "tata" : "tutu" }, { "xxx" : 42 } ), { "foo" : "bar" } )

    def testPagination( self ):
        self.expect( "GET", "/test", 'null', 200, [ ( "link", "xxx; next, xxx; last" ) ], '[ 1, 2 ]' )
        self.expect( "GET", "/test?page=2", 'null', 200, [ ( "link", "xxx; prev, xxx; first, xxx; next, xxx; last" ) ], '[ 3, 4 ]' )
        self.expect( "GET", "/test?page=3", 'null', 200, [ ( "link", "xxx; prev, xxx; first" ) ], '[ 5, 6 ]' )
        self.assertEqual( self.r.dataRequest( "GET", "/test", None, None ), [ 1, 2, 3, 4, 5, 6 ] )

unittest.main()
