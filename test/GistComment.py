import Framework

import datetime

class GistComment( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.comment = self.g.get_gist( "2729810" ).get_comment( 323629 )

    def testAttributes( self ):
        self.assertEquals( self.comment.body, "Comment created by PyGithub" )
        self.assertEquals( self.comment.created_at, datetime.datetime( 2012, 5, 19, 7, 7, 57 ) )
        self.assertEquals( self.comment.id, 323629 )
        self.assertEquals( self.comment.updated_at, datetime.datetime( 2012, 5, 19, 7, 7, 57 ) )
        self.assertEquals( self.comment.url, "https://api.github.com/gists/comments/323629" )
        self.assertEquals( self.comment.user.login, "jacquev6" )

    def testEdit( self ):
        self.comment.edit( "Comment edited by PyGithub" )
        self.assertEquals( self.comment.body, "Comment edited by PyGithub" )
        self.assertEquals( self.comment.updated_at, datetime.datetime( 2012, 5, 19, 7, 12, 32 ) )

    def testDelete( self ):
        self.comment.delete()
