import unittest
import MockMockMock

from Github import Github

class TestCase( unittest.TestCase ):
    def setUp( self ):
        unittest.TestCase.setUp( self )

        self.requester = MockMockMock.Mock( "requester" )
        self.debugFile = MockMockMock.Mock( "debugFile", self.requester )

        self.g = Github( "login", "password", self.debugFile.object )
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

    def testHooks( self ):
        self.requester.expect.dataRequest( "GET", "/user", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy", None, None ).andReturn( { "name": "yyy", "owner": { "login": "xxx" } } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy/hooks/1", None, None ).andReturn( { "name": "web", "id": 1 } )
        h = self.g.get_user().get_repo( "yyy" ).get_hook( 1 )
        self.requester.expect.statusRequest( "POST", "/repos/xxx/yyy/hooks/1/test", None, None ).andReturn( 204 )
        h.test()

    def testUserEvents( self ):
        self.requester.expect.dataRequest( "GET", "/users/xxx", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/users/xxx/events/public", None, None ).andReturn( [] )
        self.requester.expect.dataRequest( "GET", "/users/xxx/received_events/public", None, None ).andReturn( [] )
        u = self.g.get_user( "xxx" )
        u.get_public_events()
        u.get_public_received_events()

    def testRepoEvents( self ):
        self.requester.expect.dataRequest( "GET", "/user", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy", None, None ).andReturn( { "name": "yyy", "owner": { "login": "xxx" } } )
        self.requester.expect.dataRequest( "GET", "/networks/xxx/yyy/events", None, None ).andReturn( [] )
        r = self.g.get_user().get_repo( "yyy" )
        r.get_network_events()

    def testOrgEvents( self ):
        self.requester.expect.dataRequest( "GET", "/orgs/ooo", None, None ).andReturn( { "login": "ooo" } )
        self.requester.expect.dataRequest( "GET", "/user", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/users/xxx/events/orgs/ooo", None, None ).andReturn( [] )
        u = self.g.get_user()
        o = self.g.get_organization( "ooo" )
        u.get_organization_events( o )

    def testMergePullRequest( self ):
        self.requester.expect.dataRequest( "GET", "/user", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy", None, None ).andReturn( { "name": "yyy", "owner": { "login": "xxx" } } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy/pulls/42", None, None ).andReturn( { "number": 42 } )
        self.requester.expect.statusRequest( "GET", "/repos/xxx/yyy/pulls/42/merge", None, None ).andReturn( 404 )
        self.requester.expect.statusRequest( "PUT", "/repos/xxx/yyy/pulls/42/merge", None, {} ).andReturn( 204 )
        self.requester.expect.statusRequest( "GET", "/repos/xxx/yyy/pulls/42/merge", None, None ).andReturn( 204 )
        p = self.g.get_user().get_repo( "yyy" ).get_pull( 42 )
        self.assertFalse( p.is_merged() )
        p.merge()
        self.assertTrue( p.is_merged() )

    def testRepositoryCompare( self ):
        self.requester.expect.dataRequest( "GET", "/user", None, None ).andReturn( { "login": "xxx" } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy", None, None ).andReturn( { "name": "yyy", "owner": { "login": "xxx" } } )
        self.requester.expect.dataRequest( "GET", "/repos/xxx/yyy/compare/foo...bar", None, None ).andReturn( { "gabu": "zomeuh" } )
        self.assertEqual( self.g.get_user().get_repo( "yyy" ).compare( "foo", "bar" ), { "gabu": "zomeuh" } )

    def testDebugPrint( self ):
        self.requester.expect.dataRequest( "GET", "/user", None, None ).andReturn( { "login": "xxx", "unknownAttribute": 42 } )
        self.debugFile.expect.write( "Missing definition of attribute unknownAttribute in class AuthenticatedUser\n" )
        self.g.get_user().location

unittest.main()
