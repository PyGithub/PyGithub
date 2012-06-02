import Framework

import datetime

class IssueEvent( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.event = self.g.get_user().get_repo( "PyGithub" ).get_issues_event( 16348656 )

    def testAttributes( self ):
        self.assertEqual( self.event.actor.login, "jacquev6" )
        self.assertEqual( self.event.commit_id, "ed866fc43833802ab553e5ff8581c81bb00dd433" )
        self.assertEqual( self.event.created_at, datetime.datetime( 2012, 5, 27, 7, 29, 25 ) )
        self.assertEqual( self.event.event, "referenced" )
        self.assertEqual( self.event.id, 16348656 )
        self.assertEqual( self.event.issue.number, 30 )
        self.assertEqual( self.event.url, "https://api.github.com/repos/jacquev6/PyGithub/issues/events/16348656" )
