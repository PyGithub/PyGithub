# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import GithubException
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
import Commit

class Tag( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
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
        if "commit" in attributes and attributes[ "commit" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self.__commit = Commit.Commit( self.__requester, attributes[ "commit" ], completed = False )
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self.__name = attributes[ "name" ]
        if "tarball_url" in attributes and attributes[ "tarball_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tarball_url" ], ( str, unicode ) ), attributes[ "tarball_url" ]
            self.__tarball_url = attributes[ "tarball_url" ]
        if "zipball_url" in attributes and attributes[ "zipball_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "zipball_url" ], ( str, unicode ) ), attributes[ "zipball_url" ]
            self.__zipball_url = attributes[ "zipball_url" ]
