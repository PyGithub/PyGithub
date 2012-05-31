# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GitObject( GithubObject.BasicGithubObject ):
    @property
    def sha( self ):
        return self._NoneIfNotSet( self._sha )

    @property
    def type( self ):
        return self._NoneIfNotSet( self._type )

    @property
    def url( self ):
        return self._NoneIfNotSet( self._url )

    def _initAttributes( self ):
        self._sha = GithubObject.NotSet
        self._type = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "sha" in attributes: # pragma no branch
            assert attributes[ "sha" ] is None or isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "type" in attributes: # pragma no branch
            assert attributes[ "type" ] is None or isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self._type = attributes[ "type" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
