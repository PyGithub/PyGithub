import unittest
import MockMockMock

from GithubObject import *

class GithubObjectTestCase( unittest.TestCase ):
    def testDuplicatedAttributeInOnePolicy( self ):
        with self.assertRaises( BadGithubObjectException ):
            GithubObject( "", BasicAttributes( "a", "a" ) )

    def testDuplicatedAttributeInTwoPolicies( self ):
        with self.assertRaises( BadGithubObjectException ):
            GithubObject( "", BasicAttributes( "a" ), BasicAttributes( "a" ) )

class TestCaseWithGithubTestObject( unittest.TestCase ):
    def setUp( self ):
        unittest.TestCase.setUp( self )
        self.g = MockMockMock.Mock( "github" )
        self.o = self.GithubTestObject( self.g.object, { "a1": 1, "a2": 2 }, lazy = True )

    def tearDown( self ):
        self.g.tearDown()
        unittest.TestCase.tearDown( self )

    def expectDataGet( self, url, arguments = None ):
        return self.g.expect._dataRequest( "GET", url, arguments, None )

    def expectStatusPut( self, url ):
        return self.g.expect._statusRequest( "PUT", url, None, None )

    def expectStatusGet( self, url ):
        return self.g.expect._statusRequest( "GET", url, None, None )

    def expectDataPatch( self, url, data ):
        return self.g.expect._dataRequest( "PATCH", url, None, data )

    def expectDataPost( self, url, data ):
        return self.g.expect._dataRequest( "POST", url, None, data )

    def expectStatusDelete( self, url ):
        return self.g.expect._statusRequest( "DELETE", url, None, None )

class GithubObjectWithOnlyBasicAttributes( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2", "a3", "a4" )
    )

    def testInterface( self ):
        self.assertEqual( [ e for e in dir( self.o ) if not e.startswith( "_" ) ], [ "a1", "a2", "a3", "a4"  ] )

    def testCompletion( self ):
        # A GithubObject:
        # - knows the attributes given to its constructor
        self.assertEqual( self.o.a1, 1 )
        self.assertEqual( self.o.a2, 2 )
        # - is completed the first time any unknown attribute is requested
        self.expectDataGet( "/test" ).andReturn( { "a2": 22, "a3": 3 } )
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
        self.expectDataGet( "/test" ).andReturn( { "a2": 2, "a3": 3 } )
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
        BasicAttributes( "a1", "a2", "a3", "a4" )
    )

    def testCompletion( self ):
        self.expectDataGet( "/other/1" ).andReturn( { "a2": 22, "a3": 3 } )
        self.assertEqual( self.o.a3, 3 )

