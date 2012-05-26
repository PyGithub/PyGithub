import Framework

class Repository( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.user = self.g.get_user()
        self.user.login # To force completion of user in setUp

    def testAttributes( self ):
        repo = self.user.get_repo( "PyGithub" )
        self.assertEqual( repo.clone_url, "https://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( repo.created_at, "2012-02-25T12:53:47Z" )
        self.assertEqual( repo.description, "Python library implementing the full Github API v3" )
        self.assertEqual( repo.fork, False )
        self.assertEqual( repo.forks, 2 )
        self.assertEqual( repo.full_name, "jacquev6/PyGithub" )
        self.assertEqual( repo.git_url, "git://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( repo.has_downloads, True )
        self.assertEqual( repo.has_issues, True )
        self.assertEqual( repo.has_wiki, False )
        self.assertEqual( repo.homepage, "http://vincent-jacques.net/PyGithub" )
        self.assertEqual( repo.html_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( repo.id, 3544490 )
        self.assertEqual( repo.language, "Python" )
        self.assertEqual( repo.master_branch, None )
        self.assertEqual( repo.mirror_url, None )
        self.assertEqual( repo.name, "PyGithub" )
        self.assertEqual( repo.open_issues, 16 )
        self.assertEqual( repo.organization, None )
        self.assertEqual( repo.owner.login, "jacquev6" )
        self.assertEqual( repo.parent, None )
        self.assertEqual( repo.permissions.admin, True )
        self.assertEqual( repo.permissions.pull, True )
        self.assertEqual( repo.permissions.push, True )
        self.assertEqual( repo.private, False )
        self.assertEqual( repo.pushed_at, "2012-05-25T17:19:45Z" )
        self.assertEqual( repo.size, 184 )
        self.assertEqual( repo.source, None )
        self.assertEqual( repo.ssh_url, "git@github.com:jacquev6/PyGithub.git" )
        self.assertEqual( repo.svn_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( repo.updated_at, "2012-05-25T17:19:46Z" )
        self.assertEqual( repo.url, "https://api.github.com/repos/jacquev6/PyGithub" )
        self.assertEqual( repo.watchers, 13 )

    def testCreate( self ):
        repo = self.user.create_repo( "TestPyGithub" )
        self.assertEqual( repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub" )

    def testCreateWithAllArguments( self ):
        repo = self.user.create_repo( "TestPyGithub", "Repo created by PyGithub", "http://foobar.com", private = False, has_issues = False, has_wiki = False, has_downloads = False )
        self.assertEqual( repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub" )

    def testEditWithoutArguments( self ):
        repo = self.user.get_repo( "TestPyGithub" )
        self.assertEqual( repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub" )
        repo.edit( "TestPyGithub" ) ### @todo Make name an optional parameter

    def testEditWithAllArguments( self ):
        repo = self.user.get_repo( "TestPyGithub" )
        self.assertEqual( repo.url, "https://api.github.com/repos/jacquev6/TestPyGithub" )
        repo.edit( "TestPyGithub", "Repository created by PyGithub", "http://vincent-jacques.net/PyGithub", public = True, has_issues = False, has_wiki = False, has_downloads = False )
        self.assertEqual( repo.description, "Repository created by PyGithub" )

    def testContributors( self ):
        repo = self.user.get_repo( "PyGithub" )
        contributor = repo.get_contributors()[ 0 ]
        self.assertEqual( contributor.login, "jacquev6" )
        self.assertEqual( contributor.contributions, 355 )
