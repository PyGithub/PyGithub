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
        self.assertEqual( repo.git_url, "git://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( repo.has_downloads, True )
        self.assertEqual( repo.has_issues, True )
        self.assertEqual( repo.has_wiki, False )
        self.assertEqual( repo.homepage, "http://vincent-jacques.net/PyGithub" )
        self.assertEqual( repo.html_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( repo.id, 3544490 )
        self.assertEqual( repo.language, "Python" )
        self.assertEqual( repo.master_branch, None ) ### @todo Why does this trigger a new request to github ? Because the object does not know that it is already completed, and it tries to de-None-ify master_branch
        self.assertEqual( repo.mirror_url, None )
        self.assertEqual( repo.name, "PyGithub" )
        self.assertEqual( repo.open_issues, 15 )
        self.assertEqual( repo.organization, None )
        self.assertEqual( repo.owner.login, "jacquev6" )
        self.assertEqual( repo.parent, None )
        self.assertEqual( repo.permissions, { "admin": True, "pull": True, "push": True } ) ### @todo Create a Permission class
        self.assertEqual( repo.private, False )
        self.assertEqual( repo.pushed_at, "2012-05-08T19:27:43Z" )
        self.assertEqual( repo.size, 212 )
        self.assertEqual( repo.source, None )
        self.assertEqual( repo.ssh_url, "git@github.com:jacquev6/PyGithub.git" )
        self.assertEqual( repo.svn_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( repo.updated_at, "2012-05-08T19:27:43Z" )
        self.assertEqual( repo.url, "https://api.github.com/repos/jacquev6/PyGithub" )
        self.assertEqual( repo.watchers, 13 )
