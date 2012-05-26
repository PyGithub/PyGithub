import Framework

class Repository( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.repo = self.g.get_user().get_repo( "PyGithub" )

    def testAttributes( self ):
        self.assertEqual( self.repo.clone_url, "https://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( self.repo.created_at, "2012-02-25T12:53:47Z" )
        self.assertEqual( self.repo.description, "Python library implementing the full Github API v3" )
        self.assertEqual( self.repo.fork, False )
        self.assertEqual( self.repo.forks, 2 )
        self.assertEqual( self.repo.full_name, "jacquev6/PyGithub" )
        self.assertEqual( self.repo.git_url, "git://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( self.repo.has_downloads, True )
        self.assertEqual( self.repo.has_issues, True )
        self.assertEqual( self.repo.has_wiki, False )
        self.assertEqual( self.repo.homepage, "http://vincent-jacques.net/PyGithub" )
        self.assertEqual( self.repo.html_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( self.repo.id, 3544490 )
        self.assertEqual( self.repo.language, "Python" )
        self.assertEqual( self.repo.master_branch, None )
        self.assertEqual( self.repo.mirror_url, None )
        self.assertEqual( self.repo.name, "PyGithub" )
        self.assertEqual( self.repo.open_issues, 16 )
        self.assertEqual( self.repo.organization, None )
        self.assertEqual( self.repo.owner.login, "jacquev6" )
        self.assertEqual( self.repo.parent, None )
        self.assertEqual( self.repo.permissions.admin, True )
        self.assertEqual( self.repo.permissions.pull, True )
        self.assertEqual( self.repo.permissions.push, True )
        self.assertEqual( self.repo.private, False )
        self.assertEqual( self.repo.pushed_at, "2012-05-25T17:19:45Z" )
        self.assertEqual( self.repo.size, 184 )
        self.assertEqual( self.repo.source, None )
        self.assertEqual( self.repo.ssh_url, "git@github.com:jacquev6/PyGithub.git" )
        self.assertEqual( self.repo.svn_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( self.repo.updated_at, "2012-05-25T17:19:46Z" )
        self.assertEqual( self.repo.url, "https://api.github.com/repos/jacquev6/PyGithub" )
        self.assertEqual( self.repo.watchers, 13 )

    def testEditWithoutArguments( self ):
        self.repo.edit( "PyGithub" ) ### @todo Make name an optional parameter

    def testEditWithAllArguments( self ):
        self.repo.edit( "PyGithub", "Description edited by PyGithub", "http://vincent-jacques.net/PyGithub", public = True, has_issues = True, has_wiki = False, has_downloads = True )
        self.assertEqual( self.repo.description, "Description edited by PyGithub" )
        self.repo.edit( "PyGithub", "Python library implementing the full Github API v3" )
        self.assertEqual( self.repo.description, "Python library implementing the full Github API v3" )

    def testGetContributors( self ):
        self.assertListKeyEqual( self.repo.get_contributors(), lambda c: ( c.login, c.contributions ), [ ( "jacquev6", 355 ) ] )
