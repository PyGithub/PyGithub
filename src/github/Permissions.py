# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
import GithubException
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters

class Permissions( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def admin( self ):
        return self.__admin

    @property
    def pull( self ):
        return self.__pull

    @property
    def push( self ):
        return self.__push

    def __initAttributes( self ):
        self.__admin = None
        self.__pull = None
        self.__push = None

    def __useAttributes( self, attributes ):
        if "admin" in attributes and attributes[ "admin" ] is not None: # pragma no branch
            assert isinstance( attributes[ "admin" ], bool ), attributes[ "admin" ]
            self.__admin = attributes[ "admin" ]
        if "pull" in attributes and attributes[ "pull" ] is not None: # pragma no branch
            assert isinstance( attributes[ "pull" ], bool ), attributes[ "pull" ]
            self.__pull = attributes[ "pull" ]
        if "push" in attributes and attributes[ "push" ] is not None: # pragma no branch
            assert isinstance( attributes[ "push" ], bool ), attributes[ "push" ]
            self.__push = attributes[ "push" ]
