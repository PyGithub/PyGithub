import Framework

class Organization( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.org = self.g.get_organization( "BeaverSoftware" )

    def testAttributes( self ):
        self.assertEqual( self.org.avatar_url, "https://secure.gravatar.com/avatar/d563e337cac2fdc644e2aaaad1e23266?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-orgs.png" )
        self.assertEqual( self.org.billing_email, "BeaverSoftware@vincent-jacques.net" )
        self.assertEqual( self.org.blog, None )
        self.assertEqual( self.org.collaborators, 0 )
        self.assertEqual( self.org.company, None )
        self.assertEqual( self.org.created_at, "2012-02-09T19:20:12Z" )
        self.assertEqual( self.org.disk_usage, 112 )
        self.assertEqual( self.org.email, None )
        self.assertEqual( self.org.followers, 0 )
        self.assertEqual( self.org.following, 0 )
        self.assertEqual( self.org.gravatar_id, None )
        self.assertEqual( self.org.html_url, "https://github.com/BeaverSoftware" )
        self.assertEqual( self.org.id, 1424031 )
        self.assertEqual( self.org.location, "Paris, France" )
        self.assertEqual( self.org.login, "BeaverSoftware" )
        self.assertEqual( self.org.name, None )
        self.assertEqual( self.org.owned_private_repos, 0 )
        self.assertEqual( self.org.plan.name, "free" )
        self.assertEqual( self.org.plan.private_repos, 0 )
        self.assertEqual( self.org.plan.space, 307200 )
        self.assertEqual( self.org.private_gists, 0 )
        self.assertEqual( self.org.public_gists, 0 )
        self.assertEqual( self.org.public_repos, 2 )
        self.assertEqual( self.org.total_private_repos, 0 )
        self.assertEqual( self.org.type, "Organization" )
        self.assertEqual( self.org.url, "https://api.github.com/orgs/BeaverSoftware" )

    def testEditWithoutArguments( self ):
        self.org.edit()

    def testEditWithAllArguments( self ):
        self.org.edit( "BeaverSoftware2@vincent-jacques.net", "http://vincent-jacques.net", "Company edited by PyGithub", "BeaverSoftware2@vincent-jacques.net", "Location edited by PyGithub", "Name edited by PyGithub" )
        self.assertEqual( self.org.billing_email, "BeaverSoftware2@vincent-jacques.net" )
        self.assertEqual( self.org.blog, "http://vincent-jacques.net" )
        self.assertEqual( self.org.company, "Company edited by PyGithub" )
        self.assertEqual( self.org.email, "BeaverSoftware2@vincent-jacques.net" )
        self.assertEqual( self.org.location, "Location edited by PyGithub" )
        self.assertEqual( self.org.name, "Name edited by PyGithub" )

    def testCreateTeam( self ):
        team = self.org.create_team( "Team created by PyGithub" )
        self.assertEqual( team.id, 189850 )

    def testCreateTeamWithAllArguments( self ):
        team = self.org.create_team( "Team also created by PyGithub", [ "BeaverSoftware/FatherBeaver" ], "push" )
        self.assertEqual( team.id, 189852 )

    def testPublicMembers( self ):
        lyloa = self.g.get_user( "Lyloa" )
        self.assertFalse( self.org.has_in_public_members( lyloa ) )
        self.org.add_to_public_members( lyloa )
        self.assertTrue( self.org.has_in_public_members( lyloa ) )
        self.org.remove_from_public_members( lyloa )
        self.assertFalse( self.org.has_in_public_members( lyloa ) )

    def testGetPublicMembers( self ):
        self.assertListKeyEqual( self.org.get_public_members(), lambda u: u.login, [ "jacquev6" ] )

    def testGetMembers( self ):
        self.assertListKeyEqual( self.org.get_members(), lambda u: u.login, [ "cjuniet", "jacquev6", "Lyloa" ] )

    def testMembers( self ):
        lyloa = self.g.get_user( "Lyloa" )
        self.assertTrue( self.org.has_in_members( lyloa ) )
        self.org.remove_from_members( lyloa )
        self.assertFalse( self.org.has_in_members( lyloa ) )
