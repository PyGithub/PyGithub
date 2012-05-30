# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class GitBlob( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def content( self ):
        return self.__content

    @property
    def encoding( self ):
        return self.__encoding

    @property
    def sha( self ):
        return self.__sha

    @property
    def size( self ):
        return self.__size

    @property
    def url( self ):
        return self.__url

    def __initAttributes( self ):
        self.__content = None
        self.__encoding = None
        self.__sha = None
        self.__size = None
        self.__url = None

    def __useAttributes( self, attributes ):
        if "content" in attributes and attributes[ "content" ] is not None: # pragma no branch
            assert isinstance( attributes[ "content" ], ( str, unicode ) ), attributes[ "content" ]
            self.__content = attributes[ "content" ]
        if "encoding" in attributes and attributes[ "encoding" ] is not None: # pragma no branch
            assert isinstance( attributes[ "encoding" ], ( str, unicode ) ), attributes[ "encoding" ]
            self.__encoding = attributes[ "encoding" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self.__sha = attributes[ "sha" ]
        if "size" in attributes and attributes[ "size" ] is not None: # pragma no branch
            assert isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self.__size = attributes[ "size" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
