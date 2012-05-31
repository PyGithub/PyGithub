# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import urllib
##########
import GithubObject

class Label( GithubObject.GithubObject ):
    @property
    def color( self ):
        self._completeIfNotSet( self._color )
        return self._NoneIfNotSet( self._color )

    @property
    def name( self ):
        self._completeIfNotSet( self._name )
        return self._NoneIfNotSet( self._name )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    def delete( self ):
        status, headers, data = self._request(
            "DELETE",
            str( self.url ),
            None,
            None
        )
        self._checkStatus( status, data )

    def edit( self, name, color ):
        assert isinstance( name, ( str, unicode ) ), name
        assert isinstance( color, ( str, unicode ) ), color
        post_parameters = {
            "name": name,
            "color": color,
        }
        status, headers, data = self._request(
            "PATCH",
            str( self.url ),
            None,
            post_parameters
        )
        self._checkStatus( status, data )
        self._useAttributes( data )

    @property
    def _identity( self ):
        return urllib.quote( str( self.name ) )

    def _initAttributes( self ):
        self._color = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "color" in attributes: # pragma no branch
            assert attributes[ "color" ] is None or isinstance( attributes[ "color" ], ( str, unicode ) ), attributes[ "color" ]
            self._color = attributes[ "color" ]
        if "name" in attributes: # pragma no branch
            assert attributes[ "name" ] is None or isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
