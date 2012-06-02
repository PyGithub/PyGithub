# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class PullRequestMergeStatus( GithubObject.BasicGithubObject ):
    @property
    def merged( self ):
        return self._NoneIfNotSet( self._merged )

    @property
    def message( self ):
        return self._NoneIfNotSet( self._message )

    @property
    def sha( self ):
        return self._NoneIfNotSet( self._sha )

    def _initAttributes( self ):
        self._merged = GithubObject.NotSet
        self._message = GithubObject.NotSet
        self._sha = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "merged" in attributes: # pragma no branch
            assert attributes[ "merged" ] is None or isinstance( attributes[ "merged" ], bool ), attributes[ "merged" ]
            self._merged = attributes[ "merged" ]
        if "message" in attributes: # pragma no branch
            assert attributes[ "message" ] is None or isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self._message = attributes[ "message" ]
        if "sha" in attributes: # pragma no branch
            assert attributes[ "sha" ] is None or isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
