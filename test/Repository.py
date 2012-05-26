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

    def testCreateMilestone( self ):
        milestone = self.repo.create_milestone( "Milestone created by PyGithub", state = "open", description = "Description created by PyGithub", due_on = "2012-06-15" )
        self.assertEqual( milestone.number, 5 )

    def testCreateIssue( self ):
        issue = self.repo.create_issue( "Issue created by PyGithub" )
        self.assertEqual( issue.number, 28 )

    def testCreateLabel( self ):
        label = self.repo.create_label( "Label with silly name % * + created by PyGithub", "00ff00" )
        self.assertEqual( label.color, "00ff00" )
        self.assertEqual( label.name, "Label with silly name % * + created by PyGithub" )
        self.assertEqual( label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/Label+with+silly+name+%25+%2A+%2B+created+by+PyGithub" )

    def testGetLabel( self ):
        label = self.repo.get_label( "Label with silly name % * + created by PyGithub" )
        self.assertEqual( label.color, "00ff00" )
        self.assertEqual( label.name, "Label with silly name % * + created by PyGithub" )
        self.assertEqual( label.url, "https://api.github.com/repos/jacquev6/PyGithub/labels/Label+with+silly+name+%25+%2A+%2B+created+by+PyGithub" )

    def testCreateHookWithMinimalParameters( self ):
        ### @todo Implement https://api.github.com/hooks, which is not described, but refered by http://developer.github.com/v3/repos/hooks/#create-a-hook
        hook = self.repo.create_hook( "web", { "url": "http://foobar.com" } )
        self.assertEqual( hook.active, True )
        self.assertEqual( hook.config, { "url": "http://foobar.com" } )
        self.assertEqual( hook.created_at, "2012-05-19T05:03:14Z" )
        self.assertEqual( hook.events, [ "push" ] )
        self.assertEqual( hook.id, 257967 )
        self.assertEqual( hook.last_response, { "status": "unused", "message": None, "code": None } )
        self.assertEqual( hook.name, "web" )
        self.assertEqual( hook.updated_at, "2012-05-19T05:03:14Z" )
        self.assertEqual( hook.url, "https://api.github.com/repos/jacquev6/PyGithub/hooks/257967" )

    def testCreateHookWithAllParameters( self ):
        hook = self.repo.create_hook( "web", { "url": "http://foobar.com" }, [ "fork" ], False )
        self.assertEqual( hook.active, True ) # WTF
        self.assertEqual( hook.config, { "url": "http://foobar.com" } )
        self.assertEqual( hook.created_at, "2012-05-19T06:01:45Z" )
        self.assertEqual( hook.events, [ "fork" ] )
        self.assertEqual( hook.id, 257993 )
        self.assertEqual( hook.last_response, { "status": "unused", "message": None, "code": None } )
        self.assertEqual( hook.name, "web" )
        self.assertEqual( hook.updated_at, "2012-05-19T06:01:45Z" )
        self.assertEqual( hook.url, "https://api.github.com/repos/jacquev6/PyGithub/hooks/257993" )

    def testCreateDownloadWithMinimalArguments( self ):
        download = self.repo.create_download( "Foobar.txt", 1024 )
        self.assertEqual( download.id, 242562 )

    def testCreateDownloadWithAllArguments( self ):
        download = self.repo.create_download( "Foobar.txt", 1024, "Download created by PyGithub", "text/richtext" )
        self.assertEqual( download.accesskeyid, "1DWESVTPGHQVTX38V182" )
        self.assertEqual( download.acl, "public-read" )
        self.assertEqual( download.bucket, "github" )
        self.assertEqual( download.content_type, "text/richtext" )
        self.assertEqual( download.created_at, "2012-05-22T19:11:49Z" )
        self.assertEqual( download.description, "Download created by PyGithub" )
        self.assertEqual( download.download_count, 0 )
        self.assertEqual( download.expirationdate, "2112-05-22T19:11:49.000Z" )
        self.assertEqual( download.html_url, "https://github.com/downloads/jacquev6/PyGithub/Foobar.txt" )
        self.assertEqual( download.id, 242556 )
        self.assertEqual( download.mime_type, "text/richtext" )
        self.assertEqual( download.name, "Foobar.txt" )
        self.assertEqual( download.path, "downloads/jacquev6/PyGithub/Foobar.txt" )
        self.assertEqual( download.policy, "ewogICAgJ2V4cGlyYXRpb24nOiAnMjExMi0wNS0yMlQxOToxMTo0OS4wMDBaJywKICAgICdjb25kaXRpb25zJzogWwogICAgICAgIHsnYnVja2V0JzogJ2dpdGh1Yid9LAogICAgICAgIHsna2V5JzogJ2Rvd25sb2Fkcy9qYWNxdWV2Ni9QeUdpdGh1Yi9Gb29iYXIudHh0J30sCiAgICAgICAgeydhY2wnOiAncHVibGljLXJlYWQnfSwKICAgICAgICB7J3N1Y2Nlc3NfYWN0aW9uX3N0YXR1cyc6ICcyMDEnfSwKICAgICAgICBbJ3N0YXJ0cy13aXRoJywgJyRGaWxlbmFtZScsICcnXSwKICAgICAgICBbJ3N0YXJ0cy13aXRoJywgJyRDb250ZW50LVR5cGUnLCAnJ10KICAgIF0KfQ==" )
        self.assertEqual( download.prefix, "downloads/jacquev6/PyGithub" )
        self.assertEqual( download.redirect, False )
        self.assertEqual( download.s3_url, "https://github.s3.amazonaws.com/" )
        self.assertEqual( download.signature, "8FCU/4rgT3ohXfE9N6HO7JgbuK4=" )
        self.assertEqual( download.size, 1024 )
        self.assertEqual( download.url, "https://api.github.com/repos/jacquev6/PyGithub/downloads/242556" )

    def testCreateGitRef( self ):
        ref = self.repo.create_git_ref( "refs/heads/BranchCreatedByPyGithub", "4303c5b90e2216d927155e9609436ccb8984c495" )
        self.assertEqual( ref.url, "https://api.github.com/repos/jacquev6/PyGithub/git/refs/heads/BranchCreatedByPyGithub" )

    def testCreateGitBlob( self ):
        blob = self.repo.create_git_blob( "Blob created by PyGithub", "latin1" )
        self.assertEqual( blob.sha, "5dd930f591cd5188e9ea7200e308ad355182a1d8" )
