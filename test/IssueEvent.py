import Framework

class IssueEvent( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.event = self.g.get_user().get_repo( "PyGithub" ).get_issues_event( 15819975 )

    def testAttributes( self ):
        self.assertEqual( self.event.actor.login, "jacquev6" )
        self.assertEqual( self.event.commit_id, None )
        self.assertEqual( self.event.created_at, "2012-05-19T10:38:23Z" )
        self.assertEqual( self.event.event, "subscribed" )
        self.assertEqual( self.event.id, 15819975 )
        self.assertEqual( self.event.issue.number, 28 )
        self.assertEqual( self.event.url, "https://api.github.com/repos/jacquev6/PyGithub/issues/events/15819975" )
