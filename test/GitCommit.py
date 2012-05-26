import Framework

class GitCommit( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.commit = self.g.get_user().get_repo( "PyGithub" ).get_git_commit( "4303c5b90e2216d927155e9609436ccb8984c495" )

    def testAttributes( self ):
        self.assertEqual( self.commit.author.name, "Vincent Jacques" )
        self.assertEqual( self.commit.author.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.commit.author.date, "2012-04-17T10:55:16-07:00" )
        self.assertEqual( self.commit.committer.name, "Vincent Jacques" )
        self.assertEqual( self.commit.committer.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.commit.committer.date, "2012-04-17T10:55:16-07:00" )
        self.assertEqual( self.commit.message, "Merge branch 'develop'\n" )
        self.assertEqual( len( self.commit.parents ), 2 )
        self.assertEqual( self.commit.parents[ 0 ].sha, "936f4a97f1a86392637ec002bbf89ff036a5062d" )
        self.assertEqual( self.commit.parents[ 1 ].sha, "2a7e80e6421c5d4d201d60619068dea6bae612cb" )
        self.assertEqual( self.commit.sha, "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( self.commit.tree.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( self.commit.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495" )
