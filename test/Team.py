import Framework

class Team( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.org = self.g.get_organization( "BeaverSoftware" )
        self.team = self.org.get_team( 189850 )

    def testAttributes( self ):
        self.assertEqual( self.team.id, 189850 )
        self.assertEqual( self.team.members_count, 0 )
        self.assertEqual( self.team.name, "Team created by PyGithub" )
        self.assertEqual( self.team.permission, "pull" )
        self.assertEqual( self.team.repos_count, 0 )
        self.assertEqual( self.team.url, "https://api.github.com/teams/189850" )

    def testMembers( self ):
        user = self.g.get_user( "jacquev6" )
        self.assertListKeyEqual( self.team.get_members(), lambda u: u.login, [] )
        self.assertFalse( self.team.has_in_members( user ) )
        self.team.add_to_members( user )
        self.assertListKeyEqual( self.team.get_members(), lambda u: u.login, [ "jacquev6" ] )
        self.assertTrue( self.team.has_in_members( user ) )
        self.team.remove_from_members( user )
        self.assertListKeyEqual( self.team.get_members(), lambda u: u.login, [] )
        self.assertFalse( self.team.has_in_members( user ) )

    def testRepos( self ):
        repo = self.org.get_repo( "FatherBeaver" )
        self.assertListKeyEqual( self.team.get_repos(), lambda r: r.name, [] )
        self.assertFalse( self.team.has_in_repos( repo ) )
        self.team.add_to_repos( repo )
        self.assertListKeyEqual( self.team.get_repos(), lambda r: r.name, [ "FatherBeaver" ] )
        self.assertTrue( self.team.has_in_repos( repo ) )
        self.team.remove_from_repos( repo )
        self.assertListKeyEqual( self.team.get_repos(), lambda r: r.name, [] )
        self.assertFalse( self.team.has_in_repos( repo ) )

    def testEditWithoutArguments( self ):
        self.team.edit( "Name edited by PyGithub" )
        self.assertEqual( self.team.name, "Name edited by PyGithub" )

    def testEditWithAllArguments( self ):
        self.team.edit( "Name edited twice by PyGithub", "admin" )
        self.assertEqual( self.team.name, "Name edited twice by PyGithub" )
        self.assertEqual( self.team.permission, "admin" )

    def testDelete( self ):
        self.team.delete()
