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
