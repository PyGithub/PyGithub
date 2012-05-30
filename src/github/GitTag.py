# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import GitAuthor
import GitObject

class GitTag( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def message( self ):
        return self.__message

    @property
    def object( self ):
        return self.__object

    @property
    def sha( self ):
        return self.__sha

    @property
    def tag( self ):
        return self.__tag

    @property
    def tagger( self ):
        return self.__tagger

    @property
    def url( self ):
        return self.__url

    def __initAttributes( self ):
        self.__message = None
        self.__object = None
        self.__sha = None
        self.__tag = None
        self.__tagger = None
        self.__url = None

    def __useAttributes( self, attributes ):
        if "message" in attributes and attributes[ "message" ] is not None: # pragma no branch
            assert isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self.__message = attributes[ "message" ]
        if "object" in attributes and attributes[ "object" ] is not None: # pragma no branch
            assert isinstance( attributes[ "object" ], dict ), attributes[ "object" ]
            self.__object = GitObject.GitObject( self.__requester, attributes[ "object" ], completed = False )
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self.__sha = attributes[ "sha" ]
        if "tag" in attributes and attributes[ "tag" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tag" ], ( str, unicode ) ), attributes[ "tag" ]
            self.__tag = attributes[ "tag" ]
        if "tagger" in attributes and attributes[ "tagger" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tagger" ], dict ), attributes[ "tagger" ]
            self.__tagger = GitAuthor.GitAuthor( self.__requester, attributes[ "tagger" ], completed = False )
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
