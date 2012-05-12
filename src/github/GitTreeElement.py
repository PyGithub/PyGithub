# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class GitTreeElement( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def mode( self ):
        self.__completeIfNeeded( self.__mode )
        return self.__mode

    @property
    def path( self ):
        self.__completeIfNeeded( self.__path )
        return self.__path

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def size( self ):
        self.__completeIfNeeded( self.__size )
        return self.__size

    @property
    def type( self ):
        self.__completeIfNeeded( self.__type )
        return self.__type

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__mode = None
        self.__path = None
        self.__sha = None
        self.__size = None
        self.__type = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    def __complete( self ):
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "mode", "path", "sha", "size", "type", "url", ]
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "mode" in attributes and attributes[ "mode" ] is not None:
            assert isinstance( attributes[ "mode" ], ( str, unicode ) )
            self.__mode = attributes[ "mode" ]
        if "path" in attributes and attributes[ "path" ] is not None:
            assert isinstance( attributes[ "path" ], ( str, unicode ) )
            self.__path = attributes[ "path" ]
        if "sha" in attributes and attributes[ "sha" ] is not None:
            assert isinstance( attributes[ "sha" ], ( str, unicode ) )
            self.__sha = attributes[ "sha" ]
        if "size" in attributes and attributes[ "size" ] is not None:
            assert isinstance( attributes[ "size" ], int )
            self.__size = attributes[ "size" ]
        if "type" in attributes and attributes[ "type" ] is not None:
            assert isinstance( attributes[ "type" ], ( str, unicode ) )
            self.__type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
