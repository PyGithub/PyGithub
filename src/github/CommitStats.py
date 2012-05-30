# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import GithubException
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters

class CommitStats( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def additions( self ):
        return self.__additions

    @property
    def deletions( self ):
        return self.__deletions

    @property
    def total( self ):
        return self.__total

    def __initAttributes( self ):
        self.__additions = None
        self.__deletions = None
        self.__total = None

    def __useAttributes( self, attributes ):
        if "additions" in attributes and attributes[ "additions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "additions" ], int ), attributes[ "additions" ]
            self.__additions = attributes[ "additions" ]
        if "deletions" in attributes and attributes[ "deletions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "deletions" ], int ), attributes[ "deletions" ]
            self.__deletions = attributes[ "deletions" ]
        if "total" in attributes and attributes[ "total" ] is not None: # pragma no branch
            assert isinstance( attributes[ "total" ], int ), attributes[ "total" ]
            self.__total = attributes[ "total" ]
