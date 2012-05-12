import Framework

class Milestones( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.repo = self.g.get_user().get_repo( "PyGithub" )

    def testAttributes( self ):
        milestone = self.repo.get_milestone( 1 )
        self.assertEqual( milestone.closed_issues, 2 )
        self.assertEqual( milestone.created_at, "2012-03-08T12:22:10Z" )
        self.assertEqual( milestone.description, "" )
        self.assertEqual( milestone.due_on, "2012-03-13T07:00:00Z" )
        self.assertEqual( milestone.id, 93546 )
        self.assertEqual( milestone.number, 1 )
        self.assertEqual( milestone.open_issues, 0 )
        self.assertEqual( milestone.state, "closed" )
        self.assertEqual( milestone.title, "Version 0.4" )
        self.assertEqual( milestone.url, "https://api.github.com/repos/jacquev6/PyGithub/milestones/1" )
        self.assertEqual( milestone.creator.login, "jacquev6" )
