import Framework

class Authorization( Framework.TestCase ):
    def testCreateWithoutArguments( self ):
        authorization = self.g.get_user().create_authorization()
        self.assertEqual( authorization.id, 372259 )

    def testCreateWithAllArguments( self ):
        authorization = self.g.get_user().create_authorization( [ "repo" ], "Note created by PyGithub", "http://vincent-jacques.net/PyGithub" )
        self.assertEqual( authorization.id, 372294 )

    def testAttributes( self ):
        authorization = self.g.get_user().get_authorization( 372259 )
        self.assertEqual( authorization.app, {u'url': u'http://developer.github.com/v3/oauth/#oauth-authorizations-api', u'name': u'GitHub API'} ) ### @todo
        self.assertEqual( authorization.created_at, "2012-05-22T18:03:17Z" )
        self.assertEqual( authorization.id, 372259 )
        self.assertEqual( authorization.note, None )
        self.assertEqual( authorization.note_url, None )
        self.assertEqual( authorization.scopes, [] )
        self.assertEqual( authorization.token, "82459c4500086f8f0cc67d2936c17d1e27ad1c33" )
        self.assertEqual( authorization.updated_at, "2012-05-22T18:03:17Z" )
        self.assertEqual( authorization.url, "https://api.github.com/authorizations/372259" )

    def testEdit( self ):
        authorization = self.g.get_user().get_authorization( 372259 )
        authorization.edit()
        self.assertEqual( authorization.scopes, [] )
        authorization.edit( scopes = [ "user" ] )
        self.assertEqual( authorization.scopes, [ "user" ] )
        authorization.edit( add_scopes = [ "repo" ] )
        self.assertEqual( authorization.scopes, [ "user", "repo" ] )
        authorization.edit( remove_scopes = [ "repo" ] )
        self.assertEqual( authorization.scopes, [ "user" ] )
        self.assertEqual( authorization.note, None )
        self.assertEqual( authorization.note_url, None )
        authorization.edit( note = "Note created by PyGithub", note_url = "http://vincent-jacques.net/PyGithub" )
        self.assertEqual( authorization.note, "Note created by PyGithub" )
        self.assertEqual( authorization.note_url, "http://vincent-jacques.net/PyGithub" )

    def testDelete( self ):
        authorization = self.g.get_user().get_authorization( 372259 )
        authorization.delete()
