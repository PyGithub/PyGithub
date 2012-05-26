import Framework

class GitBlob( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.blob = self.g.get_user().get_repo( "PyGithub" ).get_git_blob( "53bce9fa919b4544e67275089b3ec5b44be20667" )

    def testAttributes( self ):
        self.assertTrue( self.blob.content.startswith( "IyEvdXNyL2Jpbi9lbnYgcHl0aG9uCgpmcm9tIGRpc3R1dGlscy5jb3JlIGlt\ncG9ydCBzZXR1cAppbXBvcnQgdGV4dHdyYXAKCnNldHVwKAogICAgbmFtZSA9\n" ) )
        self.assertTrue( self.blob.content.endswith( "Z3JhbW1pbmcgTGFuZ3VhZ2UgOjogUHl0aG9uIiwKICAgICAgICAiVG9waWMg\nOjogU29mdHdhcmUgRGV2ZWxvcG1lbnQiLAogICAgXSwKKQo=\n" ) )
        self.assertEqual( len( self.blob.content ), 1757 )
        self.assertEqual( self.blob.encoding, "base64" )
        self.assertEqual( self.blob.size, 1295 )
        self.assertEqual( self.blob.sha, "53bce9fa919b4544e67275089b3ec5b44be20667" )
        self.assertEqual( self.blob.url, "https://api.github.com/repos/jacquev6/PyGithub/git/blobs/53bce9fa919b4544e67275089b3ec5b44be20667" )
