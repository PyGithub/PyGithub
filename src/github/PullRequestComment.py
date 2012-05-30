# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import NamedUser

class PullRequestComment( GithubObject.CompletableGithubObject ):
    @property
    def body( self ):
        self._completeIfNeeded( self._body )
        return self._body

    @property
    def commit_id( self ):
        self._completeIfNeeded( self._commit_id )
        return self._commit_id

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def original_commit_id( self ):
        self._completeIfNeeded( self._original_commit_id )
        return self._original_commit_id

    @property
    def original_position( self ):
        self._completeIfNeeded( self._original_position )
        return self._original_position

    @property
    def path( self ):
        self._completeIfNeeded( self._path )
        return self._path

    @property
    def position( self ):
        self._completeIfNeeded( self._position )
        return self._position

    @property
    def updated_at( self ):
        self._completeIfNeeded( self._updated_at )
        return self._updated_at

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    @property
    def user( self ):
        self._completeIfNeeded( self._user )
        return self._user

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
        self._body = None
        self._commit_id = None
        self._created_at = None
        self._id = None
        self._original_commit_id = None
        self._original_position = None
        self._path = None
        self._position = None
        self._updated_at = None
        self._url = None
        self._user = None

    def _useAttributes( self, attributes ):
        if "body" in attributes and attributes[ "body" ] is not None: # pragma no branch
            assert isinstance( attributes[ "body" ], ( str, unicode ) ), attributes[ "body" ]
            self._body = attributes[ "body" ]
        if "commit_id" in attributes and attributes[ "commit_id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit_id" ], ( str, unicode ) ), attributes[ "commit_id" ]
            self._commit_id = attributes[ "commit_id" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "original_commit_id" in attributes and attributes[ "original_commit_id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "original_commit_id" ], ( str, unicode ) ), attributes[ "original_commit_id" ]
            self._original_commit_id = attributes[ "original_commit_id" ]
        if "original_position" in attributes and attributes[ "original_position" ] is not None: # pragma no branch
            assert isinstance( attributes[ "original_position" ], int ), attributes[ "original_position" ]
            self._original_position = attributes[ "original_position" ]
        if "path" in attributes and attributes[ "path" ] is not None: # pragma no branch
            assert isinstance( attributes[ "path" ], ( str, unicode ) ), attributes[ "path" ]
            self._path = attributes[ "path" ]
        if "position" in attributes and attributes[ "position" ] is not None: # pragma no branch
            assert isinstance( attributes[ "position" ], int ), attributes[ "position" ]
            self._position = attributes[ "position" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict ), attributes[ "user" ]
            self._user = NamedUser.NamedUser( self._requester, attributes[ "user" ], completed = False )
