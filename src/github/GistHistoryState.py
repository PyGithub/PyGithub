# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import NamedUser
import CommitStats

class GistHistoryState( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def change_status( self ):
        return self.__change_status

    @property
    def committed_at( self ):
        return self.__committed_at

    @property
    def url( self ):
        return self.__url

    @property
    def user( self ):
        return self.__user

    @property
    def version( self ):
        return self.__version

    def __initAttributes( self ):
        self.__change_status = None
        self.__committed_at = None
        self.__url = None
        self.__user = None
        self.__version = None

    def __useAttributes( self, attributes ):
        # @todo Remove this debug weakness: we shall assume that github will add new attributes
        for attribute in attributes:
            assert attribute in [ "change_status", "committed_at", "url", "user", "version", ], attribute
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "change_status" in attributes and attributes[ "change_status" ] is not None: # pragma no branch
            assert isinstance( attributes[ "change_status" ], dict )
            self.__change_status = CommitStats.CommitStats( self.__requester, attributes[ "change_status" ], completion = LazyCompletion )
        if "committed_at" in attributes and attributes[ "committed_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "committed_at" ], ( str, unicode ) )
            self.__committed_at = attributes[ "committed_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) )
            self.__url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict )
            self.__user = NamedUser.NamedUser( self.__requester, attributes[ "user" ], completion = LazyCompletion )
        if "version" in attributes and attributes[ "version" ] is not None: # pragma no branch
            assert isinstance( attributes[ "version" ], ( str, unicode ) )
            self.__version = attributes[ "version" ]
