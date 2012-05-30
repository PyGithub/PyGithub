import github

import Framework

class Exceptions( Framework.TestCase ):
    def testInvalidInput( self ):
        with self.assertRaises( github.GithubException ) as cm:
            self.g.get_user().create_key( "Bad key", "xxx" )
        self.assertEqual( cm.exception.status, 422 )
        self.assertEqual(
            cm.exception.data,
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
