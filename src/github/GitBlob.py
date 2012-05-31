# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GitBlob( GithubObject.GithubObject ):
    @property
    def content( self ):
        self._completeIfNotSet( self._content )
        return self._NoneIfNotSet( self._content )

    @property
    def encoding( self ):
        self._completeIfNotSet( self._encoding )
        return self._NoneIfNotSet( self._encoding )

    @property
    def sha( self ):
        self._completeIfNotSet( self._sha )
        return self._NoneIfNotSet( self._sha )

    @property
    def size( self ):
        self._completeIfNotSet( self._size )
        return self._NoneIfNotSet( self._size )

    @property
    def url( self ):
        self._completeIfNotSet( self._url )
        return self._NoneIfNotSet( self._url )

    def _initAttributes( self ):
        self._content = GithubObject.NotSet
        self._encoding = GithubObject.NotSet
        self._sha = GithubObject.NotSet
        self._size = GithubObject.NotSet
        self._url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "content" in attributes: # pragma no branch
            assert attributes[ "content" ] is None or isinstance( attributes[ "content" ], ( str, unicode ) ), attributes[ "content" ]
            self._content = attributes[ "content" ]
        if "encoding" in attributes: # pragma no branch
            assert attributes[ "encoding" ] is None or isinstance( attributes[ "encoding" ], ( str, unicode ) ), attributes[ "encoding" ]
            self._encoding = attributes[ "encoding" ]
        if "sha" in attributes: # pragma no branch
            assert attributes[ "sha" ] is None or isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "size" in attributes: # pragma no branch
            assert attributes[ "size" ] is None or isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self._size = attributes[ "size" ]
        if "url" in attributes: # pragma no branch
            assert attributes[ "url" ] is None or isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
