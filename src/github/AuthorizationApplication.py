# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class AuthorizationApplication( GithubObject.GithubObject ):
    @property
    def name( self ):
        return self._name

    @property
    def url( self ):
        return self._url

    def _initAttributes( self ):
        self._name = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
