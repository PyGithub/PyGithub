# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import PaginatedList
from GithubObject import *
import NamedUser

class IssueComment( object ):
    def __init__( self, requester, attributes, completion ):
        self.__requester = requester
        self.__initAttributes()
        self.__useAttributes( attributes )

    @property
    def body( self ):
        return self.__body

    @property
    def created_at( self ):
        return self.__created_at

    @property
    def id( self ):
        return self.__id

    @property
    def updated_at( self ):
        return self.__updated_at

    @property
    def url( self ):
        return self.__url

    @property
    def user( self ):
        return self.__user

    def delete( self ):
        status, headers, data = self.__requester.request(
            "DELETE",
            str( self.url ),
            None,
            None
        )

    def edit( self, body ):
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
        self.__created_at = None
        self.__id = None
        self.__updated_at = None
        self.__url = None
        self.__user = None

    def __useAttributes( self, attributes ):
        # @todo No need to check if attribute is in attributes when attribute is mandatory
        if "body" in attributes and attributes[ "body" ] is not None: # pragma no branch
            self.__body = attributes[ "body" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            self.__created_at = attributes[ "created_at" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            self.__id = attributes[ "id" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            self.__updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            self.__url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict )
            self.__user = NamedUser.NamedUser( self.__requester, attributes[ "user" ], completion = LazyCompletion )
