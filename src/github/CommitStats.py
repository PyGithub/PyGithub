# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class CommitStats( object ):
    def __init__( self, requester, attributes, completion ):
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
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "additions" in attributes and attributes[ "additions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "additions" ], int )
            self.__additions = attributes[ "additions" ]
        if "deletions" in attributes and attributes[ "deletions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "deletions" ], int )
            self.__deletions = attributes[ "deletions" ]
        if "total" in attributes and attributes[ "total" ] is not None: # pragma no branch
            assert isinstance( attributes[ "total" ], int )
            self.__total = attributes[ "total" ]
