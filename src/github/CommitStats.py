# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject

class CommitStats( GithubObject.GithubObject ):
    @property
    def additions( self ):
        return self._additions

    @property
    def deletions( self ):
        return self._deletions

    @property
    def total( self ):
        return self._total

    def _initAttributes( self ):
        self._additions = None
        self._deletions = None
        self._total = None

    def _useAttributes( self, attributes ):
        if "additions" in attributes and attributes[ "additions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "additions" ], int ), attributes[ "additions" ]
            self._additions = attributes[ "additions" ]
        if "deletions" in attributes and attributes[ "deletions" ] is not None: # pragma no branch
            assert isinstance( attributes[ "deletions" ], int ), attributes[ "deletions" ]
            self._deletions = attributes[ "deletions" ]
        if "total" in attributes and attributes[ "total" ] is not None: # pragma no branch
            assert isinstance( attributes[ "total" ], int ), attributes[ "total" ]
            self._total = attributes[ "total" ]