class EditableGithubObject( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2", "a3", "a4" ),
        Editable( [ "a1" ], [ "a2", "a4" ] ),
    )

    def testEditWithoutArgument( self ):
        with self.assertRaises( TypeError ):
            self.o.edit()

    def testEditWithSillyArgument( self ):
        with self.assertRaises( TypeError ):
            self.o.edit( foobar = 42 )

    def testEditWithOneKeywordArgument( self ):
        self.expectDataPatch( "/test", { "a1": 11 } ).andReturn( {} )
        self.o.edit( a1 = 11 )

    def testEditWithTwoKeywordArguments( self ):
        self.expectDataPatch( "/test", { "a1": 11, "a2": 22 } ).andReturn( {} )
        self.o.edit( a1 = 11, a2 = 22 )

    def testEditWithTwoKeywordArgumentsSkipingFirstOptionalArgument( self ):
        self.expectDataPatch( "/test", { "a1": 11, "a4": 44 } ).andReturn( {} )
        self.o.edit( a1 = 11, a4 = 44 )

    def testEditWithThreeKeywordArguments( self ):
        self.expectDataPatch( "/test", { "a1": 11, "a2": 22, "a4": 44 } ).andReturn( {} )
        self.o.edit( a1 = 11, a4 = 44, a2 = 22 )

    def testEditWithOnePositionalArgument( self ):
        self.expectDataPatch( "/test", { "a1": 11 } ).andReturn( {} )
        self.o.edit( 11 )

    def testEditWithTwoPositionalArguments( self ):
        self.expectDataPatch( "/test", { "a1": 11, "a2": 22 } ).andReturn( {} )
        self.o.edit( 11, 22 )

    def testEditWithThreePositionalArguments( self ):
        self.expectDataPatch( "/test", { "a1": 11, "a2": 22, "a4": 44 } ).andReturn( {} )
        self.o.edit( 11, 22, 44 )

    def testEditWithMixedArguments_1( self ):
        self.expectDataPatch( "/test", { "a1": 11, "a2": 22 } ).andReturn( {} )
        self.o.edit( 11, a2 = 22 )

    def testEditWithMixedArguments_2( self ):
        self.expectDataPatch( "/test", { "a1": 11, "a2": 22, "a4": 44 } ).andReturn( {} )
        self.o.edit( 11, a2 = 22, a4 = 44 )

    def testEditWithMixedArguments_3( self ):
        self.expectDataPatch( "/test", { "a1": 11, "a2": 22, "a4": 44 } ).andReturn( {} )
        self.o.edit( 11, 22, a4 = 44 )

    def testAcknoledgeUpdatesOfAttributes( self ):
        self.expectDataPatch( "/test", { "a1": 11 } ).andReturn( { "a2": 22, "a3": 3 } )
        self.o.edit( a1 = 11 )
        self.assertEqual( self.o.a1, 1 )
        self.assertEqual( self.o.a2, 22 )
        self.assertEqual( self.o.a3, 3 )
        self.expectDataGet( "/test" ).andReturn( {} )
        self.assertEqual( self.o.a4, None )

class DeletableGithubObject( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2", "a3", "a4" ),
        Deletable(),
    )

    def testDelete( self ):
        self.expectStatusDelete( "/test" ).andReturn( 204 )
        self.o.delete()

class GithubObjectWithComplexAttribute( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        BasicAttributes( "id", "name", "desc" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2" ),
        ComplexAttribute( "a3", ContainedObject )
    )

    def testCompletion( self ):
        self.expectDataGet( "/test" ).andReturn( { "a3": { "id": "id1", "name": "name1" } } )
        self.assertEqual( self.o.a3.id, "id1" )
        self.assertEqual( self.o.a3.name, "name1" )
        self.expectDataGet( "/test/a3s/id1" ).andReturn( { "desc": "desc1" } )
        self.assertEqual( self.o.a3.desc, "desc1" )

class GithubObjectWithListOfReferences( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        BasicAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2" ),
        ListOfReferences( "a3s", ContainedObject, getParameters = [ "type" ] )
    )

    def testGetList( self ):
        self.expectDataGet( "/test/a3s", {} ).andReturn( [ { "id": "id1" }, { "id": "id2" }, { "id": "id3" } ] )
        a3s = self.o.get_a3s()
        self.assertEqual( len( a3s ), 3 )
        self.assertEqual( a3s[ 0 ].id, "id1" )
        self.expectDataGet( "/test/a3s/id1" ).andReturn( { "name": "name1" } )
        self.assertEqual( a3s[ 0 ].name, "name1" )

    def testGetListWithType( self ):
        self.expectDataGet( "/test/a3s", { "type": "foobar" } ).andReturn( [ { "id": "id1" }, { "id": "id2" }, { "id": "id3" } ] )
        a3s = self.o.get_a3s( "foobar" )
        self.assertEqual( len( a3s ), 3 )

class GithubObjectWithListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        BasicAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2" ),
        ListOfObjects( "a3s", ContainedObject )
    )

    def testGetList( self ):
        self.expectDataGet( "/test/a3s" ).andReturn( [ { "id": "id1" }, { "id": "id2" }, { "id": "id3" } ] )
        a3s = self.o.get_a3s()
        self.assertEqual( len( a3s ), 3 )
        self.assertEqual( a3s[ 0 ].id, "id1" )
        self.expectDataGet( "/test/a3s/id1" ).andReturn( { "name": "name1" } )
        self.assertEqual( a3s[ 0 ].name, "name1" )

