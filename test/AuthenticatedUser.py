import Framework

class AuthenticatedUser( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.u = self.g.get_user()

    def testAttributes( self ):
        self.assertEqual( self.u.avatar_url, "https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" )
        self.assertEqual( self.u.bio, "" )
        self.assertEqual( self.u.blog, "http://vincent-jacques.net" )
        self.assertEqual( self.u.collaborators, 0 )
        self.assertEqual( self.u.company, "Criteo" )
        self.assertEqual( self.u.created_at, "2010-07-09T06:10:06Z" )
        self.assertEqual( self.u.disk_usage, 16692 )
        self.assertEqual( self.u.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.u.followers, 13 )
        self.assertEqual( self.u.following, 24 )
        self.assertEqual( self.u.gravatar_id, "b68de5ae38616c296fa345d2b9df2225" )
        self.assertEqual( self.u.hireable, False )
        self.assertEqual( self.u.html_url, "https://github.com/jacquev6" )
        self.assertEqual( self.u.id, 327146 )
        self.assertEqual( self.u.location, "Paris, France" )
        self.assertEqual( self.u.login, "jacquev6" )
        self.assertEqual( self.u.name, "Vincent Jacques" )
        self.assertEqual( self.u.owned_private_repos, 5 )
        self.assertEqual( self.u.plan.name, "micro" )
        self.assertEqual( self.u.plan.collaborators, 1 )
        self.assertEqual( self.u.plan.space, 614400 )
        self.assertEqual( self.u.plan.private_repos, 5 )
        self.assertEqual( self.u.private_gists, 5 )
        self.assertEqual( self.u.public_gists, 1 )
        self.assertEqual( self.u.public_repos, 10 )
        self.assertEqual( self.u.total_private_repos, 5 )
        self.assertEqual( self.u.type, "User" )
        self.assertEqual( self.u.url, "https://api.github.com/users/jacquev6" )

    def testEditWithoutArguments( self ):
        self.u.edit()

    def testEditWithAllArguments( self ):
        oldName = self.u.name
        newName = "Name edited by PyGithub"

        oldEmail = self.u.email
        newEmail = "Email edited by PyGithub"

        oldBlog = self.u.blog
        newBlog = "Blog edited by PyGithub"

        oldCompany = self.u.company
        newCompany = "Company edited by PyGithub"

        oldLocation = self.u.location
        newLocation = "Location edited by PyGithub"

        oldHireable = self.u.hireable
        newHireable = not oldHireable

        oldBio = self.u.bio
        newBio = "Bio edited by PyGithub"

        self.u.edit( newName, newEmail, newBlog, newCompany, newLocation, newHireable, newBio )
        self.assertEqual( self.u.name, newName )
        self.assertEqual( self.u.email, newEmail )
        self.assertEqual( self.u.blog, newBlog )
        self.assertEqual( self.u.company, newCompany )
        self.assertEqual( self.u.location, newLocation )
        self.assertEqual( self.u.hireable, newHireable )
        self.assertEqual( self.u.bio, newBio )

        self.u.edit( oldName, oldEmail, oldBlog, oldCompany, oldLocation, oldHireable, oldBio )
        self.assertEqual( self.u.name, oldName )
        self.assertEqual( self.u.email, oldEmail )
        self.assertEqual( self.u.blog, oldBlog )
        self.assertEqual( self.u.company, oldCompany )
        self.assertEqual( self.u.location, oldLocation )
        self.assertEqual( self.u.hireable, oldHireable )
        self.assertEqual( self.u.bio, oldBio )
