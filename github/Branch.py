# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import Commit

class Branch( GithubObject.BasicGithubObject ):
    @property
    def commit( self ):
        return self._NoneIfNotSet( self._commit )

    @property
    def name( self ):
        return self._NoneIfNotSet( self._name )

    def _initAttributes( self ):
        self._commit = GithubObject.NotSet
        self._name = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "commit" in attributes: # pragma no branch
            assert attributes[ "commit" ] is None or isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self._commit = None if attributes[ "commit" ] is None else Commit.Commit( self._requester, attributes[ "commit" ], completed = False )
        if "name" in attributes: # pragma no branch
            assert attributes[ "name" ] is None or isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
