import Framework

class GitTree( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.tree = self.g.get_user().get_repo( "PyGithub" ).get_git_tree( "f492784d8ca837779650d1fb406a1a3587a764ad" )

    def testAttributes( self ):
        self.assertEqual( self.tree.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( len( self.tree.tree ), 11 )
        self.assertEqual( self.tree.tree[ 0 ].mode, "100644" )
        self.assertEqual( self.tree.tree[ 0 ].path, ".gitignore" )
        self.assertEqual( self.tree.tree[ 0 ].sha, "8a9af1462c3f4e3358315c2d2e6ef1e7334c59dd" )
        self.assertEqual( self.tree.tree[ 0 ].size, 53 )
        self.assertEqual( self.tree.tree[ 0 ].type, "blob" )
        self.assertEqual( self.tree.tree[ 0 ].url, "https://api.github.com/repos/jacquev6/PyGithub/git/blobs/8a9af1462c3f4e3358315c2d2e6ef1e7334c59dd" )
        self.assertEqual( self.tree.tree[ 6 ].mode, "040000" )
        self.assertEqual( self.tree.tree[ 6 ].path, "ReplayDataForIntegrationTest" )
        self.assertEqual( self.tree.tree[ 6 ].sha, "60b4602b2c2070246c5df078fb7a5150b45815eb" )
        self.assertEqual( self.tree.tree[ 6 ].size, None )
        self.assertEqual( self.tree.tree[ 6 ].type, "tree" )
        self.assertEqual( self.tree.tree[ 6 ].url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees/60b4602b2c2070246c5df078fb7a5150b45815eb" )
        self.assertEqual( self.tree.url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees/f492784d8ca837779650d1fb406a1a3587a764ad" )
