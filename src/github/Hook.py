# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters
##########
import HookResponse

class Hook( GithubObject.GithubObject ):
    @property
    def active( self ):
        self._completeIfNeeded( self._active )
        return self._active

    @property
    def config( self ):
        self._completeIfNeeded( self._config )
        return self._config

    @property
    def created_at( self ):
        self._completeIfNeeded( self._created_at )
        return self._created_at

    @property
    def events( self ):
        self._completeIfNeeded( self._events )
        return self._events

    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def last_response( self ):
        self._completeIfNeeded( self._last_response )
        return self._last_response

    @property
    def name( self ):
        self._completeIfNeeded( self._name )
        return self._name

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

    def edit( self, name, config, events = DefaultValueForOptionalParameters, add_events = DefaultValueForOptionalParameters, remove_events = DefaultValueForOptionalParameters, active = DefaultValueForOptionalParameters ):
        assert isinstance( name, ( str, unicode ) ), name
        if events is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in events ), events
        if add_events is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in add_events ), add_events
        if remove_events is not DefaultValueForOptionalParameters:
            assert all( isinstance( element, ( str, unicode ) ) for element in remove_events ), remove_events
        if active is not DefaultValueForOptionalParameters:
            assert isinstance( active, bool ), active
        post_parameters = {
            "name": name,
            "config": config,
        }
        if events is not DefaultValueForOptionalParameters:
            post_parameters[ "events" ] = events
        if add_events is not DefaultValueForOptionalParameters:
            post_parameters[ "add_events" ] = add_events
        if remove_events is not DefaultValueForOptionalParameters:
            post_parameters[ "remove_events" ] = remove_events
        if active is not DefaultValueForOptionalParameters:
            post_parameters[ "active" ] = active
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def test( self ):
        status, headers, data = self._request(
            "POST",
            str( self.url ) + "/test",
            None,
            None
        )
        self._checkStatus( status, data )

    def _initAttributes( self ):
        self._active = None
        self._config = None
        self._created_at = None
        self._events = None
        self._id = None
        self._last_response = None
        self._name = None
        self._updated_at = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "active" in attributes and attributes[ "active" ] is not None: # pragma no branch
            assert isinstance( attributes[ "active" ], bool ), attributes[ "active" ]
            self._active = attributes[ "active" ]
        if "config" in attributes and attributes[ "config" ] is not None: # pragma no branch
            self._config = attributes[ "config" ]
        if "created_at" in attributes and attributes[ "created_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "created_at" ], ( str, unicode ) ), attributes[ "created_at" ]
            self._created_at = attributes[ "created_at" ]
        if "events" in attributes and attributes[ "events" ] is not None: # pragma no branch
            assert all( isinstance( element, ( str, unicode ) ) for element in attributes[ "events" ] ), attributes[ "events" ]
            self._events = attributes[ "events" ]
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "last_response" in attributes and attributes[ "last_response" ] is not None: # pragma no branch
            assert isinstance( attributes[ "last_response" ], dict ), attributes[ "last_response" ]
            self._last_response = HookResponse.HookResponse( self._requester, attributes[ "last_response" ], completed = False )
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "updated_at" in attributes and attributes[ "updated_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "updated_at" ], ( str, unicode ) ), attributes[ "updated_at" ]
            self._updated_at = attributes[ "updated_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
