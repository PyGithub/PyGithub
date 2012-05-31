# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class PullRequestMergeStatus( GithubObject.BasicGithubObject ):
    @property
    def merged( self ):
        return self._merged

    @property
    def message( self ):
        return self._message

    @property
    def sha( self ):
        return self._sha

    def _initAttributes( self ):
        self._merged = None
        self._message = None
        self._sha = None

    def _useAttributes( self, attributes ):
        if "merged" in attributes and attributes[ "merged" ] is not None: # pragma no branch
            assert isinstance( attributes[ "merged" ], bool ), attributes[ "merged" ]
            self._merged = attributes[ "merged" ]
        if "message" in attributes and attributes[ "message" ] is not None: # pragma no branch
            assert isinstance( attributes[ "message" ], ( str, unicode ) ), attributes[ "message" ]
            self._message = attributes[ "message" ]
        if "sha" in attributes and attributes[ "sha" ] is not None: # pragma no branch
            assert isinstance( attributes[ "sha" ], ( str, unicode ) ), attributes[ "sha" ]
            self._sha = attributes[ "sha" ]
