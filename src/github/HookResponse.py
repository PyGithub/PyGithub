# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *

class HookResponse( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def code( self ):
        return self.__code

    @property
    def message( self ):
        return self.__message

    @property
    def status( self ):
        return self.__status

    def __initAttributes( self ):
        self.__code = None
        self.__message = None
        self.__status = None

    def __useAttributes( self, attributes ):
        if "code" in attributes and attributes[ "code" ] is not None: # pragma no branch
            assert isinstance( attributes[ "code" ], int ), attributes[ "code" ]
            self.__code = attributes[ "code" ]
        if "message" in attributes and attributes[ "message" ] is not None: # pragma no branch
            assert isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self.__message = attributes[ "message" ]
        if "status" in attributes and attributes[ "status" ] is not None: # pragma no branch
            assert isinstance( attributes[ "status" ], ( str, unicode ) ), attributes[ "status" ]
            self.__status = attributes[ "status" ]
