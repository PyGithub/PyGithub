import Framework

class Tag( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.tag = self.g.get_user().get_repo( "PyGithub" ).get_tags()[ 0 ]

    def testAttributes( self ):
        self.assertEqual( self.tag.commit.sha, "636e6112deb72277b3bffcc3303cd7e8a7431a5d" )
        self.assertEqual( self.tag.name, "v0.3" )
        self.assertEqual( self.tag.tarball_url, "https://github.com/jacquev6/PyGithub/tarball/v0.3" )
        self.assertEqual( self.tag.zipball_url, "https://github.com/jacquev6/PyGithub/zipball/v0.3" )
