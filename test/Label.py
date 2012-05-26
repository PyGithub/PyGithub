import Framework

class Label( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.label = self.g.get_user().get_repo( "PyGithub" ).get_label( "Bug" )

    def testAttributes( self ):
        self.assertEqual( self.label.color, "e10c02" )
        self.assertEqual( self.label.name, "Bug" )
        self.assertEqual( self.label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/Bug" )

    def testEdit( self ):
        self.label.edit( "LabelEditedByPyGithub", "0000ff" )
        self.assertEqual( self.label.color, "0000ff" )
        self.assertEqual( self.label.name, "LabelEditedByPyGithub" )
        self.assertEqual( self.label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/LabelEditedByPyGithub" )

    def testDelete( self ):
        self.label.delete()
