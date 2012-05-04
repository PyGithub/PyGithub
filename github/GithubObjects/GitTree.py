# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class GitTree( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def recursive( self ):
        self.__completeIfNeeded( self.__recursive )
        return self.__recursive

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def tree( self ):
        self.__completeIfNeeded( self.__tree )
        return self.__tree

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__recursive = None
        self.__sha = None
        self.__tree = None
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
        if "recursive" in attributes:
            self.__recursive = attributes[ "recursive" ]
        if "sha" in attributes:
            self.__sha = attributes[ "sha" ]
        if "tree" in attributes:
            self.__tree = attributes[ "tree" ]
        if "url" in attributes:
            self.__url = attributes[ "url" ]
