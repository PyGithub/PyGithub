import Framework

class PullRequest( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.pull = self.g.get_user().get_repo( "PyGithub" ).get_pull( 31 )

    def testAttributes( self ):
        self.assertEqual( self.pull.additions, 511 )
        self.assertEqual( self.pull.base, {u'repo': {u'has_wiki': False, u'mirror_url': None, u'updated_at': u'2012-05-27T10:29:10Z', u'private': False, u'full_name': u'jacquev6/PyGithub', u'owner': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'id': 3544490, u'size': 188, u'clone_url': u'https://github.com/jacquev6/PyGithub.git', u'forks': 3, u'homepage': u'http://vincent-jacques.net/PyGithub', u'fork': False, u'description': u'Python library implementing the full Github API v3', u'has_downloads': True, u'html_url': u'https://github.com/jacquev6/PyGithub', u'git_url': u'git://github.com/jacquev6/PyGithub.git', u'svn_url': u'https://github.com/jacquev6/PyGithub', u'ssh_url': u'git@github.com:jacquev6/PyGithub.git', u'has_issues': True, u'watchers': 15, u'name': u'PyGithub', u'language': u'Python', u'url': u'https://api.github.com/repos/jacquev6/PyGithub', u'created_at': u'2012-02-25T12:53:47Z', u'pushed_at': u'2012-05-27T10:29:09Z', u'open_issues': 16}, u'sha': u'ed866fc43833802ab553e5ff8581c81bb00dd433', u'ref': u'topic/RewriteWithGeneratedCode', u'user': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'label': u'jacquev6:topic/RewriteWithGeneratedCode'} ) ### @todo
        self.assertEqual( self.pull.body, "Body edited by PyGithub" )
        self.assertEqual( self.pull.changed_files, 45 )
        self.assertEqual( self.pull.closed_at, "2012-05-27T10:29:07Z" )
        self.assertEqual( self.pull.comments, 0 )
        self.assertEqual( self.pull.commits, 3 )
        self.assertEqual( self.pull.created_at, "2012-05-27T09:25:36Z" )
        self.assertEqual( self.pull.deletions, 384 )
        self.assertEqual( self.pull.diff_url, "https://github.com/jacquev6/PyGithub/pull/31.diff" )
        self.assertEqual( self.pull.head, {u'repo': {u'has_wiki': False, u'mirror_url': None, u'updated_at': u'2012-05-27T09:09:17Z', u'private': False, u'full_name': u'BeaverSoftware/PyGithub', u'owner': {u'url': u'https://api.github.com/users/BeaverSoftware', u'login': u'BeaverSoftware', u'avatar_url': u'https://secure.gravatar.com/avatar/d563e337cac2fdc644e2aaaad1e23266?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-orgs.png', u'id': 1424031, u'gravatar_id': u'd563e337cac2fdc644e2aaaad1e23266'}, u'id': 4460787, u'size': 176, u'clone_url': u'https://github.com/BeaverSoftware/PyGithub.git', u'forks': 0, u'homepage': u'http://vincent-jacques.net/PyGithub', u'fork': True, u'description': u'Python library implementing the full Github API v3', u'has_downloads': True, u'html_url': u'https://github.com/BeaverSoftware/PyGithub', u'git_url': u'git://github.com/BeaverSoftware/PyGithub.git', u'svn_url': u'https://github.com/BeaverSoftware/PyGithub', u'ssh_url': u'git@github.com:BeaverSoftware/PyGithub.git', u'has_issues': False, u'watchers': 1, u'name': u'PyGithub', u'language': u'Python', u'url': u'https://api.github.com/repos/BeaverSoftware/PyGithub', u'created_at': u'2012-05-27T08:50:04Z', u'pushed_at': u'2012-05-27T09:09:17Z', u'open_issues': 0}, u'sha': u'8a4f306d4b223682dd19410d4a9150636ebe4206', u'ref': u'master', u'user': {u'url': u'https://api.github.com/users/BeaverSoftware', u'login': u'BeaverSoftware', u'avatar_url': u'https://secure.gravatar.com/avatar/d563e337cac2fdc644e2aaaad1e23266?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-orgs.png', u'id': 1424031, u'gravatar_id': u'd563e337cac2fdc644e2aaaad1e23266'}, u'label': u'BeaverSoftware:master'} ) ### @todo
        self.assertEqual( self.pull.html_url, "https://github.com/jacquev6/PyGithub/pull/31" )
        self.assertEqual( self.pull.id, 1436215 )
        self.assertEqual( self.pull.issue_url, "https://github.com/jacquev6/PyGithub/issues/31" )
        self.assertEqual( self.pull.mergeable, None )
        self.assertEqual( self.pull.merged, True )
        self.assertEqual( self.pull.merged_at, "2012-05-27T10:29:07Z" )
        self.assertEqual( self.pull.merged_by.login, "jacquev6" )
        self.assertEqual( self.pull.number, 31 )
        self.assertEqual( self.pull.patch_url, "https://github.com/jacquev6/PyGithub/pull/31.patch" )
        self.assertEqual( self.pull.review_comments, 1 )
        self.assertEqual( self.pull.state, "closed" )
        self.assertEqual( self.pull.title, "Title edited by PyGithub" )
        self.assertEqual( self.pull.updated_at, "2012-05-27T10:29:07Z" )
        self.assertEqual( self.pull.url, "https://api.github.com/repos/jacquev6/PyGithub/pulls/31" )
        self.assertEqual( self.pull.user.login, "jacquev6" )

    def testCreateComment( self ):
        ### @todo in_reply_to
        comment = self.pull.create_comment( "Comment created by PyGithub", "8a4f306d4b223682dd19410d4a9150636ebe4206", "src/github/Issue.py", 5 )
        self.assertEqual( comment.id, 886298 )

    def testGetComments( self ):
        self.assertListKeyEqual( self.pull.get_comments(), lambda c: c.id, [ 886298 ] )

    def testEditWithoutArguments( self ):
        self.pull.edit()

    def testEditWithAllArguments( self ):
        self.pull.edit( "Title edited by PyGithub", "Body edited by PyGithub", "open" )
        self.assertEqual( self.pull.title, "Title edited by PyGithub" )
        self.assertEqual( self.pull.body, "Body edited by PyGithub" )
        self.assertEqual( self.pull.state, "open" )

    def testGetCommits( self ):
        self.assertListKeyEqual( self.pull.get_commits(), lambda c: c.sha, [ "4aadfff21cdd2d2566b0e4bd7309c233b5f4ae23", "93dcae5cf207de376c91d0599226e7c7563e1d16", "8a4f306d4b223682dd19410d4a9150636ebe4206" ] )

    def testGetFiles( self ):
        self.assertListKeyEqual( self.pull.get_files(), lambda f: f.filename, [ "codegen/templates/GithubObject.py", "src/github/AuthenticatedUser.py", "src/github/Authorization.py", "src/github/Branch.py", "src/github/Commit.py", "src/github/CommitComment.py", "src/github/CommitFile.py", "src/github/CommitStats.py", "src/github/Download.py", "src/github/Event.py", "src/github/Gist.py", "src/github/GistComment.py", "src/github/GistHistoryState.py", "src/github/GitAuthor.py", "src/github/GitBlob.py", "src/github/GitCommit.py", "src/github/GitObject.py", "src/github/GitRef.py", "src/github/GitTag.py", "src/github/GitTree.py", "src/github/GitTreeElement.py", "src/github/Hook.py", "src/github/Issue.py", "src/github/IssueComment.py", "src/github/IssueEvent.py", "src/github/Label.py", "src/github/Milestone.py", "src/github/NamedUser.py", "src/github/Organization.py", "src/github/Permissions.py", "src/github/Plan.py", "src/github/PullRequest.py", "src/github/PullRequestComment.py", "src/github/PullRequestFile.py", "src/github/Repository.py", "src/github/RepositoryKey.py", "src/github/Tag.py", "src/github/Team.py", "src/github/UserKey.py", "test/Issue.py", "test/IssueEvent.py", "test/ReplayData/Issue.testAddAndRemoveLabels.txt", "test/ReplayData/Issue.testDeleteAndSetLabels.txt", "test/ReplayData/Issue.testGetLabels.txt", "test/ReplayData/IssueEvent.setUp.txt" ] )

    def testMerge( self ):
        self.assertFalse( self.pull.is_merged() )
        status = self.pull.merge() ### @todo message
        ### @todo PullRequestMergeStatus
        # self.assertEqual( status.sha, "" )
        # self.assertEqual( status.merged, True )
        # self.assertEqual( status.message, "" )
        self.assertTrue( self.pull.is_merged() )
