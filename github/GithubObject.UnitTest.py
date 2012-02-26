import unittest
import MockMockMock

from GithubObject import *

class GithubObjectTestCase( unittest.TestCase ):
    def testDuplicatedAttributeInOnePolicy( self ):
        with self.assertRaises( BadGithubObjectException ):
            GithubObject( "", InternalSimpleAttributes( "a", "a" ) )

    def testDuplicatedAttributeInTwoPolicies( self ):
        with self.assertRaises( BadGithubObjectException ):
            GithubObject( "", InternalSimpleAttributes( "a" ), InternalSimpleAttributes( "a" ) )

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

    def expectDataPost( self, url, data ):
        return self.g.expect._dataRequest( "POST", url, None, data )

    def expectDataPatch( self, url, data ):
        return self.g.expect._dataRequest( "PATCH", url, None, data )

    def expectStatusGet( self, url ):
        return self.g.expect._statusRequest( "GET", url, None, None )

    def expectStatusPost( self, url, data ):
        return self.g.expect._statusRequest( "POST", url, None, data )

    def expectStatusPut( self, url, data = None ):
        return self.g.expect._statusRequest( "PUT", url, None, data )

    def expectStatusDelete( self, url, data = None ):
        return self.g.expect._statusRequest( "DELETE", url, None, data )

class GithubObjectWithOnlyInternalSimpleAttributes( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2", "a3", "a4" )
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
        InternalSimpleAttributes( "a1", "a2", "a3", "a4" )
    )

    def testCompletion( self ):
        self.expectDataGet( "/other/1" ).andReturn( { "a2": 22, "a3": 3 } )
        self.assertEqual( self.o.a3, 3 )

class EditableGithubObject( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2", "a3", "a4" ),
        Editable( [ "a1" ], [ "a2", "a4" ] ),
    )

    def testEditWithoutArgument( self ):
        with self.assertRaises( TypeError ):
            self.o.edit()

    def testEditWithoutMandatoryArgument( self ):
        with self.assertRaises( TypeError ):
            self.o.edit( a2 = 2, a4 = 3 )

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

    def testEditWithRepeatedPositionalArgument( self ):
        with self.assertRaises( TypeError ):
            self.o.edit( 11, a1 = 11 )

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
        InternalSimpleAttributes( "a1", "a2", "a3", "a4" ),
        Deletable(),
    )

    def testDelete( self ):
        self.expectStatusDelete( "/test" ).andReturn( 204 )
        self.o.delete()

class GithubObjectWithInternalObjectAttribute( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        InternalSimpleAttributes( "id", "name", "desc" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        InternalObjectAttribute( "a3", ContainedObject )
    )

    def testCompletion( self ):
        self.expectDataGet( "/test" ).andReturn( { "a3": { "id": "id1", "name": "name1" } } )
        self.assertEqual( self.o.a3.id, "id1" )
        self.assertEqual( self.o.a3.name, "name1" )
        self.expectDataGet( "/test/a3s/id1" ).andReturn( { "desc": "desc1" } )
        self.assertEqual( self.o.a3.desc, "desc1" )

    def testCompletionWithNone( self ):
        self.expectDataGet( "/test" ).andReturn( { "a3": None } )
        self.assertIsNone( self.o.a3 )

class GithubObjectWithListGetableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        InternalSimpleAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, ListGetable( [], [ "type" ] ) )
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

class GithubObjectWithElementAddableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        Identity( lambda obj: obj.id ),
        InternalSimpleAttributes( "id", "name" ),
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, ElementAddable() )
    )

    def testAddToList( self ):
        a3ToAdd = self.ContainedObject( self.g.object, { "id": "idAdd", "name": "nameAdd" }, lazy = True )
        self.expectStatusPut( "/test/a3s/idAdd" ).andReturn( 204 )
        self.o.add_to_a3s( a3ToAdd )

class GithubObjectWithElementRemovableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        Identity( lambda obj: obj.id ),
        InternalSimpleAttributes( "id", "name" ),
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, ElementRemovable() )
    )

    def testRemoveFromList( self ):
        a3ToRemove = self.ContainedObject( self.g.object, { "id": "idRemove", "name": "nameRemove" }, lazy = True )
        self.expectStatusDelete( "/test/a3s/idRemove" ).andReturn( 204 )
        self.o.remove_from_a3s( a3ToRemove )

class GithubObjectWithElementHasableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        Identity( lambda obj: obj.id ),
        InternalSimpleAttributes( "id", "name" ),
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, ElementHasable() )
    )

    def testHasInList( self ):
        a3ToQuery = self.ContainedObject( self.g.object, { "id": "idQuery", "name": "nameQuery" }, lazy = True )
        self.expectStatusGet( "/test/a3s/idQuery" ).andReturn( 204 )
        self.assertTrue( self.o.has_in_a3s( a3ToQuery ) )
        self.expectStatusGet( "/test/a3s/idQuery" ).andReturn( 404 )
        self.assertFalse( self.o.has_in_a3s( a3ToQuery ) )

class GithubObjectWithElementCreatableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        Identity( lambda obj: obj.id ),
        InternalSimpleAttributes( "id", "name" ),
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, ElementCreatable( [ "name" ], [ "p1", "p2" ] ) )
    )

    def testCreate( self ):
        self.expectDataPost( "/test/a3s", { "name": "nameCreate" } ).andReturn( { "id": "idCreate" } )
        self.assertEqual( self.o.create_a3( name = "nameCreate" ).id, "idCreate" )

    def testCreateWithOptionalArguments( self ):
        self.expectDataPost( "/test/a3s", { "name": "nameCreate", "p1": 1 } ).andReturn( { "id": "idCreate" } )
        self.assertEqual( self.o.create_a3( name = "nameCreate", p1 = 1 ).id, "idCreate" )
        self.expectDataPost( "/test/a3s", { "name": "nameCreate", "p2": 2 } ).andReturn( { "id": "idCreate" } )
        self.assertEqual( self.o.create_a3( name = "nameCreate", p2 = 2 ).id, "idCreate" )
        self.expectDataPost( "/test/a3s", { "name": "nameCreate", "p1": 1, "p2": 2 } ).andReturn( { "id": "idCreate" } )
        self.assertEqual( self.o.create_a3( name = "nameCreate", p2 = 2, p1 = 1 ).id, "idCreate" )

    def testCreateWithPositionalArguments( self ):
        self.expectDataPost( "/test/a3s", { "name": "nameCreate", "p1": 1 } ).andReturn( { "id": "idCreate" } )
        self.assertEqual( self.o.create_a3( "nameCreate", 1 ).id, "idCreate" )
        self.expectDataPost( "/test/a3s", { "name": "nameCreate", "p2": 2 } ).andReturn( { "id": "idCreate" } )
        self.assertEqual( self.o.create_a3( "nameCreate", p2 = 2 ).id, "idCreate" )
        self.expectDataPost( "/test/a3s", { "name": "nameCreate", "p1": 1, "p2": 2 } ).andReturn( { "id": "idCreate" } )
        self.assertEqual( self.o.create_a3( "nameCreate", 1, 2 ).id, "idCreate" )

    def testCreateWithSillyArgument( self ):
        self.g.expect._dataRequest.andReturn( None )
        with self.assertRaises( TypeError ):
            self.o.create_a3( foobar = 42 )

class GithubObjectWithSeveralElementsAddableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        Identity( lambda obj: obj.id ),
        InternalSimpleAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, SeveralElementsAddable() )
    )

    def testAddToList( self ):
        self.expectStatusPost( "/test/a3s", [ "id1", "id2" ] )
        self.o.add_to_a3s( self.ContainedObject( self.g, { "id": "id1" }, lazy = True ), self.ContainedObject( self.g, { "id": "id2" }, lazy = True ) )

class GithubObjectWithListSetableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        Identity( lambda obj: obj.id ),
        InternalSimpleAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, ListSetable() )
    )

    def testSetList( self ):
        self.expectStatusPut( "/test/a3s", [ "id1", "id2" ] )
        self.o.set_a3s( self.ContainedObject( self.g, { "id": "id1" }, lazy = True ), self.ContainedObject( self.g, { "id": "id2" }, lazy = True ) )

class GithubObjectWithListDeletableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        InternalSimpleAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, ListDeletable() )
    )

    def testGetList( self ):
        self.expectStatusDelete( "/test/a3s" )
        self.o.delete_a3s()

class GithubObjectWithElementGetableExternalListOfObjects( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        InternalSimpleAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfObjects( "a3s", "a3", ContainedObject, ElementGetable( [ "id" ], [] ) )
    )

    def testGetList( self ):
        self.expectDataGet( "/test/a3s/idGet" ).andReturn( { "id": "idGet" } )
        self.assertEqual( self.o.get_a3( "idGet" ).id, "idGet" )

class GithubObjectWithMultiCapacityExternalListOfSimpleTypes( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalListOfSimpleTypes( "a3s", "a3", "",
            ListGetable( [], [] ),
            SeveralElementsAddable(),
            SeveralElementsRemovable(),
        )
    )

    def testGetList( self ):
        self.expectDataGet( "/test/a3s", {} ).andReturn( [ "a", "b", "c" ] )
        a3s = self.o.get_a3s()
        self.assertEqual( len( a3s ), 3 )
        self.assertEqual( a3s[ 0 ], "a" )

    def testAddToList( self ):
        self.expectStatusPost( "/test/a3s", [ "a", "b", "c" ] ).andReturn( 204 )
        a3s = self.o.add_to_a3s( "a", "b", "c" )

    def testDeleteFromList( self ):
        self.expectStatusDelete( "/test/a3s", [ "a", "b", "c" ] ).andReturn( 204 )
        a3s = self.o.remove_from_a3s( "a", "b", "c" )

class GithubObjectWithExternalSimpleAttribute( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        ExternalSimpleAttribute( "a3", "" )
    )

    def testGetAttribute( self ):
        self.expectDataGet( "/test/a3" ).andReturn( 72 )
        self.assertEqual( self.o.get_a3(), 72 )

def myCallable( obj, mock, arg ):
    return mock.call( arg )
class GithubObjectWithMethodFromCallable( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a1", "a2" ),
        MethodFromCallable( "myMethod", [ "mock", "arg" ], [], myCallable, SimpleTypePolicy( None ) )
    )

    def testCallMethod( self ):
        mock = MockMockMock.Mock( "myCallable" )
        mock.expect.call( 42 ).andReturn( 72 )
        self.assertEqual( self.o.myMethod( mock.object, 42 ), 72 )
        mock.tearDown()

class GithubObjectWithSeveralInternalSimpleAttributesAndInternalObjectAttributes( TestCaseWithGithubTestObject ):
    ContainedObject = GithubObject(
        "ContainedObject",
        BaseUrl( lambda obj: "/test/a3s/" + obj.id ),
        InternalSimpleAttributes( "id", "name" )
    )

    GithubTestObject = GithubObject(
        "GithubTestObject",
        BaseUrl( lambda obj: "/test" ),
        InternalSimpleAttributes( "a2", "a4" ),
        InternalSimpleAttributes( "a1", "a3" ),
        InternalObjectAttribute( "a5", ContainedObject ),
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
