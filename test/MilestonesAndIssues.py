import Framework

class Milestones( Framework.TestCaseWithRepo ):
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

class Issues( Framework.TestCaseWithRepo ):
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
