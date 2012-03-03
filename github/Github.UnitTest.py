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

    def testGist( self ):
        self.requester.expect.dataRequest( "GET", "/gists/123456", None, None ).andReturn( { "description": "xxx" } )
        g = self.g.get_gist( 123456 )
        self.assertEqual( g.description, "xxx" )
        self.requester.expect.statusRequest( "GET", "/gists/123456/star", None, None ).andReturn( 404 )
        self.assertFalse( g.is_starred() )
        self.requester.expect.statusRequest( "PUT", "/gists/123456/star", None, None ).andReturn( 204 )
        g.set_starred()
        self.requester.expect.statusRequest( "DELETE", "/gists/123456/star", None, None ).andReturn( 204 )
        g.reset_starred()
        self.requester.expect.dataRequest( "POST", "/gists/123456/fork", None, None ).andReturn( { "description": "yyy" } )
        self.assertEqual( g.create_fork().description, "yyy" )
        self.requester.expect.dataRequest( "GET", "/gists/starred", None, None ).andReturn( [ { "description": "xxx" }, { "description": "yyy" } ] )
        self.assertEqual( len( self.g.get_user().get_starred_gists() ), 2 )

    def testRepositoryReference( self ):
        self.requester.expect.dataRequest( "GET", "/user", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy", None, None ).andReturn( { "name": "yyy", "owner": { "login": "xxx" } } )
        r = self.g.get_user().get_repo( "yyy" )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy/milestones/1", None, None ).andReturn( { "number": 1 } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy/milestones/1/labels", {}, None ).andReturn( [ { "name": "a" } ] )
        self.assertIs( r.get_milestone( 1 ).get_labels()[ 0 ]._repo, r )

unittest.main()
