# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class HookResponse( GithubObject.BasicGithubObject ):
    @property
    def code( self ):
        return self._code

    @property
    def message( self ):
        return self._message

    @property
    def status( self ):
        return self._status

    def _initAttributes( self ):
        self._code = None
        self._message = None
        self._status = None

    def _useAttributes( self, attributes ):
        if "code" in attributes and attributes[ "code" ] is not None: # pragma no branch
            assert isinstance( attributes[ "code" ], int ), attributes[ "code" ]
            self._code = attributes[ "code" ]
        if "message" in attributes and attributes[ "message" ] is not None: # pragma no branch
            assert isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self._message = attributes[ "message" ]
        if "status" in attributes and attributes[ "status" ] is not None: # pragma no branch
            assert isinstance( attributes[ "status" ], ( str, unicode ) ), attributes[ "status" ]
            self._status = attributes[ "status" ]
