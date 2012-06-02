# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class CommitStats( GithubObject.BasicGithubObject ):
    @property
    def additions( self ):
        return self._NoneIfNotSet( self._additions )

    @property
    def deletions( self ):
        return self._NoneIfNotSet( self._deletions )

    @property
    def total( self ):
        return self._NoneIfNotSet( self._total )

    def _initAttributes( self ):
        self._additions = GithubObject.NotSet
        self._deletions = GithubObject.NotSet
        self._total = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "additions" in attributes: # pragma no branch
            assert attributes[ "additions" ] is None or isinstance( attributes[ "additions" ], int ), attributes[ "additions" ]
            self._additions = attributes[ "additions" ]
        if "deletions" in attributes: # pragma no branch
            assert attributes[ "deletions" ] is None or isinstance( attributes[ "deletions" ], int ), attributes[ "deletions" ]
            self._deletions = attributes[ "deletions" ]
        if "total" in attributes: # pragma no branch
            assert attributes[ "total" ] is None or isinstance( attributes[ "total" ], int ), attributes[ "total" ]
            self._total = attributes[ "total" ]
