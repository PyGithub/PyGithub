# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GitBlob( GithubObject.GithubObject ):
    @property
    def content( self ):
        self._completeIfNeeded( self._content )
        return self._content

    @property
    def encoding( self ):
        self._completeIfNeeded( self._encoding )
        return self._encoding

    @property
    def sha( self ):
        self._completeIfNeeded( self._sha )
        return self._sha

    @property
    def size( self ):
        self._completeIfNeeded( self._size )
        return self._size

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    def _initAttributes( self ):
        self._content = None
        self._encoding = None
        self._sha = None
        self._size = None
        self._url = None

    def _useAttributes( self, attributes ):
        if "content" in attributes and attributes[ "content" ] is not None: # pragma no branch
            assert isinstance( attributes[ "content" ], ( str, unicode ) ), attributes[ "content" ]
            self._content = attributes[ "content" ]
        if "encoding" in attributes and attributes[ "encoding" ] is not None: # pragma no branch
            assert isinstance( attributes[ "encoding" ], ( str, unicode ) ), attributes[ "encoding" ]
            self._encoding = attributes[ "encoding" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "size" in attributes and attributes[ "size" ] is not None: # pragma no branch
            assert isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self._size = attributes[ "size" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
