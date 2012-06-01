import github

import Framework

class Exceptions( Framework.TestCase ):
    def testInvalidInput( self ):
        try: # Stay compatible with Python 2.6: do not use self.assertRaises with only one argument
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
