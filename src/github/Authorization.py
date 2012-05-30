# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import AuthorizationApplication

class Authorization( GithubObject.CompletableGithubObject ):
    @property
    def app( self ):
        self._completeIfNeeded( self._app )
        return self._app

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def note( self ):
        self._completeIfNeeded( self._note )
        return self._note

    @property
    def note_url( self ):
        self._completeIfNeeded( self._note_url )
        return self._note_url

    @property
    def scopes( self ):
        self._completeIfNeeded( self._scopes )
        return self._scopes

    @property
    def token( self ):
        self._completeIfNeeded( self._token )
        return self._token

    @property
    def updated_at( self ):
        self._completeIfNeeded( self._updated_at )
        return self._updated_at

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, scopes = DefaultValueForOptionalParameters, add_scopes = DefaultValueForOptionalParameters, remove_scopes = DefaultValueForOptionalParameters, note = DefaultValueForOptionalParameters, note_url = DefaultValueForOptionalParameters ):
        if scopes is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in scopes ), scopes
        if add_scopes is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in add_scopes ), add_scopes
        if remove_scopes is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in remove_scopes ), remove_scopes
        if note is not DefaultValueForOptionalParameters:
            assert isinstance( note, ( str, unicode ) ), note
        if note_url is not DefaultValueForOptionalParameters:
            assert isinstance( note_url, ( str, unicode ) ), note_url
        post_parameters = dict()
        if scopes is not DefaultValueForOptionalParameters:
            post_parameters[ "scopes" ] = scopes
        if add_scopes is not DefaultValueForOptionalParameters:
            post_parameters[ "add_scopes" ] = add_scopes
        if remove_scopes is not DefaultValueForOptionalParameters:
            post_parameters[ "remove_scopes" ] = remove_scopes
        if note is not DefaultValueForOptionalParameters:
            post_parameters[ "note" ] = note
        if note_url is not DefaultValueForOptionalParameters:
            post_parameters[ "note_url" ] = note_url
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def _initAttributes( self ):
        self._app = None
        self._created_at = None
        self._id = None
        self._note = None
        self._note_url = None
        self._scopes = None
        self._token = None
        self._updated_at = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "app" in attributes and attributes[ "app" ] is not None: # pragma no branch
            assert isinstance( attributes[ "app" ], dict ), attributes[ "app" ]
            self._app = AuthorizationApplication.AuthorizationApplication( self._requester, attributes[ "app" ], completed = False )
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "note" in attributes and attributes[ "note" ] is not None: # pragma no branch
            assert isinstance( attributes[ "note" ], ( str, unicode ) ), attributes[ "note" ]
            self._note = attributes[ "note" ]
        if "note_url" in attributes and attributes[ "note_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "note_url" ], ( str, unicode ) ), attributes[ "note_url" ]
            self._note_url = attributes[ "note_url" ]
        if "scopes" in attributes and attributes[ "scopes" ] is not None: # pragma no branch
            assert all( isinstance( element, ( str, unicode ) ) for element in attributes[ "scopes" ] ), attributes[ "scopes" ]
            self._scopes = attributes[ "scopes" ]
        if "token" in attributes and attributes[ "token" ] is not None: # pragma no branch
            assert isinstance( attributes[ "token" ], ( str, unicode ) ), attributes[ "token" ]
            self._token = attributes[ "token" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
