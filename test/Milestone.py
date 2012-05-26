import Framework

class Milestone( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.milestone = self.g.get_user().get_repo( "PyGithub" ).get_milestone( 1 )

    def testAttributes( self ):
        self.assertEqual( self.milestone.closed_issues, 2 )
        self.assertEqual( self.milestone.created_at, "2012-03-08T12:22:10Z" )
        self.assertEqual( self.milestone.description, "" )
        self.assertEqual( self.milestone.due_on, "2012-03-13T07:00:00Z" )
        self.assertEqual( self.milestone.id, 93546 )
        self.assertEqual( self.milestone.number, 1 )
        self.assertEqual( self.milestone.open_issues, 0 )
        self.assertEqual( self.milestone.state, "closed" )
        self.assertEqual( self.milestone.title, "Version 0.4" )
        self.assertEqual( self.milestone.url, "https://api.github.com/repos/jacquev6/PyGithub/milestones/1" )
        self.assertEqual( self.milestone.creator.login, "jacquev6" )

    def testEditWithMinimalParameters( self ):
        self.milestone.edit( "Title edited by PyGithub" )
        self.assertEqual( self.milestone.title, "Title edited by PyGithub" )

    def testEditWithAllParameters( self ):
        self.milestone.edit( "Title edited twice by PyGithub", "closed", "Description edited by PyGithub", due_on = "2012-06-16" )
        self.assertEqual( self.milestone.title, "Title edited twice by PyGithub" )
        self.assertEqual( self.milestone.state, "closed" )
        self.assertEqual( self.milestone.description, "Description edited by PyGithub" )
        self.assertEqual( self.milestone.due_on, "2012-06-16T07:00:00Z" )

    def testGetLabels( self ):
        self.assertListKeyEqual( self.milestone.get_labels(), lambda l: l.name, [ "Public interface", "Project management" ] )

    def testDelete( self ):
        self.milestone.delete()
