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
        self.assertEqual( self.repo.forks, 3 )
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
        self.assertEqual( self.repo.name, "PyGithub" )
        self.assertEqual( self.repo.open_issues, 16 )
        self.assertEqual( self.repo.organization, None )
        self.assertEqual( self.repo.owner.login, "jacquev6" )
        self.assertEqual( self.repo.parent, None )
        self.assertEqual( self.repo.permissions.admin, True )
        self.assertEqual( self.repo.permissions.pull, True )
        self.assertEqual( self.repo.permissions.push, True )
        self.assertEqual( self.repo.private, False )
        self.assertEqual( self.repo.pushed_at, "2012-05-27T06:00:28Z" )
        self.assertEqual( self.repo.size, 308 )
        self.assertEqual( self.repo.source, None )
        self.assertEqual( self.repo.ssh_url, "git@github.com:jacquev6/PyGithub.git" )
        self.assertEqual( self.repo.svn_url, "https://github.com/jacquev6/PyGithub" )
        self.assertEqual( self.repo.updated_at, "2012-05-27T06:55:28Z" )
        self.assertEqual( self.repo.url, "https://api.github.com/repos/jacquev6/PyGithub" )
        self.assertEqual( self.repo.watchers, 15 )

    def testEditWithoutArguments( self ):
        self.repo.edit( "PyGithub" )

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

    def testCreateMilestoneWithMinimalArguments( self ):
        milestone = self.repo.create_milestone( "Milestone also created by PyGithub" )
        self.assertEqual( milestone.number, 6 )

    def testCreateIssue( self ):
        issue = self.repo.create_issue( "Issue created by PyGithub" )
        self.assertEqual( issue.number, 28 )

    def testCreateIssueWithAllArguments( self ):
        issue = self.repo.create_issue( "Issue also created by PyGithub", "Body created by PyGithub", "jacquev6", 2, [ "Question" ] )
        self.assertEqual( issue.number, 30 )

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

    def testCreateGitTree( self ):
        tree = self.repo.create_git_tree(
            [ {
                "path": "Foobar.txt",
                "mode": "100644",
                "type": "blob",
                "content": "File created by PyGithub"
            } ] 
        )
        self.assertEqual( tree.sha, "41cf8c178c636a018d537cb20daae09391efd70b" )

    def testCreateGitTreeWithBaseTree( self ):
        tree = self.repo.create_git_tree(
            [ {
                "path": "Barbaz.txt",
                "mode": "100644",
                "type": "blob",
                "content": "File also created by PyGithub"
            } ], 
            "41cf8c178c636a018d537cb20daae09391efd70b"
        )
        self.assertEqual( tree.sha, "107139a922f33bab6fbeb9f9eb8787e7f19e0528" )

    def testCreateGitCommit( self ):
        commit = self.repo.create_git_commit( "Commit created by PyGithub", "107139a922f33bab6fbeb9f9eb8787e7f19e0528", [] )
        self.assertEqual( commit.sha, "0b820628236ab8bab3890860fc414fa757ca15f4" )

    def testCreateGitCommitWithAllArguments( self ):
        commit = self.repo.create_git_commit( "Commit created by PyGithub", "107139a922f33bab6fbeb9f9eb8787e7f19e0528", [], { "name" : "John Doe", "email" : "j.doe@vincent-jacques.net", "date": "2008-07-09T16:13:30+12:00" }, { "name" : "John Doe", "email" : "j.doe@vincent-jacques.net", "date": "2008-07-09T16:13:30+12:00" } )
        self.assertEqual( commit.sha, "526946197ae9da59c6507cacd13ad6f1cfb686ea" )

    def testCreateGitTag( self ):
        tag = self.repo.create_git_tag( "TaggedByPyGithub", "Tag created by PyGithub", "0b820628236ab8bab3890860fc414fa757ca15f4", "commit" )
        self.assertEqual( tag.sha, "5ba561eaa2b7ca9015662510157b15d8f3b0232a" )

    def testCreateGitTagWithAllArguments( self ):
        tag = self.repo.create_git_tag( "TaggedByPyGithub2", "Tag also created by PyGithub", "526946197ae9da59c6507cacd13ad6f1cfb686ea", "commit", { "name" : "John Doe", "email" : "j.doe@vincent-jacques.net", "date": "2008-07-09T16:13:30+12:00" } )
        self.assertEqual( tag.sha, "f0e99a8335fbc84c53366c4a681118468f266625" )

    def testCreateKey( self ):
        key = self.repo.create_key( "Key added through PyGithub", "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAQEA2Mm0RjTNAYFfSCtUpO54usdseroUSIYg5KX4JoseTpqyiB/hqewjYLAdUq/tNIQzrkoEJWSyZrQt0ma7/YCyMYuNGd3DU6q6ZAyBeY3E9RyCiKjO3aTL2VKQGFvBVVmGdxGVSCITRphAcsKc/PF35/fg9XP9S0anMXcEFtdfMHz41SSw+XtE+Vc+6cX9FuI5qUfLGbkv8L1v3g4uw9VXlzq4GfTA+1S7D6mcoGHopAIXFlVr+2RfDKdSURMcB22z41fljO1MW4+zUS/4FyUTpL991es5fcwKXYoiE+x06VJeJJ1Krwx+DZj45uweV6cHXt2JwJEI9fWB6WyBlDejWw== vincent@IDEE" )
        self.assertEqual( key.id, 2626761 )

    def testCollaborators( self ):
        lyloa = self.g.get_user( "Lyloa" )
        self.assertFalse( self.repo.has_in_collaborators( lyloa ) )
        self.repo.add_to_collaborators( lyloa )
        self.assertTrue( self.repo.has_in_collaborators( lyloa ) )
        self.assertListKeyEqual( self.repo.get_collaborators(), lambda u: u.login, [ "jacquev6", "Lyloa" ] )
        self.repo.remove_from_collaborators( lyloa )
        self.assertFalse( self.repo.has_in_collaborators( lyloa ) )

    def testCompare( self ):
        self.assertEqual(
            self.repo.compare( "v0.6", "v0.7" ),
            {
                u'status': u'ahead',
                u'files': [
                    {u'status': u'modified', u'deletions': 1, u'raw_url': u'https://github.com/jacquev6/PyGithub/raw/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7/ReferenceOfClasses.md', u'blob_url': u'https://github.com/jacquev6/PyGithub/blob/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7/ReferenceOfClasses.md', u'filename': u'ReferenceOfClasses.md', u'sha': u'ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'additions': 1, u'patch': u"@@ -3,7 +3,7 @@ You obtain instances through calls to `get_` and `create_` methods.\n \n Class `Github`\n ==============\n-* Constructed from user's login and password\n+* Constructed from user's login and password or OAuth token\n * `get_user()`: `AuthenticatedUser`\n * `get_user( login )`: `NamedUser`\n * `get_organization( login )`: `Organization`", u'changes': 2},
                    {u'status': u'modified', u'deletions': 2, u'raw_url': u'https://github.com/jacquev6/PyGithub/raw/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7/github/Github.py', u'blob_url': u'https://github.com/jacquev6/PyGithub/blob/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7/github/Github.py', u'filename': u'github/Github.py', u'sha': u'ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'additions': 2, u'patch': u'@@ -2,8 +2,8 @@\n from GithubObjects import *\n \n class Github:\n-    def __init__( self, login, password, debugFile = None ):\n-        self.__requester = Requester( login, password )\n+    def __init__( self, login_or_token = None, password = None, debugFile = None ):\n+        self.__requester = Requester( login_or_token, password )\n         self.__debugFile = debugFile\n \n     def _dataRequest( self, verb, url, parameters, data ):', u'changes': 4},
                    {u'status': u'modified', u'deletions': 3, u'raw_url': u'https://github.com/jacquev6/PyGithub/raw/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7/github/Requester.py', u'blob_url': u'https://github.com/jacquev6/PyGithub/blob/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7/github/Requester.py', u'filename': u'github/Requester.py', u'sha': u'ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'additions': 14, u'patch': u'@@ -7,8 +7,15 @@ class UnknownGithubObject( Exception ):\n     pass\n \n class Requester:\n-    def __init__( self, login, password ):\n-        self.__authorizationHeader = "Basic " + base64.b64encode( login + ":" + password ).replace( \'\\n\', \'\' )\n+    def __init__( self, login_or_token, password ):\n+        if password is not None:\n+            login = login_or_token\n+            self.__authorizationHeader = "Basic " + base64.b64encode( login + ":" + password ).replace( \'\\n\', \'\' )\n+        elif login_or_token is not None:\n+            token = login_or_token\n+            self.__authorizationHeader = "token " + token\n+        else:\n+            self.__authorizationHeader = None\n \n     def dataRequest( self, verb, url, parameters, input ):\n         if parameters is None:\n@@ -46,12 +53,16 @@ def statusRequest( self, verb, url, parameters, input ):\n     def __rawRequest( self, verb, url, parameters, input ):\n         assert verb in [ "HEAD", "GET", "POST", "PATCH", "PUT", "DELETE" ]\n \n+        headers = dict()\n+        if self.__authorizationHeader is not None:\n+            headers[ "Authorization" ] = self.__authorizationHeader\n+\n         cnx = httplib.HTTPSConnection( "api.github.com", strict = True )\n         cnx.request(\n             verb,\n             self.__completeUrl( url, parameters ),\n             json.dumps( input ),\n-            { "Authorization" : self.__authorizationHeader }\n+            headers\n         )\n         response = cnx.getresponse()\n ', u'changes': 17},
                    {u'status': u'modified', u'deletions': 1, u'raw_url': u'https://github.com/jacquev6/PyGithub/raw/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7/setup.py', u'blob_url': u'https://github.com/jacquev6/PyGithub/blob/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7/setup.py', u'filename': u'setup.py', u'sha': u'ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'additions': 9, u'patch': u'@@ -5,7 +5,7 @@\n \n setup(\n     name = \'PyGithub\',\n-    version = \'0.6\',\n+    version = \'0.7\',\n     description = \'Use the full Github API v3\',\n     author = \'Vincent Jacques\',\n     author_email = \'vincent@vincent-jacques.net\',\n@@ -26,6 +26,14 @@\n                 print repo.name\n                 repo.edit( has_wiki = False )\n \n+        You can also create a Github instance without authentication::\n+\n+            g = Github( "user", "password" )\n+\n+        Or with an OAuth token::\n+\n+            g = Github( token )\n+\n         Reference documentation\n         =======================\n ', u'changes': 10}
                ],
                u'base_commit': {
                    u'committer': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'},
                    u'author': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'},
                    u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/4303c5b90e2216d927155e9609436ccb8984c495',
                    u'sha': u'4303c5b90e2216d927155e9609436ccb8984c495',
                    u'parents': [
                        {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/936f4a97f1a86392637ec002bbf89ff036a5062d', u'sha': u'936f4a97f1a86392637ec002bbf89ff036a5062d'},
                        {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/2a7e80e6421c5d4d201d60619068dea6bae612cb', u'sha': u'2a7e80e6421c5d4d201d60619068dea6bae612cb'}
                    ],
                    u'commit': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495', u'committer': {u'date': u'2012-04-17T10:55:16-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}, u'message': u"Merge branch 'develop'", u'tree': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/trees/f492784d8ca837779650d1fb406a1a3587a764ad', u'sha': u'f492784d8ca837779650d1fb406a1a3587a764ad'}, u'author': {u'date': u'2012-04-17T10:55:16-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}}
                },
                u'ahead_by': 4,
                u'url': u'https://api.github.com/repos/jacquev6/PyGithub/compare/v0.6...v0.7',
                u'merge_base_commit': {
                    u'committer': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'},
                    u'author': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'},
                    u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/4303c5b90e2216d927155e9609436ccb8984c495',
                    u'sha': u'4303c5b90e2216d927155e9609436ccb8984c495',
                    u'parents': [
                        {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/936f4a97f1a86392637ec002bbf89ff036a5062d', u'sha': u'936f4a97f1a86392637ec002bbf89ff036a5062d'},
                        {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/2a7e80e6421c5d4d201d60619068dea6bae612cb', u'sha': u'2a7e80e6421c5d4d201d60619068dea6bae612cb'}
                    ],
                    u'commit': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/commits/4303c5b90e2216d927155e9609436ccb8984c495', u'committer': {u'date': u'2012-04-17T10:55:16-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}, u'message': u"Merge branch 'develop'", u'tree': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/trees/f492784d8ca837779650d1fb406a1a3587a764ad', u'sha': u'f492784d8ca837779650d1fb406a1a3587a764ad'}, u'author': {u'date': u'2012-04-17T10:55:16-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}}
                },
                u'html_url': u'https://github.com/jacquev6/PyGithub/compare/v0.6...v0.7',
                u'behind_by': 0,
                u'patch_url': u'https://github.com/jacquev6/PyGithub/compare/v0.6...v0.7.patch',
                u'commits': [
                    {u'committer': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'author': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/5bb654d26dd014d36794acd1e6ecf3736f12aad7', u'sha': u'5bb654d26dd014d36794acd1e6ecf3736f12aad7', u'parents': [{u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/4303c5b90e2216d927155e9609436ccb8984c495', u'sha': u'4303c5b90e2216d927155e9609436ccb8984c495'}], u'commit': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/commits/5bb654d26dd014d36794acd1e6ecf3736f12aad7', u'committer': {u'date': u'2012-05-25T05:10:54-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}, u'message': u'Implement the three authentication schemes', u'tree': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/trees/59d755d95bc2e2de4dcef70a7c73e81e677f610b', u'sha': u'59d755d95bc2e2de4dcef70a7c73e81e677f610b'}, u'author': {u'date': u'2012-05-25T05:10:54-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}}},
                    {u'committer': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'author': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/cb0313157bf904f2d364377d35d9397b269547a5', u'sha': u'cb0313157bf904f2d364377d35d9397b269547a5', u'parents': [{u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/4303c5b90e2216d927155e9609436ccb8984c495', u'sha': u'4303c5b90e2216d927155e9609436ccb8984c495'}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/5bb654d26dd014d36794acd1e6ecf3736f12aad7', u'sha': u'5bb654d26dd014d36794acd1e6ecf3736f12aad7'}], u'commit': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/commits/cb0313157bf904f2d364377d35d9397b269547a5', u'committer': {u'date': u'2012-05-25T10:04:22-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}, u'message': u"Merge branch 'topic/Authentication' into develop", u'tree': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/trees/59d755d95bc2e2de4dcef70a7c73e81e677f610b', u'sha': u'59d755d95bc2e2de4dcef70a7c73e81e677f610b'}, u'author': {u'date': u'2012-05-25T10:04:22-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}}},
                    {u'committer': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'author': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/0cec0d25e606c023a62a4fc7cdc815309ebf6d16', u'sha': u'0cec0d25e606c023a62a4fc7cdc815309ebf6d16', u'parents': [{u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/cb0313157bf904f2d364377d35d9397b269547a5', u'sha': u'cb0313157bf904f2d364377d35d9397b269547a5'}], u'commit': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/commits/0cec0d25e606c023a62a4fc7cdc815309ebf6d16', u'committer': {u'date': u'2012-05-25T10:13:33-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}, u'message': u'Publish version 0.7', u'tree': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/trees/78735573611521bb3ade95921c668097e2a4dc5e', u'sha': u'78735573611521bb3ade95921c668097e2a4dc5e'}, u'author': {u'date': u'2012-05-25T10:13:33-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}}}, 
                    {u'committer': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'author': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'sha': u'ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'parents': [{u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/4303c5b90e2216d927155e9609436ccb8984c495', u'sha': u'4303c5b90e2216d927155e9609436ccb8984c495'}, {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/commits/0cec0d25e606c023a62a4fc7cdc815309ebf6d16', u'sha': u'0cec0d25e606c023a62a4fc7cdc815309ebf6d16'}], u'commit': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/commits/ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'committer': {u'date': u'2012-05-25T10:14:34-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}, u'message': u"Merge branch 'develop'", u'tree': {u'url': u'https://api.github.com/repos/jacquev6/PyGithub/git/trees/78735573611521bb3ade95921c668097e2a4dc5e', u'sha': u'78735573611521bb3ade95921c668097e2a4dc5e'}, u'author': {u'date': u'2012-05-25T10:14:34-07:00', u'email': u'vincent@vincent-jacques.net', u'name': u'Vincent Jacques'}}}
                ],
                u'total_commits': 4,
                u'diff_url': u'https://github.com/jacquev6/PyGithub/compare/v0.6...v0.7.diff',
                u'permalink_url': u'https://github.com/jacquev6/PyGithub/compare/jacquev6:4303c5b...jacquev6:ecda065'
            }
        )

    def testGetComments( self ):
        self.assertListKeyEqual(
            self.repo.get_comments(),
            lambda c: c.body,
            [
                "probably a noob question: does this completion refer to autocompletion in IDE's/editors? \nI have observed that this is pretty erratic sometimes. I'm using PyDev+Eclipse.\nFor example, in the tutorial from the readme, `g.get_u` gets autocompleted correctly, but `g.get_user().get_r` (or any method or attribute applicable to NamedUsers/AuthenticatedUser, really) does not show autocompletion to `g.get_user().get_repo()`. Is that by design? It makes exploring the library/API a bit cumbersome. ",
                "No, it has nothing to do with auto-completion in IDEs :D\n\nGithub API v3 sends only the main part of objects in reply to some requests. So, if the user wants an attribute that has not been received yet, I have to do another request to complete the object.\n\nYet, in version 1.0 (see the milesone), my library will be much more readable for IDEs and their auto-completion mechanisms, because I am giving up the meta-description that I used until 0.6, and I'm now generating much more traditional code, that you will be able to explore as if it was written manually.\n\nIf you want to take the time to open an issue about auto-completion in IDEs, I'll deal with it in milestone 1.0.\n\nThanks !",
                "Ah, thanks for the clarification. :blush:\n\nI made issue #27 for the autocompletion. I already suspected something like this meta-description magic, since I tried to read some of the code and it was pretty arcane. I attributed that to my pythonic noobness, though. Thank you. ",
                "Comment created by PyGithub"
            ]
        )

    def testGetCommits( self ):
        self.assertListKeyBegin( self.repo.get_commits(), lambda c: c.sha, [ u'ecda065e01876209d2bdf5fe4e91cee8ffaa9ff7', u'0cec0d25e606c023a62a4fc7cdc815309ebf6d16', u'cb0313157bf904f2d364377d35d9397b269547a5', u'5bb654d26dd014d36794acd1e6ecf3736f12aad7', u'4303c5b90e2216d927155e9609436ccb8984c495', u'2a7e80e6421c5d4d201d60619068dea6bae612cb', u'0af24499a98e85f8ab2191898e8b809e5cebd4c5', u'e5ae923a68a9ae295ce5aa20b1227253de60e918', u'2f64b625f7e2afc9bef61d0decb459e2ef65c550', u'590798d349cba7de6e83b43aa5d4f8b0a38e685d', u'e7dca9143a23b8e2045a4a910a4a329007b10086', u'ab3f9b422cb3043d35cf6002fc9c042f8ead8c2a', u'632d8b63c32a2b79e87eb3b93e1ad228724de4bd', u'64c6a1e975e61b9c1449bed016cd19f33ee4b1c5', u'99963536fc81db3b9986c761b9dd08de22089aa2', u'8d57522bbd15d1fb6b616fae795cd8721deb1c4d', u'1140a91f3e45d09bc15463724f178a7ebf8e3149', u'936f4a97f1a86392637ec002bbf89ff036a5062d', u'e10470481795506e2c232720e2a9ecf588c8b567', u'e456549e5265406f8090ae5145255c8ca9ea5e4e', u'a91131be42eb328ae030f584af500f56aa08424b', u'2469c6e1aeb7919126a8271f6980b555b167e8b0', u'a655d0424135befd3a0d53f3f7eff2d1c754854f', u'ce62e91268aa34dad0ba0dbee4769933e3a71e50', u'1c88ee221b7f995855a1fdfac7d0ba19db918739', u'bd1a5dff3c547c634b2d89f5847218820e343883', u'b226b5b4e2f44107dde674e7a5d3e88d4e3518df', u'25dbd4053e982402c7d92139f167dbe46008c932', u'a0cc821c1beada4aa9ca0d5218664c5372720936', u'c1440bdf20bfeb62684c6d1779448719dce9d2df', u'1095d304b7fab3818dcb4c42093c8c56d3ac05e4', u'bd39726f7cf86ea7ffb33b5718241fdab5fc8f53', u'1d2b27824d20612066d84be42d6691c66bb18ef4', u'6af2bfd0d46bc0eeb8c37b85c7b3003e0e4ae297', u'a475d685d8ae709095d09094ea0962ac182d33f0', u'a85de99ea5b5e7b38bd68e076d09c49207b8687e', u'd24cf209ddd1758188c5f35344f76df818d09a46', u'0909fec395bb1f97e2580d6a029cfc64b352aff9', u'6e421e9e85e12008758870bc046bc2c6120af72a', u'32ed0ebc377efbed5b482b3d49ff54bf1715d55a', u'8213df1d744f251aa8e52229643a9f6ce352f3c0', u'69cc298fd159f19eb204dd09f17d31dc4abc3d41', u'85eef756353e13efcb24c726320cd2617c2a7bd8', u'50ac55b25ceba555b84709839f80447552450697', u'767d75a580279e457f9bc52bc308a17ff8ea0509', u'75e72ffa3066693291f7da03070666e8f885097a', u'504047e218e6b34a3828ccc408431634f17b9504', u'960db1d5c9853e9f5fbbc9237c2c166ceef1f080', u'877dde23e140bbf038f9a2d8f0f07b4e3a965c61', u'1c95ddfa09ec0aa1f07ee9ad50a77be1dd74b55e', u'99564c1cab139d1e4678f5f83f60d26f1210db7e', u'231926207709ceaa61e87b64e34e17d85adecd9c', u'fb722625dddb9a32f75190723f7da12683b7c4b2', u'cab9d71603e127bdd1f600a759dccea1781fa1ab', u'e648e5aeb5edc1fbf83e9d37d2a3cb57c005019a', u'4a5cf98e7f959f1b5d9af484760c25cd27d9180d', u'5d1add448e0b0b1dadb8c6094a9e5e19b255f67e', u'0d9fc99a4b5d1ec6473c9c81c888917c132ffa65', u'b56aa09011378b014221f86dffb8304957a9e6bd', u'3e8169c0a98ce1e2c6a32ae1256ae0f735065df5', u'378558f6cac6183b4a7100c0ce5eaad1cfff6717', u'58b4396aa0e7cb72911b75cb035798143a06e0ee', u'a3be28756101370fbc689eec3a7825c4c385a6c9', u'3d6bd49ce229243fea4bb46a937622d0ec7d4d1c', u'58cb0dbdef9765e0e913c726f923a47315aaf80e', u'7b7ac20c6fa27f72a24483c73ab1bf4deffc89f0', u'97f308e67383368a2d15788cac28e126c8528bb2', u'fc33a6de4f0e08d7ff2de05935517ec3932d212e', u'cc6d0fc044eadf2e6fde5da699f61654c1e691f3', u'2dd71f3777b87f2ba61cb20d2c67f10401e3eb2c', u'366ca58ca004b9129f9d435db8204ce0f5bc57c3', u'0d3b3ffd1e5c143af8725fdee808101f626f683d', u'157f9c13275738b6b39b8d7a874f5f0aee47cb18' ] )

    def testGetDownloads( self ):
        self.assertListKeyEqual( self.repo.get_downloads(), lambda d: d.id, [ 245143 ] )

    def testGetEvents( self ):
        self.assertListKeyBegin( self.repo.get_events(), lambda e: e.type, [ "DownloadEvent", "DownloadEvent", "PushEvent", "IssuesEvent", "MemberEvent", "MemberEvent" ] )

    def testGetForks( self ):
        self.assertListKeyEqual( self.repo.get_forks(), lambda r: r.owner.login, [ "abersager" ] )

    def testGetGitRefs( self ):
        self.assertListKeyEqual( self.repo.get_git_refs(), lambda r: r.ref, [ "refs/heads/develop", "refs/heads/master", "refs/heads/topic/DependencyGraph", "refs/heads/topic/RewriteWithGeneratedCode", "refs/tags/v0.1", "refs/tags/v0.2", "refs/tags/v0.3", "refs/tags/v0.4", "refs/tags/v0.5", "refs/tags/v0.6", "refs/tags/v0.7" ] )

    def testGetGitTreeWithRecursive( self ):
        tree = self.repo.get_git_tree( "f492784d8ca837779650d1fb406a1a3587a764ad", True )
        self.assertEqual( len( tree.tree ), 90 )
        self.assertEqual( tree.tree[ 50 ].path, "github/GithubObjects/Gist.py" )

    def testGetHooks( self ):
        self.assertListKeyEqual( self.repo.get_hooks(), lambda h: h.id, [ 257993 ] )

    def testGetIssues( self ):
        self.assertListKeyEqual( self.repo.get_issues(), lambda i: i.id, [ 4769659, 4639931, 4452000, 4356743, 3716033, 3715946, 3643837, 3628022, 3624595, 3624570, 3624561, 3624556, 3619973, 3527266, 3527245, 3527231 ] )

    def testGetKeys( self ):
        self.assertListKeyEqual( self.repo.get_keys(), lambda k: k.title, [ "Key added through PyGithub" ] )

    def testGetLabels( self ):
        self.assertListKeyEqual( self.repo.get_labels(), lambda l: l.name, [ "Refactoring", "Public interface", "Functionalities", "Project management", "Bug", "Question" ] )

    def testGetLanguages( self ):
        self.assertEqual( self.repo.get_languages(), { "Python": 127266, "Shell": 673} )

    def testGetMilestones( self ):
        self.assertListKeyEqual( self.repo.get_milestones(), lambda m: m.id, [ 93547 ] )

    def testGetIssuesEvents( self ):
        self.assertListKeyBegin( self.repo.get_issues_events(), lambda e: e.event, [ "assigned", "subscribed", "closed", "assigned", "closed" ] )

    def testGetNetworkEvents( self ):
        self.assertListKeyBegin( self.repo.get_network_events(), lambda e: e.type, [ "DownloadEvent", "DownloadEvent", "PushEvent", "IssuesEvent", "MemberEvent" ] )

    def testGetTeams( self ):
        repo = self.g.get_organization( "BeaverSoftware" ).get_repo( "FatherBeaver" )
        self.assertListKeyEqual( repo.get_teams(), lambda t: t.name, [ "Members" ] )

    def testGetWatchers( self ):
        self.assertListKeyEqual( self.repo.get_watchers(), lambda u: u.login, [ "Stals", "att14", "jardon-u", "huxley", "mikofski", "L42y", "fanzeyi", "abersager", "waylan", "adericbourg", "tallforasmurf", "pvicente", "roskakori", "michaelpedersen", "BeaverSoftware" ] )

    def testCreatePull( self ):
        pull = self.repo.create_pull( "Pull request created by PyGithub", "Body of the pull request", "topic/RewriteWithGeneratedCode", "BeaverSoftware:master" )
        self.assertEqual( pull.id, 1436215 )

    def testCreatePullFromIssue( self ):
        pull = self.repo.create_pull( 32, "topic/RewriteWithGeneratedCode", "BeaverSoftware:master" )
        self.assertEqual( pull.id, 1436310 )

    def testGetPulls( self ):
        self.assertListKeyEqual( self.repo.get_pulls(), lambda p: p.id, [ 1436310 ] )
