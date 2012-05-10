import Framework

class Branch( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.b = self.g.get_user().get_repo( "PyGithub" ).get_branches()[ 0 ]

    def testAttributes( self ):
        self.assertEqual( self.b.name, "topic/RewriteWithGeneratedCode" )
        self.assertEqual( self.b.commit.author.login, "jacquev6" )
        self.assertEqual( self.b.commit.commit.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.b.commit.committer.login, "jacquev6" )
        self.assertEqual( len( self.b.commit.files ), 1 )
        self.assertEqual( self.b.commit.files[ 0 ].additions, 0 )
        self.assertEqual( self.b.commit.files[ 0 ].blob_url, "https://github.com/jacquev6/PyGithub/blob/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/github/GithubObjects/GitAuthor.py" )
        self.assertEqual( self.b.commit.files[ 0 ].changes, 20 )
        self.assertEqual( self.b.commit.files[ 0 ].deletions, 20 )
        self.assertEqual( self.b.commit.files[ 0 ].filename, "github/GithubObjects/GitAuthor.py" )
        self.assertTrue( isinstance( self.b.commit.files[ 0 ].patch, ( str, unicode ) ) )
        self.assertEqual( self.b.commit.files[ 0 ].raw_url, "https://github.com/jacquev6/PyGithub/raw/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/github/GithubObjects/GitAuthor.py" )
        self.assertEqual( self.b.commit.files[ 0 ].sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.b.commit.files[ 0 ].status, "modified" )
        self.assertEqual( len( self.b.commit.parents ), 1 )
        self.assertEqual( self.b.commit.parents[ 0 ].sha, "b46ed0dfde5ad02d3b91eb54a41c5ed960710eae" )
        self.assertEqual( self.b.commit.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.b.commit.stats.deletions, 20 )
        self.assertEqual( self.b.commit.stats.additions, 0 )
        self.assertEqual( self.b.commit.stats.total, 20 )
        self.assertEqual( self.b.commit.url, "https://api.github.com/repos/jacquev6/PyGithub/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )

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

class GitRef( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.r = self.g.get_user().get_repo( "PyGithub" ).get_git_ref( "refs/heads/topic/RewriteWithGeneratedCode" )

    def testAttributes( self ):
        self.assertEqual( self.r.object.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.r.object.type, "commit" )
        self.assertEqual( self.r.object.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.r.ref, "refs/heads/topic/RewriteWithGeneratedCode" )
        self.assertEqual( self.r.url, "https://api.github.com/repos/jacquev6/PyGithub/git/refs/heads/topic/RewriteWithGeneratedCode" )

class GitTag( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.t = self.g.get_user().get_repo( "PyGithub" ).get_git_tag( "f5f37322407b02a80de4526ad88d5f188977bc3c" )

    def testAttributes( self ):
        self.assertEqual( self.t.message, "Version 0.6\n" )
        self.assertEqual( self.t.object.sha, "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( self.t.object.type, "commit" )
        self.assertEqual( self.t.object.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( self.t.sha, "f5f37322407b02a80de4526ad88d5f188977bc3c" )
        self.assertEqual( self.t.tag, "v0.6" )
        self.assertEqual( self.t.tagger.date, "2012-05-10T11:14:15-07:00" )
        self.assertEqual( self.t.tagger.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.t.tagger.name, "Vincent Jacques" )
        self.assertEqual( self.t.url, "https://api.github.com/repos/jacquev6/PyGithub/git/tags/f5f37322407b02a80de4526ad88d5f188977bc3c" )

class GitTree( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.t = self.g.get_user().get_repo( "PyGithub" ).get_git_tree( "f492784d8ca837779650d1fb406a1a3587a764ad" )

    def testAttributes( self ):
        self.assertEqual( self.t.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( len( self.t.tree ), 11 ) ### @todo
        self.assertEqual( self.t.url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees/f492784d8ca837779650d1fb406a1a3587a764ad" )