class GithubObjectWithModifiableListOfReferences( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        Identity( lambda obj: obj.id ),
        BasicAttributes( "id", "name" ),
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2" ),
        ListOfReferences( "a3s", ContainedObject, addable = True, removable = True, hasable = True )
    )

    def testAddToList( self ):
        a3ToAdd = self.ContainedObject( self.g.object, { "id": "idAdd", "name": "nameAdd" }, lazy = True )
        self.expectStatusPut( "/test/a3s/idAdd" ).andReturn( 204 )
        self.o.add_to_a3s( a3ToAdd )

    def testRemoveFromList( self ):
        a3ToRemove = self.ContainedObject( self.g.object, { "id": "idRemove", "name": "nameRemove" }, lazy = True )
        self.expectStatusDelete( "/test/a3s/idRemove" ).andReturn( 204 )
        self.o.remove_from_a3s( a3ToRemove )

    def testHasInList( self ):
        a3ToQuery = self.ContainedObject( self.g.object, { "id": "idQuery", "name": "nameQuery" }, lazy = True )
        self.expectStatusGet( "/test/a3s/idQuery" ).andReturn( 204 )
        self.assertTrue( self.o.has_in_a3s( a3ToQuery ) )
        self.expectStatusGet( "/test/a3s/idQuery" ).andReturn( 404 )
        self.assertFalse( self.o.has_in_a3s( a3ToQuery ) )

class GithubObjectWithModifiableListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        Identity( lambda obj: obj.id ),
        BasicAttributes( "id", "name" ),
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2" ),
        ListOfObjects( "a3s", ContainedObject, creatable = True )
    )

    def testCreate( self ):
        self.expectDataPost( "/test/a3s", { "name": "nameCreate" } ).andReturn( { "id": "idCreate" } )
        self.assertEqual( self.o.create_a3s( name = "nameCreate" ).id, "idCreate" )

def myCallable( obj, mock, arg ):
    return mock.call( arg )

class GithubObjectWithMethodFromCallable( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a1", "a2" ),
        MethodFromCallable( "myMethod", myCallable )
    )

    def testCallMethod( self ):
        mock = MockMockMock.Mock( "myCallable" )
        mock.expect.call( 42 ).andReturn( 72 )
        self.assertEqual( self.o.myMethod( mock.object, 42 ), 72 )
        mock.tearDown()

class GithubObjectWithSeveralBasicAttributesAndComplexAttributes( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        BasicAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        BasicAttributes( "a2", "a4" ),
        BasicAttributes( "a1", "a3" ),
        ComplexAttribute( "a5", ContainedObject ),
    )

    def testCompletionInOneCall_1( self ):
        self.expectDataGet( "/test" ).andReturn( {} )
        self.assertIsNone( self.o.a3 )
        self.assertIsNone( self.o.a4 )
        self.assertIsNone( self.o.a5 )

    def testCompletionInOneCall_2( self ):
        self.expectDataGet( "/test" ).andReturn( {} )
        self.assertIsNone( self.o.a4 )
        self.assertIsNone( self.o.a3 )
        self.assertIsNone( self.o.a5 )

    def testCompletionInOneCall_3( self ):
        self.expectDataGet( "/test" ).andReturn( {} )
        self.assertIsNone( self.o.a5 )
        self.assertIsNone( self.o.a3 )
        self.assertIsNone( self.o.a4 )

    def testCompletionInOneCall_4( self ):
        self.expectDataGet( "/test" ).andReturn( {} )
        self.assertIsNone( self.o.a5 )
        self.assertIsNone( self.o.a4 )
        self.assertIsNone( self.o.a3 )

unittest.main()
