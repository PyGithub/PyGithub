# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Commit

class Branch( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def commit( self ):
        return self.__commit

    @property
    def name( self ):
        return self.__name

    def __initAttributes( self ):
        self.__commit = None
        self.__name = None

    def __useAttributes( self, attributes ):
        if "commit" in attributes and attributes[ "commit" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self.__commit = Commit.Commit( self.__requester, attributes[ "commit" ], completion = LazyCompletion )
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self.__name = attributes[ "name" ]
