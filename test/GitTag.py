import Framework

class GitTag( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.tag = self.g.get_user().get_repo( "PyGithub" ).get_git_tag( "f5f37322407b02a80de4526ad88d5f188977bc3c" )

    def testAttributes( self ):
        self.assertEqual( self.tag.message, "Version 0.6\n" )
        self.assertEqual( self.tag.object.sha, "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( self.tag.object.type, "commit" )
        self.assertEqual( self.tag.object.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( self.tag.sha, "f5f37322407b02a80de4526ad88d5f188977bc3c" )
        self.assertEqual( self.tag.tag, "v0.6" )
        self.assertEqual( self.tag.tagger.date, "2012-05-10T11:14:15-07:00" )
        self.assertEqual( self.tag.tagger.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.tag.tagger.name, "Vincent Jacques" )
        self.assertEqual( self.tag.url, "https://api.github.com/repos/jacquev6/PyGithub/git/tags/f5f37322407b02a80de4526ad88d5f188977bc3c" )
