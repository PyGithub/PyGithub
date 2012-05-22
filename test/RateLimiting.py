import Framework

class RateLimiting( Framework.TestCase ):
    def testRateLimiting( self ):
        self.assertEqual( self.g.rate_limiting, ( 5000, 5000 ) )
        self.g.get_user( "jacquev6" )
        self.assertEqual( self.g.rate_limiting, ( 4999, 5000 ) )
