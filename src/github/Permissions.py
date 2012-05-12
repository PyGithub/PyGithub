# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class Permissions( object ):
    def __init__( self, requester, attributes, lazy ):
        self.__requester = requester
        self.__completed = False
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
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "admin", "pull", "push", ]
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "admin" in attributes and attributes[ "admin" ] is not None:
            assert isinstance( attributes[ "admin" ], bool )
            self.__admin = attributes[ "admin" ]
        if "pull" in attributes and attributes[ "pull" ] is not None:
            assert isinstance( attributes[ "pull" ], bool )
            self.__pull = attributes[ "pull" ]
        if "push" in attributes and attributes[ "push" ] is not None:
            assert isinstance( attributes[ "push" ], bool )
            self.__push = attributes[ "push" ]
