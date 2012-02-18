import unittest
import MockMockMock

from Github import Github

class TestCase( unittest.TestCase ):
    def setUp( self ):
        unittest.TestCase.setUp( self )

        self.g = Github( "login", "password" )

        self.requester = MockMockMock.Mock( "requester" )
        self.g._Github__requester = self.requester.object

    def tearDown( self ):
        self.requester.tearDown()
        unittest.TestCase.tearDown( self )

    def testCreateForkForUser( self ):
        self.requester.expect.dataRequest( "GET", "/users/xxx", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy", None, None ).andReturn( { "name": "yyy", "owner": { "login": "xxx" } } )
        self.requester.expect.dataRequest( "POST", "/repos/xxx/yyy/forks", None, None ).andReturn( { "name": "yyy", "owner": { "login": "login" } } )
        self.g.get_user().create_fork( self.g.get_user( "xxx" ).get_repo( "yyy" ) )

    def testCreateForkForOrganization( self ):
        self.requester.expect.dataRequest( "GET", "/orgs/ooo", None, None ).andReturn( { "login": "ooo" } )
        self.requester.expect.dataRequest( "GET", "/users/xxx", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy", None, None ).andReturn( { "name": "yyy", "owner": { "login": "xxx" } } )
        self.requester.expect.dataRequest( "POST", "/repos/xxx/yyy/forks", { "org": "ooo" }, None ).andReturn( { "name": "yyy", "owner": { "login": "ooo" } } )
        self.g.get_organization( "ooo" ).create_fork( self.g.get_user( "xxx" ).get_repo( "yyy" ) )

    def testQueryFollowing( self ):
        self.requester.expect.dataRequest( "GET", "/users/xxx", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.statusRequest( "GET", "/user/following/xxx", None, None ).andReturn( 404 )
        self.requester.expect.dataRequest( "GET", "/users/yyy", None, None ).andReturn( { "login": "yyy" } )
        self.requester.expect.statusRequest( "GET", "/user/following/yyy", None, None ).andReturn( 204 )
        self.assertFalse( self.g.get_user().has_in_following( self.g.get_user( "xxx" ) ) )
        self.assertTrue( self.g.get_user().has_in_following( self.g.get_user( "yyy" ) ) )

unittest.main()
