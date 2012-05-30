# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GitTreeElement( GithubObject.GithubObject ):
    @property
    def mode( self ):
        return self._mode

    @property
    def path( self ):
        return self._path

    @property
    def sha( self ):
        return self._sha

    @property
    def size( self ):
        return self._size

    @property
    def type( self ):
        return self._type

    @property
    def url( self ):
        return self._url

    def _initAttributes( self ):
        self._mode = None
        self._path = None
        self._sha = None
        self._size = None
        self._type = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "mode" in attributes and attributes[ "mode" ] is not None: # pragma no branch
            assert isinstance( attributes[ "mode" ], ( str, unicode ) ), attributes[ "mode" ]
            self._mode = attributes[ "mode" ]
        if "path" in attributes and attributes[ "path" ] is not None: # pragma no branch
            assert isinstance( attributes[ "path" ], ( str, unicode ) ), attributes[ "path" ]
            self._path = attributes[ "path" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "size" in attributes and attributes[ "size" ] is not None: # pragma no branch
            assert isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self._size = attributes[ "size" ]
        if "type" in attributes and attributes[ "type" ] is not None: # pragma no branch
            assert isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self._type = attributes[ "type" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
