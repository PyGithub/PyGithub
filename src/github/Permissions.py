# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class Permissions( GithubObject.BasicGithubObject ):
    @property
    def admin( self ):
        return self._admin

    @property
    def pull( self ):
        return self._pull

    @property
    def push( self ):
        return self._push

    def _initAttributes( self ):
        self._admin = None
        self._pull = None
        self._push = None

    def _useAttributes( self, attributes ):
        if "admin" in attributes and attributes[ "admin" ] is not None: # pragma no branch
            assert isinstance( attributes[ "admin" ], bool ), attributes[ "admin" ]
            self._admin = attributes[ "admin" ]
        if "pull" in attributes and attributes[ "pull" ] is not None: # pragma no branch
            assert isinstance( attributes[ "pull" ], bool ), attributes[ "pull" ]
            self._pull = attributes[ "pull" ]
        if "push" in attributes and attributes[ "push" ] is not None: # pragma no branch
            assert isinstance( attributes[ "push" ], bool ), attributes[ "push" ]
            self._push = attributes[ "push" ]
