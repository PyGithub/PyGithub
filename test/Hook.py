import Framework

class Hook( Framework.TestCase ):
    def setUp( self ):
        Framework.TestCase.setUp( self )
        self.hook = self.g.get_user().get_repo( "PyGithub" ).get_hook( 257993 )

    def testEditWithMinimalParameters( self ):
        self.hook.edit( "web", { "url": "http://foobar.com/hook" } )
        self.assertEqual( self.hook.config, { "url": "http://foobar.com/hook" } )
        self.assertEqual( self.hook.updated_at, "2012-05-19T05:08:16Z" )

    def testDelete( self ):
        self.hook.delete()

    def testTest( self ):
        self.hook.test() # This does not update attributes of hook

    def testEditWithAllParameters( self ):
        self.hook.edit( "web", { "url": "http://foobar.com" }, events = [ "fork", "push" ] )
        self.assertEqual( self.hook.events, [ "fork", "push" ] )
        self.hook.edit( "web", { "url": "http://foobar.com" }, add_events = [ "push" ] )
        self.assertEqual( self.hook.events, [ "fork", "push" ] )
        self.hook.edit( "web", { "url": "http://foobar.com" }, remove_events = [ "fork" ] )
        self.assertEqual( self.hook.events, [ "push" ] )
        self.hook.edit( "web", { "url": "http://foobar.com" }, active = True )
        self.assertEqual( self.hook.active, True )
