import unittest
import MockMockMock

from GithubObject import BadGithubObjectException, GithubObject, SimpleScalarAttributes

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

class GithubObjectWithOnlySimpleAttributes( TestCaseWithGithubTestObject ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        SimpleScalarAttributes( "a1", "a2", "a3", "a4" )
    )

    def testConstruction( self ):
        pass # Everything is done in setUp/tearDown

    def testCompletion( self ):
        # A GithubObject:
        # - knows the attributes given to its constructor
        self.assertEqual( self.o.a1, 1 )
        self.assertEqual( self.o.a2, 2 )

    def testUnknownAttribute( self ):
        # A GithubObject:
        # - does not have silly attributes
        self.assertRaises( AttributeError, lambda: self.o.foobar )
unittest.main()
