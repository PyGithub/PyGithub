# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class HookResponse( GithubObject.BasicGithubObject ):
    @property
    def code( self ):
        return self._NoneIfNotSet( self._code )

    @property
    def message( self ):
        return self._NoneIfNotSet( self._message )

    @property
    def status( self ):
        return self._NoneIfNotSet( self._status )

    def _initAttributes( self ):
        self._code = GithubObject.NotSet
        self._message = GithubObject.NotSet
        self._status = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "code" in attributes: # pragma no branch
            assert attributes[ "code" ] is None or isinstance( attributes[ "code" ], int ), attributes[ "code" ]
            self._code = attributes[ "code" ]
        if "message" in attributes: # pragma no branch
            assert attributes[ "message" ] is None or isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self._message = attributes[ "message" ]
        if "status" in attributes: # pragma no branch
            assert attributes[ "status" ] is None or isinstance( attributes[ "status" ], ( str, unicode ) ), attributes[ "status" ]
            self._status = attributes[ "status" ]
