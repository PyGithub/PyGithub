# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
from DefaultValueForOptionalParameters import DefaultValueForOptionalParameters

class UserKey( GithubObject.CompletableGithubObject ):
    @property
    def id( self ):
        self._completeIfNeeded( self._id )
        return self._id

    @property
    def key( self ):
        self._completeIfNeeded( self._key )
        return self._key

    @property
    def title( self ):
        self._completeIfNeeded( self._title )
        return self._title

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    @property
    def verified( self ):
        self._completeIfNeeded( self._verified )
        return self._verified

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, title = DefaultValueForOptionalParameters, key = DefaultValueForOptionalParameters ):
        if title is not DefaultValueForOptionalParameters:
            assert isinstance( title, ( str, unicode ) ), title
        if key is not DefaultValueForOptionalParameters:
            assert isinstance( key, ( str, unicode ) ), key
        post_parameters = dict()
        if title is not DefaultValueForOptionalParameters:
            post_parameters[ "title" ] = title
        if key is not DefaultValueForOptionalParameters:
            post_parameters[ "key" ] = key
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    def _initAttributes( self ):
        self._id = None
        self._key = None
        self._title = None
        self._url = None
        self._verified = None

    def _useAttributes( self, attributes ):
        if "id" in attributes and attributes[ "id" ] is not None: # pragma no branch
            assert isinstance( attributes[ "id" ], int ), attributes[ "id" ]
            self._id = attributes[ "id" ]
        if "key" in attributes and attributes[ "key" ] is not None: # pragma no branch
            assert isinstance( attributes[ "key" ], ( str, unicode ) ), attributes[ "key" ]
            self._key = attributes[ "key" ]
        if "title" in attributes and attributes[ "title" ] is not None: # pragma no branch
            assert isinstance( attributes[ "title" ], ( str, unicode ) ), attributes[ "title" ]
            self._title = attributes[ "title" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "verified" in attributes and attributes[ "verified" ] is not None: # pragma no branch
            assert isinstance( attributes[ "verified" ], bool ), attributes[ "verified" ]
            self._verified = attributes[ "verified" ]
