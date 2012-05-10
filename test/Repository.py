import Framework

class Repository( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.r = self.g.get_user().get_repo( "PyGithub" )

    def testAttributes( self ):
        self.assertEqual( self.r.clone_url, "https://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( self.r.created_at, "2012-02-25T12:53:47Z" )
        self.assertEqual( self.r.description, "Python library implementing the full Github API v3" )
        self.assertEqual( self.r.fork, False )
        self.assertEqual( self.r.forks, 2 )
        self.assertEqual( self.r.git_url, "git://github.com/jacquev6/PyGithub.git" )
        self.assertEqual( self.r.has_downloads, True )
        self.assertEqual( self.r.has_issues, True )
        self.assertEqual( self.r.has_wiki, False )
        self.assertEqual( self.r.homepage, "http://vincent-jacques.net/PyGithub" )
        self.assertEqual( self.r.html_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( self.r.id, 3544490 )
        self.assertEqual( self.r.language, "Python" )
        self.assertEqual( self.r.master_branch, None ) ### @todo Why does this trigger a new request to github ? Because the object does not know that it is already completed, and it tries to de-None-ify master_branch
        self.assertEqual( self.r.mirror_url, None )
        self.assertEqual( self.r.name, "PyGithub" )
        self.assertEqual( self.r.open_issues, 15 )
        self.assertEqual( self.r.organization, None )
        self.assertEqual( self.r.owner.login, "jacquev6" )
        self.assertEqual( self.r.parent, None )
        self.assertEqual( self.r.permissions, { "admin": True, "pull": True, "push": True } ) ### @todo Create a Permission class
        self.assertEqual( self.r.private, False )
        self.assertEqual( self.r.pushed_at, "2012-05-08T19:27:43Z" )
        self.assertEqual( self.r.size, 212 )
        self.assertEqual( self.r.source, None )
        self.assertEqual( self.r.ssh_url, "git@github.com:jacquev6/PyGithub.git" )
        self.assertEqual( self.r.svn_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( self.r.updated_at, "2012-05-08T19:27:43Z" )
        self.assertEqual( self.r.url, "https://api.github.com/repos/jacquev6/PyGithub" )
        self.assertEqual( self.r.watchers, 13 )
