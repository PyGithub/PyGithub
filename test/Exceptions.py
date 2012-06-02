import github

import Framework

# To stay compatible with Python 2.6, we do not use self.assertRaises with only one argument
class Exceptions( Framework.TestCase ):
    def testInvalidInput( self ):
        try:
            self.g.get_user().create_key( "Bad key", "xxx" )
            self.fail( "Should have raised" )
        except github.GithubException, exception:
            self.assertEqual( exception.status, 422 )
            self.assertEqual(
                exception.data,
                {
                    "errors": [
                        {
                            "code": "custom",
                            "field": "key",
                            "message": "key is invalid. It must begin with 'ssh-rsa' or 'ssh-dss'. Check that you're copying the public half of the key",
                            "resource": "PublicKey"
                        }
                    ],
                    "message": "Validation Failed"
                }
            )
            self.assertEqual( str( exception ), "422 {u\'message\': u\'Validation Failed\', u\'errors\': [{u\'field\': u\'key\', u\'message\': u\"key is invalid. It must begin with \'ssh-rsa\' or \'ssh-dss\'. Check that you\'re copying the public half of the key\", u\'code\': u\'custom\', u\'resource\': u\'PublicKey\'}]}" )

    def testUnknownObject( self ):
        try:
            self.g.get_user().get_repo( "Xxx" )
            self.fail( "Should have raised" )
        except github.GithubException, exception:
            self.assertEqual( exception.status, 404 )
            self.assertEqual( exception.data, { "message": "Not Found" } )
            self.assertEqual( str( exception ), "404 {u'message': u'Not Found'}" )

    def testUnknownUser( self ):
        try:
            self.g.get_user( "ThisUserShouldReallyNotExist" )
            self.fail( "Should have raised" )
        except github.GithubException, exception:
            self.assertEqual( exception.status, 404 )
            self.assertEqual( exception.data, { "message": "Not Found" } )
            self.assertEqual( str( exception ), "404 {u'message': u'Not Found'}" )

    def testBadAuthentication( self ):
        try:
            github.Github( "BadUser", "BadPassword" ).get_user().login
            self.fail( "Should have raised" )
        except github.GithubException, exception:
            self.assertEqual( exception.status, 401 )
            self.assertEqual( exception.data, { "message": "Bad credentials" } )
            self.assertEqual( str( exception ), "401 {u'message': u'Bad credentials'}" )
