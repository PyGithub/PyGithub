# WARNING: this file is generated automaticaly.
# Do not modify it manually, your work would be lost.

import GithubObject
##########
import NamedUser
import CommitStats

class GistHistoryState( GithubObject.GithubObject ):
    @property
    def change_status( self ):
        self._completeIfNeeded( self._change_status )
        return self._change_status

    @property
    def committed_at( self ):
        self._completeIfNeeded( self._committed_at )
        return self._committed_at

    @property
    def url( self ):
        self._completeIfNeeded( self._url )
        return self._url

    @property
    def user( self ):
        self._completeIfNeeded( self._user )
        return self._user

    @property
    def version( self ):
        self._completeIfNeeded( self._version )
        return self._version

    def _initAttributes( self ):
        self._change_status = None
        self._committed_at = None
        self._url = None
        self._user = None
        self._version = None

    def _useAttributes( self, attributes ):
        if "change_status" in attributes and attributes[ "change_status" ] is not None: # pragma no branch
            assert isinstance( attributes[ "change_status" ], dict ), attributes[ "change_status" ]
            self._change_status = CommitStats.CommitStats( self._requester, attributes[ "change_status" ], completed = False )
        if "committed_at" in attributes and attributes[ "committed_at" ] is not None: # pragma no branch
            assert isinstance( attributes[ "committed_at" ], ( str, unicode ) ), attributes[ "committed_at" ]
            self._committed_at = attributes[ "committed_at" ]
        if "url" in attributes and attributes[ "url" ] is not None: # pragma no branch
            assert isinstance( attributes[ "url" ], ( str, unicode ) ), attributes[ "url" ]
            self._url = attributes[ "url" ]
        if "user" in attributes and attributes[ "user" ] is not None: # pragma no branch
            assert isinstance( attributes[ "user" ], dict ), attributes[ "user" ]
            self._user = NamedUser.NamedUser( self._requester, attributes[ "user" ], completed = False )
        if "version" in attributes and attributes[ "version" ] is not None: # pragma no branch
            assert isinstance( attributes[ "version" ], ( str, unicode ) ), attributes[ "version" ]
            self._version = attributes[ "version" ]
