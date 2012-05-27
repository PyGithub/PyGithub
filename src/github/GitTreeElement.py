# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class GitTreeElement( object ):
    def __init__( self, requester, attributes, completion ):
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
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "mode", "path", "sha", "size", "type", "url", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "mode" in attributes and attributes[ "mode" ] is not None: # pragma no branch
            assert isinstance( attributes[ "mode" ], ( str, unicode ) )
            self.__mode = attributes[ "mode" ]
        if "path" in attributes and attributes[ "path" ] is not None: # pragma no branch
            assert isinstance( attributes[ "path" ], ( str, unicode ) )
            self.__path = attributes[ "path" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) )
            self.__sha = attributes[ "sha" ]
        if "size" in attributes and attributes[ "size" ] is not None: # pragma no branch
            assert isinstance( attributes[ "size" ], int )
            self.__size = attributes[ "size" ]
        if "type" in attributes and attributes[ "type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "type" ], ( str, unicode ) )
            self.__type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
