import unittest
import MockMockMock

from GithubObject import BadGithubObjectException, GithubObject, SimpleScalarAttributes, Editable

class GithubObjectTestCase( unittest.TestCase ):
    def testDuplicatedAttribute( self ):
        with self.assertRaises( BadGithubObjectException ):
            GithubObject( "", SimpleScalarAttributes( "a", "a" ) )
        with self.assertRaises( BadGithubObjectException ):
            GithubObject( "", SimpleScalarAttributes( "a" ), SimpleScalarAttributes( "a" ) )

class TestCaseWithGithubTestObject( unittest.TestCase ):
    def setUp( self ):
        unittest.TestCase.setUp( self )
        self.g = MockMockMock.Mock( "github" )
        self.o = self.GithubTestObject( self.g.object, { "a1": 1, "a2": 2 }, lazy = True )

    def tearDown( self ):
        self.g.tearDown()
        unittest.TestCase.tearDown( self )

    def expectGet( self, url ):
        return self.g.expect.rawRequest( "GET", url )

    def expectPatch( self, url, data ):
        return self.g.expect.rawRequest( "PATCH", url, data )

class GithubObjectWithOnlySimpleScalarAttributes( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        SimpleScalarAttributes( "a1", "a2", "a3", "a4" )
    )


    def testCompletion( self ):
        # A GithubObject:
        # - knows the attributes given to its constructor
        self.assertEqual( self.o.a1, 1 )
        self.assertEqual( self.o.a2, 2 )
        # - is completed the first time any unknown attribute is requested
        self.expectGet( "/test" ).andReturn( { "a2": 22, "a3": 3 } )
        self.assertEqual( self.o.a3, 3 )
        # - remembers the attributes that were not updated
        self.assertEqual( self.o.a1, 1 )
        # - acknowledges updates of attributes
        self.assertEqual( self.o.a2, 22 )
        # - remembers that some attributes are absent even after an update
        self.assertEqual( self.o.a4, None )

    def testUnknownAttribute( self ):
        # A GithubObject:
        # - does not have silly attributes
        self.assertRaises( AttributeError, lambda: self.o.foobar )

    def testNonLazyConstruction( self ):
        self.expectGet( "/test" ).andReturn( { "a2": 2, "a3": 3 } )
        o = self.GithubTestObject( self.g.object, {}, lazy = False )
        self.g.tearDown()
        self.assertEqual( o.a1, None )
        self.assertEqual( o.a2, 2 )
        self.assertEqual( o.a3, 3 )
        self.assertEqual( o.a4, None )

class EditableGithubObject( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        SimpleScalarAttributes( "a1", "a2", "a3", "a4" ),
        Editable( [ "a1" ], [ "a2", "a4" ] ),
    )

    def testEdit( self ):
        self.expectPatch( "/test", { "a1": 11, "a2": 22 } ).andReturn( {} )
        self.o.edit( a1 = 11, a2 = 22 )

unittest.main()
