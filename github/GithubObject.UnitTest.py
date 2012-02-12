import unittest
import MockMockMock

from GithubObject import *

class GithubObjectTestCase( unittest.TestCase ):
    def testDuplicatedAttributeInOnePolicy( self ):
        with self.assertRaises( BadGithubObjectException ):
            GithubObject( "", SimpleScalarAttributes( "a", "a" ) )

    def testDuplicatedAttributeInTwoPolicies( self ):
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

    def expectDelete( self, url ):
        return self.g.expect.rawRequest( "DELETE", url )

class GithubObjectWithOnlySimpleScalarAttributes( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
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
        self.assertRaises( AttributeError, lambda: self.o.foobar )

    def testNonLazyConstruction( self ):
        self.expectGet( "/test" ).andReturn( { "a2": 2, "a3": 3 } )
        o = self.GithubTestObject( self.g.object, {}, lazy = False )
        self.g.tearDown()
        self.assertEqual( o.a1, None )
        self.assertEqual( o.a2, 2 )
        self.assertEqual( o.a3, 3 )
        self.assertEqual( o.a4, None )

class GithubObjectWithOtherBaseUrl( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/other/" + str( obj.a1 ) ),
        SimpleScalarAttributes( "a1", "a2", "a3", "a4" )
    )

    def testCompletion( self ):
        self.expectGet( "/other/1" ).andReturn( { "a2": 22, "a3": 3 } )
        self.assertEqual( self.o.a3, 3 )

class EditableGithubObject( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        SimpleScalarAttributes( "a1", "a2", "a3", "a4" ),
        Editable( [ "a1" ], [ "a2", "a4" ] ),
    )

    def testEditWithoutArgument( self ):
        with self.assertRaises( TypeError ):
            self.o.edit()

    def testEditWithSillyArgument( self ):
        with self.assertRaises( TypeError ):
            self.o.edit( foobar = 42 )

    def testEditWithOneKeywordArgument( self ):
        self.expectPatch( "/test", { "a1": 11 } ).andReturn( {} )
        self.o.edit( a1 = 11 )

    def testEditWithTwoKeywordArguments( self ):
        self.expectPatch( "/test", { "a1": 11, "a2": 22 } ).andReturn( {} )
        self.o.edit( a1 = 11, a2 = 22 )

    def testEditWithTwoKeywordArgumentsSkipingFirstOptionalArgument( self ):
        self.expectPatch( "/test", { "a1": 11, "a4": 44 } ).andReturn( {} )
        self.o.edit( a1 = 11, a4 = 44 )

    def testEditWithThreeKeywordArguments( self ):
        self.expectPatch( "/test", { "a1": 11, "a2": 22, "a4": 44 } ).andReturn( {} )
        self.o.edit( a1 = 11, a4 = 44, a2 = 22 )

    def testEditWithOnePositionalArgument( self ):
        self.expectPatch( "/test", { "a1": 11 } ).andReturn( {} )
        self.o.edit( 11 )

    def testEditWithTwoPositionalArguments( self ):
        self.expectPatch( "/test", { "a1": 11, "a2": 22 } ).andReturn( {} )
        self.o.edit( 11, 22 )

    def testEditWithThreePositionalArguments( self ):
        self.expectPatch( "/test", { "a1": 11, "a2": 22, "a4": 44 } ).andReturn( {} )
        self.o.edit( 11, 22, 44 )

    def testEditWithMixedArguments_1( self ):
        self.expectPatch( "/test", { "a1": 11, "a2": 22 } ).andReturn( {} )
        self.o.edit( 11, a2 = 22 )

    def testEditWithMixedArguments_2( self ):
        self.expectPatch( "/test", { "a1": 11, "a2": 22, "a4": 44 } ).andReturn( {} )
        self.o.edit( 11, a2 = 22, a4 = 44 )

    def testEditWithMixedArguments_3( self ):
        self.expectPatch( "/test", { "a1": 11, "a2": 22, "a4": 44 } ).andReturn( {} )
        self.o.edit( 11, 22, a4 = 44 )

    def testAcknoledgeUpdatesOfAttributes( self ):
        self.expectPatch( "/test", { "a1": 11 } ).andReturn( { "a2": 22, "a3": 3 } )
        self.o.edit( a1 = 11 )
        self.assertEqual( self.o.a1, 1 )
        self.assertEqual( self.o.a2, 22 )
        self.assertEqual( self.o.a3, 3 )
        self.expectGet( "/test" ).andReturn( {} )
        self.assertEqual( self.o.a4, None )

class DeletableGithubObject( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        SimpleScalarAttributes( "a1", "a2", "a3", "a4" ),
        Deletable(),
    )

    def testDelete( self ):
        self.expectDelete( "/test" )
        self.o.delete()

unittest.main()
