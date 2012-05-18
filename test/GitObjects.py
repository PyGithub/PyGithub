import Framework

class Branch( Framework.TestCaseWithRepo ):
    def testAttributes( self ):
        branch = self.repo.get_branches()[ 0 ]
        self.assertEqual( branch.name, "topic/RewriteWithGeneratedCode" )
        self.assertEqual( branch.commit.author.login, "jacquev6" )
        self.assertEqual( branch.commit.commit.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( branch.commit.committer.login, "jacquev6" )
        self.assertEqual( len( branch.commit.files ), 1 )
        self.assertEqual( branch.commit.files[ 0 ].additions, 0 )
        self.assertEqual( branch.commit.files[ 0 ].blob_url, "https://github.com/jacquev6/PyGithub/blob/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/github/GithubObjects/GitAuthor.py" )
        self.assertEqual( branch.commit.files[ 0 ].changes, 20 )
        self.assertEqual( branch.commit.files[ 0 ].deletions, 20 )
        self.assertEqual( branch.commit.files[ 0 ].filename, "github/GithubObjects/GitAuthor.py" )
        self.assertTrue( isinstance( branch.commit.files[ 0 ].patch, ( str, unicode ) ) )
        self.assertEqual( branch.commit.files[ 0 ].raw_url, "https://github.com/jacquev6/PyGithub/raw/1292bf0e22c796e91cc3d6e24b544aece8c21f2a/github/GithubObjects/GitAuthor.py" )
        self.assertEqual( branch.commit.files[ 0 ].sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( branch.commit.files[ 0 ].status, "modified" )
        self.assertEqual( len( branch.commit.parents ), 1 )
        self.assertEqual( branch.commit.parents[ 0 ].sha, "b46ed0dfde5ad02d3b91eb54a41c5ed960710eae" )
        self.assertEqual( branch.commit.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( branch.commit.stats.deletions, 20 )
        self.assertEqual( branch.commit.stats.additions, 0 )
        self.assertEqual( branch.commit.stats.total, 20 )
        self.assertEqual( branch.commit.url, "https://api.github.com/repos/jacquev6/PyGithub/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )

class GitBlob( Framework.TestCaseWithRepo ):
    def testAttributes( self ):
        blob = self.repo.get_git_blob( "53bce9fa919b4544e67275089b3ec5b44be20667" )
        self.assertTrue( blob.content.startswith( "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCgpmcm9tIGRpc3R1dGlscy5jb3JlIGlt\ncG9ydCBzZXR1cAppbXBvcnQgdGV4dHdyYXAKCnNldHVwKAogICAgbmFtZSA9\n" ) )
        self.assertTrue( blob.content.endswith( "Z3JhbW1pbmcgTGFuZ3VhZ2UgOjogUHl0aG9uIiwKICAgICAgICAiVG9waWMg\nOjogU29mdHdhcmUgRGV2ZWxvcG1lbnQiLAogICAgXSwKKQo=\n" ) )
        self.assertEqual( len( blob.content ), 1757 )
        self.assertEqual( blob.encoding, "base64" )
        self.assertEqual( blob.size, 1295 )
        self.assertEqual( blob.sha, "53bce9fa919b4544e67275089b3ec5b44be20667" )
        self.assertEqual( blob.url, "https://api.github.com/repos/jacquev6/PyGithub/git/blobs/53bce9fa919b4544e67275089b3ec5b44be20667" )

    def testCreate( self ):
        blob = self.repo.create_git_blob( "Blob created by PyGithub", "latin1" )
        self.assertEqual( blob.sha, "5dd930f591cd5188e9ea7200e308ad355182a1d8" )

class GitCommit( Framework.TestCaseWithRepo ):
    def testAttributes( self ):
        commit = self.repo.get_git_commit( "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( commit.author.name, "Vincent Jacques" )
        self.assertEqual( commit.author.email, "vincent@vincent-jacques.net" )
        self.assertEqual( commit.author.date, "2012-04-17T10:55:16-07:00" )
        self.assertEqual( commit.committer.name, "Vincent Jacques" )
        self.assertEqual( commit.committer.email, "vincent@vincent-jacques.net" )
        self.assertEqual( commit.committer.date, "2012-04-17T10:55:16-07:00" )
        self.assertEqual( commit.message, "Merge branch 'develop'\n" )
        self.assertEqual( len( commit.parents ), 2 )
        self.assertEqual( commit.parents[ 0 ].sha, "936f4a97f1a86392637ec002bbf89ff036a5062d" )
        self.assertEqual( commit.parents[ 1 ].sha, "2a7e80e6421c5d4d201d60619068dea6bae612cb" )
        self.assertEqual( commit.sha, "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( commit.tree.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( commit.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495" )

class GitRef( Framework.TestCaseWithRepo ):
    def testAttributes( self ):
        ref = self.repo.get_git_ref( "refs/heads/topic/RewriteWithGeneratedCode" )
        self.assertEqual( ref.object.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( ref.object.type, "commit" )
        self.assertEqual( ref.object.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( ref.ref, "refs/heads/topic/RewriteWithGeneratedCode" )
        self.assertEqual( ref.url, "https://api.github.com/repos/jacquev6/PyGithub/git/refs/heads/topic/RewriteWithGeneratedCode" )

    def testCreateEditDelete( self ):
        ref = self.repo.create_git_ref( "refs/heads/BranchCreatedByPyGithub", "4303c5b90e2216d927155e9609436ccb8984c495" )
        ref.edit( "04cde900a0775b51f762735637bd30de392a2793" )
        ref.edit( "4303c5b90e2216d927155e9609436ccb8984c495", force = True )
        ref.delete()

class GitTag( Framework.TestCaseWithRepo ):
    def testAttributes( self ):
        tag = self.repo.get_git_tag( "f5f37322407b02a80de4526ad88d5f188977bc3c" )
        self.assertEqual( tag.message, "Version 0.6\n" )
        self.assertEqual( tag.object.sha, "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( tag.object.type, "commit" )
        self.assertEqual( tag.object.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( tag.sha, "f5f37322407b02a80de4526ad88d5f188977bc3c" )
        self.assertEqual( tag.tag, "v0.6" )
        self.assertEqual( tag.tagger.date, "2012-05-10T11:14:15-07:00" )
        self.assertEqual( tag.tagger.email, "vincent@vincent-jacques.net" )
        self.assertEqual( tag.tagger.name, "Vincent Jacques" )
        self.assertEqual( tag.url, "https://api.github.com/repos/jacquev6/PyGithub/git/tags/f5f37322407b02a80de4526ad88d5f188977bc3c" )

class GitTree( Framework.TestCaseWithRepo ):
    def testAttributes( self ):
        tree = self.repo.get_git_tree( "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( tree.sha, "f492784d8ca837779650d1fb406a1a3587a764ad" )
        self.assertEqual( len( tree.tree ), 11 )
        self.assertEqual( tree.tree[ 0 ].mode, "100644" )
        self.assertEqual( tree.tree[ 0 ].path, ".gitignore" )
        self.assertEqual( tree.tree[ 0 ].sha, "8a9af1462c3f4e3358315c2d2e6ef1e7334c59dd" )
        self.assertEqual( tree.tree[ 0 ].size, 53 )
        self.assertEqual( tree.tree[ 0 ].type, "blob" )
        self.assertEqual( tree.tree[ 0 ].url, "https://api.github.com/repos/jacquev6/PyGithub/git/blobs/8a9af1462c3f4e3358315c2d2e6ef1e7334c59dd" )
        self.assertEqual( tree.tree[ 6 ].mode, "040000" )
        self.assertEqual( tree.tree[ 6 ].path, "ReplayDataForIntegrationTest" )
        self.assertEqual( tree.tree[ 6 ].sha, "60b4602b2c2070246c5df078fb7a5150b45815eb" )
        # self.assertEqual( tree.tree[ 6 ].size, None ) ### @todo This test tries to __complete the GitTreeElement. (Lazy-)Complete-ability should be specified in the json description, not deduced from the presence of a url attribute.
        self.assertEqual( tree.tree[ 6 ].type, "tree" )
        self.assertEqual( tree.tree[ 6 ].url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees/60b4602b2c2070246c5df078fb7a5150b45815eb" )
        self.assertEqual( tree.url, "https://api.github.com/repos/jacquev6/PyGithub/git/trees/f492784d8ca837779650d1fb406a1a3587a764ad" )
