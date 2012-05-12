# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import GitAuthor
import GitObject
# This allows None as a valid value for an optional parameter

class DefaultValueForOptionalParametersType:
    pass
DefaultValueForOptionalParameters = DefaultValueForOptionalParametersType()

class GitTag( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
        self.__initAttributes()
        self.__useAttributes( attributes )
        if not lazy:
            self.__complete()

    @property
    def message( self ):
        self.__completeIfNeeded( self.__message )
        return self.__message

    @property
    def object( self ):
        self.__completeIfNeeded( self.__object )
        return self.__object

    @property
    def sha( self ):
        self.__completeIfNeeded( self.__sha )
        return self.__sha

    @property
    def tag( self ):
        self.__completeIfNeeded( self.__tag )
        return self.__tag

    @property
    def tagger( self ):
        self.__completeIfNeeded( self.__tagger )
        return self.__tagger

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    def __initAttributes( self ):
        self.__message = None
        self.__object = None
        self.__sha = None
        self.__tag = None
        self.__tagger = None
        self.__url = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete()

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
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "message", "object", "sha", "tag", "tagger", "url", ]
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "message" in attributes and attributes[ "message" ] is not None:
            assert isinstance( attributes[ "message" ], ( str, unicode ) )
            self.__message = attributes[ "message" ]
        if "object" in attributes and attributes[ "object" ] is not None:
            assert isinstance( attributes[ "object" ], dict )
            self.__object = GitObject.GitObject( self.__requester, attributes[ "object" ], lazy = True )
        if "sha" in attributes and attributes[ "sha" ] is not None:
            assert isinstance( attributes[ "sha" ], ( str, unicode ) )
            self.__sha = attributes[ "sha" ]
        if "tag" in attributes and attributes[ "tag" ] is not None:
            assert isinstance( attributes[ "tag" ], ( str, unicode ) )
            self.__tag = attributes[ "tag" ]
        if "tagger" in attributes and attributes[ "tagger" ] is not None:
            assert isinstance( attributes[ "tagger" ], dict )
            self.__tagger = GitAuthor.GitAuthor( self.__requester, attributes[ "tagger" ], lazy = True )
        if "url" in attributes and attributes[ "url" ] is not None:
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
