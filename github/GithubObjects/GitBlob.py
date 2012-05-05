# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class GitBlob( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def content( self ):
        self.__completeIfNeeded( self.__content )
        return self.__content

    @property
    def encoding( self ):
        self.__completeIfNeeded( self.__encoding )
        return self.__encoding

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def size( self ):
        self.__completeIfNeeded( self.__size )
        return self.__size

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__content = None
        self.__encoding = None
        self.__sha = None
        self.__size = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

    # @todo Do not generate __complete if type has no url attribute
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
         #@todo No need to check if attribute is in attributes when attribute is mandatory
        if "content" in attributes:
            self.__content = attributes[ "content" ]
        if "encoding" in attributes:
            self.__encoding = attributes[ "encoding" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "size" in attributes:
            self.__size = attributes[ "size" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
