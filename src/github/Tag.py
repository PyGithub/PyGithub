# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import Commit

class Tag( GithubObject.BasicGithubObject ):
    @property
    def commit( self ):
        return self._commit

    @property
    def name( self ):
        return self._name

    @property
    def tarball_url( self ):
        return self._tarball_url

    @property
    def zipball_url( self ):
        return self._zipball_url

    def _initAttributes( self ):
        self._commit = None
        self._name = None
        self._tarball_url = None
        self._zipball_url = None

    def _useAttributes( self, attributes ):
        if "commit" in attributes and attributes[ "commit" ] is not None: # pragma no branch
            assert isinstance( attributes[ "commit" ], dict ), attributes[ "commit" ]
            self._commit = Commit.Commit( self._requester, attributes[ "commit" ], completed = False )
        if "name" in attributes and attributes[ "name" ] is not None: # pragma no branch
            assert isinstance( attributes[ "name" ], ( str, unicode ) ), attributes[ "name" ]
            self._name = attributes[ "name" ]
        if "tarball_url" in attributes and attributes[ "tarball_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "tarball_url" ], ( str, unicode ) ), attributes[ "tarball_url" ]
            self._tarball_url = attributes[ "tarball_url" ]
        if "zipball_url" in attributes and attributes[ "zipball_url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "zipball_url" ], ( str, unicode ) ), attributes[ "zipball_url" ]
            self._zipball_url = attributes[ "zipball_url" ]
