# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class Permissions( GithubObject.BasicGithubObject ):
    @property
    def admin( self ):
        return self._NoneIfNotSet( self._admin )

    @property
    def pull( self ):
        return self._NoneIfNotSet( self._pull )

    @property
    def push( self ):
        return self._NoneIfNotSet( self._push )

    def _initAttributes( self ):
        self._admin = GithubObject.NotSet
        self._pull = GithubObject.NotSet
        self._push = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "admin" in attributes: # pragma no branch
            assert attributes[ "admin" ] is None or isinstance( attributes[ "admin" ], bool ), attributes[ "admin" ]
            self._admin = attributes[ "admin" ]
        if "pull" in attributes: # pragma no branch
            assert attributes[ "pull" ] is None or isinstance( attributes[ "pull" ], bool ), attributes[ "pull" ]
            self._pull = attributes[ "pull" ]
        if "push" in attributes: # pragma no branch
            assert attributes[ "push" ] is None or isinstance( attributes[ "push" ], bool ), attributes[ "push" ]
            self._push = attributes[ "push" ]
