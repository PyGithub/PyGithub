import Framework

class Download( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.download = self.g.get_user().get_repo( "PyGithub" ).get_download( 242550 )

    def testAttributes( self ):
        self.assertEqual( self.download.accesskeyid, None )
        self.assertEqual( self.download.acl, None )
        self.assertEqual( self.download.bucket, None )
        self.assertEqual( self.download.content_type, "text/plain" )
        self.assertEqual( self.download.created_at, "2012-05-22T18:58:32Z" )
        self.assertEqual( self.download.description, None )
        self.assertEqual( self.download.download_count, 0 )
        self.assertEqual( self.download.expirationdate, None )
        self.assertEqual( self.download.html_url, "https://github.com/downloads/jacquev6/PyGithub/Foobar.txt" )
        self.assertEqual( self.download.id, 242550 )
        self.assertEqual( self.download.mime_type, None )
        self.assertEqual( self.download.name, "Foobar.txt" )
        self.assertEqual( self.download.path, None )
        self.assertEqual( self.download.policy, None )
        self.assertEqual( self.download.prefix, None )
        self.assertEqual( self.download.redirect, None )
        self.assertEqual( self.download.s3_url, None )
        self.assertEqual( self.download.signature, None )
        self.assertEqual( self.download.size, 1024 )
        self.assertEqual( self.download.url, "https://api.github.com/repos/jacquev6/PyGithub/downloads/242550" )

    def testDelete( self ):
        self.download.delete()
