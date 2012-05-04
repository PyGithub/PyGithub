# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import Commit
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class Tag( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def commit( self ):
        self.__completeIfNeeded( self.__commit )
        return self.__commit

    @property
    def name( self ):
        self.__completeIfNeeded( self.__name )
        return self.__name

    @property
    def tarball_url( self ):
        self.__completeIfNeeded( self.__tarball_url )
        return self.__tarball_url

    @property
    def zipball_url( self ):
        self.__completeIfNeeded( self.__zipball_url )
        return self.__zipball_url

    def __initAttributes( self ):
        self.__commit = None
        self.__name = None
        self.__tarball_url = None
        self.__zipball_url = None

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
        if "commit" in attributes:
            self.__commit = Commit.Commit( self.__requester, attributes[ "commit" ], lazy = True )
        if "name" in attributes:
            self.__name = attributes[ "name" ]
        if "tarball_url" in attributes:
            self.__tarball_url = attributes[ "tarball_url" ]
        if "zipball_url" in attributes:
            self.__zipball_url = attributes[ "zipball_url" ]
