import Framework
import github

class Authentication( Framework.BasicTestCase ):
    def testNoAuthentication( self ):
        g = github.Github()
        self.assertEqual( g.get_user( "jacquev6" ).name, "Vincent Jacques" )

    def testBasicAuthentication( self ):
        g = github.Github( self.login, self.password )
        self.assertEqual( g.get_user( "jacquev6" ).name, "Vincent Jacques" )

    def testOAuthAuthentication( self ):
        g = github.Github( self.oauth_token )
        self.assertEqual( g.get_user( "jacquev6" ).name, "Vincent Jacques" )
