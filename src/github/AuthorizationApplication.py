# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class AuthorizationApplication( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def name( self ):
        return self.__name

    @property
    def url( self ):
        return self.__url

    def __initAttributes( self ):
        self.__name = None
        self.__url = None

    def __useAttributes( self, attributes ):
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self.__name = attributes[ "name" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
