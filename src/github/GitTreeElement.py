# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import GithubException
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters

class GitTreeElement( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def mode( self ):
        return self.__mode

    @property
    def path( self ):
        return self.__path

    @property
    def sha( self ):
        return self.__sha

    @property
    def size( self ):
        return self.__size

    @property
    def type( self ):
        return self.__type

    @property
    def url( self ):
        return self.__url

    def __initAttributes( self ):
        self.__mode = None
        self.__path = None
        self.__sha = None
        self.__size = None
        self.__type = None
        self.__url = None

    def __useAttributes( self, attributes ):
        if "mode" in attributes and attributes[ "mode" ] is not None: # pragma no branch
            assert isinstance( attributes[ "mode" ], ( str, unicode ) ), attributes[ "mode" ]
            self.__mode = attributes[ "mode" ]
        if "path" in attributes and attributes[ "path" ] is not None: # pragma no branch
            assert isinstance( attributes[ "path" ], ( str, unicode ) ), attributes[ "path" ]
            self.__path = attributes[ "path" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self.__sha = attributes[ "sha" ]
        if "size" in attributes and attributes[ "size" ] is not None: # pragma no branch
            assert isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self.__size = attributes[ "size" ]
        if "type" in attributes and attributes[ "type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self.__type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
