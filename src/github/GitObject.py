# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GitObject( GithubObject.BasicGithubObject ):
    @property
    def sha( self ):
        return self._sha

    @property
    def type( self ):
        return self._type

    @property
    def url( self ):
        return self._url

    def _initAttributes( self ):
        self._sha = None
        self._type = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "type" in attributes and attributes[ "type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self._type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
