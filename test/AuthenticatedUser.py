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
        self.user.edit( "Name edited by PyGithub", "Email edited by PyGithub", "Blog edited by PyGithub", "Company edited by PyGithub", "Location edited by PyGithub", True, "Bio edited by PyGithub" )
        self.assertEqual( self.user.name, "Name edited by PyGithub" )
        self.assertEqual( self.user.email, "Email edited by PyGithub" )
        self.assertEqual( self.user.blog, "Blog edited by PyGithub" )
        self.assertEqual( self.user.company, "Company edited by PyGithub" )
        self.assertEqual( self.user.location, "Location edited by PyGithub" )
        self.assertEqual( self.user.hireable, True )
        self.assertEqual( self.user.bio, "Bio edited by PyGithub" )

    def testEmails( self ):
        self.assertEqual( self.user.get_emails(), [ "vincent@vincent-jacques.net", "github.com@vincent-jacques.net" ] )
        self.user.add_to_emails( "1@foobar.com", "2@foobar.com" )
        self.assertEqual( self.user.get_emails(), [ "vincent@vincent-jacques.net", "1@foobar.com", "2@foobar.com", "github.com@vincent-jacques.net" ] )
        self.user.remove_from_emails( "1@foobar.com", "2@foobar.com" )
        self.assertEqual( self.user.get_emails(), [ "vincent@vincent-jacques.net", "github.com@vincent-jacques.net" ] )

    def testFollowing( self ):
        nvie = self.g.get_user( "nvie" )
        self.assertListKeyEqual( self.user.get_following(), lambda u: u.login, [ "schacon", "jamis", "chad", "unclebob", "dabrahams", "jnorthrup", "brugidou", "regisb", "walidk", "tanzilli", "fjardon", "r3c", "sdanzan", "vineus", "cjuniet", "gturri", "ant9000", "asquini", "claudyus", "jardon-u", "s-bernard", "kamaradclimber", "Lyloa", "nvie" ] )
        self.assertEqual( self.user.has_in_following( nvie ), True )
        self.user.remove_from_following( nvie )
        self.assertEqual( self.user.has_in_following( nvie ), False )
        self.user.add_to_following( nvie )
        self.assertEqual( self.user.has_in_following( nvie ), True )
        self.assertListKeyEqual( self.user.get_followers(), lambda u: u.login, [ "jnorthrup", "brugidou", "regisb", "walidk", "afzalkhan", "sdanzan", "vineus", "gturri", "fjardon", "cjuniet", "jardon-u", "kamaradclimber", "L42y" ] )

    def testWatching( self ):
        gitflow = self.g.get_user( "nvie" ).get_repo( "gitflow" )
        self.assertListKeyEqual( self.user.get_watched(), lambda r: r.name, [ "git", "boost.php", "capistrano", "boost.perl", "git-subtree", "git-hg", "homebrew", "celtic_knot", "twisted-intro", "markup", "hub", "gitflow", "murder", "boto", "agit", "d3", "pygit2", "git-pulls", "django_mathlatex", "scrumblr", "developer.github.com", "python-github3", "PlantUML", "bootstrap", "drawnby", "django-socketio", "django-realtime", "playground", "BozoCrack", "FatherBeaver", "PyGithub", "django", "django", "TestPyGithub" ] )
        self.assertEqual( self.user.has_in_watched( gitflow ), True )
        self.user.remove_from_watched( gitflow )
        self.assertEqual( self.user.has_in_watched( gitflow ), False )
        self.user.add_to_watched( gitflow )
        self.assertEqual( self.user.has_in_watched( gitflow ), True )

    def testGetAuthorizations( self ):
        self.assertListKeyEqual( self.user.get_authorizations(), lambda a: a.id, [ 372294 ] )

    def testCreateRepository( self ):
        repo = self.user.create_repo( "TestPyGithub" )
        self.assertEqual( repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub" )

    def testCreateRepositoryWithAllArguments( self ):
        repo = self.user.create_repo( "TestPyGithub", "Repo created by PyGithub", "http://foobar.com", private = False, has_issues = False, has_wiki = False, has_downloads = False )
        self.assertEqual( repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub" )

    def testCreateAuthorizationWithoutArguments( self ):
        authorization = self.user.create_authorization()
        self.assertEqual( authorization.id, 372259 )

    def testCreateAuthorizationWithAllArguments( self ):
        authorization = self.user.create_authorization( [ "repo" ], "Note created by PyGithub", "http://vincent-jacques.net/PyGithub" )
        self.assertEqual( authorization.id, 372294 )

    def testCreateGist( self ):
        gist = self.user.create_gist( True, { "foobar.txt": { "content": "File created by PyGithub" } }, "Gist created by PyGithub" )
        self.assertEqual( gist.description, "Gist created by PyGithub" )
        self.assertEqual( gist.files, {u'foobar.txt': {u'raw_url': u'https://gist.github.com/raw/2729810/73a1c7f17aa0ad5d7cbb5a8ca033ce47d3d23197/foobar.txt', u'language': u'Text', u'filename': u'foobar.txt', u'content': u'File created by PyGithub', u'type': u'text/plain', u'size': 24}} ) ### @todo

    def testCreateGistWithoutDescription( self ):
        gist = self.user.create_gist( True, { "foobar.txt": { "content": "File created by PyGithub" } } )
        self.assertEqual( gist.description, None )
        self.assertEqual( gist.files, {u'foobar.txt': {u'raw_url': u'https://gist.github.com/raw/2793179/73a1c7f17aa0ad5d7cbb5a8ca033ce47d3d23197/foobar.txt', u'language': u'Text', u'filename': u'foobar.txt', u'content': u'File created by PyGithub', u'type': u'text/plain', u'size': 24}} ) ### @todo

    def testCreateKey( self ):
        key = self.user.create_key( "Key added through PyGithub", "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA2Mm0RjTNAYFfSCtUpO54usdseroUSIYg5KX4JoseTpqyiB/hqewjYLAdUq/tNIQzrkoEJWSyZrQt0ma7/YCyMYuNGd3DU6q6ZAyBeY3E9RyCiKjO3aTL2VKQGFvBVVmGdxGVSCITRphAcsKc/PF35/fg9XP9S0anMXcEFtdfMHz41SSw+XtE+Vc+6cX9FuI5qUfLGbkv8L1v3g4uw9VXlzq4GfTA+1S7D6mcoGHopAIXFlVr+2RfDKdSURMcB22z41fljO1MW4+zUS/4FyUTpL991es5fcwKXYoiE+x06VJeJJ1Krwx+DZj45uweV6cHXt2JwJEI9fWB6WyBlDejWw== vincent@IDEE" )
        self.assertEqual( key.id, 2626650 )

    def testGetEvents( self ):
        self.assertListKeyBegin( self.user.get_events(), lambda e: e.type, [ "PushEvent", "IssuesEvent", "IssueCommentEvent", "PushEvent" ] )

    def testGetOrganizationEvents( self ):
        self.assertListKeyBegin( self.user.get_organization_events( self.g.get_organization( "BeaverSoftware" ) ), lambda e: e.type, [ "CreateEvent", "CreateEvent", "PushEvent", "PushEvent" ] )

    def testGetGists( self ):
        self.assertListKeyEqual( self.user.get_gists(), lambda g: g.id, [ "2793505", "2793179", "11cb445f8197e17d303d", "1942384", "dcb7de17e8a52b74541d" ] )

    def testGetStarredGists( self ):
        self.assertListKeyEqual( self.user.get_starred_gists(), lambda g: g.id, [ "1942384", "dcb7de17e8a52b74541d" ] )

    def testGetIssues( self ):
        self.assertListKeyEqual( self.user.get_issues(), lambda i: i.id, [ 4639931, 4452000, 4356743, 3716033, 3715946, 3643837, 3628022, 3624595, 3624570, 3624561, 3624556, 3619973, 3527266, 3527245, 3527231 ] )

    def testGetKeys( self ):
        self.assertListKeyEqual( self.user.get_keys(), lambda k: k.title, [ "vincent@home", "vincent@gandi", "vincent@aws", "vincent@macbook" ] )

    def testGetOrgs( self ):
        self.assertListKeyEqual( self.user.get_orgs(), lambda o: o.login, [ "BeaverSoftware" ] )

    def testGetRepos( self ):
        self.assertListKeyEqual( self.user.get_repos(), lambda r: r.name,  [ "TestPyGithub", "django", "PyGithub", "developer.github.com", "acme-public-website", "C4Planner", "Hacking", "vincent-jacques.net", "Contests", "Candidates", "Tests", "DrawTurksHead", "DrawSyntax", "QuadProgMm", "Boost.HierarchicalEnum", "ViDE" ] )

    def testCreateFork( self ):
        repo = self.user.create_fork( self.g.get_user( "nvie" ).get_repo( "gitflow" ) )
        self.assertEqual( repo.source.full_name, "nvie/gitflow" )
