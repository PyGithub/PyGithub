import Framework

class Milestone( Framework.TestCaseWithRepo ):
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

    def testCreate( self ):
        milestone = self.repo.create_milestone( "Milestone created by PyGithub", state = "open", description = "Description created by PyGithub", due_on = "2012-06-15" )
        self.assertEqual( milestone.number, 5 )

    def testEditWithMinimalParameters( self ):
        milestone = self.repo.get_milestone( 5 )
        milestone.edit( "Title edited by PyGithub" )
        self.assertEqual( milestone.title, "Title edited by PyGithub" )

    def testEditWithAllParameters( self ):
        milestone = self.repo.get_milestone( 5 )
        milestone.edit( "Title edited twice by PyGithub", "closed", "Description edited by PyGithub", due_on = "2012-06-16" )
        self.assertEqual( milestone.title, "Title edited twice by PyGithub" )
        self.assertEqual( milestone.state, "closed" )
        self.assertEqual( milestone.description, "Description edited by PyGithub" )
        self.assertEqual( milestone.due_on, "2012-06-16T07:00:00Z" )

    def testGetLabels( self ):
        milestone = self.repo.get_milestone( 2 )
        labels = milestone.get_labels()
        self.assertEqual( labels[ 0 ].name, "Public interface" )

    def testDelete( self ):
        milestone = self.repo.get_milestone( 5 )
        milestone.delete()

class Issue( Framework.TestCaseWithRepo ):
    def testAttributes( self ):
        issue = self.repo.get_issue( 1 )
        self.assertEqual( issue.assignee.login, "jacquev6" )
        self.assertEqual( issue.body, "" )
        self.assertEqual( issue.closed_at, "2012-03-12T20:46:35Z" )
        self.assertEqual( issue.closed_by.login, "jacquev6" )
        self.assertEqual( issue.comments, 0 )
        self.assertEqual( issue.created_at, "2012-02-27T09:11:14Z" )
        self.assertEqual( issue.html_url, "https://github.com/jacquev6/PyGithub/issues/1" )
        self.assertEqual( issue.id, 3397707 )
        self.assertEqual( len( issue.labels ), 1 )
        self.assertEqual( issue.labels[ 0 ].name, "Bug" )
        self.assertEqual( issue.milestone.title, "Version 0.4" )
        self.assertEqual( issue.number, 1 )
        # self.assertEqual( issue.pull_request, "" )
        self.assertEqual( issue.state, "closed" )
        self.assertEqual( issue.title, "Gitub -> Github everywhere" )
        self.assertEqual( issue.updated_at, "2012-03-12T20:46:35Z" )
        self.assertEqual( issue.url, "https://api.github.com/repos/jacquev6/PyGithub/issues/1" )
        self.assertEqual( issue.user.login, "jacquev6" )

    def testCreate( self ):
        issue = self.repo.create_issue( "Issue created by PyGithub" )
        self.assertEqual( issue.number, 28 )

    def testEditWithoutParameters( self ):
        issue = self.repo.get_issue( 28 )
        issue.edit()

    def testEditWithAllParameters( self ):
        issue = self.repo.get_issue( 28 )
        ### @todo Variadic argument for labels?
        ### @todo NamedUser instead of string for assignee
        issue.edit( "Title edited by PyGithub", "Body edited by PyGithub", "jacquev6", "open", 2, [ "Bug" ] )
        self.assertEqual( issue.assignee.login, "jacquev6" )
        self.assertEqual( issue.body, "Body edited by PyGithub" )
        self.assertEqual( issue.state, "open" )
        self.assertEqual( issue.title, "Title edited by PyGithub" )
        self.assertEqual( len( issue.labels ), 1 )
        self.assertEqual( issue.labels[ 0 ].name, "Bug" )

class Label( Framework.TestCaseWithRepo ):
    def testAttributes( self ):
        label = self.repo.get_label( "Bug" )
        self.assertEqual( label.color, "e10c02" )
        self.assertEqual( label.name, "Bug" )
        self.assertEqual( label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/Bug" )

    def testCreate( self ):
        label = self.repo.create_label( "Label with silly name % * + created by PyGithub", "00ff00" )
        self.assertEqual( label.color, "00ff00" )
        self.assertEqual( label.name, "Label with silly name % * + created by PyGithub" )
        self.assertEqual( label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/Label+with+silly+name+%25+%2A+%2B+created+by+PyGithub" )

    def testGetLabelWithSillyName( self ):
        label = self.repo.get_label( "Label with silly name % * + created by PyGithub" )
        self.assertEqual( label.color, "00ff00" )
        self.assertEqual( label.name, "Label with silly name % * + created by PyGithub" )
        self.assertEqual( label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/Label+with+silly+name+%25+%2A+%2B+created+by+PyGithub" )

    def testEdit( self ):
        label = self.repo.get_label( "Label with silly name % * + created by PyGithub" )
        label.edit( "LabelEditedByPyGithub", "0000ff" )
        self.assertEqual( label.color, "0000ff" )
        self.assertEqual( label.name, "LabelEditedByPyGithub" )
        self.assertEqual( label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/LabelEditedByPyGithub" )

    def testDelete( self ):
        label = self.repo.get_label( "LabelEditedByPyGithub" )
        label.delete()
