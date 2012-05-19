import Framework

class Hook( Framework.TestCaseWithRepo ):
    def testCreateWithMinimalParameters( self ):
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

    def testEditWithMinimalParameters( self ):
        hook = self.repo.get_hook( 257967 )
        hook.edit( "web", { "url": "http://foobar.com/hook" } )
        self.assertEqual( hook.config, { "url": "http://foobar.com/hook" } )
        self.assertEqual( hook.updated_at, "2012-05-19T05:08:16Z" )

    def testDelete( self ):
        hook = self.repo.get_hook( 257967 )
        hook.delete()

    def testCreateWithAllParameters( self ):
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

    def testTest( self ):
        hook = self.repo.get_hook( 257993 )
        hook.test() # This does not update attributes of hook

    def testEditWithAllParameters( self ):
        hook = self.repo.get_hook( 257993 )
        hook.edit( "web", { "url": "http://foobar.com" }, events = [ "fork", "push" ] )
        self.assertEqual( hook.events, [ "fork", "push" ] )
        hook.edit( "web", { "url": "http://foobar.com" }, add_events = [ "push" ] )
        self.assertEqual( hook.events, [ "fork", "push" ] )
        hook.edit( "web", { "url": "http://foobar.com" }, remove_events = [ "fork" ] )
        self.assertEqual( hook.events, [ "push" ] )
        hook.edit( "web", { "url": "http://foobar.com" }, active = True )
        self.assertEqual( hook.active, True )
