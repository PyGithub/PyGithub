# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
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

    @property
    def commit( self ):
        return self.__commit

    @property
    def name( self ):
        return self.__name

    @property
    def tarball_url( self ):
        return self.__tarball_url

    @property
    def zipball_url( self ):
        return self.__zipball_url

    def __initAttributes( self ):
        self.__commit = None
        self.__name = None
        self.__tarball_url = None
        self.__zipball_url = None

    def __useAttributes( self, attributes ):
         #@todo No need to check if attribute is in attributes when attribute is mandatory
        if "commit" in attributes and attributes[ "commit" ] is not None:
            assert isinstance( attributes[ "commit" ], dict )
            self.__commit = Commit.Commit( self.__requester, attributes[ "commit" ], lazy = True )
        if "name" in attributes and attributes[ "name" ] is not None:
            self.__name = attributes[ "name" ]
        if "tarball_url" in attributes and attributes[ "tarball_url" ] is not None:
            self.__tarball_url = attributes[ "tarball_url" ]
        if "zipball_url" in attributes and attributes[ "zipball_url" ] is not None:
            self.__zipball_url = attributes[ "zipball_url" ]
