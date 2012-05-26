import Framework

class GitRef( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.ref = self.g.get_user().get_repo( "PyGithub" ).get_git_ref( "refs/heads/BranchCreatedByPyGithub" )

    def testAttributes( self ):
        self.assertEqual( self.ref.object.sha, "1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.ref.object.type, "commit" )
        self.assertEqual( self.ref.object.url, "https://api.github.com/repos/jacquev6/PyGithub/git/commits/1292bf0e22c796e91cc3d6e24b544aece8c21f2a" )
        self.assertEqual( self.ref.ref, "refs/heads/BranchCreatedByPyGithub" )
        self.assertEqual( self.ref.url, "https://api.github.com/repos/jacquev6/PyGithub/git/refs/heads/BranchCreatedByPyGithub" )

    def testEdit( self ):
        self.ref.edit( "04cde900a0775b51f762735637bd30de392a2793" )

    def testEditWithForce( self ):
        self.ref.edit( "4303c5b90e2216d927155e9609436ccb8984c495", force = True )

    def testDelete( self ):
        self.ref.delete()
