import Framework

class AuthenticatedUser( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.user = self.g.get_user()

    def testAttributes( self ):
        self.assertEqual( self.user.avatar_url, "https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" )
        self.assertEqual( self.user.bio, "" )
        self.assertEqual( self.user.blog, "http://vincent-jacques.net" )
        self.assertEqual( self.user.collaborators, 0 )
        self.assertEqual( self.user.company, "Criteo" )
        self.assertEqual( self.user.created_at, "2010-07-09T06:10:06Z" )
        self.assertEqual( self.user.disk_usage, 16692 )
        self.assertEqual( self.user.email, "vincent@vincent-jacques.net" )
        self.assertEqual( self.user.followers, 13 )
        self.assertEqual( self.user.following, 24 )
        self.assertEqual( self.user.gravatar_id, "b68de5ae38616c296fa345d2b9df2225" )
        self.assertEqual( self.user.hireable, False )
        self.assertEqual( self.user.html_url, "https://github.com/jacquev6" )
        self.assertEqual( self.user.id, 327146 )
        self.assertEqual( self.user.location, "Paris, France" )
        self.assertEqual( self.user.login, "jacquev6" )
        self.assertEqual( self.user.name, "Vincent Jacques" )
        self.assertEqual( self.user.owned_private_repos, 5 )
        self.assertEqual( self.user.plan.name, "micro" )
        self.assertEqual( self.user.plan.collaborators, 1 )
        self.assertEqual( self.user.plan.space, 614400 )
        self.assertEqual( self.user.plan.private_repos, 5 )
        self.assertEqual( self.user.private_gists, 5 )
        self.assertEqual( self.user.public_gists, 1 )
        self.assertEqual( self.user.public_repos, 10 )
        self.assertEqual( self.user.total_private_repos, 5 )
        self.assertEqual( self.user.type, "User" )
        self.assertEqual( self.user.url, "https://api.github.com/users/jacquev6" )

    def testEditWithoutArguments( self ):
        self.user.edit()

    def testEditWithAllArguments( self ):
        oldName = self.user.name
        newName = "Name edited by PyGithub"

        oldEmail = self.user.email
        newEmail = "Email edited by PyGithub"

        oldBlog = self.user.blog
        newBlog = "Blog edited by PyGithub"

        oldCompany = self.user.company
        newCompany = "Company edited by PyGithub"

        oldLocation = self.user.location
        newLocation = "Location edited by PyGithub"

        oldHireable = self.user.hireable
        newHireable = not oldHireable

        oldBio = self.user.bio
        newBio = "Bio edited by PyGithub"

        self.user.edit( newName, newEmail, newBlog, newCompany, newLocation, newHireable, newBio )
        self.assertEqual( self.user.name, newName )
        self.assertEqual( self.user.email, newEmail )
        self.assertEqual( self.user.blog, newBlog )
        self.assertEqual( self.user.company, newCompany )
        self.assertEqual( self.user.location, newLocation )
        self.assertEqual( self.user.hireable, newHireable )
        self.assertEqual( self.user.bio, newBio )

        self.user.edit( oldName, oldEmail, oldBlog, oldCompany, oldLocation, oldHireable, oldBio )
        self.assertEqual( self.user.name, oldName )
        self.assertEqual( self.user.email, oldEmail )
        self.assertEqual( self.user.blog, oldBlog )
        self.assertEqual( self.user.company, oldCompany )
        self.assertEqual( self.user.location, oldLocation )
        self.assertEqual( self.user.hireable, oldHireable )
        self.assertEqual( self.user.bio, oldBio )

    def testEmails( self ):
        self.assertEqual( self.user.get_emails(), [ "vincent@vincent-jacques.net", "github.com@vincent-jacques.net" ] )
        self.user.add_to_emails( "1@foobar.com", "2@foobar.com" )
        self.assertEqual( self.user.get_emails(), [ "vincent@vincent-jacques.net", "1@foobar.com", "2@foobar.com", "github.com@vincent-jacques.net" ] )
        self.user.remove_from_emails( "1@foobar.com", "2@foobar.com" )
        self.assertEqual( self.user.get_emails(), [ "vincent@vincent-jacques.net", "github.com@vincent-jacques.net" ] )

    def testFollowing( self ):
        nvie = self.g.get_user( "nvie" )
        self.assertEqual( self.user.get_following()[ 0 ].login, "schacon" )
        self.assertEqual( self.user.has_in_following( nvie ), True )
        self.user.remove_from_following( nvie )
        self.assertEqual( self.user.has_in_following( nvie ), False )
        self.user.add_to_following( nvie )
        self.assertEqual( self.user.has_in_following( nvie ), True )
        self.assertEqual( self.user.get_followers()[ 0 ].login, "jnorthrup" )

    def testWatching( self ):
        gitflow = self.g.get_user( "nvie" ).get_repo( "gitflow" )
        self.assertEqual( self.user.get_watched()[ 0 ].name, "git" )
        self.assertEqual( self.user.has_in_watched( gitflow ), True )
        self.user.remove_from_watched( gitflow )
        self.assertEqual( self.user.has_in_watched( gitflow ), False )
        self.user.add_to_watched( gitflow )
        self.assertEqual( self.user.has_in_watched( gitflow ), True )
