import Framework

class Issue( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.repo = self.g.get_user().get_repo( "PyGithub" )
        self.issue = self.repo.get_issue( 28 )

    def testAttributes( self ):
        self.assertEqual( self.issue.assignee.login, "jacquev6" )
        self.assertEqual( self.issue.body, "Body edited by PyGithub" )
        self.assertEqual( self.issue.closed_at, "2012-05-26T14:59:33Z" )
        self.assertEqual( self.issue.closed_by.login, "jacquev6" )
        self.assertEqual( self.issue.comments, 0 )
        self.assertEqual( self.issue.created_at, "2012-05-19T10:38:23Z" )
        self.assertEqual( self.issue.html_url, "https://github.com/jacquev6/PyGithub/issues/28" )
        self.assertEqual( self.issue.id, 4653757 )
        self.assertListKeyEqual( self.issue.labels, lambda l: l.name, [ "Bug", "Project management", "Question" ] )
        self.assertEqual( self.issue.milestone.title, "Version 0.4" )
        self.assertEqual( self.issue.number, 28 )
        self.assertEqual( self.issue.pull_request, {u'diff_url': None, u'patch_url': None, u'html_url': None} )
        self.assertEqual( self.issue.state, "closed" )
        self.assertEqual( self.issue.title, "Issue created by PyGithub" )
        self.assertEqual( self.issue.updated_at, "2012-05-26T14:59:33Z" )
        self.assertEqual( self.issue.url, "https://api.github.com/repos/jacquev6/PyGithub/issues/28" )
        self.assertEqual( self.issue.user.login, "jacquev6" )

    def testEditWithoutParameters( self ):
        self.issue.edit()

    def testEditWithAllParameters( self ):
        self.issue.edit( "Title edited by PyGithub", "Body edited by PyGithub", "jacquev6", "open", 2, [ "Bug" ] )
        self.assertEqual( self.issue.assignee.login, "jacquev6" )
        self.assertEqual( self.issue.body, "Body edited by PyGithub" )
        self.assertEqual( self.issue.state, "open" )
        self.assertEqual( self.issue.title, "Title edited by PyGithub" )
        self.assertListKeyEqual( self.issue.labels, lambda l: l.name, [ "Bug" ] )

    def testCreateComment( self ):
        comment = self.issue.create_comment( "Comment created by PyGithub" )
        self.assertEqual( comment.id, 5808311 )

    def testGetComments( self ):
        self.assertListKeyEqual( self.issue.get_comments(), lambda c: c.user.login, [ "jacquev6", "roskakori" ] )

    def testGetEvents( self ):
        self.assertListKeyEqual( self.issue.get_events(), lambda e: e.id, [ 15819975, 15820048 ] )

    def testGetLabels( self ):
        self.assertListKeyEqual( self.issue.get_labels(), lambda l: l.name, [ "Bug", "Project management", "Question" ] )

    def testAddAndRemoveLabels( self ):
        bug = self.repo.get_label( "Bug" )
        question = self.repo.get_label( "Question" )
        self.assertListKeyEqual( self.issue.get_labels(), lambda l: l.name, [ "Bug", "Project management", "Question" ] )
        self.issue.remove_from_labels( bug )
        self.assertListKeyEqual( self.issue.get_labels(), lambda l: l.name, [ "Project management", "Question" ] )
        self.issue.remove_from_labels( question )
        self.assertListKeyEqual( self.issue.get_labels(), lambda l: l.name, [ "Project management" ] )
        self.issue.add_to_labels( bug, question )
        self.assertListKeyEqual( self.issue.get_labels(), lambda l: l.name, [ "Bug", "Project management", "Question" ] )

    def testDeleteAndSetLabels( self ):
        bug = self.repo.get_label( "Bug" )
        question = self.repo.get_label( "Question" )
        self.assertListKeyEqual( self.issue.get_labels(), lambda l: l.name, [ "Bug", "Project management", "Question" ] )
        self.issue.delete_labels()
        self.assertListKeyEqual( self.issue.get_labels(), lambda l: l.name, [] )
        self.issue.set_labels( bug, question )
        self.assertListKeyEqual( self.issue.get_labels(), lambda l: l.name, [ "Bug", "Question" ] )
