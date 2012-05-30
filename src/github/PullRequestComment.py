# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import NamedUser

class PullRequestComment( object ):
    def __init__( self, requester, attributes, completed ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )
        self.__completed = completed

    @property
    def body( self ):
        self.__completeIfNeeded( self.__body )
        return self.__body

    @property
    def commit_id( self ):
        self.__completeIfNeeded( self.__commit_id )
        return self.__commit_id

    @property
    def created_at( self ):
        self.__completeIfNeeded( self.__created_at )
        return self.__created_at

    @property
    def id( self ):
        self.__completeIfNeeded( self.__id )
        return self.__id

    @property
    def original_commit_id( self ):
        self.__completeIfNeeded( self.__original_commit_id )
        return self.__original_commit_id

    @property
    def original_position( self ):
        self.__completeIfNeeded( self.__original_position )
        return self.__original_position

    @property
    def path( self ):
        self.__completeIfNeeded( self.__path )
        return self.__path

    @property
    def position( self ):
        self.__completeIfNeeded( self.__position )
        return self.__position

    @property
    def updated_at( self ):
        self.__completeIfNeeded( self.__updated_at )
        return self.__updated_at

    @property
    def url( self ):
        self.__completeIfNeeded( self.__url )
        return self.__url

    @property
    def user( self ):
        self.__completeIfNeeded( self.__user )
        return self.__user

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, body ):
        assert isinstance( body, ( str, unicode ) ), body
        post_parameters = {
            "body": body,
        }
        status, headers, data = self.__requester.request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self.__useAttributes( data )

    def __initAttributes( self ):
        self.__body = None
        self.__commit_id = None
        self.__created_at = None
        self.__id = None
        self.__original_commit_id = None
        self.__original_position = None
        self.__path = None
        self.__position = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __completeIfNeeded( self, testedAttribute ):
        if not self.__completed and testedAttribute is None:
            self.__complete() # pragma: no cover

    def __complete( self ): # pragma: no cover
        status, headers, data = self.__requester.request(
            "GET",
            self.__url,
            None,
            None
        )
        self.__useAttributes( data )
        self.__completed = True

    def __useAttributes( self, attributes ):
        if "body" in attributes and attributes[ "body" ] is not None: # pragma no branch
            assert isinstance( attributes[ "body" ], ( str, unicode ) ), attributes[ "body" ]
            self.__body = attributes[ "body" ]
        if "commit_id" in attributes and attributes[ "commit_id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit_id" ], ( str, unicode ) ), attributes[ "commit_id" ]
            self.__commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self.__created_at = attributes[ "created_at" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self.__id = attributes[ "id" ]
        if "original_commit_id" in attributes and attributes[ "original_commit_id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "original_commit_id" ], ( str, unicode ) ), attributes[ "original_commit_id" ]
            self.__original_commit_id = attributes[ "original_commit_id" ]
        if "original_position" in attributes and attributes[ "original_position" ] is not None: # pragma no branch
            assert isinstance( attributes[ "original_position" ], int ), attributes[ "original_position" ]
            self.__original_position = attributes[ "original_position" ]
        if "path" in attributes and attributes[ "path" ] is not None: # pragma no branch
            assert isinstance( attributes[ "path" ], ( str, unicode ) ), attributes[ "path" ]
            self.__path = attributes[ "path" ]
        if "position" in attributes and attributes[ "position" ] is not None: # pragma no branch
            assert isinstance( attributes[ "position" ], int ), attributes[ "position" ]
            self.__position = attributes[ "position" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self.__url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict ), attributes[ "user" ]
            self.__user = NamedUser.NamedUser( self.__requester, attributes[ "user" ], completed = False )
