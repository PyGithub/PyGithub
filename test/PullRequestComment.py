import Framework

class PullRequestComment( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.comment = self.g.get_user().get_repo( "PyGithub" ).get_pull( 31 ).get_comment( 886298 )

    def testAttributes( self ):
        self.assertEqual( self.comment.body, "Comment created by PyGithub" )
        self.assertEqual( self.comment.commit_id, "8a4f306d4b223682dd19410d4a9150636ebe4206" )
        self.assertEqual( self.comment.created_at, "2012-05-27T09:40:12Z" )
        self.assertEqual( self.comment.id, 886298 )
        self.assertEqual( self.comment.original_commit_id, "8a4f306d4b223682dd19410d4a9150636ebe4206" )
        self.assertEqual( self.comment.original_position, 5 )
        self.assertEqual( self.comment.path, "src/github/Issue.py" )
        self.assertEqual( self.comment.position, 5 )
        self.assertEqual( self.comment.updated_at, "2012-05-27T09:40:12Z" )
        self.assertEqual( self.comment.url, "https://api.github.com/repos/jacquev6/PyGithub/pulls/comments/886298" )
        self.assertEqual( self.comment.user.login, "jacquev6" )

    def testEdit( self ):
        self.comment.edit( "Comment edited by PyGithub" )
        self.assertEqual( self.comment.body, "Comment edited by PyGithub" )

    def testDelete( self ): # Test PullRequest.get_comments before
        self.comment.delete()
