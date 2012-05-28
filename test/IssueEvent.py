import Framework

class IssueEvent( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.event = self.g.get_user().get_repo( "PyGithub" ).get_issues_event( 16348656 )

    def testAttributes( self ):
        self.assertEqual( self.event.actor.login, "jacquev6" )
        self.assertEqual( self.event.commit_id, "ed866fc43833802ab553e5ff8581c81bb00dd433" )
        self.assertEqual( self.event.created_at, "2012-05-27T07:29:25Z" )
        self.assertEqual( self.event.event, "referenced" )
        self.assertEqual( self.event.id, 16348656 )
        self.assertEqual( self.event.issue.number, 30 )
        self.assertEqual( self.event.url, "https://api.github.com/repos/jacquev6/PyGithub/issues/events/16348656" )
