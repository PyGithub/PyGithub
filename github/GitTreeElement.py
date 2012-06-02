# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GitTreeElement( GithubObject.BasicGithubObject ):
    @property
    def mode( self ):
        return self._NoneIfNotSet( self._mode )

    @property
    def path( self ):
        return self._NoneIfNotSet( self._path )

    @property
    def sha( self ):
        return self._NoneIfNotSet( self._sha )

    @property
    def size( self ):
        return self._NoneIfNotSet( self._size )

    @property
    def type( self ):
        return self._NoneIfNotSet( self._type )

    @property
    def url( self ):
        return self._NoneIfNotSet( self._url )

    def _initAttributes( self ):
        self._mode = GithubObject.NotSet
        self._path = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._size = GithubObject.NotSet
        self._type = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "mode" in attributes: # pragma no branch
            assert attributes[ "mode" ] is None or isinstance( attributes[ "mode" ], ( str, unicode ) ), attributes[ "mode" ]
            self._mode = attributes[ "mode" ]
        if "path" in attributes: # pragma no branch
            assert attributes[ "path" ] is None or isinstance( attributes[ "path" ], ( str, unicode ) ), attributes[ "path" ]
            self._path = attributes[ "path" ]
        if "sha" in attributes: # pragma no branch
            assert attributes[ "sha" ] is None or isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "size" in attributes: # pragma no branch
            assert attributes[ "size" ] is None or isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self._size = attributes[ "size" ]
        if "type" in attributes: # pragma no branch
            assert attributes[ "type" ] is None or isinstance( attributes[ "type" ], ( str, unicode ) ), attributes[ "type" ]
            self._type = attributes[ "type" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
