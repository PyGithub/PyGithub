import Framework

class NamedUser( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.user = self.g.get_user( "jacquev6" )

    def testAttributesOfOtherUser( self ):
        self.user = self.g.get_user( "nvie" )
        self.assertEqual( self.user.avatar_url, "https://secure.gravatar.com/avatar/c5a7f21b46df698f3db31c37ed0cf55a?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" )
        self.assertEqual( self.user.bio, None )
        self.assertEqual( self.user.blog, "http://nvie.com" )
        self.assertEqual( self.user.collaborators, None )
        self.assertEqual( self.user.company, "3rd Cloud" )
        self.assertEqual( self.user.created_at, "2009-05-12T21:19:38Z" )
        self.assertEqual( self.user.disk_usage, None )
        self.assertEqual( self.user.email, "vincent@3rdcloud.com" )
        self.assertEqual( self.user.followers, 296 )
        self.assertEqual( self.user.following, 41 )
        self.assertEqual( self.user.gravatar_id, "c5a7f21b46df698f3db31c37ed0cf55a" )
        self.assertEqual( self.user.hireable, False )
        self.assertEqual( self.user.html_url, "https://github.com/nvie" )
        self.assertEqual( self.user.id, 83844 )
        self.assertEqual( self.user.location, "Netherlands" )
        self.assertEqual( self.user.login, "nvie" )
        self.assertEqual( self.user.name, "Vincent Driessen" )
        self.assertEqual( self.user.owned_private_repos, None )
        self.assertEqual( self.user.plan, None )
        self.assertEqual( self.user.private_gists, None )
        self.assertEqual( self.user.public_gists, 16 )
        self.assertEqual( self.user.public_repos, 61 )
        self.assertEqual( self.user.total_private_repos, None )
        self.assertEqual( self.user.type, "User" )
        self.assertEqual( self.user.url, "https://api.github.com/users/nvie" )

    def testAttributesOfSelf( self ):
        self.assertEqual( self.user.avatar_url, "https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png" )
        self.assertEqual( self.user.bio, "" )
        self.assertEqual( self.user.blog, "http://vincent-jacques.net" )
        self.assertEqual( self.user.collaborators, 0 )
        self.assertEqual( self.user.company, "Criteo" )
        self.assertEqual( self.user.created_at, "2010-07-09T06:10:06Z" )
        self.assertEqual( self.user.disk_usage, 17080 )
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
        self.assertEqual( self.user.public_gists, 2 )
        self.assertEqual( self.user.public_repos, 11 )
        self.assertEqual( self.user.total_private_repos, 5 )
        self.assertEqual( self.user.type, "User" )
        self.assertEqual( self.user.url, "https://api.github.com/users/jacquev6" )

    def testCreateGist( self ):
        gist = self.user.create_gist( True, { "foobar.txt": { "content": "File created by PyGithub" } }, "Gist created by PyGithub on a NamedUser" )
        self.assertEqual( gist.description, "Gist created by PyGithub on a NamedUser" )
        gist.delete()

    def testGetGists( self ):
        gist = self.user.get_gists()[ 0 ]
        self.assertEqual( gist.description, "Gist created by PyGithub" )

    def testFollowing( self ):
        follower = self.user.get_followers()[ 0 ]
        self.assertEqual( follower.login, "jnorthrup" )
        followed = self.user.get_following()[ 0 ]
        self.assertEqual( followed.login, "nvie" )

    def testEvents( self ):
        event = self.user.get_events()[ 0 ]
        self.assertEqual( event.actor.login, "jacquev6" )
        self.assertEqual( event.commit_id, None )
        self.assertEqual( event.created_at, "2012-05-20T12:14:09Z" )
        self.assertEqual( event.event, None )
        self.assertEqual( event.id, "1553915048" )
        self.assertEqual( event.issue, None )
        self.assertEqual( event.org, None )
        self.assertEqual( event.payload,  {u'action': u'create', u'gist': {u'files': {}, u'description': u'Gist created by PyGithub on a NamedUser', u'url': u'https://api.github.com/gists/2757859', u'created_at': u'2012-05-20T12:14:08Z', u'updated_at': u'2012-05-20T12:14:08Z', u'comments': 0, u'id': u'2757859', u'html_url': u'https://gist.github.com/2757859', u'user': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'git_pull_url': u'git://gist.github.com/2757859.git', u'git_push_url': u'git@gist.github.com:2757859.git', u'public': True}} ) ### @todo
        self.assertEqual( event.public, True )
        self.assertEqual( event.repo.name, "/" ) # WTF
        self.assertEqual( event.type, "GistEvent" )
        self.assertEqual( event.url, None )

    def testOrganizations( self ):
        org = self.user.get_orgs()[ 0 ]
        self.assertEqual( org.login, "BeaverSoftware" )

    def testPublicEvents( self ):
        event = self.user.get_public_events()[ 0 ]
        self.assertEqual( event.actor.login, "jacquev6" )
        self.assertEqual( event.commit_id, None )
        self.assertEqual( event.created_at, "2012-05-20T12:14:09Z" )
        self.assertEqual( event.event, None )
        self.assertEqual( event.id, "1553915048" )
        self.assertEqual( event.issue, None )
        self.assertEqual( event.org, None )
        self.assertEqual( event.payload,  {u'action': u'create', u'gist': {u'files': {}, u'description': u'Gist created by PyGithub on a NamedUser', u'url': u'https://api.github.com/gists/2757859', u'created_at': u'2012-05-20T12:14:08Z', u'updated_at': u'2012-05-20T12:14:08Z', u'comments': 0, u'id': u'2757859', u'html_url': u'https://gist.github.com/2757859', u'user': {u'url': u'https://api.github.com/users/jacquev6', u'login': u'jacquev6', u'avatar_url': u'https://secure.gravatar.com/avatar/b68de5ae38616c296fa345d2b9df2225?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 327146, u'gravatar_id': u'b68de5ae38616c296fa345d2b9df2225'}, u'git_pull_url': u'git://gist.github.com/2757859.git', u'git_push_url': u'git@gist.github.com:2757859.git', u'public': True}} ) ### @todo
        self.assertEqual( event.public, True )
        self.assertEqual( event.repo.name, "/" ) # WTF
        self.assertEqual( event.type, "GistEvent" )
        self.assertEqual( event.url, None )

    def testPublicReceivedEvents( self ):
        event = self.user.get_public_received_events()[ 0 ]
        self.assertEqual( event.actor.login, "cherryboss" )
        self.assertEqual( event.commit_id, None )
        self.assertEqual( event.created_at, "2012-05-20T12:29:18Z" )
        self.assertEqual( event.event, None )
        self.assertEqual( event.id, "1553916447" )
        self.assertEqual( event.issue, None )
        self.assertEqual( event.org.login, "github" )
        self.assertEqual( event.payload,   {u'comment': {u'body': u'+1', u'url': u'https://api.github.com/repos/github/markup/issues/comments/5808535', u'created_at': u'2012-05-20T12:29:17Z', u'updated_at': u'2012-05-20T12:29:17Z', u'user': {u'url': u'https://api.github.com/users/cherryboss', u'login': u'cherryboss', u'avatar_url': u'https://secure.gravatar.com/avatar/b3cb2e7b64cad46d1cd6e5d3294c12cc?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 1078894, u'gravatar_id': u'b3cb2e7b64cad46d1cd6e5d3294c12cc'}, u'id': 5808535}, u'action': u'created', u'issue': {u'body': u"Hello, I've created support for great Texy! text-to-HTML formatter and converter library (http://texy.info, http://github.com/dg/texy).\r\n\r\nHere's my implementation branch: https://github.com/smasty/markup/tree/texy", u'labels': [], u'title': u'[new markup] Texy! formatter support', u'url': u'https://api.github.com/repos/github/markup/issues/34', u'created_at': u'2011-01-21T16:04:58Z', u'milestone': None, u'number': 34, u'comments': 23, u'updated_at': u'2012-05-20T12:29:17Z', u'assignee': None, u'html_url': u'https://github.com/github/markup/issues/34', u'state': u'open', u'user': {u'url': u'https://api.github.com/users/smasty', u'login': u'smasty', u'avatar_url': u'https://secure.gravatar.com/avatar/c27f2f0deb68f04a58db7b7254df893b?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 218524, u'gravatar_id': u'c27f2f0deb68f04a58db7b7254df893b'}, u'pull_request': {u'diff_url': u'https://github.com/github/markup/pull/34.diff', u'patch_url': u'https://github.com/github/markup/pull/34.patch', u'html_url': u'https://github.com/github/markup/pull/34'}, u'closed_at': None, u'id': 541804}} ) ### @todo
        self.assertEqual( event.public, True )
        self.assertEqual( event.repo.name, "github/markup" ) # WTF
        self.assertEqual( event.type, "IssueCommentEvent" )
        self.assertEqual( event.url, None )

    def testReceivedEvents( self ):
        event = self.user.get_received_events()[ 0 ]
        self.assertEqual( event.actor.login, "cherryboss" )
        self.assertEqual( event.commit_id, None )
        self.assertEqual( event.created_at, "2012-05-20T12:29:18Z" )
        self.assertEqual( event.event, None )
        self.assertEqual( event.id, "1553916447" )
        self.assertEqual( event.issue, None )
        self.assertEqual( event.org.login, "github" )
        self.assertEqual( event.payload,   {u'comment': {u'body': u'+1', u'url': u'https://api.github.com/repos/github/markup/issues/comments/5808535', u'created_at': u'2012-05-20T12:29:17Z', u'updated_at': u'2012-05-20T12:29:17Z', u'user': {u'url': u'https://api.github.com/users/cherryboss', u'login': u'cherryboss', u'avatar_url': u'https://secure.gravatar.com/avatar/b3cb2e7b64cad46d1cd6e5d3294c12cc?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 1078894, u'gravatar_id': u'b3cb2e7b64cad46d1cd6e5d3294c12cc'}, u'id': 5808535}, u'action': u'created', u'issue': {u'body': u"Hello, I've created support for great Texy! text-to-HTML formatter and converter library (http://texy.info, http://github.com/dg/texy).\r\n\r\nHere's my implementation branch: https://github.com/smasty/markup/tree/texy", u'labels': [], u'title': u'[new markup] Texy! formatter support', u'url': u'https://api.github.com/repos/github/markup/issues/34', u'created_at': u'2011-01-21T16:04:58Z', u'milestone': None, u'number': 34, u'comments': 23, u'updated_at': u'2012-05-20T12:29:17Z', u'assignee': None, u'html_url': u'https://github.com/github/markup/issues/34', u'state': u'open', u'user': {u'url': u'https://api.github.com/users/smasty', u'login': u'smasty', u'avatar_url': u'https://secure.gravatar.com/avatar/c27f2f0deb68f04a58db7b7254df893b?d=https://a248.e.akamai.net/assets.github.com%2Fimages%2Fgravatars%2Fgravatar-140.png', u'id': 218524, u'gravatar_id': u'c27f2f0deb68f04a58db7b7254df893b'}, u'pull_request': {u'diff_url': u'https://github.com/github/markup/pull/34.diff', u'patch_url': u'https://github.com/github/markup/pull/34.patch', u'html_url': u'https://github.com/github/markup/pull/34'}, u'closed_at': None, u'id': 541804}} ) ### @todo
        self.assertEqual( event.public, True )
        self.assertEqual( event.repo.name, "github/markup" ) # WTF
        self.assertEqual( event.type, "IssueCommentEvent" )
        self.assertEqual( event.url, None )

    def testGetRepo( self ):
        repo = self.user.get_repo( "PyGithub" )
        self.assertEqual( repo.description, "Python library implementing the full Github API v3" )

    def testGetRepos( self ):
        repo = self.user.get_repos()[ 0 ]
        self.assertEqual( repo.name, "TestPyGithub" )

    def testGetWatched( self ):
        repo = self.user.get_watched()[ 0 ]
        self.assertEqual( repo.name, "git" )
