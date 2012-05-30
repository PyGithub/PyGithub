# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import GithubException
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters

class PullRequestMergeStatus( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def merged( self ):
        return self.__merged

    @property
    def message( self ):
        return self.__message

    @property
    def sha( self ):
        return self.__sha

    def __initAttributes( self ):
        self.__merged = None
        self.__message = None
        self.__sha = None

    def __useAttributes( self, attributes ):
        if "merged" in attributes and attributes[ "merged" ] is not None: # pragma no branch
            assert isinstance( attributes[ "merged" ], bool ), attributes[ "merged" ]
            self.__merged = attributes[ "merged" ]
        if "message" in attributes and attributes[ "message" ] is not None: # pragma no branch
            assert isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self.__message = attributes[ "message" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self.__sha = attributes[ "sha" ]
