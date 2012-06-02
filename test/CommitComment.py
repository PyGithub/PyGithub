import Framework

import datetime

class CommitComment( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.comment = self.g.get_user().get_repo( "PyGithub" ).get_comment( 1361949 )

    def testAttributes( self ):
        self.assertEqual( self.comment.body, "Comment created by PyGithub" )
        self.assertEqual( self.comment.commit_id, "6945921c529be14c3a8f566dd1e483674516d46d" )
        self.assertEqual( self.comment.created_at, datetime.datetime( 2012, 5, 22, 18, 40, 18 ) )
        self.assertEqual( self.comment.html_url, "https://github.com/jacquev6/PyGithub/commit/6945921c529be14c3a8f566dd1e483674516d46d#commitcomment-1361949" )
        self.assertEqual( self.comment.id, 1361949 )
        self.assertEqual( self.comment.line, None )
        self.assertEqual( self.comment.path, None )
        self.assertEqual( self.comment.position, None )
        self.assertEqual( self.comment.updated_at, datetime.datetime( 2012, 5, 22, 18, 40, 18 ) )
        self.assertEqual( self.comment.url, "https://api.github.com/repos/jacquev6/PyGithub/comments/1361949" )
        self.assertEqual( self.comment.user.login, "jacquev6" )

    def testEdit( self ):
        self.comment.edit( "Comment edited by PyGithub" )

    def testDelete( self ):
        self.comment.delete()
