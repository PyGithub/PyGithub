# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class GistFile( GithubObject.BasicGithubObject ):
    @property
    def content( self ):
        return self._NoneIfNotSet( self._content )

    @property
    def filename( self ):
        return self._NoneIfNotSet( self._filename )

    @property
    def language( self ):
        return self._NoneIfNotSet( self._language )

    @property
    def raw_url( self ):
        return self._NoneIfNotSet( self._raw_url )

    @property
    def size( self ):
        return self._NoneIfNotSet( self._size )

    def _initAttributes( self ):
        self._content = GithubObject.NotSet
        self._filename = GithubObject.NotSet
        self._language = GithubObject.NotSet
        self._raw_url = GithubObject.NotSet
        self._size = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "content" in attributes: # pragma no branch
            assert attributes[ "content" ] is None or isinstance( attributes[ "content" ], ( str, unicode ) ), attributes[ "content" ]
            self._content = attributes[ "content" ]
        if "filename" in attributes: # pragma no branch
            assert attributes[ "filename" ] is None or isinstance( attributes[ "filename" ], ( str, unicode ) ), attributes[ "filename" ]
            self._filename = attributes[ "filename" ]
        if "language" in attributes: # pragma no branch
            assert attributes[ "language" ] is None or isinstance( attributes[ "language" ], ( str, unicode ) ), attributes[ "language" ]
            self._language = attributes[ "language" ]
        if "raw_url" in attributes: # pragma no branch
            assert attributes[ "raw_url" ] is None or isinstance( attributes[ "raw_url" ], ( str, unicode ) ), attributes[ "raw_url" ]
            self._raw_url = attributes[ "raw_url" ]
        if "size" in attributes: # pragma no branch
            assert attributes[ "size" ] is None or isinstance( attributes[ "size" ], int ), attributes[ "size" ]
            self._size = attributes[ "size" ]
