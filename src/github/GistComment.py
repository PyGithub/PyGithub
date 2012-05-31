# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import NamedUser

class GistComment( GithubObject.GithubObject ):
    @property
    def body( self ):
        self._completeIfNotSet( self._body )
        return self._NoneIfNotSet( self._body )

    @property
    def created_at( self ):
        self._completeIfNotSet( self._created_at )
        return self._NoneIfNotSet( self._created_at )

    @property
    def id( self ):
        self._completeIfNotSet( self._id )
        return self._NoneIfNotSet( self._id )

    @property
    def updated_at( self ):
        self._completeIfNotSet( self._updated_at )
        return self._NoneIfNotSet( self._updated_at )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    @property
    def user( self ):
        self._completeIfNotSet( self._user )
        return self._NoneIfNotSet( self._user )

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, body ):
        assert isinstance( body, ( str, unicode ) ), body
        post_parameters = {
            "body": body,
        }
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def _initAttributes( self ):
        self._body = GithubObject.NotSet
        self._created_at = GithubObject.NotSet
        self._id = GithubObject.NotSet
        self._updated_at = GithubObject.NotSet
        self._url = GithubObject.NotSet
        self._user = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "body" in attributes: # pragma no branch
            assert attributes[ "body" ] is None or isinstance( attributes[ "body" ], ( str, unicode ) ), attributes[ "body" ]
            self._body = attributes[ "body" ]
        if "created_at" in attributes: # pragma no branch
            assert attributes[ "created_at" ] is None or isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "id" in attributes: # pragma no branch
            assert attributes[ "id" ] is None or isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "updated_at" in attributes: # pragma no branch
            assert attributes[ "updated_at" ] is None or isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "user" in attributes: # pragma no branch
            assert attributes[ "user" ] is None or isinstance( attributes[ "user" ], dict ), attributes[ "user" ]
            self._user = None if attributes[ "user" ] is None else NamedUser.NamedUser( self._requester, attributes[ "user" ], completed = False )
