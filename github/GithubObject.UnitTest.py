import unittest
import MockMockMock

from GithubObject import GithubObject, SimpleScalarAttributes

class TestCase( unittest.TestCase ):
    def setUp( self ):
        unittest.TestCase.setUp( self )
        self.g = MockMockMock.Mock( "github" )
        self.o = self.GithubTestObject( self.g.object, { "a1": 1, "a2": 2 }, lazy = True )

    def tearDown( self ):
        self.g.tearDown()
        unittest.TestCase.tearDown( self )

class GithubObjectWithOnlySimpleAttributes( TestCase ):
    GithubTestObject = GithubObject(
        "GithubTestObject",
        SimpleScalarAttributes( "a1", "a2", "a3", "a4" )
    )

    def testConstruction( self ):
        pass # Everything is done in setUp/tearDown

unittest.main()
