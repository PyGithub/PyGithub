# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import Commit

class Branch( GithubObject.BasicGithubObject ):
    @property
    def commit( self ):
        return self._commit

    @property
    def name( self ):
        return self._name

    def _initAttributes( self ):
        self._commit = None
        self._name = None

    def _useAttributes( self, attributes ):
        if "commit" in attributes and attributes[ "commit" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self._commit = Commit.Commit( self._requester, attributes[ "commit" ], completed = False )
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
