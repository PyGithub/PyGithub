# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import GitAuthor
import GitObject

class GitTag( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__completed = completion != LazyCompletion
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
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "message", "object", "sha", "tag", "tagger", "url", ]
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "message" in attributes and attributes[ "message" ] is not None:
            assert isinstance( attributes[ "message" ], ( str, unicode ) )
            self.__message = attributes[ "message" ]
        if "object" in attributes and attributes[ "object" ] is not None:
            assert isinstance( attributes[ "object" ], dict )
            self.__object = GitObject.GitObject( self.__requester, attributes[ "object" ], completion = LazyCompletion )
        if "sha" in attributes and attributes[ "sha" ] is not None:
            assert isinstance( attributes[ "sha" ], ( str, unicode ) )
            self.__sha = attributes[ "sha" ]
        if "tag" in attributes and attributes[ "tag" ] is not None:
            assert isinstance( attributes[ "tag" ], ( str, unicode ) )
            self.__tag = attributes[ "tag" ]
        if "tagger" in attributes and attributes[ "tagger" ] is not None:
            assert isinstance( attributes[ "tagger" ], dict )
            self.__tagger = GitAuthor.GitAuthor( self.__requester, attributes[ "tagger" ], completion = LazyCompletion )
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
