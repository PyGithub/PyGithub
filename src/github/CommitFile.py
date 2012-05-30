# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class CommitFile( GithubObject.GithubObject ):
    @property
    def additions( self ):
        return self._additions

    @property
    def blob_url( self ):
        return self._blob_url

    @property
    def changes( self ):
        return self._changes

    @property
    def deletions( self ):
        return self._deletions

    @property
    def filename( self ):
        return self._filename

    @property
    def patch( self ):
        return self._patch

    @property
    def raw_url( self ):
        return self._raw_url

    @property
    def sha( self ):
        return self._sha

    @property
    def status( self ):
        return self._status

    def _initAttributes( self ):
        self._additions = None
        self._blob_url = None
        self._changes = None
        self._deletions = None
        self._filename = None
        self._patch = None
        self._raw_url = None
        self._sha = None
        self._status = None

    def _useAttributes( self, attributes ):
        if "additions" in attributes and attributes[ "additions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "additions" ], int ), attributes[ "additions" ]
            self._additions = attributes[ "additions" ]
        if "blob_url" in attributes and attributes[ "blob_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "blob_url" ], ( str, unicode ) ), attributes[ "blob_url" ]
            self._blob_url = attributes[ "blob_url" ]
        if "changes" in attributes and attributes[ "changes" ] is not None: # pragma no branch
            assert isinstance( attributes[ "changes" ], int ), attributes[ "changes" ]
            self._changes = attributes[ "changes" ]
        if "deletions" in attributes and attributes[ "deletions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "deletions" ], int ), attributes[ "deletions" ]
            self._deletions = attributes[ "deletions" ]
        if "filename" in attributes and attributes[ "filename" ] is not None: # pragma no branch
            assert isinstance( attributes[ "filename" ], ( str, unicode ) ), attributes[ "filename" ]
            self._filename = attributes[ "filename" ]
        if "patch" in attributes and attributes[ "patch" ] is not None: # pragma no branch
            assert isinstance( attributes[ "patch" ], ( str, unicode ) ), attributes[ "patch" ]
            self._patch = attributes[ "patch" ]
        if "raw_url" in attributes and attributes[ "raw_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "raw_url" ], ( str, unicode ) ), attributes[ "raw_url" ]
            self._raw_url = attributes[ "raw_url" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
        if "status" in attributes and attributes[ "status" ] is not None: # pragma no branch
            assert isinstance( attributes[ "status" ], ( str, unicode ) ), attributes[ "status" ]
            self._status = attributes[ "status" ]
