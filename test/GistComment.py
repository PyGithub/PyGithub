import Framework

class GistComment( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.comment = self.g.get_gist( "2729810" ).get_comment( 323629 )

    def testAttributes( self ): ### @todo Move
        self.assertEquals( self.comment.body, "Comment created by PyGithub" )
        self.assertEquals( self.comment.created_at, "2012-05-19T07:07:57Z" )
        self.assertEquals( self.comment.id, 323629 )
        self.assertEquals( self.comment.updated_at, "2012-05-19T07:07:57Z" )
        self.assertEquals( self.comment.url, "https://api.github.com/gists/comments/323629" )
        self.assertEquals( self.comment.user.login, "jacquev6" )

    def testEdit( self ): ### @todo Move
        self.comment.edit( "Comment edited by PyGithub" )
        self.assertEquals( self.comment.body, "Comment edited by PyGithub" )
        self.assertEquals( self.comment.updated_at, "2012-05-19T07:12:32Z" )

    def testDelete( self ):
        self.comment.delete()
