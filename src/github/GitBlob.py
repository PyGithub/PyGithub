# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class GitBlob( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__completed = completion != LazyCompletion
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
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "content", "encoding", "sha", "size", "url", ]
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "content" in attributes and attributes[ "content" ] is not None:
            assert isinstance( attributes[ "content" ], ( str, unicode ) )
            self.__content = attributes[ "content" ]
        if "encoding" in attributes and attributes[ "encoding" ] is not None:
            assert isinstance( attributes[ "encoding" ], ( str, unicode ) )
            self.__encoding = attributes[ "encoding" ]
        if "sha" in attributes and attributes[ "sha" ] is not None:
            assert isinstance( attributes[ "sha" ], ( str, unicode ) )
            self.__sha = attributes[ "sha" ]
        if "size" in attributes and attributes[ "size" ] is not None:
            assert isinstance( attributes[ "size" ], int )
            self.__size = attributes[ "size" ]
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
