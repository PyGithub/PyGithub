# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import Commit

class Tag( GithubObject.BasicGithubObject ):
    @property
    def commit( self ):
        return self._NoneIfNotSet( self._commit )

    @property
    def name( self ):
        return self._NoneIfNotSet( self._name )

    @property
    def tarball_url( self ):
        return self._NoneIfNotSet( self._tarball_url )

    @property
    def zipball_url( self ):
        return self._NoneIfNotSet( self._zipball_url )

    def _initAttributes( self ):
        self._commit = GithubObject.NotSet
        self._name = GithubObject.NotSet
        self._tarball_url = GithubObject.NotSet
        self._zipball_url = GithubObject.NotSet

    def _useAttributes( self, attributes ):
        if "commit" in attributes: # pragma no branch
            assert attributes[ "commit" ] is None or isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self._commit = None if attributes[ "commit" ] is None else Commit.Commit( self._requester, attributes[ "commit" ], completed = False )
        if "name" in attributes: # pragma no branch
            assert attributes[ "name" ] is None or isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "tarball_url" in attributes: # pragma no branch
            assert attributes[ "tarball_url" ] is None or isinstance( attributes[ "tarball_url" ], ( str, unicode ) ), attributes[ "tarball_url" ]
            self._tarball_url = attributes[ "tarball_url" ]
        if "zipball_url" in attributes: # pragma no branch
            assert attributes[ "zipball_url" ] is None or isinstance( attributes[ "zipball_url" ], ( str, unicode ) ), attributes[ "zipball_url" ]
            self._zipball_url = attributes[ "zipball_url" ]
