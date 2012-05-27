# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import Organization
import Repository
import NamedUser

class Event( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def actor( self ):
        return self.__actor

    @property
    def created_at( self ):
        return self.__created_at

    @property
    def id( self ):
        return self.__id

    @property
    def org( self ):
        return self.__org

    @property
    def payload( self ):
        return self.__payload

    @property
    def public( self ):
        return self.__public

    @property
    def repo( self ):
        return self.__repo

    @property
    def type( self ):
        return self.__type

    def __initAttributes( self ):
        self.__actor = None
        self.__created_at = None
        self.__id = None
        self.__org = None
        self.__payload = None
        self.__public = None
        self.__repo = None
        self.__type = None

    def __useAttributes( self, attributes ):
        if "actor" in attributes and attributes[ "actor" ] is not None: # pragma no branch
            assert isinstance( attributes[ "actor" ], dict ), attributes[ "actor" ]
            self.__actor = NamedUser.NamedUser( self.__requester, attributes[ "actor" ], completion = LazyCompletion )
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self.__created_at = attributes[ "created_at" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], ( str, unicode ) ), attributes[ "id" ]
            self.__id = attributes[ "id" ]
        if "org" in attributes and attributes[ "org" ] is not None: # pragma no branch
            assert isinstance( attributes[ "org" ], dict ), attributes[ "org" ]
            self.__org = Organization.Organization( self.__requester, attributes[ "org" ], completion = LazyCompletion )
        if "payload" in attributes and attributes[ "payload" ] is not None: # pragma no branch
            self.__payload = attributes[ "payload" ]
        if "public" in attributes and attributes[ "public" ] is not None: # pragma no branch
            assert isinstance( attributes[ "public" ], bool ), attributes[ "public" ]
            self.__public = attributes[ "public" ]
        if "repo" in attributes and attributes[ "repo" ] is not None: # pragma no branch
            assert isinstance( attributes[ "repo" ], dict ), attributes[ "repo" ]
            self.__repo = Repository.Repository( self.__requester, attributes[ "repo" ], completion = LazyCompletion )
        if "type" in attributes and attributes[ "type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self.__type = attributes[ "type" ]
