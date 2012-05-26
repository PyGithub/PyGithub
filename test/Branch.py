import Framework

class Branch( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.branch = self.g.get_user().get_repo( "PyGithub" ).get_branches()[ 0 ]

    def testAttributes( self ):
        self.assertEqual( self.branch.name, "topic/RewriteWithGeneratedCode" )
        self.assertEqual( self.branch.commit.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
