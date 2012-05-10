import Framework

class GitBlob( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.b = self.g.get_user().get_repo( "PyGithub" ).get_git_blob( "53bce9fa919b4544e67275089b3ec5b44be20667" )

    def testAttributes( self ):
        self.assertTrue( self.b.content.startswith( "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCgpmcm9tIGRpc3R1dGlscy5jb3JlIGlt\ncG9ydCBzZXR1cAppbXBvcnQgdGV4dHdyYXAKCnNldHVwKAogICAgbmFtZSA9\n" ) )
        self.assertTrue( self.b.content.endswith( "Z3JhbW1pbmcgTGFuZ3VhZ2UgOjogUHl0aG9uIiwKICAgICAgICAiVG9waWMg\nOjogU29mdHdhcmUgRGV2ZWxvcG1lbnQiLAogICAgXSwKKQo=\n" ) )
        self.assertEqual( len( self.b.content ), 1757 )
        self.assertEqual( self.b.encoding, "base64" )
        self.assertEqual( self.b.size, 1295 )
        self.assertEqual( self.b.sha, "53bce9fa919b4544e67275089b3ec5b44be20667" )
        self.assertEqual( self.b.url, "https://api.github.com/repos/jacquev6/PyGithub/git/blobs/53bce9fa919b4544e67275089b3ec5b44be20667" )

class GitCommit( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.c = self.g.get_user().get_repo( "PyGithub" ).get_git_commit( "4303c5b90e2216d927155e9609436ccb8984c495" )

    def testAttributes( self ):
        self.assertEqual( self.c.author.name, "Vincent Jacques" )
        self.assertEqual( self.c.author.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.c.author.date, "2012-04-17T10:55:16-07:00" )
        self.assertEqual( self.c.committer.name, "Vincent Jacques" )
        self.assertEqual( self.c.committer.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.c.committer.date, "2012-04-17T10:55:16-07:00" )
        self.assertEqual( self.c.message, "Merge branch 'develop'\n" )
        self.assertEqual( len( self.c.parents ), 2 )
        self.assertEqual( self.c.parents[ 0 ].sha, "936f4a97f1a86392637ec002bbf89ff036a5062d" )
        self.assertEqual( self.c.parents[ 1 ].sha, "2a7e80e6421c5d4d201d60619068dea6bae612cb" )
        self.assertEqual( self.c.sha, "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( self.c.tree.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( self.c.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495" )

class GitTree( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.t = self.g.get_user().get_repo( "PyGithub" ).get_git_tree( "f492784d8ca837779650d1fb406a1a3587a764ad" )

    def testAttributes( self ):
        self.assertEqual( self.t.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( len( self.t.tree ), 11 )
        self.assertEqual( self.t.url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees/f492784d8ca837779650d1fb406a1a3587a764ad" )
